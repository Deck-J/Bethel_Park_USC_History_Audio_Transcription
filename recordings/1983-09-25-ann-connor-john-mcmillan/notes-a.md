# Ann Connor — John McMillan Lecture (25 September 1983) — transcription record

Recording stem: `Ann Connor - John McMillan Lecture (25 September 1983)`. Every file in this folder
carries that stem; this note is the working record behind the document.

## What this is

A 31 m 11 s (1,871.45 s) **lecture on the Reverend John McMillan**, delivered by **Ann Connor** on
**25 September 1983** to a gathering that had just been looking at a 1935 McMillan family reunion
photograph. It is a talk, not an interview: Ann speaks from her own notes through a continuous
historical narrative — the McMillans in Scotland, the Plantation of Ulster, the Scotch-Irish
migration into western Pennsylvania, McMillan's education at Princeton under John Witherspoon, his
ordination by the Donegal Presbytery in 1776, his preaching at Chartiers and Pigeon Creek, the log
and stone churches, his revival style ("he rattled them out of hell"), his politics and his support
for Albert Gallatin, and the academies and colleges at Canonsburg and Washington that grew out of
his work.

She is also the compiler of a McMillan genealogy — a supplement to "Bennett's book" of 1935,
published 1981 after twelve years of collecting — and the first three minutes are her presentation
of that book and of McMillan relics (his saddlebag, the buckles from his knee breeches, borrowed
from a direct descendant, Sam McDowell).

**How it was found.** The file was sitting inside `JD Patterson - Side A/` under the name
`Ann-Connor John McMillian 9-25-83.m4a`, with a byte-identical second copy loose at the archive
root (both md5 `6c9a120aa52d6f650473ba60d740ce66`). It matches no other recording in the archive:
it is 31:11 where JD Patterson is 35:56, the George Marshall talk 31:44 and the Valentine panel
25:59, and its content is a different event from all of them. The filename means "Ann Connor, on
John McMillan, 9-25-83" — McMillan is her **subject**, not a participant (he died in 1853; he could
not be a voice on a 1983 tape). It was never transcribed. This folder is its first transcription.

**The pairing that matters.** 25 September 1983 is also the date of
`Valentine, Maits and Snowden (25 September 1983)/` — the three-voice panel recorded the same day.
Two recordings, one day, one subject (the history of Bethel), two very different formats: a
moderated panel of three old members recollecting, and a prepared lecture by the woman who had
spent years in the records. Read together they are the strongest single day in this archive, and
they corroborate each other on the ministers' names, the buildings and the 1776 founding.

## Date, and what the date rests on

- **25 September 1983 — filename-supplied** (John Decker's original capture name
  `Ann-Connor John McMillian 9-25-83`).
- **The tape states no date of its own**, and **nothing on it contradicts 25 September 1983**. No
  conflict was found, so no conflict is recorded.
- Internal dating is consistent but not decisive: she speaks of the 1981 publication of her book in
  the past tense ("up to 1981 when we published this book"), and of having retired from 32½ years
  of public school teaching.

## Speaker attribution and the evidence for it

**Ann Connor is the speaker.** The attribution is John Decker's, and the audio agrees with it: the
woman who introduces her names her in the third person and praises the work she has done on the
church's history, and the lecturer then speaks as the compiler of the McMillan genealogy. The
surname **Connor is never spoken on the tape** — it comes from the archive.

Three voices are present, and only the first three minutes are not Ann's:

| Label | Time | Evidence |
|---|---|---|
| `HOST` | 0:00–0:34 | A woman introducing Ann in the third person: "I don't think anyone like Ann has spent so much time in the history of the church". She and her husband are "members of Venice United Presbyterian Church". Unnamed. |
| `ANN` | 0:34–1:33 | "I first of all would like to tell you that the saddlebag that Dr. John McMillan used…"; "I would like my husband to … show you this picture". |
| `HUSBAND` | 1:33–3:27 | Ann's husband, showing round the 1935 reunion photograph he had reproduced and numbered himself: "my wife has composed this book", "I'm a little skinny guy in the back", "I called it my center hole". |
| `ANN` | 3:27–31:05 | Resumes as the book's compiler: "I did the calligraphy in the book as well as I did all the compiling", then the lecture proper from 6:33 ("First of all, I would like to start with the John McMillans way back in Scotland"). |

**Method, and its limits.** The split rests on content — third-person self-reference, "my husband" /
"my wife has composed this book", and the resumption of the book authorship — not on voice
matching. Median f0 was measured and is **not** usable here: this is a band-limited cassette
capture and Ann's own blocks range from 168 to 242 Hz depending on the window, so pitch cannot
separate the speakers. One consequence: a two-word interjection by Ann, "Oh, very handsome"
(~2:17), sits inside her husband's turn because the ASR merged it into his sentence. It is noted
here rather than split out.

Everything from 3:27 to the end is one voice. There is no interviewer, no audience question and no
second participant anywhere in the lecture.

## Source and measurement

- `Ann Connor - John McMillan Lecture (25 September 1983).m4a` — ALAC, 48 kHz, 2 ch, 16-bit,
  1,871.445333 s, 60,417,099 bytes, md5 `6c9a120aa52d6f650473ba60d740ce66`, **unchanged as
  received** (md5 verified before and after the move out of the JD Patterson folder).
- Level: mean **−39.5 dBFS**, peak **−8.0 dBFS**. Even across the file — 31 one-minute blocks all
  peak between −8.0 and −20.7 dBFS. Speech runs 0:11–30:50; the first ~9 s and the last ~15 s are
  the only real silence.
- **Stereo: delayed duplicate.** Measured on eight 30 s windows: a constant **5-sample** (0.10 ms)
  lag at r = 0.977–0.990, ch1 3.2–3.7 dB stronger throughout. Summed with the lag compensated,
  weighted 2:1 toward ch1; an equal-weight sum would have added the weaker feed's noise at full
  weight, and dropping ch0 would have thrown away a near-perfect second copy.
- **No denoise, no re-mastering.** The master is the capture as received; the only processing is
  the 2:1 channel sum, done once for the ASR.

## Transcription

- Whisper **large-v3** (Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads), `en`.
- **16 chunks** of ~120 s, boundaries snapped to the quietest 10 ms frame within ±5 s of each
  target. Never a whole-file pass. `beam_size=5`, `condition_on_previous_text=False`,
  `temperature=0.0`, `compression_ratio_threshold=2.4`, `vad_filter=False`, word timestamps.
- Audio decoded by ffmpeg to float32 numpy arrays. **PyAV in this build rejects the
  `metadata_errors` kwarg** faster-whisper passes, so the array path is used deliberately — the
  same trap that has bitten this archive twice.
- `initial_prompt` seeded with corroborated names only (McMillan, Clark, Woods, Marshall, Wycoff,
  Reiter, Chartiers, Mingo Creek, Canonsburg, Bethel Academy, Oliver Miller Homestead, Dido,
  Doddridge, Princeton Theological Seminary, Croco, Strobl, Coverdale, Slumbury).

### Prompt leak — four segments, all repaired

The seeded prompt leaked at four chunk heads, each a segment made **100 % of seed tokens**:
13.9–29.7 s, 355.6–385.5 s, 713.6–743.6 s and 954.2–984.2 s. Every span was **re-transcribed
un-prompted and spliced back — nothing was deleted**. The recovery was substantial: the first
leak had overwritten the host's opening sentence, and the second had swallowed a whole
question-and-answer aside ("…could I have some questions? Or you haven't thought of any yet?").
The repaired text is what the document carries; the leak text survives only in `leak_repair.json`
in the working directory, not in the deliverable.

### Chunk seams — why the word count is 4,585, not 4,300

Overlapping chunk seams initially dropped whole segments whose start fell just before the previous
segment's end. The dedupe now trims only the **duplicated prefix**, which recovered real content
that would otherwise have been lost — including "He went into the ministry and he served for 59
years. He had 20 children", "The Hebrews had it when they went to Egypt", "Now, at Princeton, they
would rise at 5 o'clock in the morning", and the medical-school sentence at 30:00. Two clauses lost
at a seam were restored verbatim from the un-prompted re-transcription of the same audio
("…at a rate of about 30, 35 miles a day on horseback"; "…you go and get the old Noah Webster's");
both are recorded in `post_edits`.

### Quality

- 276 segments, **4,585 words**, **mean per-word probability 0.9386**, **3.20 % of words below 0.5**
  (6.9 % below 0.7).
- The weak stretches are the band-limited passages at 11:50–12:40 (the school-English digression)
  and the 2:50–5:50 book discussion, where two voices share a distant microphone. The lecture body
  from 6:33 runs clean.
- **Read end to end**, all 276 segments, and corrected by sense as well as by name.

## Corrections applied (203 `post_edits` entries)

All are recorded in the JSON `post_edits` with their raw ASR form, reason and certainty. The
substantive ones:

| # | As transcribed | Corrected | Why | Certainty |
|---|---|---|---|---|
| 1 | "shark ears … pigeon cream" | Chartiers … Pigeon Creek | the two congregations he served; both named again at 26:36 as "Chartiers Church" | certain |
| 2 | "charters church" | Chartiers Church | built 1778 | certain |
| 3 | "Cairnsburg" / "Canberra College" | Canonsburg / Canonsburg College | Washington County; named correctly later in the same passage | certain |
| 4 | "secretary of the church", "Secretary of the Treasurer" | Secretary of the Treasury | Gallatin's office | certain |
| 5 | "knee bridges" | knee breeches | the buckles he used for them | certain |
| 6 | "mcnellan", "Mcnone", "McGowan" | McMillan | the same man throughout; she names him correctly a line later each time | certain / probable |
| 7 | "the John McMillan's" | the John McMillans | the family, plural — not a possessive | certain |
| 8 | "Mignola clan" | McMillan clan | "the beginning of the McMillan clan with Dr. John McMillan" | probable |
| 9 | "plantation of ulster" | Plantation of Ulster | the 1609 plantation, six counties | certain |
| 10 | "albert gallatin" | Albert Gallatin | proper noun | certain |
| 11 | "checked his gut" | checked his gun | context: "he carried his guns with him" | probable |
| 12 | "a linear descendant" | a lineal descendant | standard phrase | probable |
| 13 | "out of laws" | out of logs | a log church, built 1778 | probable |
| 14 | "take a stamp" | take a stand | the sense of the passage | probable |
| 15 | "Dr. John Park" | Dr. John Clark | the three men are Clark, his adopted son William Jones, and his son | probable |
| 16 | "MacMillan" (×2) | McMillan | one spelling throughout | certain |
| 17 | "Thank you." at 31:05 | removed | hallucinated over room tone (−59 dB) ten seconds after speech ended; the same artifact was removed from the Valentine transcript | certain |

Mechanical repairs applied alongside: doubled words collapsed where they straddle a chunk seam
("needed needed", "That That"), sentence case and proper-noun case repaired, "World War II"
duplicated across a seam resolved by clause order. Hesitations and false starts left alone.

## Unresolved (left as heard, not guessed)

1. **"Books, dictionaries back in 1800 and still up until World War II…"** (12:34–13:00) — the
   clause order across the seam is as spoken, but the sentence remains awkward and the exact
   wording of the dictionary reference is not recoverable.
2. **"I called it my center hole"** (~3:08) — the husband's name for his reproduction of the 1935
   photograph. Not resolvable.
3. **"a Director of the Senate"** (~3:42) — said of the artist Gail Boak's wife.
4. **"George Briggs"** (13:06) — "besides teaching Greek, believe it or not, they taught George
   Briggs". A curriculum subject whose name is not recoverable from context.
5. **"the joint germ"** (29:10) — probably the jointure/merger of the two colleges; the word as
   heard is not English.
6. **"Natural Ridge"** (15:05) — where McMillan preached in Virginia; no such place found (possibly
   Natural Bridge).
7. **"Paul Mandel"** (25:53) — the man said to have campaigned for Gallatin.
8. **"Bennett's book"** — the 1935 McMillan genealogy she calls her supplement to; the compiler's
   full name is not given on the tape.
9. **"he practically rattled a preaching"** (22:13) — a garbled clause in the passage about his
   revival style; the sense is clear from the next sentence, the wording is not.
10. **The missing "one regret" quotation** — "he couldn't pass on or give his weak, I mean, his
    strong voice to some weak voice preacher" — she corrects herself mid-sentence; kept verbatim
    rather than tidied.

## File inventory

| File | What it is |
|---|---|
| `Ann Connor - John McMillan Lecture (25 September 1983).m4a` | the master, as received; md5 `6c9a120aa52d6f650473ba60d740ce66` |
| `Ann Connor - John McMillan Lecture (25 September 1983).txt` | the transcript: 140 labelled turns, source of truth for both documents |
| `Ann Connor - John McMillan Lecture (25 September 1983).srt` | 276 timed cues, speaker label on the first cue of each turn |
| `Ann Connor - John McMillan Lecture (25 September 1983).json` | provenance: raw ASR segments, per-word timings and probabilities, stereo measurement, 203 `post_edits`, 10 `unresolved`, `speaker_attribution` |
| `Ann Connor - John McMillan Lecture (25 September 1983).docx` | the filed document, built from the `.txt` |
| `Ann Connor - John McMillan Lecture (25 September 1983).md` | the same document in Markdown |
| `Ann Connor - John McMillan Lecture (25 September 1983).mp3` | mono 64 kbps listening copy, 31:11.4 |
| `NOTES - Ann Connor - John McMillan Lecture (25 September 1983).md` | this record |

**The MP3 is a straight conversion, not a condensation.** The recording has almost no dead space:
apart from ~9 s at the head and ~15 s at the tail, the longest pause in 31 minutes is 2.9 s. There
was nothing worth cutting, so none was cut; the copy runs the full duration. It carries
`volume=+20 dB` and a limiter (−1.4 dBFS measured peak) because the master is quiet (−39.5 dBFS
mean); the master itself is untouched.

**Duplicate copy.** The byte-identical second copy found loose at the archive root is kept at
`superseded/backups/Ann-Connor John McMillian 9-25-83.m4a.bak-duplicate-of-master`. Nothing was
deleted.

Rebuild the documents only from the `.txt` (see the archive README); never edit the `.docx` or
`.md` by hand, or the next rebuild silently reverts it.
