# J.D. Patterson — teaching in Bethel and Canton townships, and the Stilley shooting (side A, 20 April 1979)

**Side A of a two-sided interview.** Side B is filed separately as `unknown-jd-patterson-side-b`; the
two are one conversation on one cassette and are read as one document. The typed transcript of the same
interview — 64 pages, far fuller than the tapes — is filed as `unknown-jd-patterson-documents`.

| | |
|---|---|
| **Speaker** | James Douglass ("J.D.") Patterson, of 57 Boyer Road, Bethel Park, Pennsylvania |
| **Interviewer** | June Ellington |
| **Recorded** | Friday, 20 April 1979, Bethel Park, Pennsylvania (see §1) |
| **Length** | **35 m 56 s** as captured, of which 31 m 02 s is speech; the rest is tape running on |
| **Words** | 4,491 in the filed transcript, 194 speaker turns |
| **Status** | Transcribed, corrected, labelled; master on the archive NAS |

---

## 1. How the date is established

Half from the tape, half from the paper.

The tape gives the day and month in its first breath, and the interviewer misnames him in the same
sentence and corrects herself — which is why the name is evidenced as well as the date:

> "April 20th, and I'm talking to A.J. Patterson. J.D. Patterson. J.D. Patterson, I'm sorry. And he was
> telling about his teaching." — JUNE, 0:09

**No year is spoken anywhere on either side.** The year comes from the **typescript of the same
interview** (`unknown-jd-patterson-documents`), whose first page reads "Oral interview with Mr. J. D.
Patterson, April 20, 1979 / Interviewed by June Ellington. Typist, Mrs. T. R. Stump", and whose later
pages carry the same date in the running head. The archive's transcription record supplies 20 April 1979
independently and names the interviewer.

The date is consistent with the man: he says he was 17 in 1921 (21:37), i.e. born c. 1904 — the
typescript gives **14 March 1904** — and he speaks of a 1930–31 killing in the past tense.

The folder id keeps the `unknown-` prefix this item was queued under. The date is established, so if the
id should match it, renaming to `1979-04-20-jd-patterson-side-a` needs only the folder name and
`metadata.id`: `checksums.sha256` records file names inside the folder, not the folder name.

## 2. The audio, as measured

| | |
|---|---|
| Master | `JD Patterson - Side A.m4a` — ALAC 48 kHz stereo 16-bit |
| Length | **2,156.288 s** (35:56.288) |
| Size | 105,592,428 bytes |
| sha256 | `6b99a72c6feb402a63923a92628c22fe7b914b096d0a3138efa651a9a1408ed2` |
| Mean / peak | **−25.1 dBFS / 0.0 dBFS** (volumedetect, this reading) |
| Speech | 00:09.3 – 31:01.8; the last **294.4 s is digital silence** (mean −91 dB) |
| Access copy | `JD Patterson - Side A.mp3`, mono 64 kbps, **1,849.933 s** (30:49.9) |

**The peak of 0.0 dBFS is not saturation.** A 36-block per-minute sweep peaks at −2.3 to −4.7 dBFS
throughout with mean −23 to −26 dBFS; the one 0.0 dB sample at 22:12 is **12 clipped samples (0.25 ms)**,
a capture click. That sweep is also the evidence that there is no second session spliced onto this side.

**Stereo.** Channels measured on three 30 s windows (420 s, 900 s, 1300 s): channel 0 at −23.1/−22.7/−23.3
dBFS, channel 1 consistently **3.1 dB weaker**, raw correlation 0.972–0.985, rising to **0.990–0.992 at a
constant 1-sample lag**. A fixed lag and a fixed level offset is the delayed-duplicate case, so the channels
were summed with the lag compensated, weighted 2:1 toward the stronger channel — an equal sum would have
added the weaker feed's noise at full weight, and dropping it would have discarded a near-perfect second
copy.

**Processing: gain only.** `channelsplit → adelay 1 sample on L → 0.6667·L + 0.3333·R → +4.5 dB →
limiter (−1.5 dBFS)`, giving −18.96 LUFS integrated and −1.41 dBTP. No denoise: the source is lossless and
the 8 kHz+ band sits 11.6 dB below the speech band, which is real tape hiss, not an artefact worth
filtering.

**The access copy** is condensed, not cleaned: 35:56.3 → 30:49.9 by removing 306.3 s (14.2 %) — the 294.4 s
silent tail, 8.9 s of silent head, and one 3.0 s internal gap. **No speech was cut**; six of the ten
detected silences were left alone because a cut inside them would have clipped a word's span.

## 3. Transcription

- **Engine:** Whisper large-v3, Systran faster-whisper / CTranslate2 **int8**, 14 CPU threads, `en`,
  **beam 5**, `condition_on_previous_text=False`, word timestamps, `vad_filter=False`.
- **16 chunks** of ~120 s, each boundary snapped to the quietest 10 ms frame within ±5 s. Never a
  whole-file pass.
- **Seed:** `initial_prompt` carrying the corroborated local names (Bethel, McMillan, Clark, Marshall,
  Wycoff, Reiter, Bethel Academy, Oliver Miller Homestead, Mingo Creek, Canonsburg, Chartiers, Dido,
  Doddridge, Princeton, Croco, Strobl, Coverdale, Ellington, Patterson). **Prompt-leak check: clean** —
  every seeded token in the output is actually spoken (the tape itself says "J.D. Patterson" at 0:14), and
  no window needed re-transcribing unprompted.
- **Quality as reported:** 449 segments, **4,333 words**, mean per-word probability **0.9485**, only
  **2.98 %** of words below 0.5. The weakest five-second stretches are 11:16, 18:48 and 30:52 — mostly
  names and numbers.
- **Labels:** two voices, `JD` and `JUNE`, 119 and 75 turns, 194 in all. The SRT carries 516 cues with the
  speaker label on the first cue of each turn.

## 4. Corrections (26 logged)

Twenty-six `post_edits` entries in the source JSON, each with what was heard, what it became, why, and a
certainty. The ones that matter:

| heard | changed to | basis |
|---|---|---|
| "Shartiers" | **Chartiers** | the same school, named correctly two lines earlier |
| "which has Jesse Holly" | "**Wichas**, Jesse Holly" | the 1919 graduate list — "which has" is the surname |
| "Kenton Township" | **Canton** Township | he self-corrects to "Canton Town" in the next breath |
| "pod / pld" | **POD / PLD** | Problems of Democracy |
| "Alder", "elder schools" | **Alda** | the Nebraska town he names three lines earlier |
| "Silley" | **Stilley** | the family, spelled Stilley elsewhere in the passage |
| "work couch", "Fort Couture" | **Fort Couch** | Fort Couch Road at Route 19 |
| "the ore farm" | the **Orr** farm | Howard Orr and Roy McEwen, two sentences earlier |
| "web murray's" | **Webb Murray's** | spelled so later in the same passage |
| "mine three" | **Mine Three** | the place name (Phillips School at Mine Three) |
| "Rob Bob Stilley" | "Rob — Bob Stilley" | self-correction, marked with a dash |
| "graduated in 1917 in 1918" | "1917. In 1918" | two years run together by the engine |

Mechanical fixes, applied and counted separately: 8 doubled words collapsed ("had had" protected as past
perfect), 18 proper-noun casing fixes, sentence-initial capitals, lone lowercase `i` → `I`. Hesitations and
false starts were left alone.

**Kept verbatim on purpose:** "A.J. Patterson" at the head. The interviewer misspeaks and corrects herself;
that is the recording, and it is how the name is evidenced.

## 5. What is uncertain

- **"TITSO subjects"** (14:23) — probably a trade/industrial curriculum term; no reading is provable.
- **"J-5"** (28:42) — "some of the Walther boys, J-5, Donald McKeown had been in": a name or a service
  designation, unresolved.
- **"Vernon Mullenauer" / "Leo Molinar"** (19:07, 19:12) — the same family written two ways; neither
  spelling corroborated.
- **The Rausch residence** (24:45) — the church now in the house is heard ("Unity, Unitarians,
  Unitarian") but not identified.
- **The Hayes Avenue / Route 70 clause** (20:33) — garbled; the sense (the road was cut by Route 70) is
  clear from the context, the wording is not recoverable.
- **"Mitchell corners"**, **"Emerson … Hugh"** (the two older Stilley brothers), and the 1920 class list —
  heard, not corroborated.
- **The year 1979** rests on the typescript and the archive, not on the tape. The tape gives "April 20th".

## 6. What is on the tape

- **0:09** "April 20th, and I'm talking to A.J. Patterson…"; he is talking about his teaching
- **0:18** **Taylorstown**: a fourth-class district, eight months a year, $100 a month, and the year they
  had to give back $10 a month
- **1:16** **Canton Township** — West Washington, Wolfdale — a third-class district, $1,000 rising to
  $1,400; seven years, departmental teaching, his degree finished at California
- **2:20** The war years at Chartiers Township High School as a substitute for men on military leave;
  1947 and Nebraska — **Wood River**, four English classes and public speaking, and the town's first
  senior prom
- **3:38** **Alda** schools as superintendent, then **Shelton** High School for four years
- **5:18** Back to Pennsylvania for the retirement years; **Peters Township**, fourteen years under
  contract, then two years' leave and three more in West Virginia
- **5:30** What college cost: token tuition, $8 a week for room, board and laundry, a $24 registration
  bill with a "breakage fee" refunded if you broke nothing
- **7:22** **Hayes Avenue** school, Canton Township — and how Route 70 cut the road that led to it
- **8:50** Peters Township: a seventh-grade room, then departmental 7th–8th, then the high school —
  **POD** in American history, 11th-grade English, world geography as an elective
- **10:24** Class size 25–35; the year he had 48 in an eighth grade and asked an education professor what
  to do — "first I think you better pray a little"
- **12:21** The **Bethel school of 1916–17**: two rooms down, a big room up, Mr. Hildy principal, Miss
  Hazlett and Miss Hubbard below
- **13:39** The **vocational** programme added in 1917: girls' vocational (cooking, sewing, house care),
  woodshop in the basement, and the four-year farm curriculum — vegetable gardening and poultry, field
  crops and surveying, orcharding and dairying, farm mechanics and rural sociology
- **17:14** **Mine Three** and the Phillips School, where the shop class built the cement walks
- **18:03** The graduating classes: two in 1917 (Bill Lytle, Doug McElvain), two in 1918, six in 1919,
  eight in 1920, and **twelve in 1921** — his own
- **20:36** What he took: algebra, physical geography, four years of English, American history, civics,
  biology, a year of French (German was dropped in 1917) and Latin
- **21:47** The war: too young to go, but selling **Liberty Bonds** at the high school and the music —
  "Keep the Home Fires Burning", "The Long, Long Trail"
- **22:23** The **McKeown** cousins, and the Walther boys
- **23:23** The McEwen/Miller question, Howard Orr, and the **Orr farm** swallowed by Trotwood
- **24:12** **Route 19** before it was built up: Becker's Farm and its milk round at three in the morning,
  the wooden eight-room school at the Mount Lebanon loop, the Italian truck farm
- **27:01** The **Stilley** farm on Fort Couch Road, and **Bob Stilley** — the youngest of three brothers,
  shot in his own yard at midnight after the Wharf Market run, 1930 or '31; the hired man who disappeared
  and the stepmother sent to Woodville
- **30:37** The Higbee farm — not the one on Fort Couch, the one in Orchard Park — and Bethel Church Road
  down to Baptist Road
- **31:01** Last speech; the tape runs on in silence for 4 min 54 s

## 7. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The labelled, corrected transcript. **Start here.** |
| `transcript-a.srt` | The same text as 516 timed cues, speaker label on the first cue of each turn |
| `notes-a.md` | The working notes: measurements, engine settings, every correction and every open reading |
| `metadata.json` | Date and its source, speakers, masters with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder |
| `README.md` | This file |

The master is **not** here: it is on the archive NAS, identified above by sha256 (see `docs/AUDIO.md`).

## 8. Citing it

> Patterson, James Douglass. "Teaching in Bethel and Canton townships, and the Stilley shooting."
> Interview by June Ellington, 20 April 1979, Bethel Park, Pennsylvania. Side A of 2. Historical Room,
> Bethel Presbyterian Church: digitised 19 October 2026. Transcript, 4,491 words.

Cite the timestamp for anything quoted.

## 9. Related material in the collection

- **`unknown-jd-patterson-side-b`** — the other half of this interview. It opens mid-question ("What was
  his first name? Was it Samuel?"), so there is no break: read the two together, and use
  `unknown-jd-patterson-side-b/transcript-both-sides.srt` for one continuous clock (Side B's cues offset
  by 2,156.288 s, this side's duration).
- **`unknown-jd-patterson-documents`** — the 64-page typescript of the same interview, which carries the
  year, the interviewer's name and the typist's name, and covers ground these 67 minutes do not.
- **1971-07-15 A.D. White** — the same Historical Room, a different generation of the same local history;
  the Stilley and Fife names recur across both.
