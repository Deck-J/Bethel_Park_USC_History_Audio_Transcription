# J.D. Patterson — the Fife family and the ground it stood on (side B, 20 April 1979)

**Side B of a two-sided interview.** Side A is filed separately as `unknown-jd-patterson-side-a`; the
two are one conversation on one cassette, and this side opens mid-question — "What was his first name?
Was it Samuel?" — with no break in the talk. The 64-page typescript of the same interview is filed as
`unknown-jd-patterson-documents`.

Where Side A is Patterson's teaching career and the Bob Stilley killing, Side B is **the Fife family and
the land it farmed**: who married whom, which farmhouse was built when, the streetcar stops on the
Washington interurban, the neighbours along Brookside and Old Washington Road, and the Klan's meeting
place above Clifton. It ends with the tape's own ownership announcement.

| | |
|---|---|
| **Speaker** | James Douglass ("J.D.") Patterson, of 57 Boyer Road, Bethel Park, Pennsylvania |
| **Interviewer** | June Ellington |
| **Recorded** | Friday, 20 April 1979, Bethel Park, Pennsylvania (see §1) |
| **Length** | **31 m 06 s** |
| **Words** | 4,207 in the filed transcript, 92 speaker turns |
| **Status** | Transcribed, corrected, labelled; master on the archive NAS |

---

## 1. How the date is established

Side B carries **no date of its own**. It is dated from Side A, which opens "April 20th, and I'm talking
to A.J. Patterson — J.D. Patterson" (Side A, 0:09), and by its content it is the same sitting: it begins
mid-question and continues the same subject without an introduction.

**No year is spoken on either side.** The year comes from the **typescript of the same interview**
(`unknown-jd-patterson-documents`): "Oral interview with Mr. J. D. Patterson, April 20, 1979 / Interviewed
by June Ellington. Typist, Mrs. T. R. Stump", repeated in the running head on later pages.

The folder id keeps the `unknown-` prefix this item was queued under; if the id should carry the
established date, renaming to `1979-04-20-jd-patterson-side-b` needs only the folder name and
`metadata.id` — `checksums.sha256` lists file names inside the folder, not the folder name.

## 2. The audio, as measured

| | |
|---|---|
| Master | `JD Patterson - Side B.m4a` — ALAC 48 kHz stereo 16-bit |
| Length | **1,866.240 s** (31:06.240) |
| Size | 104,071,166 bytes |
| sha256 | `a2f38e54a226c5b468d2c14629d8386dcf3db2227a03f45edd198ab5306a230b` |
| Mean / peak | **−22.9 dBFS / −0.6 dBFS** (volumedetect, this reading) |
| Access copy | `JD Patterson - Side B.mp3`, stereo 192 kbps, 1,866.232 s — a straight transcode, nothing cut |

The side was received as `JD Patterson Side B.m4a` in the collection root and renamed to the archive stem;
the samples were not touched. Level is even across the file — 60-second blocks run −21.1 to −25.6 dBFS,
with no step that would suggest a second session spliced on. Sound runs to 30:52, then the closing
"Thank you." at 31:04.8; the tape ends there.

**Stereo.** The channels are only **0.2–0.5 dB apart**, correlated at **r = 0.98 on a constant 1–3 sample
lag** on every window measured (120 s, 700 s, 1400 s, 1800 s) — one programme on two feeds, unlike Side A's
3.1 dB gap. So they were **summed** (`pan=mono|c0=0.5*c0+0.5*c1`) rather than one channel being kept: with
no meaningful level difference there is nothing to weight, and summing recovers a little signal.

## 3. Transcription

- **Engine:** Whisper large-v3 in the pinned **`whisper-worker:v0.2`** container — faster-whisper 1.2.1 /
  CTranslate2 4.8.3 / numpy 2.5.4 on Python 3.13, the versions Side A used — 14 CPU threads, int8, `en`,
  **beam 5**, `condition_on_previous_text=False`, word timestamps, `vad_filter=False`.
- **16 chunks** of ~120 s, boundaries snapped to the quietest 10 ms frame. No whole-file pass.
- **Seed, and the leak it caused.** The prompt carried the subject, the interviewer and the local names
  (Bethel, Chartiers, Peters Township, Mount Lebanon, Fort Couch Road, Castle Shannon, Canonsburg, Mingo
  Creek, McMillan). At the head of this side the **seed echoed over the first 20 seconds** — the whole
  prompt came back as a segment, covering whatever was said underneath it. That window was re-transcribed
  **unprompted three ways** (beam 5, beam 1, beam 5 + VAD; cold pass `w01`); all three returned the same
  dialogue, and the recovered text replaced the echo. The raw echo is kept in the JSON (`segments[0].raw_asr`,
  `prompt_leak`) so the record shows both what the model printed and what was actually said.
- **Cold passes:** 23 windows over every doubtful passage × three settings = **69 transcriptions**.
- **Quality as reported:** 522 segments, **4,081 words**, mean per-word probability **0.9333**, **3.81 %**
  of words below 0.5.
- **Labels:** **92 turns — JD 77, JUNE 14, ANNOUNCEMENT 1**, one per paragraph, deliberately not merged:
  joining consecutive same-speaker paragraphs turned ten minutes of talk into a single wall of text that
  read as garbled even where every word was right. JUNE is labelled only where her words are unambiguous
  (a question, a name-check, an aside to the room); her one-word acknowledgements stay under JD, because
  no diarisation separates them and a wrong label is worse than none.

**One clock for both sides.** `transcript-both-sides.srt` in this folder is Side A's 516 cues plus this
side's 522 cues offset by **2,156.288 s** — 1,038 cues, monotonic, with a 313.2 s gap at the flip (Side A's
294.4 s silent tail plus the head of this side). Use it when quoting across the two sides.

## 4. Corrections (45 logged)

`post_edits` in the source JSON holds **45 entries**, each with pattern, replacement, count, certainty and
reason; the notes describe 50 corrections applied, the difference being counts per entry. The ones worth
seeing:

| heard | changed to | basis |
|---|---|---|
| "Bar Hill Road" | **Bower Hill Road** | six unprompted passes hear "Bar Hill"; OpenStreetMap has Bower Hill Road through Upper St. Clair |
| "Pima Tuning Dam" | **Pymatuning Dam** | the reservoir on the PA–Ohio line |
| "billy five" | **Billy Fife** | the family, named repeatedly |
| "Fyfe" | **Fife** | the family's own spelling |
| "Cremora" | **Cremona** | the Pittsburgh Railways stop list |
| "Fifeshire / Fife Shire" | **Fifeshire** | the development Emily Cheeseman laid out and named |
| "Fullert" | **Fulliart** | he spells it on the tape: "F-U-L-L-I-A-R-T" |
| "Hamels Mortuary" | kept | no such funeral home found; the hill above Clifton is identifiable, the business is not |

Also applied: stutters normalised, sentence case repaired, family and place names spelled to the Fife
family history and the streetcar stop list.

**One editorial note inside the transcript**, at 4:09: "Isabel has one daughter, Catherine, the dog woman."
The words are clear on the tape and were confirmed by ear (nine passes, p 0.93–0.99 on "dog", a 220 ms
token), but what "dog woman" refers to — a nickname, a kennel, an occupation — is **not stated**, and
nothing is assumed. The note sits in the text so a reader sees that the reading is settled while the
meaning is not.

## 5. What is uncertain

- **"Isabel Hemlinger, the pianist"** (3:48) — all three passes agree on the name; no Hemlinger or
  Henninger could be corroborated in Bethel Park records.
- **"Hamels Mortuary"** (26:20) — no funeral home of that name found.
- **"Earl married a swim girl"** (28:51) — probably a surname (Swaim?), but no pass returns it cleanly.
- **"Hayes River"** (30:06) — where Genevieve's husband came from is not recoverable, and the clause after
  "Hayes" is lost.
- **"Attention."** (14:18) — a single unintelligible word between two exchanges.
- **The house dates** — this is the honest core of the side: he dates the Fife houses by memory ("I would
  say in the 1870s or 80s", "built after 1900", "older than the Jim Fife house") and says so. Those are
  estimates by a man born in 1904, not records. The transcript keeps them as estimates.
- **The McCartney connection** — he says outright "I'm lost on that part", and the transcript does not
  invent one.

## 6. What is on the tape

- **0:18** Frank Fife and Caroline, his father's youngest sister; the rented farm above Hamlet; the move
  to **2550 Old Washington Road** in 1927
- **3:48** The children: Jean (Mrs. Don Haas), **Isabel Hemlinger**, Jay killed in 1925 running a truck
  into a pole to avoid a child, John, Edna Cole at Charleroi
- **4:09** Isabel's daughter Catherine — the "dog woman" note
- **5:22** John's daughters, the house behind Foodland on Brookside, and where the various grandchildren
  went
- **7:06** **Fifeshire**: Hulse Fife, Carrie McMurray, their daughter Emily who married Taylor Cheeseman —
  and Emily laid out and named the development
- **8:08** Hulse as a first name: Albert Hulse's aunt married a Boyer, and **Hulse Boyer** made them drop it
  and went by Jim
- **9:32** The **streetcar stops**: Cremona for the Will T. Fife house, **Valley Farm** for John T.'s, and
  the bronze plaque now going on the Will T. Fife house
- **10:18** The Farmer's Protective Association picnics, 1916–19, and which Fife farm hosted each year
- **12:34** Dating the houses by the people in them: the Jim Fife place, the Wiltie Fife house older, the
  **Albert Fife** house after 1900
- **13:53** The **John Fife** house at the end of Fife Drive; his father's year there; "the Douglases didn't
  like people"
- **17:42** McCartney and Mary Woods — the Mount Lebanon undertaker and his wife who embalmed better than he did
- **21:41** The Fifes in the Civil War: John T. and William James, their rifles, and who might have them now
- **23:06** **Thomas Espy**'s Civil War sword, now with **J. Walter Phillips**; the Phillips farm above
  Clifton, and the cow he bought there at eighteen
- **25:11–25:45** The **Klan** meeting place on the hill above Clifton; the DeVores at Thomas Station, the
  Macdonalds off Sugar Run Road, and the 1920s
- **26:20** Hamels Mortuary, the hill, and whether the Klan met up there
- **27:19** Where **Brookside Lumber** stands: the Fulliart place, market gardening, apples and grapes
- **28:01** The **Hultz** families — Will's peach orchard on Fort Couch Road, Harry's on Bethel Church Road
- **29:50** The Hayes connections, Dwight and George, and the Wilhals
- **30:49** The tape's own announcement: "This is a recording of oral history to be the property of Upper
  St. Clair Historical Society and will only be used by non-profit"
- **31:04** "Thank you."

## 7. Rights — a flag, not a clearance

That closing announcement matters. The collection sits in **Bethel Presbyterian's** Historical Room, but
the recording states **Upper St. Clair Historical Society's** ownership and restricts it to non-profit use.
That is an ownership claim by another institution, not a release by this one. `metadata.json` therefore
records `rights.status: "unknown"` with the statement quoted verbatim, and the item should not be treated
as cleared until the Historical Room resolves it (see `docs/RIGHTS.md`, rule 1).

## 8. Files here

| file | what it is |
|---|---|
| `transcript-b.md` | The labelled, corrected transcript. **Start here.** |
| `transcript-b.srt` | The same text as 522 timed cues |
| `transcript-both-sides.srt` | Both sides on one clock: 1,038 cues, this side offset by 2,156.288 s |
| `notes-b.md` | The working notes and the fact-check record, in that order |
| `metadata.json` | Date and its source, speakers, masters with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder |
| `README.md` | This file |

The master is **not** here: it is on the archive NAS, identified above by sha256 (see `docs/AUDIO.md`).

## 9. Citing it

> Patterson, James Douglass. "The Fife family and the ground it stood on." Interview by June Ellington,
> 20 April 1979, Bethel Park, Pennsylvania. Side B of 2. Historical Room, Bethel Presbyterian Church:
> digitised 19 October 2026. Transcript, 4,207 words.

## 10. Related material in the collection

- **`unknown-jd-patterson-side-a`** — the first half, and the side that carries the date. Read it first.
- **`unknown-jd-patterson-documents`** — the 64-page typescript: the same interview with the year and the
  names in print, and much more of it than the two tapes hold.
- **1971-07-15 A.D. White** — the Fife, Gilfillan, Espy and Stilley names recur there, from the Bethel side
  of the same hills.
