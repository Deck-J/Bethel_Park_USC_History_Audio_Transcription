# Ann Connor — lecture on the Reverend John McMillan (25 September 1983)

Oral history recorded for the Historical Room at Bethel Presbyterian Church, Bethel Park,
Pennsylvania: a prepared lecture on the church's founder, given by the woman who had spent twelve
years compiling the McMillan genealogy and three more writing it.

| | |
|---|---|
| **Speaker** | Ann Connor (surname from the archive; never spoken on the tape) |
| **Also heard** | An unnamed woman who introduces her (`HOST`), and her husband (`HUSBAND`), showing round a 1935 reunion photograph |
| **Recorded** | Sunday, 25 September 1983 — date supplied by the archive's capture filename, not by the tape (see §1) |
| **Length** | 31 m 11 s (1,871.45 s), one continuous capture |
| **Words** | 4,585 in the filed transcript |
| **Status** | Transcribed, corrected, labelled; one reading pass, no second engine; audio master held on the archive NAS |

This is a **talk, not an interview**. There is no interviewer, no audience question and no second
participant anywhere after 3:27. The first three and a half minutes are the hand-over: the host's
introduction, Ann presenting McMillan relics, and her husband passing a photograph round the room.

---

## 1. How the date is established

**The tape states no date.** Nothing on it is a slate, and no voice says the year. The date comes
from the archive's original capture name, `Ann-Connor John McMillian 9-25-83.m4a`, recorded in the
source JSON's `date_recorded_basis` — a **filename**, which is evidence of the kind this archive
accepts, but weaker than a slate.

Two details inside the lecture agree with 1983 without proving it:

- she speaks of her genealogy as published in **1981** ("compiled it from there up to 1981 when we
  published this book"), in the past tense;
- she describes herself as recently retired from "32 and a half years of public school".

Nothing on the tape contradicts 25 September 1983. Two other dates in the material are **not** the
recording date: **2026-10-18** in the archive's collection folder name is the digitisation date, and
**2026-10-20** is the value of `date_digitised` in the source JSON — four days later than the
collection's capture date, with nothing in the notes to explain the gap. `metadata.json` records
2026-10-20 because that is what the source says.

## 2. The physical recording and its capture

| | |
|---|---|
| Master file | `Ann Connor - John McMillan Lecture (25 September 1983).m4a` |
| Format | ALAC 48 kHz stereo 16-bit (lossless) |
| Duration | 1,871.445333 s (31 m 11 s) |
| Size | 60,417,099 bytes |
| sha256 | `fa8c8fe039dfee3da9675fb74037862cede120a6f474a3490d2f20e4bda609a8` |
| md5 | `6c9a120aa52d6f650473ba60d740ce66` — recomputed here, identical to the md5 in the source notes |
| Mean level | −39.5 dBFS |
| Peak | −8.0 dBFS |
| Bit rate | 258 kbps |

Duration, format, sample rate, channel count, size, sha256, md5, mean level and peak were measured
on the master for this record (`ffprobe`, `hashlib`, `ffmpeg volumedetect`). The level figures agree
with the source notes to the decimal; nothing was re-processed to produce them.

**It is a quiet capture.** −39.5 dBFS mean is 16 dB below the 1983 Bethel panel in this same set
(−23.1 dBFS), and the source notes record that it is even across the file — 31 one-minute blocks all
peaking between −8.0 and −20.7 dBFS. That is why the listening MP3 made by the archive carries
+20 dB of gain and a limiter; the master does not, and this repository's transcripts were made from
the master.

**How the file was found.** It was sitting inside the archive's `JD Patterson - Side A/` folder under
the name `Ann-Connor John McMillian 9-25-83.m4a`, with a byte-identical second copy loose at the
archive root at the time (both copies md5 `6c9a120a…`). The source notes record that the md5 was
verified before and after the move to its own folder, and that the duplicate is kept under
`superseded/backups/`. The filename reads "Ann Connor, on John McMillan, 9-25-83" — McMillan is her
**subject**, not a participant. He died in 1853 and cannot be a voice on a 1983 tape.

**Stereo.** The source JSON records the pair as a **delayed duplicate**: a constant 5-sample
(0.10 ms) lag at r = 0.977–0.990 across eight 30-second windows, with channel 1 3.2–3.7 dB stronger
throughout. The working copy was summed 2:1 toward channel 1 with the lag compensated. That
measurement was made during transcription and is reported here from the JSON; it was **not**
re-measured for this package.

## 3. What was done to it (the method, as the source notes record it)

1. **No re-mastering.** The master is the capture as received: no gain, no denoise, no cropped dead
   tape. Speech runs 0:11–30:50; only the first ~9 s and last ~15 s are real silence.
2. **Chunked, never whole-file.** 16 chunks of ~120 s, each boundary snapped to the quietest 10 ms
   frame within ±5 s of its target.
3. **Seeded prompt**, corroborated names only: McMillan, Clark, Woods, Marshall, Wycoff, Reiter,
   Chartiers, Mingo Creek, Canonsburg, Bethel Academy, Oliver Miller Homestead, Dido, Doddridge,
   Princeton Theological Seminary, Croco, Strobl, Coverdale, Slumbury.
4. **Prompt-leak check, and repair.** The seed leaked at four chunk heads, each a segment made 100 %
   of seed tokens (13.9–29.7 s, 355.6–385.5 s, 713.6–743.6 s, 954.2–984.2 s). Every span was
   re-transcribed **un-prompted and spliced back**; nothing was deleted. The first leak had
   overwritten the host's opening sentence and the second had swallowed a whole aside ("could I have
   some questions? Or you haven't thought of any yet?").
5. **Chunk seams repaired by content, not by eye.** Overlapping seams had dropped segments whose
   start fell just before the previous segment's end; the de-duplication now trims only the
   duplicated prefix. Four recovered passages are named in the source notes, and two clauses lost at
   a seam were restored verbatim from an un-prompted pass.
6. **Read end to end** — all 276 segments — and corrected by sense as well as by name.
7. **Every change recorded** in the source JSON's `post_edits`: the raw ASR form, the replacement,
   the reason and the certainty. 203 entries.

## 4. The engine, and what it measured

| | |
|---|---|
| Engine | Whisper **large-v3**, Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads |
| Decoding | `en`, `beam_size=5`, `condition_on_previous_text=False`, `temperature=0.0`, `compression_ratio_threshold=2.4`, `vad_filter=False`, word timestamps |
| Audio path | ffmpeg → float32 numpy arrays (PyAV in this build rejects the `metadata_errors` kwarg faster-whisper passes) |
| Segments | 276 |
| Words | 4,585 |
| Mean per-word probability | **0.9386** |
| Words below 0.5 | 3.20 % (7.57 % below 0.7) |

Only **one** engine was run on this item. The 1971 A.D. White interview beside it in this repository
carries a second, GPU-engine cross-check with a measured WER; there is no equivalent run for this
lecture, so no inter-engine agreement figure can be quoted here.

The weak stretches are the band-limited passages at 11:50–12:40 (a digression on school English) and
2:50–5:50 (the book discussion, two voices at a distant microphone). The lecture body from 6:33 runs
clean.

## 5. Corrections (203 `post_edits` entries, all reversible)

The substantive ones, with the reason each was changed:

| heard | changed to | basis | certainty |
|---|---|---|---|
| "shark ears … pigeon cream" | Chartiers … Pigeon Creek | the two congregations he served; both named again at 26:36 | certain |
| "charters church" | Chartiers Church | built 1778 | certain |
| "Cairnsburg", "Canberra College" | Canonsburg, Canonsburg College | Washington County; said correctly later in the same passage | certain |
| "secretary of the church", "Secretary of the Treasurer" | Secretary of the Treasury | Gallatin's office | certain |
| "knee bridges" | knee breeches | the buckles he used for them | certain |
| "mcnellan", "Mcnone", "McGowan" | McMillan | the same man; she says it correctly a line later | certain / probable |
| "the John McMillan's" | the John McMillans | the family, plural | certain |
| "Mignola clan" | McMillan clan | "the beginning of the McMillan clan with Dr. John McMillan" | probable |
| "plantation of ulster" | Plantation of Ulster | the 1609 plantation | certain |
| "checked his gut" | checked his gun | "he carried his guns with him" | probable |
| "a linear descendant" | a lineal descendant | standard phrase | probable |
| "out of laws" | out of logs | the log church of 1778 | probable |
| "take a stamp" | take a stand | the sense of the passage | probable |
| "Dr. John Park" | Dr. John Clark | the three men are Clark, his adopted son William Jones, and his son | probable |
| "MacMillan" (×2) | McMillan | one spelling throughout | certain |
| "Thank you." at 31:05 | **not resolved — see §6** | the source notes contradict themselves on this one | — |

Mechanical work alongside: doubled words across chunk seams ("needed needed", "That That"), sentence
and proper-noun case, and one "World War II" duplicated across a seam resolved by clause order.
Hesitations and false starts were left alone.

## 6. Left as heard — the honest gaps

- **The date is filename-supplied.** There is no slate. If `9-25-83` in John Decker's capture name is
  wrong, the item's date is wrong, and nothing in the audio would catch it.
- **The surname is not on the tape.** Ann is addressed and referred to by first name only; "Connor"
  is the archive's attribution. Her husband and the host are unnamed.
- **The trailing "Thank you." is contradictory in the source.** The `.srt` carries it as cue 276 at
  31:05, ten seconds after speech ends and in near-silence (the 31:00 block measures −59 dB); the
  `.md` and `.txt` do **not** carry it. The source notes list it in the corrections table as
  *removed* and in the unresolved list as *kept as heard*. Both files are reproduced here exactly as
  the archive holds them, so the discrepancy is visible rather than tidied away. On the audio
  evidence it is an ASR hallucination over room tone and should not be quoted.
- **Ten unresolved readings** in the source JSON, kept as heard: "I called it my center hole" (~3:08,
  the husband's name for his reproduction of the 1935 photograph); "a Director of the Senate" (~3:42,
  of the artist Gail Boak's wife); "George Briggs" (13:06, a curriculum subject); "the joint germ"
  (29:10, probably the jointure of the two colleges); "Natural Ridge" (15:05, where McMillan preached
  in Virginia — no such place found, possibly Natural Bridge); "Paul Mandel" (25:53); "Bennett's
  book" (the 1935 genealogy she calls her supplement to — the compiler's full name is never given);
  "he practically rattled a preaching" (22:13, garbled); the crossing-out and restart in "his weak, I
  mean, his strong voice"; and the dictionary clause at 12:34–13:00, whose word order is as spoken
  but whose exact wording is not recoverable.
- **The 2:17 interjection.** "Oh, very handsome" is Ann's, but it sits inside her husband's turn
  because the ASR merged it into his sentence. It is not split out.
- **Rights.** The public-domain status recorded in `metadata.json` rests on the collection-level
  release in `docs/RIGHTS.md`. No per-item release document is in the source folder.
- **Not re-measured here:** the per-minute level sweep, the stereo lag/correlation figures and the
  MP3's loudness. They are quoted from the source JSON and notes, attributed as such.

## 7. What is on the tape — outline with timestamps

- **0:11** The host introduces Ann: "I don't think anyone like Ann has spent so much time in the
  history of the church"
- **0:34** McMillan's saddlebag ("what quite often was his pillow") and the buckles from his knee
  breeches, borrowed from a direct descendant, Sam McDowell
- **1:19** Her husband takes over with the 1935 McMillan reunion photograph (1:48), reproduced and
  numbered by hand; reunions every three years
- **3:36** The book: artwork by Gail Boak, calligraphy and compiling by Ann; 12 years collecting and
  3 more assembling
- **4:05** It is a supplement to **Bennett's book** (1935), carried forward to publication in 1981
- **5:09** What a genealogy cannot say — divorces, separations, "put this wife in and don't put that
  one"; what she keeps confidential
- **6:16** An invitation for questions before she starts
- **6:33** **Scotland**: the McMillans "being mistreated"; why the Presbyterians had to leave
- **7:30** A digression on **John Clark** and his adopted son **William Jones** — 59 years in the
  ministry, 20 children, six of them doctors; over 150 years of ministry across three men
- **9:14** The **Plantation of Ulster**, six counties, James I
- **10:27** Passage to America, and the 25,000 Scotch-Irish into western Pennsylvania from 1769
- **11:20** McMillan at school to 13, Princeton to 18; Latin grammar schools and why they wrote good
  English
- **12:34** Dictionaries and the two Englishes; "George Briggs" (13:06)
- **14:23** Graduated **1772**; the **Donegal Presbytery**; Virginia and "Natural Ridge" (15:05)
- **15:19** Chartiers and Pigeon Creek — "he felt he was home"
- **15:49** 30–35 miles a day on horseback; ordination in June; married in August; the wife and child
  brought over two years later (16:50), and the forts
- **18:14** How Presbyterian families schooled their sons; free education for the poor
- **19:20** The **College of New Jersey** (Princeton) under **John Witherspoon**; the 5 a.m. rising,
  chapel at 5:30, Greek and Hebrew read aloud in English
- **21:07** Ordination **19 June 1776**; "no conversions are affected beyond the hour"
- **21:49** "He practically rattled them out of hell"; the voice heard a mile away; the one regret
  about his voice (22:13)
- **22:41** The other half of his preaching — love, compassion, kindness; people falling over
- **23:38** He carried his guns; a neighbouring preacher checked his before the sermon
- **24:45** **Albert Gallatin** and the Secretary of the Treasury; McMillan in politics
- **26:36** The fourth Sunday of August 1775 at Chartiers; the log church of **1778**; no heat, no
  instruments
- **27:02** The **Stone Church** at Hill Church, 1800, enlarged 1832; the revival preacher (27:14);
  "you cannot become a Presbyterian minister unless you have been born again" (27:41)
- **28:05** **Jefferson College** and the academies at Canonsburg and Washington
- **29:03** The Canonsburg–Washington feud, the 1960 high school, "the joint germ" (29:10)
- **29:53** **Jefferson Medical College**, Philadelphia
- **30:13** **Xenia Seminary**, Old Allegheny, later united with Pittsburgh Seminary
- **30:41** "The McMillans were basically people who could save a great deal of money" — and the tape
  ends mid-thought at 31:05

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The transcript: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt` | The same text as timed cues (276), for playback or captioning |
| `notes-a.md` | The archive's working notes: measurements, engine settings, leak repair, every judgement call |
| `metadata.json` | The record of record: date and its source, speakers, master with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

`transcript-a.md`, `transcript-a.srt` and `notes-a.md` are **byte-for-byte copies** of the archive's
files of the same stem, taken on 2026-10-23. Nothing in them was edited for this repository; the
"Side A" label in `metadata.json` names the single file, not a cassette side — this capture has no
side break.

The audio master is **not** here (see `docs/AUDIO.md`): it is held on the archive NAS, identified
above by sha256.

## 9. Citing it

> Connor, Ann. *Lecture on the Reverend John McMillan*. Lecture for the Historical Room, Bethel
> Presbyterian Church, 25 September 1983. Historical Room, Bethel Presbyterian Church: digitised
> 20 October 2026. Transcript, 4,585 words.

Cite the timestamp for anything quoted — the transcript keeps the tape's own timebase, so a claim can
always be checked against the master. Note that the surname is not spoken on the tape; cite "Ann
Connor" as the archive's attribution, not as something the recording says.

## 10. Reproducing this transcript

The environment is pinned in `docker/`. What this recording used:

- model: large-v3, CTranslate2 **int8**, language `en`, **beam 5**, 14 threads
- `--chunk-seconds 120`, snapped to quiet points: **16 chunks**
- seed: the archive's corroborated name list, with a leak check and four un-prompted splices
- input: the 2:1 channel sum described in §2 — not the raw stereo master

A re-run on the same master, engine and settings reproduces the raw ASR text. The filed transcript
differs from it by the 203 `post_edits` in the source JSON, each of which names its reason and
certainty and can be reverted in one line.

## 11. Related material in the collection

- **`1983-09-25-valentine-maits-snowden`** — the three-voice panel recorded the **same day**, on the
  same subject. They agree on the ministers' names (Clark, McMillan, Marshall) and on the 1776
  founding, and they **differ on when McMillan began to preach here**: the panel says from 1775 and
  for 55 years into 1830, this lecture says he arrived in 1775 and was ordained in June 1776. Neither
  reading is corrected; the disagreement is left where it is.
- **`1977-11-06-ann-connor-bethel-needlepoint`** — Ann Connor five years earlier, teaching children
  the same McMillan and Miller history.
- **`1971-07-15-ad-white-cross-creek`** — A.D. White's interview, the collection's other long
  first-hand account of the church's records.
