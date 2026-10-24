#!/usr/bin/env python3
"""Chunked Whisper transcription for archival speech.

Decodes the source with ffmpeg to a float32 mono array (bypasses the PyAV
`metadata_errors` breakage in faster-whisper's file loader), then transcribes in
~2-minute chunks whose boundaries are snapped to the quietest 10 ms point within
+-5 s, so no word is cut. Checkpoints after every chunk so a killed run resumes.

Usage:
  python3 transcribe_chunked.py IN.m4a OUTDIR --stem "Recording Name" \
      [--chunk 120] [--prompt-file seed.txt] [--channel 0|sum] \
      [--start 0] [--end 0] [--language en] [--beam 5] [--resume]

Writes OUTDIR/<stem>.json (segments + words + metadata), .txt and .srt.
"""
import argparse, json, os, subprocess, sys, array, time

import numpy as np


def decode(path, channel="0", start=None, end=None, sr=16000):
    cmd = ["ffmpeg", "-v", "error"]
    if start:
        cmd += ["-ss", str(start)]
    if end:
        cmd += ["-t", str(end - (start or 0))]
    cmd += ["-i", path]
    if channel == "sum":
        cmd += ["-af", f"pan=mono|c0=0.5*c0+0.5*c1,aresample={sr}"]
    else:
        cmd += ["-af", f"pan=mono|c0=c{channel},aresample={sr}"]
    cmd += ["-f", "f32le", "-ac", "1", "-ar", str(sr), "-"]
    raw = subprocess.run(cmd, stdout=subprocess.PIPE, check=True).stdout
    return np.frombuffer(raw, dtype="<f4").copy(), sr


def quiet_points(audio, sr, lo, hi, win_ms=10):
    """Return the sample index of the quietest `win_ms` window in [lo, hi)."""
    w = int(sr * win_ms / 1000)
    seg = audio[lo:hi]
    if len(seg) < w:
        return lo
    n = len(seg) // w
    blocks = seg[: n * w].reshape(n, w)
    rms = np.sqrt((blocks.astype(np.float64) ** 2).mean(axis=1))
    return lo + int(np.argmin(rms)) * w


def fmt_ts(t, srt=False):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    if srt:
        return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")
    return f"{h:02d}:{m:02d}:{s:06.3f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("outdir")
    ap.add_argument("--stem", required=True)
    ap.add_argument("--chunk", type=float, default=120.0)
    ap.add_argument("--prompt-file")
    ap.add_argument("--channel", default="0")
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--end", type=float, default=0.0)
    ap.add_argument("--language", default="en")
    ap.add_argument("--beam", type=int, default=5)
    ap.add_argument("--model", default="/opt/data/models/faster-whisper-large-v3")
    ap.add_argument("--threads", type=int, default=14)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--vad", action="store_true")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    ckpt = os.path.join(args.outdir, f".{args.stem}.chunks.jsonl")

    prompt = None
    if args.prompt_file:
        prompt = open(args.prompt_file, encoding="utf-8-sig").read().strip() or None

    audio, sr = decode(args.input, args.channel, args.start or None, args.end or None)
    dur = len(audio) / sr
    print(f"decoded {dur:.2f}s @ {sr} Hz, chunk={args.chunk}s, prompt={'yes' if prompt else 'no'}", flush=True)

    from faster_whisper import WhisperModel
    t0 = time.time()
    model = WhisperModel(args.model, device="cpu", compute_type="int8", cpu_threads=args.threads)
    print(f"model loaded in {time.time()-t0:.1f}s", flush=True)

    done = {}
    if args.resume and os.path.exists(ckpt):
        for line in open(ckpt):
            r = json.loads(line)
            done[r["idx"]] = r
        print(f"resuming: {len(done)} chunks already done", flush=True)
    else:
        open(ckpt, "w").close()

    bounds = [0.0]
    while bounds[-1] < dur - 0.5:
        target = bounds[-1] + args.chunk
        if target >= dur - 0.5:
            break
        lo = int(max(bounds[-1] + 60, target - 5) * sr)
        hi = int(min(dur, target + 5) * sr)
        bounds.append(quiet_points(audio, sr, lo, hi) / sr)
    bounds.append(dur)
    print(f"{len(bounds)-1} chunks: " + ", ".join(f"{b:.1f}" for b in bounds[:6]) + " ...", flush=True)

    segs = []
    for idx in range(len(bounds) - 1):
        s, e = bounds[idx], bounds[idx + 1]
        if idx in done:
            segs.extend(done[idx]["segments"])
            print(f"chunk {idx+1}/{len(bounds)-1} cached ({len(done[idx]['segments'])} segs)", flush=True)
            continue
        t0 = time.time()
        a = audio[int(s * sr): int(e * sr)]
        it, info = model.transcribe(
            a, language=args.language, beam_size=args.beam, best_of=args.beam,
            initial_prompt=prompt, condition_on_previous_text=False,
            word_timestamps=True, vad_filter=args.vad,
            temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        )
        out = []
        for sg in it:
            words = [{"w": w.word, "s": round(s + w.start, 3), "e": round(s + w.end, 3),
                      "p": round(w.probability, 4)} for w in (sg.words or [])]
            out.append({"start": round(s + sg.start, 3), "end": round(s + sg.end, 3),
                        "text": sg.text.strip(), "words": words,
                        "avg_logprob": round(sg.avg_logprob, 4),
                        "no_speech_prob": round(sg.no_speech_prob, 4)})
        rec = {"idx": idx, "start": round(s, 3), "end": round(e, 3), "segments": out}
        segs.extend(out)
        with open(ckpt, "a") as fh:
            fh.write(json.dumps(rec) + "\n")
        words = sum(len(o["words"]) for o in out)
        print(f"chunk {idx+1}/{len(bounds)-1}  {s:6.1f}-{e:6.1f}s  {len(out)} segs  {words} words  {time.time()-t0:.0f}s", flush=True)

    segs.sort(key=lambda x: x["start"])
    words = [w for sg in segs for w in sg["words"]]
    probs = [w["p"] for w in words]
    meta = {
        "source": os.path.abspath(args.input),
        "stem": args.stem,
        "model": args.model, "language": args.language, "beam": args.beam,
        "chunk_seconds": args.chunk, "channel": args.channel,
        "start": args.start, "end": args.end or dur, "duration": round(dur, 3),
        "prompt": prompt,
        "word_count": len(words),
        "mean_word_prob": round(float(np.mean(probs)), 4) if probs else None,
        "share_below_0.5": round(float(np.mean([p < 0.5 for p in probs])), 4) if probs else None,
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "segments": segs,
        "post_edits": [],
    }
    js = os.path.join(args.outdir, f"{args.stem}.json")
    json.dump(meta, open(js, "w"), indent=1, ensure_ascii=False)

    with open(os.path.join(args.outdir, f"{args.stem}.txt"), "w") as fh:
        for sg in segs:
            fh.write(sg["text"] + "\n")
    with open(os.path.join(args.outdir, f"{args.stem}.srt"), "w") as fh:
        for i, sg in enumerate(segs, 1):
            fh.write(f"{i}\n{fmt_ts(sg['start'], True)} --> {fmt_ts(sg['end'], True)}\n{sg['text']}\n\n")

    print(f"WROTE {js}\nwords={len(words)} mean_p={meta['mean_word_prob']} below0.5={meta['share_below_0.5']}")


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------
# COPIED FILE — do not edit here.
# Source of truth: the archive tooling (archival-voice-transcription skill), scripts/transcribe_chunked.py
# sha256 4bae82b8ce423b95d8063f56afc90fca8a7cb53ec8a563e4fdfe2607aac08d03 (171 lines) as copied 2026-10-23.
# It is here so this repository can reproduce a transcript on its own; if the tooling changes, the copy
# is refreshed and this hash with it.
# ---------------------------------------------------------------------------------------------
