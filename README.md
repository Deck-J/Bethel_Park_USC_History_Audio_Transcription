# Bethel Presbyterian Church — Historical Room oral histories

Public-domain transcripts of oral-history recordings held by the Historical Room at Bethel
Presbyterian Church, Bethel Park, Pennsylvania. **Text in this repo; audio masters do not live here**
(see `docs/AUDIO.md` for why and where).

## What is here

```
recordings/<YYYY-MM-DD>-<slug>/     one folder per recording
    metadata.json                   the record of record: date, speakers, source, rights, checksums
    transcript.md                   labelled, corrected transcript (the readable copy)
    transcript.srt                  same text, timed cues, one side per file when a tape has two
    notes.md                        provenance: audio measurements, crop, engine, corrections, open items
    checksums.sha256                sha256 of every file in the folder
schema/recording.schema.json        JSON Schema the metadata must satisfy
bin/check.py                        the gate: schema, files present, checksums, no audio
docs/AUDIO.md                       where the masters are and why they are not in git
docs/RIGHTS.md                      the public-domain statement and how provenance is recorded
```

## The gate

```bash
python3 bin/check.py          # every recording; exits non-zero on any failure
python3 bin/check.py --dir recordings/<one>
```

It refuses a recording whose metadata does not satisfy the schema, whose checksums do not match, that
carries an audio file, or whose transcript is empty. Nothing here trusts a directory listing.

## Adding a recording

1. New folder `recordings/<YYYY-MM-DD>-<slug>/` (date = when the recording was made, not when it was
   digitised; use `unknown` in place of a date you cannot establish, and say so in `metadata.json`).
2. Fill `metadata.json` (see the schema; `date_source` must say where the date comes from).
3. Transcribe, correct, label, and write `notes.md` — the notes carry what the transcript cannot: what
   the audio measures, what was cropped, which engine ran, what is guesswork.
4. `python3 bin/gen_checksums.py recordings/<that folder>` then run the gate.

## Rights

Every recording here is public domain (see `docs/RIGHTS.md`). The transcripts are released CC0 1.0.
Audio masters are not distributed from this repository.
