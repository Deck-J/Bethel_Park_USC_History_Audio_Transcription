# Ann Connor — a tour of the Historical Room, sides A and B (c. 2001)

Two cassette sides of the woman who built the Historical Room walking a visitor through it, case by
case: the Marshall desk, the Miller family Bible, the Academy bell, John Clark's slaves, the pewter,
the pew-rental indentures, the communion tokens. It is a tour rather than an interview — the questions
come from off-mic, and the room, not the questioner, sets the order.

| | |
|---|---|
| **Speaker** | Ann Connor, of Bethel Presbyterian Church, Bethel Park, Pennsylvania |
| **Interviewer** | unidentified; at least one voice off-mic, never named on the tape |
| **Recorded** | c. 2001, place not stated. Exact date **unknown** — see §1 |
| **Length** | Side A 46 m 13 s + Side B 46 m 42 s = **1 h 32 m 55 s** |
| **Words** | 11,018 in the filed transcript (5,219 + 5,799), speaker-labelled |
| **Status** | Transcribed, fact-checked against the 1951 church history, labelled; masters on the archive NAS |

---

## 1. How the date is established — and why it is not

**It is not.** There is no slate, no label read aloud, and no year spoken anywhere on either side. What
the recording does say fixes it only to a year:

> "you can't ring the bells 225 times, but you could ring it two, two, five … that would be giving you
> your 225th anniversary" — Side B, 18:11

The congregation dates itself from John McMillan's meeting of 5 November 1776, which she names on
Side A at 2:44; 1776 + 225 = **2001**, and she speaks of the anniversary as work in hand ("we're
working on the 225th anniversary", "on the 22nd of July, we're going to do that skit down in the
homestead"). The archive's own transcript header records "recorded c. 2001". That is a year, not a
date: the day and month are not recoverable from the material, so `metadata.json` carries
`date: "unknown"` and this reasoning in `date_source`.

Two other dates are in circulation and neither is the recording date: **2026-10-18** in the source
folder name is the digitisation date, and the transcription files' timestamps are 2026.

## 2. The audio, as measured

Seven audio files are held for this item — the two ALAC masters, two MP3 access copies, and a *second,
earlier capture of Side A* with two derivatives. All seven are listed in `metadata.json` `sides[]`,
each with its own sha256; none is in this repository.

| | file | format | length | size | mean / peak | sha256 (first 12) |
|---|---|---|---|---|---|---|
| Side A master | `… Side A.m4a` | ALAC 48 kHz stereo 16-bit | 2,773.248 s (46:13.25) | 95,038,489 B | −27.8 / −4.3 dBFS | `ba58608dfda5` |
| Side A copy | `… Side A.mp3` | MP3 48 kHz mono 64 kbps | 2,773.200 s | 22,186,228 B | — | `5f6578a7e3df` |
| Side B master | `… Side B.m4a` | ALAC 48 kHz stereo 16-bit | 2,801.749 s (46:41.75) | 106,884,706 B | −33.2 / −2.3 dBFS | `51b20ac45316` |
| Side B copy | `… Side B.mp3` | MP3 48 kHz mono 64 kbps | 2,801.692 s | 22,414,324 B | — | `60b8847dd68f` |
| Side A, original capture | `audio_106911687b1d.m4a` | AAC 48 kHz mono 58 kbps | 2,761.792 s (46:01.79) | 20,010,825 B | **−44.1 / −17.8 dBFS** | `aa337e4cab60` |
| "2026-10-18 capture", lossless | `… (2026-10-18 capture).flac` | FLAC 48 kHz mono 16-bit | 2,761.792 s | 121,225,023 B | −17.9 / −1.5 dBFS | `32eee074954b` |
| "2026-10-18 capture", MP3 | `… (2026-10-18 capture).mp3` | MP3 48 kHz mono 192 kbps | 2,761.792 s | 66,284,955 B | — | `cf2419d6641e` |

**What the two captures of Side A are.** The AAC file is a very quiet mono original — 26 dB below the
deliverable masters. The FLAC is the same programme, the same length to the millisecond, and **31.9 dB
hotter** (measured on a 90 s window at 10:00); a 1 Hz energy-envelope cross-correlation of the two full
sides peaks at **0 s lag with r = 0.80**. So the FLAC is a gain-raised lossless rendering of the
original capture, not a separate transfer, and the MP3 beside it is a 192 kbps derivative of the FLAC.

The ALAC master is a *different* transfer. It runs **11.456 s longer**, and the same envelope
correlation puts it **17 s behind** the original capture at the head (r = 0.48) — a longer leader on a
separate pass, not a transcode. The exact edit is not reconstructed here; what matters is that the
transcripts follow the ALAC masters (the longer files), and that the original capture is preserved
untouched beside them.

**Stereo.** Side A is the familiar delayed-duplicate case: channels 2.7 dB apart, correlation 0.986–0.993
at a constant 3-sample (0.19 ms) lag, so they were summed with the lag compensated. Side B is not:
channel 1 is 7.1 dB weaker in all 47 one-minute blocks measured and never louder, coherent with channel 0
at r ≈ 0.98 on a 5–6 sample lag, so **channel 0 was used alone** rather than adding a weaker copy's noise
at full weight. In both cases the measurements are in the source JSON, not assumed.

**Levels.** Nothing was normalised, denoised or limited for transcription. Side B's lower mean is the
stereo mix (−31.0 dBFS on channel 0 alone, second channel quieter); it is a quieter side, not a damaged one.

## 3. Transcription

- **Engine:** Whisper large-v3, faster-whisper (CTranslate2 int8), CPU-only, 14 threads, `en`, beam 5,
  `condition_on_previous_text=False`, word timestamps, `vad_filter=False`.
- **Chunking:** 24 chunks per side, ~120 s windows snapped to the quietest 10 ms point within ±5 s of each
  mark — never a whole-file pass.
- **Seed:** a prompt naming the collection's recurring names (McMillan, Reitter, Marshall, Kroko, McMaster,
  Bethel Academy, Oliver Miller, Spencer Watson). On Side B the prompt **echoed over real speech** twice,
  at 358.77–372.37 s and 476.41–491.61 s; both regions were re-transcribed **without the prompt** and the
  recovered text substituted. The echoed strings are kept in the JSON (`prompt_leaks_removed`), so the
  record shows both what the model printed and what was said.
- **Quality, as the engine reported it:** Side A — 368 segments, 5,220 words, mean per-word probability
  **0.888**, 7.7 % of words below 0.5. Side B — 495 segments, 644 cues, 5,715 words, mean **0.888**,
  8.1 % below 0.5. The weakest Side A stretch is 330–360 s (mean p 0.55): two people talking away from
  the microphone. It is flagged in the JSON and treated as indicative, not quotable.
- **Labels:** `ANN` (main speaker), `INTERVIEWER` (question syntax, backchannels, prompts),
  `OTHER` (a third voice in the room). No diarisation: where two speakers run inside one segment the split
  is by text, so a turn boundary can be off by a clause.

There is no separate per-side transcript in the archive. `transcript-a.md` and `transcript-b.md` here are
the **merged, labelled transcript split at the side boundary** — the first line of `transcript-b.md`
("He would be in Washington, PA …") is the first line of Side B — with the side-B header written for this
folder. The per-side `.txt` files in the source folder are the same text without speaker labels and differ
from it in about 2 % of tokens (labels, casing, later corrections).

## 4. Corrections (18 logged, plus 18 from the fact-check pass)

Every change is a `post_edits` entry in the source JSONs — six on Side A, twelve on Side B — with the
reason and a certainty. Representative:

| heard | changed to | basis |
|---|---|---|
| "Raymond Ryder", "Reitter", "River Ryders" | Rev. Murray C. **Reiter** | 1951 history: fifth minister, 1914–1946; 82 occurrences, zero "Reitter" |
| "Kroko", "Grokos", "a croquette" | **Croco** | 1951 history (34×), incl. the roll entry "Miss Edna M. Croco" |
| "the Mishnah" | the **Coverdale** mission | Coverdale was a Bethel mission from 1924 (client-supplied, corroborated) |
| "46 ministers are Berry here" | "**The first six** ministers are **buried** here" | ASR collapsed "the first six" into a numeral and "buried" into a name |
| "What happened today is not mentioned in the will" | "What happened **to Dave in** the will" | the question is about Dave, the male slave in the inventory |
| "Carla terrible" | **Carla Strobl** | 1951 history "Miss Karla R. Strobl", Presbyterial missionary; family spells Carla |
| "Aldermiller Homestead" | **Oliver Miller** Homestead | the sibling recording of the same tour |
| "Mango Creek Escruterian" | **Mingo Creek Presbyterian** | the congregation's own history |
| "Wyckoff" | **Wycoff** | 1951 history, 111:0 |
| "Hilt Church" | **Hill Church** | Reiter was pastor of "the Chartiers or Hill Church" |

A separate **fact-check pass** (recorded in `notes-a.md`) applied 18 more, and a **review pass**
(`notes-b.md`) lists 29 further candidates — rubbings, mulatto, Dido, yoke of oxen, whooping cough,
"Know all men by these presents", pew number 39, Bethel token — that were **proposed and not applied**.
They are not corrections; they are a to-do list, and the text here still reads as it did before that pass.

## 5. What is uncertain

- **The recording date**, as above: a year at best.
- **The interviewer** is never named; the archive's transcript does not name one either.
- **The surname Connor** is never spoken. Only the first name is, at ~8:50 by another voice ("now we're
  recording Ann as she's discussing"). The surname comes from the family and the filename.
- **"Frank Ear", the artist** (3:46) — the audio says something closer to "Frank Geer"; unresolved.
- **"Robert Bryder"** (39:39), **"John McMiller"** (40:44, almost certainly McMillan), **"Paul Caulgolden,
  C-A-U-L-G-O-L-D-E-N"** (41:45, spelled on tape, no match found), **"Thomas Cadoux"**, **"Russell Low"**,
  **"Rev. Dean and Stella Walder"** — names as heard, uncorroborated.
- **"Decman City, Washington"** (Side B 0:xx, in Marshall's letter about Jefferson College closing) — checked
  against Deemston, Donegal and Dutch Fork; nothing fits, so it stands as heard.
- **"Service Seminary / Princeton Service Seminary"** was changed to Princeton Theological Seminary on
  instruction, with a caveat recorded in the fact-check: Service Theological Seminary (Service, Beaver
  County, 1794) is historically attested, and the identification should be reviewed.
- **Vocatives that do not fit**: "Bev" (00:54) and "Beth" (00:56) where the speaker elsewhere calls her Ann.
- **Two fragmentary passages** at Side B 44:30–45:00 and 45:30–46:00, where the room talk collapses.

## 6. What is on the tape

**Side A (46 m 13 s)** — the tour, west wall first

- **0:00** Why the room exists: a history teacher's objection to "items scattered here and there"; she
  asked for Reiter's old study on the second floor; her husband John helped put up the cases
- **1:27** Marshall's schoolmaster's desk, and Bethel Academy as the church's own school
- **2:19** Where to start a tour: the Oliver Miller Homestead picture and the Miller family Bible —
  "the birthplace of our church", McMillan's meeting of **5 November 1776**
- **3:11** The buildings: a log church across the street, two red-brick houses, the present fourth
  building of **1910**; brick from the earlier churches reused inside the bell tower
- **6:35** The Miller family Bible and what a family Bible records
- **10:17** The one known photograph of a Bethel Academy class — co-educational, and a Croco in it; a
  present confirmand, Jenna Nestor, is a Croco descendant
- **12:46** George Marshall: taught at **Cross Creek Academy** while studying under Dr. John Stockton,
  then Jefferson College; Greek and Latin; the open Bible on his tombstone
- **13:44** **1856**: the two-storey academy at the southeast corner of the cemetery; torn down c. 1880,
  its bell moved to the third meeting house, then to this building — "the bell you hear every Sunday"
- **15:30** The Academy's debating society, and the slide from "trivial and laughable" subjects into
  slavery as the war approached; a debater who did not appear because he had enlisted
- **18:43** John **Gilfillan**, wounded at Fair Oaks, brought home by his brother, dead before he arrived
- **21:00** Taking schoolchildren through the cemetery: the rules, the crayons, the rubbings
- **23:03** The rubbing of **John Clark**'s stone (1718–1797), and why the metal plaque exists
- **26:26** Clark renamed West Peters Creek **Bethel** (and East Peters Creek Lebanon); his part in the
  Whiskey Rebellion
- **27:40** **Dido and Dave**, bought in Maryland; the orphan William Jones; Dave and the oxen
- **29:40** Clark's will: "my mulatto", a feather bed, and three volumes of Doddridge — evidence she could read
- **31:52** McMillan as executor: the expense account, coverlets, doctor's bills, 25 cents a month for snuff
- **33:40** Dido sent to the **poorhouse**; the W&J appeal that funded one year only
- **34:07** The unnamed poorhouse graves on the hillside above the Washington County fairground
- **36:02** Dave in the 1797 inventory: "one yoke of oxen at 15 pounds"
- **39:11** Which ministers are buried here — the first six
- **41:14** **Spencer Watson**, the McMaster farm's hired man, in Paul Caulgolden's written account

**Side B (46 m 42 s)** — the cases and the small objects

- **0:06** Marshall's letter on Jefferson College closing — "that Decman City, Washington, was appalling"
- **1:52** The **cooler** from the third meeting house, and the boy whose job was to fill it
- **2:35** McMillan's **saddlebags**; his journal; the horse that bolted and the lonely log cabin
- **8:57** The **broad axe** for squaring logs
- **10:35** Bob Wycoff's photograph; the silver service
- **11:10** The **pewter communion service**, bought from Reed & Barton between 1835 and 1840 — "the most
  complete unit … anywhere in this country"
- **13:00** Betty May's **communion cutter** and the shortbread recipe
- **15:28** Edna Croco's apple-butter stirrer, made from a floorboard of the Academy; the Croco Hessian
- **17:27** The two **hand bells** from the Academy, and ringing 2-2-5 for the anniversary
- **19:08** The **passing bell** — rung for her husband John
- **21:41** Marshall's **travelling chest**; the European trip with Thomas Cadoux, by canal
- **23:13** The "marryin' and buryin' suit"; Reiter's coat beside it
- **24:19** Marshall's family Bible, the common cup, whiskey as the everyday drink — and the McMillan /
  Joseph Patterson story: "you must learn to watch as well as pray"
- **26:31** Temperance in the ledgers of James Miller: whiskey sales falling from c. 1825, gone by 1830
- **27:56** The brown vases from the third meeting house, out of place on this wall
- **30:33** The rice-straw **collection basket** (her copy; the original is at Mingo Creek)
- **32:35** **Pew rental**: the 1825 and 1850 indentures, pew 39, the 1864 gallery; "Know all men by these presents"
- **34:53** **Communion tokens** — Mingo, Mount Pleasant, Bethany (given in 1971), and not one from Bethel
- **37:23** The **Whiskey Rebellion** split in the congregation; the Millers' bankruptcy; McMillan's threat
  to withhold communion; Clark riding out to the Whiskey Boys at Fort Couch
- **41:34** Reiter at Hill Church; the church's birthday made official; horse, then car, then camels
- **43:48** **Karla Strobl** and the Coverdale mission; the rope the children held on to

## 7. Files here

| file | what it is |
|---|---|
| `transcript-a.md`, `transcript-b.md` | The labelled transcript, split at the side boundary. **Start here.** |
| `transcript-a.srt`, `transcript-b.srt` | The same text as timed cues (449 and 644 cues) |
| `notes-a.md` | The fact-check record (18 entries, both sides) — copied from the source folder |
| `notes-b.md` | The misplaced-word review (29 proposals, **not** applied) — copied from the source folder |
| `metadata.json` | Dates and their source, speakers, all seven masters with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder |
| `README.md` | This file |

The audio masters are **not** here. They are on the archive NAS, identified above and in
`metadata.json` by sha256; see `docs/AUDIO.md`.

## 8. Citing it

> Connor, Ann. *A tour of the Historical Room*. Interview by an unidentified interviewer, c. 2001.
> Historical Room, Bethel Presbyterian Church: digitised 18 October 2026. Transcript, 11,018 words.

Cite the timestamp for anything quoted: the transcripts keep the tape's own timebase, so every claim can
be checked against the master.

## 9. Related material in the collection

- **A.D. White**, Cross Creek records and the Whiskey Rebellion, 15 July 1971 — the same room, twenty
  years earlier, and the source she names for several of these stories ("I think we have a tape of him,
  don't we Ann"); the Russell Low communion token in her case came from him.
- **Edna Croco interview** — the Croco family whose Academy photograph and apple-butter stirrer she
  discusses at Side A 10:17 and Side B 15:28.
- **Ann Connor, John McMillan lecture, 25 September 1983** — the same speaker, the same subject matter,
  in lecture form.
