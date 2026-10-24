# Bethel Presbyterian Church — Historical Room oral histories

Public-domain transcripts of oral-history recordings held by the Historical Room at Bethel
Presbyterian Church, Bethel Park, Pennsylvania — the church's own historians, elders and oldest
families talking about what they remember, on tape, in 1971.

**Text only. The audio masters are held on an archive NAS, not in this repository** (an 83 MB side
would break a clone) — see `docs/AUDIO.md` for exactly where they are and how they are identified.

---

## What is in here

```
recordings/<YYYY-MM-DD>-<slug>/
    README.md          what this recording is: who, when, how it was recorded, how it was transcribed,
                       what is still uncertain — the fullest account we have of the item
    transcript-*.md    the labelled, corrected transcript: WHITE: / INTERVIEWER: / NARRATOR:
    transcript-*.srt   the same text as timed cues, for playback or captioning
    notes-*.md         the working notes behind the transcript: measurements, engine settings, cold
                       passes, every judgement call
    metadata.json      the record of record: date and its source, speakers, masters with sha256, rights
    checksums.sha256   sha256 of every file in the folder
schema/recording.schema.json   the shape metadata.json must take
bin/check.py                   the gate (schema, files, checksums, no audio)
bin/gen_checksums.py           writes checksums.sha256 for a recording folder
docker/                        the pinned environment that produced the transcripts, and how to run it
bin/gen_collection.py          regenerates the index from the recordings themselves
docs/COLLECTION.md             the index: every item, its date, length, words and speakers
docs/AUDIO.md                  where the masters live, and why they are not here
docs/RIGHTS.md                 the rights statement, and what a future deposit must record
```

Every recording is self-describing: someone who opens
`recordings/1971-07-15-ad-white-cross-creek/` should never need this file to understand it.

## The method

The point of the pipeline is that a transcript can be **checked** — by a reader, by a later editor, or
by rebuilding it. Each step exists because skipping it produced a wrong result at least once.

1. **Measure the audio before touching it.** Duration, mean level, peak, and a per-minute level sweep,
   looking for a level step or a second session spliced onto one side. No gain, no denoise, no
   "enhancement": the capture is lossless and any processing is a claim about the original.
2. **Establish the date from the object, not from the folder.** A slate read on the tape, a cassette
   label, a filename — and `metadata.json` says which (`date_source`). A folder name is not evidence.
3. **Check the stereo relationship rather than assuming it.** These sides are a mono signal recorded
   twice, one channel delayed six samples and about 2.7 dB hotter. Align the lag and sum; do not throw
   a channel away, and do not "fix" a delay that is real.
4. **Crop dead tape, but only after measuring it.** A cassette left running adds tens of minutes of
   silence, and an ASR engine will hallucinate speech into it. Sweep for the last real speech, crop
   with room tone to spare, and keep the untouched capture as received.
5. **Chunk on quiet points.** Windows of ~120 s snapped to the nearest quiet sample, so no chunk begins
   or ends mid-word. Chunk boundaries are what make a long side tractable; a bad boundary is what makes
   a transcript lose a syllable.
6. **Transcribe with a seeded prompt** carrying the collection's standing name list — the churches, the
   mills, the families that recur across these tapes. The seed biases the engine toward names that are
   actually in the material, and a **seed-leak check** confirms the list did not appear as content.
7. **Run cold passes on the garbled stretches.** The same windows re-transcribed with no seed at all.
   A prompt can paper over a bad reading; a cold pass shows what the audio alone supports. Two
   corrections in the first recording came only from this step.
8. **Correct, and record the correction.** Every changed proper name, title or number goes into the
   JSON's `post_edits` with what was heard, what it became, the reason, and how certain that is.
   Nothing is silently rewritten, and every change can be reverted in one line.
9. **Label the speakers, and share a label rather than guess.** `WHITE` is the subject; `INTERVIEWER`
   covers two interviewers when the tape does not say which one is speaking; `NARRATOR` is the
   copyist's slate, not a voice in the room; `UNKNOWN` is a voice that cannot be placed.
10. **Build the documents from the transcript, then verify them.** The `.md` and the `.srt` are
    generated from the labelled text and compared against it — paragraph count, word count and
    label-run count — not read over by eye.
11. **Say what is still uncertain.** Guesses stay marked, unresolved readings stay as heard, and the
    notes list them. A transcript that claims to be clean everywhere cannot be trusted anywhere.
12. **Checksum everything and gate the repository.** `bin/check.py` fails on a missing file, an empty
    transcript, a bad checksum, or any audio in git; the same check runs in CI on every push.

The engine is pinned because it decides the words: `faster-whisper 1.2.1` / `CTranslate2 4.8.3` /
`numpy 2.5.4`, large-v3 int8, beam 5, on a base image pinned by digest. `docker/` holds that
environment and the exact command line; a bump in any of those is a new transcription, not an upgrade.

Speed was measured and rejected as a reason to change engines: an OpenVINO GPU engine ran this
collection 3.4–5.6× faster and was retired, because it could not report per-word probabilities and its
text sat 6–11 % away from the CPU engine's. A faster draft of a different document is not progress.

## The gate

```bash
python3 bin/check.py                 # every recording
python3 bin/check.py --dir recordings/1971-07-15-ad-white-cross-creek
```

It enforces the schema (stdlib only, no dependencies), the presence of the folder README, transcript,
notes and metadata, a non-empty transcript, a matching `checksums.sha256`, and the absence of audio
files. `.github/workflows/check.yml` runs it on every push, so the repository cannot drift into a state
where a transcript has lost its provenance.

## Adding a recording

1. `recordings/<YYYY-MM-DD>-<slug>/` — the recording date, or `unknown` plus an explanation.
2. `metadata.json` (see `schema/recording.schema.json`); `date_source` must say where the date came
   from, never "the folder name".
3. Transcript, `.srt`, `notes-*.md`, and a `README.md` for the folder — copy the shape of the existing
   one: identity, provenance, audio measurements, engine and its numbers, corrections, open questions,
   outline with timestamps, files, citation.
4. `python3 bin/gen_checksums.py recordings/<that folder>`, then `python3 bin/check.py`.

## Rights

Public domain, released by the rights holder; the transcripts are **CC0 1.0**. The claim is per
recording, never per repository, and `docs/RIGHTS.md` says what a future deposit must record before it
may be added. If you are a participant or a rights holder and want something changed or removed, open
an issue — that is honoured without argument.

## Contents

The index is **generated**, not written by hand — `python3 bin/gen_collection.py` reads every
recording's `metadata.json` and rebuilds it, so it cannot list an item that is not here or miss one
that is:

- **→ [`docs/COLLECTION.md`](docs/COLLECTION.md)** — all items, with date, length, word count and
  speaker(s)

Fourteen items so far: interviews and lectures recorded between 1971 and 1983 with the church's own
historians and oldest families, plus one papers-only item (the J.D. Patterson typescript).
