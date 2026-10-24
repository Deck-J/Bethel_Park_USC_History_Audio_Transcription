# Alvin Dinsmore White — Cross Creek and the Dinsmore Family (31 October 1971)

Recording stem: `Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971)`.
Every file in this folder carries that stem; this note is the working record behind the document.

## What this is

A 31 m 2.9 s (1,862.997 s) **lecture given to Ann Connor's church-history class by Alvin
Dinsmore White** (1894–1992), educator and historian of the Cross Creek country of northern
Washington County. Ann Connor introduces him for about six and a half minutes — presenting his
own book to the class library, reading the gift inscription he wrote in it — and then he speaks
for the remaining twenty-three.

He works through the two subjects her outline asked for:

- **The Dinsmore family**, from his great-great-great-grandfather **James Dinsmore** (b. County
  Antrim, 26 April 1742; d. 1817): the crossing of the Alleghenies on snowshoes, the farm on
  Miller's Run in South Fayette Township, the removal to Upper Buffalo in 1795, the triple
  intermarriage with the Carr family, the brick house of 1810 still in the family, and the two
  quotations on his character — one from the printed record, one from a grandson, the Rev. James
  H. Dinsmore — including White's own corrections of the grandson's errors.
- **Cross Creek**, through the man who ties the two congregations together: the **Reverend John
  Stockton**, pastor at Cross Creek from 1827, who founded **Cross Creek Academy in 1828** and
  hired the young **George Marshall** as a teacher. White then lists the dates and texts of
  Marshall's recorded preaching at Cross Creek — Exodus 15:26 (2 April 1854), 1 Thessalonians 5:6
  (18 June 1858), the communion weekend of 23–25 September 1864 (Hosea 10:12 and Luke 15:10),
  Revelation 2:5 (28 January 1866) and Jeremiah 8:22 (23 June 1867) — and the tape cuts off in the
  middle of the last text.

## Date — 31 October 1971, and the recording it answers

- **The date is on the cassette label**: `10.31.71`. That is the primary evidence.
- **The label's weekday checks out.** 31 October 1971 was a **Sunday**, and this is the same
  Sunday class that met on 17 October.
- **The tape dates itself by reference.** White opens "We were here last February"; Ann's
  invitation was "some weeks ago"; and Ann says at 1:39 "Last week, we sort of left the church and
  went elsewhere, took the group and went to Mingo Presbyterian Church" — the class's previous
  meeting. Nothing on the tape contradicts the label.
- **This recording is the fulfilment of a promise made on the 17 October tape.** In
  `George Marshall Class (17 October 1971)/`, at 12:10, Ann says:

  > "And on the 31st of this month, Mr. Alvin Dinsmore White is going to come back, and I'm going
  > to ask him to tell you a little bit about this man, John Stockton."

  This file is dated the 31st, and he does exactly that: Stockton gets his own section from 21:28,
  with his 1820 graduation from Washington College, his arrival at Cross Creek in 1827, the
  founding of the academy in 1828, and the hiring of George Marshall. **The two recordings are a
  pair** — one announces the lecture, the other is the lecture. Read together they also show what
  Ann did with the two weeks: on the 17th she says "I didn't know anything about Cross Creek",
  and by the 31st she is introducing the man who wrote the book about it.

  The same class tape adds that White had spoken to them **"last fall"** as well, so this is his
  third appearance in front of the group, not his second.

## Speakers — two voices, and the measurement behind the split

| Label | Where | Evidence |
|---|---|---|
| `ANN` | 0:00–6:35, 13 paragraphs | Ann Connor. White thanks her by name at 6:40 ("Thank you, Mrs. Conner"); she introduces him, presents his book to the library under Mrs. Tanner's supervision, and quotes the inscription. Median f0 **188–219 Hz**. |
| `WHITE` | 6:40–30:00, 62 paragraphs | Alvin Dinsmore White. Named on tape by Ann at 5:41 ("to you, Alvin Dinsmore White"); he speaks in the first person of "my great-great-great-grandfather, James Dinsmore" and "my middle name being Dinsmore". Median f0 **130–167 Hz**. |

**The split rests on measurement plus content, not on the label.** Pitch was taken per paragraph by
autocorrelation over voiced frames (40 ms window, 70–320 Hz, 0.3 correlation floor). The two ranges
do not overlap: Ann 188–219 Hz across 13 paragraphs, White 130–167 Hz across 62. The content
independently confirms it — Ann introduces and hands over; White lectures.

**No third voice is audible.** The one short paragraph with a female-range f0 (21:25, "John
Stockton.", 219 Hz on 23 voiced frames) is White repeating the name at the end of a broken
sentence; 23 frames is too few to measure and the words are his. It is labelled `WHITE`.

**Both names are on the tape.** Nothing here is supplied from the filename.

## Source and measurement

- `Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971).m4a` — ALAC, 48 kHz,
  2 ch, 1,862.997 s, 60,978,057 bytes, md5 `674b2c72569f0c908c729d9101a7729a`, **unchanged as
  received**. Moved out of the archive root into this folder, md5 verified either side of the move.
- **Level before: quiet, but not in the class of its neighbours.** mean **−30.2 dBFS**, peak
  **−3.1 dBFS**, integrated loudness **−25.73 LUFS**, true peak −3.07 dBTP, LRA 12.2 LU. That is
  **7 to 11 dB above** the 17 October class (−42.1 dBFS) and the Edna Croco tape (−45.5 dBFS) but
  still about **7 dB below** the archive's −16 to −19 LUFS band, so gain was required.
- **Level after: on target.** mean **−19.6 dBFS**, peak **−1.4 dBFS**, integrated **−18.38 LUFS**,
  true peak **−1.43 dBTP**, LRA 7.0 LU.
- **Gain applied: +10.2 dB effective**, as a two-pass `loudnorm` to `I=-18.5, TP=-1.5, LRA=11`
  (measured input −28.56 LUFS, −3.61 dBTP, LRA 12.10, threshold −39.57, offset −0.50). Applied to
  the **ASR working copy before transcription** and to the portable MP3; the master carries no
  processing at all.
- **The gain was applied before Whisper ran, not after.** The working copy was built first, measured
  back at −19.6 dBFS mean, and only then handed to the model in 16 kHz float32.
- **A large boost raises the noise floor with the voice.** This tape's noise is tape and cassette
  hiss rolled off above ~3 kHz, so the lift is in the speech band, not in hiss.
- **There is nothing to denoise.** Energy by band over a representative minute: 0–300 Hz **8.10 %**,
  300 Hz–3 kHz **91.73 %**, 3–8 kHz **0.16 %**, 8–16 kHz **0.007 %**. The capture is band-limited to
  roughly 3 kHz — tape and deck response, not hiss. No filter was used anywhere.
- **Stereo: a delayed duplicate — summed with the lag compensated.** Measured on sixteen 30 s
  windows: ch0 **−31.18 dBFS**, ch1 **−29.37 dBFS** (**1.81 dB** apart), correlation **0.985–0.993
  at a constant 1–3 sample lag** (0.02–0.06 ms; raw correlation without compensation 0.92–0.98).
  Same programme on two feeds, one slightly hotter and very slightly ahead. Summed as
  `(1·ch0 + 2·ch1)/3` with ch1 shifted back 2 samples: an equal-weight sum would have carried the
  weaker feed at full weight, and taking ch1 alone would have thrown away a near-perfect second
  copy. The 1→3 sample drift across 31 minutes is capture-clock drift, not a fixed azimuth offset;
  compensating at a constant 2 samples leaves at most 0.06 ms of misalignment.
- The last 63 seconds are digital near-silence (silence from 29:59.7 to the end, with a single
  click at 31:01). The first 9.7 seconds are tape leader.

## Transcription

- Whisper **large-v3** (Systran faster-whisper 1.2.1, CTranslate2 4.8.3, int8, 14 CPU threads),
  language `en`, `beam_size=5`, `condition_on_previous_text=False`, `temperature=0.0`,
  `compression_ratio_threshold=2.4`, `vad_filter=False`, word timestamps.
- **16 chunks** of 113–118 s, each boundary snapped to the quietest 10 ms frame within ±5 s of a
  120 s target (0, 118.67, 233.68, 348.70, 464.60, 580.85, 696.74, 813.09, 930.52, 1045.52, 1161.29,
  1278.47, 1394.19, 1511.46, 1626.46, 1742.55, 1862.94). Three seconds of padding either side;
  each word assigned to the chunk whose core holds its midpoint, with a seam orphan pass that keeps
  a word outside its own core only where no word owned by that core covers its span. **Never a
  whole-file pass.**
- Audio decoded by ffmpeg to float32 arrays at 16 kHz. **PyAV in this build rejects the
  `metadata_errors` kwarg** faster-whisper passes, so the array path was used deliberately.
- **Seeded prompt: 89 words (~130 tokens).** The general `whisper_seed.txt` vocabulary plus this
  archive's corroborated Bethel names and the Cross Creek/Dinsmore names this recording is about
  (Alvin Dinsmore White, Dinsmore, Cross Creek, Stockton, Dinsmore family names, Hultz, Miller,
  Millar, Fife, McKnight, McCormick, Nevill). `seed_bethel.txt` was read but **not** added — the
  subject is Washington County (Cross Creek, Canton Township, Buffalo Village), not Bethel Township,
  and each township seed is an alternative rather than an addition. `review_notes.txt` was read
  first; **none of its uncertain readings** (Keykendall, Hampstead, Middleswart, Gilfillin,
  Barrackman, Hewey) was seeded. `names_and_locations.csv` was **not** pasted into the prompt.
  The package's spelling controls were applied in the fact-check: **Miller not Milber**,
  **Hultz not Hutz**, **Millar and Miller kept apart** — and where the speaker says a name the seed
  does not contain, the acoustic evidence decided it, not the map.
- **A full second pass with `initial_prompt=None` over the same 16 boundaries** was run as the
  leak and collapse detector.

### Prompt leak — none

No segment in the prompted pass is made of seed tokens; the one paragraph that tripped a
seed-fraction filter is the single word "family." at 14:44, which is the end of "his son John and
his wife and family." The prompted pass produced **3,690 words** against the plain pass's
**3,681**, and the two agree within a few words per 30 s window. **No window was deleted.**

Where the two passes disagreed the span was judged on its own words:

| At | Prompted pass | Plain pass | Taken |
|---|---|---|---|
| 5:00 | "who served as elder in the Cross-Mexico District" | "served as elder in the Cross church" | prompted, with the district corrected to Cross Creek |
| 6:00 | "an elder in the Montmartre Cross Creek Church" | "an elder in the Montmartre Presbyterian church" | neither — marked `[unclear]` |
| 18:00 | "he was very well acquainted with Dr. John Macmillan" | same, with "yes" inserted | prompted |

### Collapse — both passes failed the same place, and the fix was a re-pass, not a deletion

The **first thirty seconds** are speech recorded 25 dB below the rest of the programme (−45 dBFS
against −20 dBFS). **Both** passes returned a single `Thank you.` at 0:10 and then nothing until
0:30, where the text resumes mid-sentence ("and a deeper appreciation…"). That is the
`Thank you for joining us.` failure mode, and here the two passes agreeing was not evidence of
anything — they share a model.

Re-transcribed 0–45 s on its own at **+20 dB with `initial_prompt=None`**, which recovered the
opening sentence and 44 words:

> "As far as we have been able to know, we really didn't get very far. We only scratched the
> surface as far as the history of our church and of the Presbyterian Church in Western
> Pennsylvania. But I hope that out of these classes we can have a deeper appreciation…"

Those segments replace chunk 0 for 0–44.86 s and are marked `"head_repair": true` in the JSON. A
further boosted pass on the final 40 s confirmed that the lecture ends in the middle of Jeremiah
8:22 and that the two `Thank you.` segments at 30:30 and 30:53 sit over room tone at −60 dBFS,
38 and 61 seconds after speech stops; those two are hallucination and were dropped, as the same
artifact was dropped from the Marshall and McMillan transcripts.

### Chunk seams

355 of the 3,914 raw words were duplicates at chunk heads and were trimmed by **prefix-only**
de-duplication (each word assigned to its own core, then the seam orphan pass), leaving 3,690. The
merged word count was reconciled against the per-chunk totals, and every seam was read across.
**No segment was dropped whole** — the failure that cost 97 words on the Edna Croco interview.

## Quality

- 259 segments, **3,692 words** of speech in the corrected transcript — 3,767 words in the built
  container, which counts its 75 label tokens as well (75 paragraphs: 13 `ANN`, 62 `WHITE`),
  **328 `.srt` cues**.
- **Mean per-word probability 0.8836**, **6.70 % of words below 0.5**, 14.7 % below 0.7 — the
  strongest of the four quiet tapes in this archive, and above the Marshall class's 0.8609.
- **Weak stretches** (mean probability / share below 0.5, per two minutes): **2:00–6:00** (0.84–0.86
  / 10 % — Ann's introduction, spoken away from the microphone), **18:00–20:00** (0.858 / 9.5 % —
  White reading the grandson's tribute), **28:00–30:00** (0.858 / 7.3 % — the scripture citations
  and the truncated ending). The strongest stretch is 8:00–10:00 (0.927 / 2.9 %).
- **Read end to end**, all 259 segments and all 75 paragraphs, in order, twice: once against the raw
  ASR and once as rendered prose for misplaced words and split compounds. No `Stone Man's` /
  `short bread` / `for bear` class of error survived; the compounds this tape produced were place
  names (`Cross Creek`, `South Fayette`, `Upper Buffalo`), all of which the ASR had broken into
  real English words and all of which were corrected and logged.

## Audio review of the doubtful readings (2026-10-20)

The nineteen doubtful readings were re-listened to with the seed prompt removed — the prompt that
produced them was not used anywhere.

**Method.** Each window was cut from the master at 48 kHz, about 60 s of context centred on the
phrase, and **re-normalised on its own** with two-pass `loudnorm I=-18.5:TP=-1.5:LRA=11`, because
the windows measured **−23.98 to −34.11 LUFS** (the introduction is 8–10 dB quieter than the
lecture) and one gain would have handed the quiet ones to the model at exactly the level that
produces filler. Every window left at about −19.3 dBFS mean / −1.5 dBFS peak. Model: faster-whisper
**large-v3** int8, `language="en"`, **`initial_prompt=None` on every pass**,
`condition_on_previous_text=False`, `temperature=0.0`. Settings: **A** beam 5 · **B** beam 1 ·
**C** beam 5 with VAD · **D** a matched 14–20 s crop of the phrase; then **F/G** beam 10 crops (the
second at +6 dB), **H** crop slowed to 0.8× with pitch preserved, and **I/J** micro-crops at 0.7× and
below. **131 passes over 4,146 s of audio** — about 69 minutes of model input for 31 minutes of tape.
The working material (19 windows and 19 crops, normalised; every pass with its settings and
per-segment log-probabilities in `passes*.jsonl`) is in `/opt/data/cache/scratch/white_audio/` on the
Hermes host, outside this archive; the master was decoded to a float32 copy and never re-encoded.

**The test is stability, not confidence.** Where every pass returns the same word the reading is
treated as sound; where the word moves with beam width, gain, VAD or speed it is a guess and stays a
gap. Two model artefacts were identified and discounted: `James Moore` for *Dinsmore* (systematic in
every pass of the 21:14 window, and again at 12:22 and 23:00) and `You've been very quiet. And let's
go.` emitted over digital silence at 13:35.

**Outcome: nine text changes, five gaps left.**

- **Certain (5):** 12:22 the rough coffin · 10:48 salt · 15:41 Brice · 13:35 the bracket removed
  (dropout, nothing missing) · 29:05 with the sacrament.
- **Probable (3):** 26:30 the Lee family · 28:20 communion / post-communion · 4:56 1806 to 1870.
  Plus 11:29 Canaan, already in the text, whose audio reason is now recorded.
- **Uncertain (1):** 21:14 "during the rest of Dinsmore's life" — "the rest of" is 4/4, the object
  "life" rests on the phrase as returned.
- **Permanent gaps (5), left bracketed:** 1:49 **[POTENTIAL TAPE DAMAGE]** · 6:04 · 15:12 · 12:54/14:29 · 29:40. Each was
  re-listened to across the full set and still returns two or more shapes; the unresolved list below
  now says so, because "re-listened and unresolved" is stronger evidence than "not checked".

### The 1.05 s dropout at 13:35 — why the timing jumps

The 20 ms level envelope explains both the empty bracket and the odd timing. Speech ends at
**814.70 s**; the signal is **digital silence (−180 dB) from 814.75 to 815.80**; speech resumes at
816.25 with "In 1800". That is a **1.05 s dropout**, not a breath and not an aside: the sentence is
complete — "in a double wedding ceremony, James Dinsmore was married to his third wife, Elizabeth
Carr" — and all four full passes read straight through the gap. The bracket has been removed. A
reader comparing the `.srt` cues at 13:35–13:47 with the master will see the silence and should not
read it as missing speech; the transcript's clock is unbroken, the tape's is not.

### 1895 against 1896 — recorded, not changed

At 23:15 he dates the academy's end to **1895**: four of four passes hear it, and the text says
1895. Two of his own sources say **1896**:

- *History of Cross Creek Country* (1969): "…opened an Academy at Cross Creek Village, and this
  served as a Secondary School for the community **until 1896**, when the Cross Creek Township High
  School was opened to take the place of the Academy."
- The marker erected in **1954 by the Alumni Association** at Cross Creek Road and Home Street
  Extension: "Site of Cross Creek Academy **1828 – 1896** and of Cross Creek Township High School
  **1896 – 1929**."

The number has **not** been altered. The transcript is faithful to the tape, and the discrepancy is
the finding: a researcher citing the year should cite the book or the marker.

### Two things the audio settled, neither of which changed the text

- **17:11 "at Montour or Miller's Run"** is not a slip, and "Montour" is confirmed rather than
  doubtful. The 1889 *History of the Presbytery of Washington* — the volume Ann Connor presents to
  the class library at 1:30 of this same tape — lists **"Montours, Allegheny County"** among the
  presbytery's charges, with Joseph Patterson installed there and John McClain and Michael Law after
  him. Both halves of the phrase are real Allegheny County congregations. (This is also why
  "Montour" must **not** be moved to 6:04: the modifier there is a three-syllable word with a medial
  /m/–/mb/ and a final /-tər/, a shape no pass produces for Montour.)
- **15:41 the first ruling elders.** The same book's roll reads "**Bethel. — James Dinsmore, James
  Brice, James Kirkpatrick, John Vance.**" White names the three Jameses and says "three men, I
  believe the name James in that direction" — which is exactly right, because his three are the three
  Jameses. **He omits the fourth elder, John Vance**, and no name has been inserted: the transcript
  records what he said, and this note records what the roll says.

### Not touched

- **The Marshall dating conflict** (item 19 below) stands exactly as spoken in each lecture, per
  John's instruction: no harmonising, no cross-reference, no edit to either transcript.
- **One gap outside the seventeen** — "that great evangelistic [unclear]" at 24:20 — is unchanged;
  it was not one of the reviewed windows.
- The `.m4a` master was read only. No audio was written, moved or deleted.

## Corrections applied (182 `post_edits`)

Every change from the raw ASR is in the JSON `post_edits` with its raw form, its replacement, a
reason and a certainty marker; `reconcile_md_json.py` reports **JSON-CONSISTENT, 0 unexplained
words**. Of the 182 entries, 127 locate in the raw segments, 31 are corrections already folded into
them, and 24 are pure **insertions** whose `find` is empty by nature (a word the ASR dropped — "I"
before "have jotted down", the em dashes, "1817"). An insertion has no raw form to locate; that is
the only sense in which those 24 are "unresolved", and it is not a defect. The substantive ones:

| # | As transcribed | Corrected | Why | Certainty |
|---|---|---|---|---|
| 1 | "Thank you." at 0:10 | the real opening sentence (44 words) | both passes collapsed over speech 25 dB below programme level; recovered by a +20 dB re-pass with no prompt | certain |
| 2 | "the period Christi Frisella" | "the period [unclear]" | re-listened across the full cold-pass set (see the audio review below): the onset is stable, the second word is not, and no reading is defensible | unresolved |
| 3 | "during the passport of Dr. George Warne" | "during the pastorate of Dr. George Marshall" | the subject of the sentence and of the previous class | certain |
| 4 | "History of the Conflict Church" | "history of the Cross Creek Church" | the church Ann is introducing; named correctly twice more in the same paragraph | certain |
| 5 | "Mr. Albert Dinsmore White" | "Mr. Alvin Dinsmore White" | his name, given correctly in the inscription Ann reads 40 s later | certain |
| 6 | "James Binsmore … John Binsmore … James Dunmore" | James / John **Dinsmore** | one family, named correctly in the same paragraph and throughout the lecture | certain |
| 7 | "the Isabella school district" | "the **Avella** school district" | White's own published biography: Elementary Principal of the Avella Joint Schools | certain |
| 8 | "in the present South Bay of the Panthers" | "in the present **South Fayette Township**" | Miller's Run runs through South Fayette/Cecil, "a couple of miles southwest of Bridgeville"; the ASR resolves an unfamiliar township name to English words | probable |
| 9 | "the land of Hayden" | "the Land of Canaan" | re-listened: the 10:40 mention is "Canaan" 4/4 and the 11:29 mention is the same syllable (`Hayden`/`Payton`); one tract, one name | probable |
| 10 | "joined the BAR and SAR" | "joined the **DAR** and SAR" | Daughters and Sons of the American Revolution | certain |
| 11 | "her body was spread for burial" | "her body was **brought** for burial" | internal corroboration: "her body was brought here for burial" at 12:20 | certain |
| 12 | "too far from Cherk about seven miles" | "too far from **church** — about seven miles" | "Cherk" is the ASR's church throughout this tape | certain |
| 13 | "the Pittsford and the Carr families" | "the **Dinsmore** and the Carr families" | the three intermarriages described are Dinsmore–Carr | certain |
| 14 | "a brother of Elizabeth and James" | "a brother of Elizabeth and **Jane**" | Elizabeth and Jane Carr are the two sisters just named | certain |
| 15 | "served as a hoder" | "served as an **elder**" | the office he held at Upper Buffalo | certain |
| 16 | "the Board and Customs of the Western Missionary Society" | "the Board of **Commissioners**" | the society's board, 1804 | probable |
| 17 | "plenty of dissenters up to the old Miller's Run Presbyterian Church" | "plenty of **Dinsmores** went up to…" | the sentence is about Dinsmore graves in that graveyard | probable |
| 18 | "at Upper Bowman" | "at **Upper Buffalo**" | the church of the whole passage | certain |
| 19 | "Thomas Marcus" | "Thomas **Marquis**" | the same correction the 17 October class needed; Marquis of Chartiers | probable |
| 20 | "the great revival of the 18-2" | "the great revival of **1802**" | the camp meeting at Upper Buffalo | certain |
| 21 | "Iowa gave him maybe only two years" | "So **I would give** him maybe only two years" | plain sense of the sentence | probable |
| 22 | "the Craft Breaker Academy in 1828" | "the **Cross Creek** Academy in 1828" | founded by Stockton, named in White's own book | certain |
| 23 | "a friend of Jefferson College, the class of 1831" | "a **graduate** of Jefferson College, class of 1831" | Ann's class: he graduated in 1831 | probable |
| 24 | "united into the Princeton, Washington, and Jefferson counties" | "united into the **present Washington and Jefferson College**" | the 1865 union; a cold pass returns "President's", i.e. "present" | certain |
| 25 | "Exodus 15-2 … that healed thee" | "Exodus 15:**26** … that **healeth** thee" | the verse quoted is Exodus 15:26, KJV | certain |
| 26 | "the Tribunan service … a post-Tribunan sermon" | "the **communion** service … a post-communion sermon" | re-listened: no pass at any setting returns "thanksgiving"; the only English word in the `com-/con-/tri-bunan` shape is *communion*, and it is the Monday service of a communion season | probable |
| 27 | "Soak yourselves in righteousness" | "**Sow** yourselves in righteousness" | Hosea 10:12 | certain |
| 28 | "he assisted the doctors talking with the doctors" | "he assisted **Dr. Stockton with the sacrament**" | the clean cold pass returns the object directly; no longer an inference from the earlier service | certain |
| 29 | "Revelations 2-5" | "**Revelation 2:5**" | the verse quoted | certain |
| 30 | "from Jeremiah 1822 … no bomb in gillian … no station" | "Jeremiah **8:22** — 'Is there no **balm** in **Gilead**? Is there no **physician** there?'" | the verse quoted identifies itself | certain |
| 31 | "he died in 1972" | "he died in **1872**" | Marshall's death, given as 1872 twice elsewhere in the same passage | certain |
| 32 | "the Crossbridge / Cross Street / Crown Street / Crosstreet area" | **Cross Creek** | the village, church and academy; the ASR varies the form each time | certain |
| 33 | "Densmore" throughout | **Dinsmore** | the family spelling, and his own middle name; the pronunciation is "Densmore" | certain |
| 34 | "Rev. Coughlin was strapped to a pair of farm wagon wheels" | "**the rough coffin** was strapped to a pair of farm wagon wheels" | 12:22 — 10 of 12 un-prompted passes; there is no minister and no "Coughlin" in the sentence, and "thus transported to the graveyard" describes a coffin | certain |
| 35 | "to obtain silk" | "to obtain **salt**" | 10:48 — "salt" in 5 of 6 passes (both no-VAD full passes and both check crops), and it is what a settler rode east for | certain |
| 36 | "James Bryce" | "James **Brice**" | 15:41 — the printed roll of the 1889 *History of the Presbytery of Washington* spells it Brice; the audio is 4/4 on the sound | certain |
| 37 | "a double wedding ceremony — [unclear] —" | "a double wedding ceremony, **James Dinsmore was married** …" | 13:35 — the bracket was a 1.05 s digital dropout, not an aside; see the audio review | certain |
| 38 | "during the [unclear] of Dinsmore's" | "during the **rest of Dinsmore's life**" | 21:14 — "the rest of" 4/4; the object rests on the phrase as returned, hence "uncertain" | uncertain |
| 39 | "married into the [unclear] family of Cross Creek" | "married into the **Lee** family of Cross Creek" | 26:30 — "Lee" in 3 of 7 passes, and he names Mary Lee, daughter of Hugh Lee, 13 s later; the modifier stays a gap | probable |
| 40 | "James Dinsmore, 1860 to 1870" | "James Dinsmore, **1806** to 1870" | 4:56 — every pass that isolates the numeral gives 180x; 1860 is impossible (elder from 1837, d. 1870, b. 20 May 1803) | probable |

Mechanical repairs alongside: chunk-seam stutters collapsed ("years. years.", "came. came.",
"do do not", "Walker, Walker", "three.", "go."), sentence case and proper-noun case restored,
`i` → `I` where it stood as the pronoun, and `[unclear]` inserted only where no pass recovered a
word.

## Unresolved (five permanent gaps, each re-listened and still unresolved)

Each of these was re-listened to across the full cold-pass set on 2026-10-20 — the method is in the
audio review above. They are not transcriptions that nobody has checked; they are readings the audio
will not settle, and the bracket stays.

1. **1:49 — "during the period [unclear]".** The onset is stable as a "Christi-/Christian" word; the
   word after it alternates between a "results" shape and a "rebellion" shape with beam width and
   speed, which is the signature of a guess. The Whiskey Rebellion, the obvious historical candidate,
   appears in no pass at any setting and has not been adopted.
2. **6:04 — "was an elder in the [unclear] Cross Creek Church".** The modifier is heard as
   "Montmartre/Montblanc" in six of eight passes, and the church name after it moves too
   ("Presbyterian", "Cross", "Prospect Christian"). **"Montour" is not a reading of this sound** — it
   is two syllables ending /-tʊər/ and nothing in eight passes produces that shape — and the earlier
   "Montour" candidate is withdrawn.
3. **15:12 — "two quotations … from [unclear] concerning his saintliness".** Six of eight passes open
   on "Lois/Lawson" and the rest of the citation changes every time. It is a written source — the
   next sentence is the 1889 Presbytery history's own wording — but the name he gave it is not
   recoverable.
4. **12:54 / 14:29 — "Huntington Plantation" then "Huntington Plantation".** Each mention is stable on
   its own (12:55 Huntington 6/6; 14:29 Huntington 6/7) and beam width, gain, VAD and speed each fail
   to move either one. **The split is real** — he used two different words for the same tract within
   90 seconds — and has not been harmonised. Which form is the tract's name cannot be settled from
   the audio.
5. **29:40 — "on June 23, 1867, which was indicated as the last day".** The date splits 3–3 (21st /
   23rd) and the phrase three ways ("first day" ×4, "fast day" ×3, "last day" ×1). The 1867 calendar
   makes 21 June a Friday — the fast day of a communion season, and its first day in the season's own
   phrasing — the only internally coherent combination; but the digits cannot be forced. Left as
   spoken.

**Not transcript gaps, preserved here unchanged:**

6. **The tape ends mid-quotation** at 29:52 ("Is there no physician there?"). Nothing follows but
   room tone and a click at 31:01. The lecture is truncated, not the transcription.
7. **DATING CONFLICT — 1833 against 1832.** White says George Marshall "was ordained to the ministry
   and became a pastor of the Bethel Church here **in 1833**" (25:20) and repeats it (26:01). Ann
   Connor's class of 17 October 1971 says the first Sabbath of **June 1832**. This is the same order
   of discrepancy as her own 1803/1806 slip on Marshall's birth in that class, and the 1951 history
   is not on hand to settle it. Both readings stand as spoken; a researcher citing the date should
   cite the speaker. **Nothing has been harmonised or cross-referenced**, in either transcript or in
   either note.

## File inventory

| File | What it is |
|---|---|
| `Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971).m4a` | the master, as received; md5 `674b2c72569f0c908c729d9101a7729a` |
| `… .txt` | the transcript: 75 labelled turns, source of truth for both documents |
| `… .srt` | 328 timed cues, speaker label on the first cue of each turn |
| `… .json` | provenance: raw ASR segments (head repair flagged), per-word timings and probabilities, stereo and level measurements, 182 `post_edits`, 5 `unresolved` (+2 notes preserved outside that list), `speaker_attribution`, `head_repair` |
| `… .docx` | the filed document, built from the `.txt` |
| `… .md` | the same document in Markdown |
| `… (portable).mp3` | mono 64 kbps listening copy, full 31:02.9 timeline, level correction applied |
| `NOTES - … .md` | this record |

**The MP3 is a portable copy, not a condensation** — hence the name. Measured dead space at
`silencedetect=noise=-35dB:d=1.5`: 7.3 s of leader at the head and 63.3 s at the tail; the other
31 detected "silences" are 1.5–4.3 s pauses inside ordinary speech, which in a lecture are the
speaker thinking. **No speech-bearing time was removed and the timeline is unshifted**, so every
`.srt` cue points at the same moment in the MP3 as in the master. The MP3 measures **−20.1 dBFS
mean, −18.83 LUFS, −1.12 dBTP**; the master carries no processing.

## Verification

```
verify_md_docx.py --dir .          -> 75 / 75 paragraphs, 3,767 / 3,767 words, 75 / 75 labels, MATCH
reconcile_md_json.py --md … .md --json … .json
                                  -> JSON-CONSISTENT, md-only 29 / unrecorded 0, not_reflected 0, orphans 0,
                                     post_edits 182 (127 applied, 31 already in segments, 24 insertions)
```

## Rebuild

Rebuild the documents only from the `.txt`; never edit the `.docx` or `.md` by hand, or the next
rebuild silently reverts it.

```bash
cd "Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971)"
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_docx.py \
    "Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971).txt" \
    "Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971).docx" \
    --title "Bethel Presbyterian Church" --subtitle "Historical Room - Oral History" \
    --byline "Alvin Dinsmore White | a lecture on Cross Creek and the Dinsmore family | recorded 31 October 1971 | 31 min 3 s" \
    --note "<provenance note>" --main-speaker WHITE --secondary ANN
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_md.py \
    "Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971).txt" \
    "Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971).md" \
    --title "Bethel Presbyterian Church" --subtitle "Historical Room - Oral History" \
    --byline "Alvin Dinsmore White | a lecture on Cross Creek and the Dinsmore family | recorded 31 October 1971 | 31 min 3 s" \
    --note "<provenance note>" --main-speaker WHITE --secondary ANN \
    --verify-docx "Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971).docx"
```

Both labels here are one word, so neither needs quoting; if either is ever renamed to a two-word
name, **quote it** (`--secondary "ANN CONNOR"`) or the builder splits the flag and silently drops
the label.

## Relation to the other recordings in this archive

- **`George Marshall Class (17 October 1971)/`** — the companion. Ann announces this lecture at
  12:10 of that tape and asks White to talk about John Stockton; he does, from 21:28 here. The two
  are best read in that order.
- **`History of George Marshall and other Ministers/`** (c. 2001) — Ann's later, expanded version of
  the Marshall material, in which she says "a lot of what I have is what Alvin Dinsmore White gave
  to me" and describes him as "a fabulous historian … from Cross Creek". This recording is the
  primary evidence behind that debt: the Cross Creek detail, the Stockton academy, the Marshall-1831
  connection and the dates of Marshall's Cross Creek sermons all originate here.
- **`Ann Connor - Sides A and B/`** (c. 2001) — the same archive voice; the c. 2001 talk uses the
  Dinsmore family as an example of a Bethel family that left for Upper Buffalo because of distance,
  which White explains from the other end at 11:29 here.

## Potential tape damage at 1:49

The 1:47-1:53 window is measurably degraded in the source: **24 dB of roll-off above 6 kHz** (6 kHz band -57.2 dB against a -33.8 dB speech band), **no clipping** (flat factor 0.000000), and **8 micro-gap dropouts in 6 seconds** - the worn or shed-oxide signature. The consonants that would separate the candidate readings are not present in the recording, so this gap may be physical rather than acoustic. Marked **potential** because it is measured from the digitised copy, not from the original tape.
