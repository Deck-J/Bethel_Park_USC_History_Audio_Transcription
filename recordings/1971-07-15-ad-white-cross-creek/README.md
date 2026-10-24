# A.D. White — Cross Creek records and the Whiskey Rebellion (15 July 1971)

Oral history recorded for the Historical Room at Bethel Presbyterian Church, Bethel Park,
Pennsylvania: the church's own historian talks through the records he has spent his life reading, and
reads a Civil War letter aloud in full.

| | |
|---|---|
| **Speaker** | Alvin Dinsmore White, of Hickory, Pennsylvania |
| **Interviewers** | Ann Connor and John Connor |
| **Recorded** | Thursday, 15 July 1971, at Hickory, Pennsylvania |
| **Length** | Side A 31 m 12 s + Side B 20 m 15 s = **51 m 27 s** of programme |
| **Words** | 6,525 (3,884 + 2,641), speaker-labelled |
| **Status** | Transcribed, corrected, labelled, verified; audio masters held on the archive NAS |

---

## 1. How the date is established

The date is **on the tape**, not inferred: Side A opens with a copyist's slate, added when the cassette
was duplicated —

> "…a record of the interview of Mr. A.D. White and his wife by Ann Conner and John Conner."
> — 0:10–0:30, labelled `NARRATOR`

The slate gives "July the 15th, a Thursday evening, 1971"; **15 July 1971 was a Thursday**, so the
reading is internally consistent. Side B carries no date of its own and is dated from that slate.

Two dates are *not* the recording date and are often mistaken for it:

- **2026-10-18** in the archive's folder name is the **digitisation** date.
- The ASR transcript's file timestamps are the transcription date (2026-10-23).

## 2. The physical recording and its capture

The source is a cassette, duplicated at least once (hence the slate), played back and captured as ALAC
— lossless, so nothing in these transcripts was limited by a lossy intermediate.

| | Side A | Side B |
|---|---|---|
| Master file | `Side A.m4a` | `Side B.m4a` |
| Format | ALAC 48 kHz stereo 16-bit | ALAC 48 kHz stereo 16-bit |
| **Length as received** | 1,872.043 s (31 m 12 s) | 5,721.685 s (1 h 35 m 22 s) |
| **Programme used** | 1,872.043 s — the whole side | **1,215.061 s (20 m 15 s)** — 75 m 07 s of tape left running was cropped |
| Size | 83,169,298 bytes | 56,300,439 bytes |
| sha256 | `e2169af30fba84291e0a1b997b2d7aef76a14b16d1083c3668ce5491511be28f` | `fe0363c0cf0cc644eec1bc8097c5ba04bca0856abcd38d88181ac8f150e92698` |
| md5 (capture record) | `7494fde23b36fb686982332a1432efe7` | — |
| Mean level | −23.5 dBFS | −21.9 dBFS (probe) |
| Peak | −1.2 dBFS | −4.3 dBFS (probe) |

**Side B's dead tail.** The capture runs 1 h 35 m but the conversation ends at about 20 m 04 s and the
tape then runs silent to the end of the file. A 1-second sweep of 1,204–1,222 s put the last speech at
~1,204 s; the programme was cropped at **1,215 s**, leaving eleven seconds of room tone rather than
cutting on the last phoneme. Nothing was discarded but the silence — the untouched capture is kept as
received and is the file the checksum above describes.

**Stereo.** Both sides are effectively mono recorded twice: the two channels are the same signal with
one copy delayed **6 samples** (0.125 ms at 48 kHz) and about 2.7 dB hotter. Left/right correlation is
**r ≈ 0.99** at that constant lag, so the channels were aligned (channel 0 delayed 6 samples) and
summed 0.5/0.5 for the transcription pass — no denoise, no gain, no channel discarded.

## 3. What was done to it (the method)

1. **Measure before touching.** Duration, levels, per-minute level sweep and peak, to catch a level step
   or a second session on one side. Side A is even (−21.6 to −25.7 dB mean per minute); there is no
   join.
2. **Check the stereo relationship** rather than assuming it: correlation and lag sweep to establish
   the channels are a delayed duplicate, then align and sum.
3. **Chunk on quiet points, not on the clock.** 120 s windows snapped to the quietest nearby sample, so
   no chunk begins mid-word. 17 chunks on Side A, 11 on Side B.
4. **Transcribe with a seeded prompt** carrying the collection's standing name list — Bethel, Snowden,
   Chartiers, Canonsburg, Mingo Creek, Peters Creek, Thomas Mill, Gill Hall, Cochran Mill, Oliver
   Miller Homestead, Bethel Academy, Stone Manse, Princeton; McMillan, Clark, Woods, George Marshall,
   Wycoff, Reiter, Tidball, Wolfe, Croco, Strobl, McCully, Stilley, Webb Murray, Maits, Valentine,
   Connor, Patterson, Douglas, Miller/Millar, Fife. This biases the engine toward the names that are
   actually in these recordings; a seed-leak check confirmed none of the list appeared as content.
5. **Run the engine twice, on both sides**: faster-whisper large-v3, CTranslate2 int8, beam 5 — the
   archive's pinned CPU engine (`whisper-worker:v0.3`), 14 of 16 threads.
6. **Cold passes on the garbled stretches** — nine un-prompted windows re-transcribed without the seed,
   so a prompt cannot paper over a bad reading. They settled several readings and overturned two (see §5).
7. **Correct, and record every correction** in `metadata.json`… no: in the sibling JSON's `post_edits`
   — find, replace, reason, certainty. Nothing is silently rewritten.
8. **Label the speakers** — `WHITE`, `INTERVIEWER`, `NARRATOR`, `UNKNOWN` — and join run-on fragments
   and stutters, dropping filler only.
9. **Build the documents from the labelled text** (`transcript-a.md`, `transcript-b.md`, plus `.srt`
   cues), then verify: the documents are regenerated from the transcript and compared, not eyeballed.
10. **Archive the checksums** and keep the masters out of this repository (see `docs/AUDIO.md`).

## 4. Engines, and what they measured

Both engines ran the **same chunk boundaries and the same seed**, on the same summed audio, so their
outputs are comparable.

| | CPU — faster-whisper large-v3 int8, beam 5 | GPU — openvino-genai large-v3 int8, greedy |
|---|---|---|
| Side A words | 3,833 | 3,824 |
| Mean word probability | **0.909** (5.5 % of words below 0.5) | not reported |
| Side A wall-clock | 1,140 s — 1.6× realtime | 205 s — **9.1× realtime** |
| Agreement with the filed text | — (reference) | WER **0.063** (93.7 % word agreement) |
| Side B | 1,215 s of audio, 11 chunks | WER **0.113**, 3.4× faster than CPU |

The filed transcripts are the **CPU** engine's. The GPU engine was faster and was **retired on
2026-10-23**: it reports no per-word probabilities, decodes greedily only (GPU beam search is
unimplemented in OpenVINO), and its text sits 6–11 % away from the CPU's — a different document rather
than the same one sooner. `docs/AUDIO.md` and the `whisper-worker` repo's `docs/GPU.md` carry the
measurement.

## 5. Corrections made (24, all reversible)

Each is a `post_edits` entry in the JSON that ships beside the transcript: what the engine heard, what
it was changed to, why, and how certain that is.

**Side A — 14**

| heard | changed to | basis | certainty |
|---|---|---|---|
| Cannonsburg | Canonsburg | the borough's name | certain |
| "I claim, in fact, that I was incestuous married at one time" | "They claim, in fact, that it was an incestuous marriage at one time" | two cold passes agree | probable |
| Dr. Stockman | Dr. Stockton | John Stockton was Cross Creek's minister | probable |
| Dr. Stockley | Dr. Stockton | same man; cold pass returns "Dr. Stock…" | probable |
| the Craftsman Academy | the Cross Creek Academy | the academy under discussion | probable |
| built in 1958 | built in **1858** | Cross Creek Academy predates Marshall's death (1868) | probable |
| Borgon | Morgan ("the Raider") | John Hunt Morgan; Morgan's Raid, July 1863 | certain |
| mrs mates | Mrs. **Maits** | archive spelling | certain |
| the stone man's | the **Stone Manse** | the church's minister's house | certain |
| "George Martin. Marshall. Marshall, partner." | George Marshall | the letter's signer; the ASR split the name | probable |
| in standard cross | at Cross Creek | the burial island is in Delaware Bay | probable |
| Cross-Crick's Academy | Cross Creek's Academy | same academy | probable |
| Marvin Marshall | Reverend Marshall | Simpson's note, communion assistance | probable |
| "under impairment site of one eye" | "under impairment of sight of one eye" | "site" mishears "sight" | certain |

**Side B — 10**

| heard | changed to | basis | certainty |
|---|---|---|---|
| Colorado Atlas of Washington County | **Caldwell's** Atlas of Washington County | the 1876 county atlas | probable |
| the latimers | the Latimers | the county history he asks for | probable |
| sim green | Sam Green | county-history author named with Latimer | probable |
| reverend clark | Reverend Clark | John Clark, Bethel's first pastor | certain |
| whiskey rebellion | Whiskey Rebellion | proper name | certain |
| Margaret Gill Phelan | Margaret **Gilfillan** | same speaker is "Ms. Gilfillan" a few lines later | probable |
| hill church | Hill Church | the Chartiers/Hill Church named on Side A | probable |
| james espy jr | James Espy Jr. | caption read aloud | certain |
| a custer hero or a butcher | "a Custer: hero or a butcher" | article title read aloud | probable |
| 20 years ago | twenty years ago | spoken as a word | certain |

Also applied, but **not** recorded as corrections because they change no word: punctuation,
capitalisation of surnames, and the joining of run-on fragments where the engine split a sentence
across chunks.

## 6. Left as heard — the honest gaps

- **"the station at Crosby"** (Side A) — three cold passes all return "Crosby". Almost certainly "the
  session at Cross Creek", but the tape says Crosby and it has not been "fixed".
- **Armand Denny** (Board of Missions president) — personal name, spelling not corroborated.
- **"the wind of the panes knocked out"** (1:57) — garbled; no confident reading, left as heard.
- **"he was taken in the family of Reverend John Clark; die, daddy, kill, alive; twice married"**
  (26:20) — the tape itself is mangled here; left as heard rather than invented.
- **1958 / 1858** is a judgement: if a Cross Creek Academy source contradicts it, the `post_edit`
  carries its reason and can be reverted in one line.
- **`INTERVIEWER` is shared** between Ann and John Connor because the tape does not identify which of
  them asks each question. The one unidentified voice at the close of Side B is labelled `UNKNOWN`.
- Run-on joins mean a few words in the final text merge two ASR tokens; a merge cannot be expressed as a
  find→replace `post_edit`, which is why the transcript/JSON reconciler reports a 1-word (Side A) and
  3-word (Side B) residue. The words are listed in the side notes.

## 7. What is on the tape — outline with timestamps

**Side A (31 m 12 s)**

- **0:10** Copyist's slate: who, when, where
- **0:35** The old library books; were Canonsburg's taken to Washington & Jefferson College?
- **3:12** The **William Vance case** — married his deceased wife's sister, deprived of communion at
  Cross Creek, appealed to the General Assembly in 1821, again in 1822, and lost both times
- **4:42** How the case came back down to the session; what a session could and could not do
- **5:34** Communion-season customs; the guest-pastor rotation — Stockton at Cross Creek, Marshall at
  Bethel, Clark and McMillan elsewhere
- **7:21** Jimmy Simpson's three-line diary; elders holding "society" when there was no minister
- **10:34** **Cross Creek Academy** — its teachers, its building (1858), its pupils
- **12:19** George Marshall and the **Board of Missions**; his obituaries
- **18:10** The Graham connection; **Marshall's letter of 27 July 1863** to General James Lee on the
  death of Henry Graham, read onto the tape in full
- **20:25** The letter's close — "how many of our precious young men have been cut down"
- **21:21** The postscript: raids, and whether the draft will bring trouble — **Morgan's Raid**, July 1863
- **26:25** **Oliver Miller**, mortally wounded at General Neville's, 16 July 1794; his widow in 1813
- **27:26** William Miller the distiller, who disappeared; the **still** kept at the **Stone Manse** until
  the park took it over, then with Mrs. Maits
- **30:55** Tape runs down

**Side B (20 m 15 s)**

- **0:00** Resuming over the books; a newspaper headline read aloud ("a Custer: hero or a butcher")
- **1:12** The county histories — **Caldwell's Atlas**, Latimer, Sam Green; looking for **Reverend Clark**
  and the **Whiskey Rebellion** in them
- **4:47** **Morgan's Raid and the Church in the Wildwood**
- **8:50** **James Espy Jr.**, and how much was written about him
- **9:04** The **Grahams** — James Lee Graham and the family photographs
- **11:13** Ms. **Gilfillan** and the picture she lent
- **13:25** Dr. Marshall as a Greek and Hebrew scholar; the old **session ledgers**
- **15:37** Where the church stood, and "over there at Bethel"
- **20:04** Last speech; the tape runs on

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md`, `transcript-b.md` | The transcripts: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt`, `transcript-b.srt` | The same text as timed cues, for playback or captioning |
| `notes-a.md`, `notes-b.md` | The working notes: measurements, engine settings, cold passes, every judgement call |
| `metadata.json` | The record of record: dates and their source, speakers, masters with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

The audio masters are **not** here (see `docs/AUDIO.md`): they are held on the archive NAS, two copies,
identified above by sha256.

## 9. Citing it

> White, A. D. (Alvin Dinsmore). *Cross Creek records and the Whiskey Rebellion*. Interview by Ann
> Connor and John Connor, 15 July 1971, Hickory, Pennsylvania. Historical Room, Bethel Presbyterian
> Church: digitised 18 October 2026. Transcript, 6,525 words.

Cite the timestamp for anything quoted — the transcripts keep the tape's own timebase, so a claim can
always be checked against the master.

## 10. Reproducing this transcript

The environment is pinned in `docker/` (faster-whisper 1.2.1, CTranslate2 4.8.3, numpy 2.5.4, base
image by digest) with the exact command line. What this recording used, in the tooling's terms:

- model: large-v3, CTranslate2 **int8** (`compute_type=int8`), language `en`, **beam 5**
- `--chunk-seconds 120`, snapped to quiet points: **17 chunks** (Side A) and **11 chunks** (Side B)
- seed: the collection's standing name list (`docker/seed.txt`), with a seed-leak check
- input: the aligned, summed audio described in §2 — not the raw stereo master

A re-run on the same master, engine and settings reproduces the raw ASR text; the filed transcript
differs from it only by the corrections in §5, each of which is a line in the JSON's `post_edits`.

## 11. Related material in the collection

- A.D. White's lecture on **Cross Creek and the Dinsmore family**, 31 October 1971 (same series, same
  speaker, four months later — the formal version of much of this interview)
- The **George Marshall** class, 17 October 1971
- The **Gertrude Tanner** lecture (same series)
