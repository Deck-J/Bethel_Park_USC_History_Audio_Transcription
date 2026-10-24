# Transcribing this collection

The environment that produced the filed transcripts, pinned so the work can be repeated and checked.

```bash
docker build -t oral-history-transcriber .

docker run --rm -it \
  -v "/path/to/masters:/media:ro" \
  -v "/path/to/models:/models:ro" \
  -v "$PWD/docker:/scripts:ro" \
  -v "$PWD/out:/out" \
  oral-history-transcriber \
  python /scripts/transcribe_chunked.py \
    --input /media/"Side A.m4a" \
    --model /models/large-v3 \
    --out /out \
    --language en \
    --beam 5 \
    --chunk-seconds 120 \
    --seed-file /scripts/seed.txt
```

`--chunk-seconds 120` snaps each window to a nearby quiet point rather than cutting on the clock, which
is what keeps the chunk joins from landing mid-word. The seed file carries the collection's standing
name list; a seed-leak check should confirm none of it appears as content.

Practical notes, learned the hard way and worth not re-learning:

- **Pin the model path, not the model name.** A cached `large-v3` is whatever was downloaded first; the
  transcripts above were made from the int8 CTranslate2 conversion of `openai/whisper-large-v3` at HF
  revision `06f233fe06e710322aca913c1bc4249a0d71fce1`.
- **Give the container 14 threads, not 16.** The NAS needs the last two to stay responsive; the run
  takes 1.6× realtime either way.
- **The container writes as root.** Mount `out/` from an account that can read it afterwards, or pass
  `--user`, or the files come back unreadable to everything else.
- **Do not transcribe the dead tail.** A tape left running adds tens of minutes of silence that the
  engine will happily hallucinate over. Measure where speech stops and crop first — see the notes for
  this recording, where 75 minutes of it was cut off Side B.
- **A second engine is a second document.** A faster GPU engine was measured on this collection and
  retired: it could not report per-word probabilities and its text sat 6–11 % away from the CPU
  engine's. Speed is not the deciding property of an archive transcript.

`./test-build.sh` builds the image and prints `ENGINE_OK <faster-whisper> <ctranslate2> <numpy>` — the
proof that the pins actually resolve, and the check to run before believing any transcript made with
it. Expected output for the filed transcripts: `ENGINE_OK 1.2.1 4.8.3 2.5.4`.
