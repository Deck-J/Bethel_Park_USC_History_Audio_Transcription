# A.D. White — Cross Creek and the Dinsmore family (31 October 1971)

Oral history recorded for the Historical Room at Bethel Presbyterian Church, Bethel Park,
Pennsylvania: a lecture to Ann Connor's church-history class, in which Alvin Dinsmore White — who
wrote the history of Cross Creek church — is asked to talk about his own family and about the
minister who ties Cross Creek and Bethel together.

| | |
|---|---|
| **Speaker** | Alvin Dinsmore White (1894–1992), of Hickory, Pennsylvania |
| **Introduced by** | Ann Connor, who teaches the class |
| **Recorded** | Sunday, 31 October 1971 (the date is on the cassette label — see §1) |
| **Length** | **31 m 03 s** (1,862.997 s), one continuous side |
| **Words** | 3,718 spoken words in 75 labelled paragraphs (13 `ANN`, 62 `WHITE`), counted from the filed transcript with the speaker labels excluded |
| **Status** | Transcribed, corrected, labelled, verified; master held on the archive NAS |

---

## 1. How the date is established

The date is **on the cassette**: the label reads `10.31.71`. That is the primary evidence, and it is
recorded in the archive JSON's `date_basis`. The name the capture came in with also carries it —
`10.31.71 Alvin Dinsmore White  History of Cross Creek and Dinsmore family.m4a`, the `source_file` in
that JSON (the file itself is now named for the folder). A filename alone would not be enough, so the
date is checked three ways:

- **The weekday fits.** 31 October 1971 was a **Sunday**, and this is a Sunday-school class.
- **The tape dates itself by reference.** White opens "We were here last February"; he refers to Ann's
  outline arriving "in a recent communication"; and Ann begins at 1:39 with "Last week, we sort of left
  the church and went elsewhere, took the group and went to Mingo Presbyterian Church" — the class's
  previous meeting.
- **The previous week's tape names this one.** In the 17 October 1971 class recording, at 12:10, Ann
  says: "And on the 31st of this month, Mr. Alvin Dinsmore White is going to come back, and I'm going
  to ask him to tell you a little bit about this man, John Stockton." This lecture is that promise
  kept — Stockton gets his own section from 21:09.

Two dates that are **not** the recording date: `2026-10-18` in the archive folder name is the
**digitisation** date, and the file timestamps on the transcript are the transcription date.

## 2. The physical recording and its capture

| | |
|---|---|
| Master file | `Alvin Dinsmore White - Cross Creek and the Dinsmore Family (31 October 1971).m4a` |
| Format | ALAC 48 kHz stereo 16-bit (`s16p`), 261.8 kb/s |
| Duration | **1,862.997 s (31 m 03 s)** |
| Size | 60,978,057 bytes |
| sha256 | `bc783c63321fb20937a877f692517080361e7c87be86d3448e84d1b756ac40c9` |
| md5 (capture record) | `674b2c72569f0c908c729d9101a7729a` |
| Mean level | **−30.2 dBFS** |
| Peak | **−3.1 dBFS** |
| Integrated loudness | **−25.7 LUFS**, LRA 12.2 LU |

Measured here with `ffmpeg` (`volumedetect`, `ebur128`) against the master as it sits on the NAS; the
figures agree with the archive's own record to the tenth of a dB. The capture is lossless, so nothing
in these transcripts was limited by a lossy intermediate.

**Level.** Mean −30.2 dBFS is 7–11 dB above the 17 October class (−42.1 dBFS) and the Edna Croco tape
(−45.5 dBFS), but still about 7 dB below the archive's −16 to −19 LUFS band, so the audio was
**amplified, not enhanced**: a two-pass `loudnorm` to I = −18.5, TP = −1.5, LRA = 11 gave an effective
+10.2 dB, applied to the ASR working copy and to the portable MP3. **The master carries no processing
at all**, and no denoise was used anywhere: the capture is band-limited to roughly 3 kHz (0–300 Hz
8.10 %, 300 Hz–3 kHz 91.73 %, 3–8 kHz 0.16 %, 8–16 kHz 0.007 %), which is tape and deck response, not
hiss.

**Stereo.** A delayed duplicate, not two microphones: ch0 −31.18 dBFS, ch1 −29.37 dBFS (1.81 dB
apart), correlation 0.985–0.993 at a constant 1–3 sample lag. The channels were summed as
`(1·ch0 + 2·ch1)/3` with ch1 shifted back 2 samples — an equal-weight sum would carry the weaker feed
at full weight, and taking ch1 alone would throw away a near-perfect second copy.

**A second capture in the same folder.** `second recording.m4a` (1,858.304 s, 62,391,122 bytes,
sha256 `f182d9f5be73bc9602ebdacb7a91c96aea720ec9516f39db63ffe8536bd6abdf`) sits beside the master and
is **not** the same file: shorter, larger, a different hash. It appears to be the **same performance on
a second recorder**, and that is measured rather than assumed — its one-second level envelope tracks
the master's with a slowly drifting lag, −1 s at two minutes to −6 s at twenty-eight minutes, which is
a clock offset and not a different talk. It was not transcribed and is not filed as a side; the
transcript follows the longer, named master. Anyone re-transcribing this lecture should know it exists
as a second acoustic witness to the words disputed in §6.

## 3. What was done to it (the method)

1. **Measured before touching.** Duration, level, spectrum and quietness sweep, and a check for a
   level step that would mean two sessions spliced onto one file. There is none.
2. **Established the stereo relationship** rather than assuming it, then aligned and summed.
3. **Built the ASR working copy** at +10.2 dB, measured it back at −19.6 dBFS mean / −1.4 dBFS peak /
   −18.38 LUFS, and only then handed it to the model in 16 kHz float32.
4. **Chunked on quiet points.** **16 chunks** of 113–118 s, each boundary snapped to the quietest
   10 ms frame within ±5 s of a 120 s target, with 3 s of padding either side. Never a whole-file pass.
5. **Seeded the prompt with 89 words** of names this recording is actually about — Dinsmore, Cross
   Creek, Stockton, Miller/Millar, Fife, McKnight, McCormick, Nevill — plus the general collection
   vocabulary. The Bethel township seed was read and **not** added, because the subject is Washington
   County. Uncertain readings from the review notes were deliberately left out of the prompt.
6. **Ran a full second pass with no prompt** over the same 16 boundaries as a leak and collapse
   detector, and compared the two word by word.
7. **Repaired a head collapse.** The first thirty seconds are speech 25 dB below the rest of the
   programme; both passes returned a single "Thank you." and then nothing until 0:30. That window was
   re-transcribed alone at **+20 dB with no prompt**, which recovered the opening sentence and 44
   words. Those segments replace chunk 0 and are flagged `"head_repair": true` in the JSON.
8. **Corrected, and recorded every correction** in the JSON's `post_edits` — what was heard, what it
   became, why, and how certain.
9. **Labelled the speakers** (`ANN`, `WHITE`) and joined run-on fragments, dropping filler only.
10. **Built the `.md` and `.srt` from the labelled text** and verified them against it — paragraph
    count, word count and label runs — rather than reading them over by eye.
11. **Checksummed the folder** (`checksums.sha256`) and kept the master out of the repository.

## 4. Engine, and what it measured

| | |
|---|---|
| Engine | faster-whisper **large-v3**, CTranslate2 **int8**, beam 5, 14 CPU threads |
| Version | faster-whisper 1.2.1 / CTranslate2 4.8.3 |
| Chunks | 16, quiet-point snapped, 113–118 s |
| Seeded / plain pass words | 3,690 / 3,681 |
| Segments | 259 |
| Mean per-word probability | **0.8836** (6.70 % of words below 0.5; 14.7 % below 0.7) |
| Weakest stretches | 2:00–6:00 (Ann's introduction, off-mic), 18:00–20:00, 28:00–30:00 |
| Strongest | 8:00–10:00 (0.927) |

**No prompt leak.** No segment in the prompted pass is built out of seed tokens; the one paragraph
that tripped a seed-fraction filter is the single word "family" at 14:44, at the end of "his son John
and his wife and family". The two passes agree within a few words per 30 s window, and **no window was
deleted**. Where they disagreed the span was judged on its own words: at 5:00 the prompted "Cross
Mexico District" was corrected to Cross Creek; at 6:00 "Montmartre Cross Creek Church" was marked
`[unclear]` because neither pass supports a name; at 18:00 the prompted reading was taken.

**Seams.** 355 of the 3,914 raw words were duplicates at chunk heads and were trimmed by prefix-only
de-duplication — each word assigned to its own core — leaving 3,690. Every seam was read across.

## 5. Corrections made (183, all reversible)

The JSON holds **183 `post_edits`** entries (the archive note's prose says 182; the array is what was
counted here), of which 153 are marked probable, 29 certain and 1 uncertain. Each carries the raw
form, the replacement, a reason and a certainty. The substantive ones:

| heard | changed to | basis | certainty |
|---|---|---|---|
| "Thank you." at 0:10 | the real opening sentence (44 words) | both passes collapsed over speech 25 dB down; recovered by a +20 dB unprompted re-pass | certain |
| "during the passport of Dr. George Warne" | "during the pastorate of Dr. George Marshall" | the subject of the sentence and of the previous class | certain |
| "History of the Conflict Church" | "history of the Cross Creek Church" | the church Ann is introducing, named correctly twice in the same paragraph | certain |
| "Mr. Albert Dinsmore White" | "Mr. Alvin Dinsmore White" | his name, correct in the inscription Ann reads 40 s later | certain |
| "James Binsmore … John Binsmore … James Dunmore" | James / John **Dinsmore** | one family, named correctly in the same paragraph | certain |
| "the Isabella school district" | "the **Avella** school district" | White's own published biography, Elementary Principal of the Avella Joint Schools | certain |
| "in the present South Bay of the Panthers" | "in the present **South Fayette Township**" | Miller's Run runs through South Fayette, a couple of miles southwest of Bridgeville | probable |
| "the land of Hayden" | "the **Land of Canaan**" | re-listened: the 10:40 and 11:29 mentions are the same syllable | probable |
| "joined the BAR and SAR" | "joined the **DAR** and SAR" | Daughters and Sons of the American Revolution | certain |
| "her body was spread for burial" | "her body was **brought** for burial" | internal corroboration at 12:20 | certain |
| "too far from Cherk about seven miles" | "too far from **church**" | "Cherk" is the ASR's *church* throughout this tape | certain |
| "the Craft Breaker Academy in 1828" | the **Cross Creek** Academy | founded by Stockton, named in White's own book | certain |
| "Exodus 15-2 … that healed thee" | Exodus 15:**26** … that **healeth** thee | the verse quoted is Exodus 15:26, KJV | certain |
| "the Tribunan service … a post-Tribunan sermon" | the **communion** service … **post-communion** sermon | no pass at any setting returns "thanksgiving"; communion is the Monday service | probable |
| "Soak yourselves in righteousness" | "**Sow** yourselves in righteousness" | Hosea 10:12 | certain |
| "from Jeremiah 1822 … no bomb in gillian" | Jeremiah **8:22** — "no **balm** in **Gilead**" | the verse identifies itself | certain |
| "he died in 1972" | "he died in **1872**" | Marshall's death, given as 1872 twice in the same passage | certain |
| "Densmore" throughout | **Dinsmore** | the family spelling and his own middle name; the pronunciation is "Densmore" | certain |
| "Rev. Coughlin was strapped to a pair of farm wagon wheels" | "**the rough coffin** was strapped to a pair of farm wagon wheels" | 12:22 — 10 of 12 unprompted passes; "thus transported to the graveyard" | certain |
| "to obtain silk" | "to obtain **salt**" | 10:48 — what a settler rode east for | certain |
| "James Dinsmore, 1860 to 1870" | "James Dinsmore, **1806** to 1870" | elder from 1837, d. 1870, b. 20 May 1803 — 1860 is impossible | probable |

Mechanical repairs alongside: chunk-seam stutters collapsed ("years. years.", "do do not", "Walker,
Walker"), sentence and proper-noun case restored, and `[unclear]` inserted only where no pass
recovered a word.

## 6. Left as heard — the honest gaps

Nineteen doubtful windows were re-listened to on 2026-10-20 with the seed prompt removed — 131 passes
over 4,146 s of audio, at beam 5 and 1, with and without VAD, at +6 dB, slowed to 0.8× with pitch
preserved, and as micro-crops. **Stability, not confidence, was the test**: a word that moves with
beam width, gain, VAD or speed is a guess and stays a gap. Nine readings changed; five were left:

- **1:49 — "during the period [unclear]"**, bracketed and marked **[POTENTIAL TAPE DAMAGE]**. The
  1:47–1:53 window measures 24 dB of roll-off above 6 kHz and 8 micro-gap dropouts in 6 seconds — the
  shed-oxide signature — so the consonants that would separate the candidates are not there.
  "Whiskey Rebellion", the obvious historical guess, appears in no pass and was not adopted.
- **6:04 — "was an elder in the [unclear] Cross Creek Church"**; the modifier moves every pass.
- **15:12 — "two quotations now that I want to give you from [unclear]"**; the source is a written one
  but the name he gave it is not recoverable.
- **12:54 and 14:29 — "Huntington Plantation"**, each mention stable on its own, the two forms not
  harmonised. He used two different words for the same tract within 90 seconds; which is the name
  cannot be settled from the audio.
- **29:40 — "on June 23, 1867, which was indicated as the last day"**; the date splits 3–3 (21st/23rd)
  and the phrase three ways. The 1867 calendar makes 21 June a Friday, the fast day of a communion
  season, but the digits cannot be forced.

Two things that are **not** transcription gaps, preserved as spoken:

- **The tape ends mid-quotation** at 29:52 ("Is there no physician there?"). Nothing follows but room
  tone and a click at 31:01. The lecture is truncated, not the transcription.
- **A dating conflict.** White says Marshall was ordained at Bethel "in 1833" (25:25 and 26:01); Ann
  Connor's class of 17 October says the first Sabbath of June 1832. Both stand as spoken, with no
  harmonising. A researcher citing the year should cite the speaker.

Also left alone: **1895 against 1896** for the academy's end. He says 1895 and four of four passes hear
it; his own *History of Cross Creek Country* (1969) and the 1954 alumni marker both say 1896. The
number was not altered — the discrepancy is the finding.

And one label that is a judgement: **`ANN` is an introducer, not an interviewer.** She presents the
speaker and his book and asks no questions; the 13 paragraphs under her name are all introduction.

## 7. What is on the tape — outline with timestamps

- **0:10** Ann Connor: the class has been working through the Presbyterian forefathers; the surface
  has only been scratched
- **1:39** Last week the class went to **Mingo**; this week, **Cross Creek**
- **3:16** She introduces the man who wrote the Cross Creek history and has "an extensive library of
  his own"
- **4:00** She presents his book, *History of the Presbytery of Washington*, to the class library and
  reads the gift inscription he wrote in it
- **6:40** White takes over: "Thank you, Mrs. Conner"; he was here last February
- **8:19** Ann sent an outline; the first item is **his great-great-great-grandfather James Dinsmore**
- **9:06** James Dinsmore, Scotch-Irish, b. County Antrim 26 April 1742; the family reunions
- **10:05** The crossing of the Alleghenies on snowshoes in the winter of 1761–62
- **10:23** Miller's Run in South Fayette Township, 1772; the patent for the **Land of Canaan**, 1786
- **11:15** Rebecca Walker, married at Gettysburg in 1776; his Revolutionary War service and the
  family's DAR and SAR membership on it
- **11:37** Bethel's elder; Rebecca's death in 1791 and the unmarked grave; **the rough coffin on
  wagon wheels**
- **12:54** 1795: the farm sold because it was seven miles from church; **Huntington Plantation** in
  Canton Township
- **13:35** 1800: the double wedding — James to Elizabeth Carr, his son John to her sister Jane — and
  the third Carr marriage three years later
- **14:24** The brick house of 1810, fourteen rooms, still in the Dinsmore name
- **15:12** Two quotations on his saintliness (the source's name is a gap); the first ruling elders
- **16:19** The grandson's tribute, the Rev. James H. Dinsmore — and White's corrections of it
- **19:05** Upper Buffalo, Joseph Smith, Thomas Marquis, John Anderson, the revival of 1802
- **20:21** The "trilogy": Bethel, Upper Buffalo and Cross Creek; his own great-grandparents
- **21:09** **John Stockton** at Cross Creek, and why the two congregations are tied together
- **21:45** Stockton's family, Washington College class of 1820
- **22:18** 1827: no public schools before the Act of 1834, subscription schools, the academies
- **23:05** **Cross Creek Academy, 1828** — and the young **George Marshall** hired to teach in it
- **24:07** Marshall, Jefferson College class of 1831; the W&J rivalry; licensed to preach in 1830
- **25:25** Ordained at Bethel in 1833 (see the dating conflict above); his marriage to **Mary Lee**
  of Cross Creek
- **26:45** Marshall's death in 1872 and the friendship with Stockton
- **27:42** Marshall's recorded preaching at Cross Creek: Exodus 15:26 (2 April 1854), 1 Thessalonians
  5:6 (18 June 1858), and the **communion weekend of 23–25 September 1864** — Hosea 10:12, Luke 15:10
- **29:14** Revelation 2:5 (28 January 1866)
- **29:35** Jeremiah 8:22 (23 June 1867) — the tape stops mid-verse

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The transcript: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt` | The same text as 328 timed cues, for playback or captioning |
| `notes-a.md` | The archive's working record, verbatim: measurements, chunks, cold passes, every judgement |
| `metadata.json` | The record of record: date and its source, speakers, master with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

The **audio master is not here** (see `docs/AUDIO.md`): it is held on the archive NAS, two copies,
identified above by sha256.

## 9. Citing it

> White, A. D. (Alvin Dinsmore). *Cross Creek and the Dinsmore family*. A lecture to Ann Connor's
> church-history class, 31 October 1971. Historical Room, Bethel Presbyterian Church: digitised
> 18 October 2026. Transcript, 3,718 words.

Cite the timestamp for anything quoted — the transcript keeps the tape's own timebase, so a claim can
always be checked against the master.

## 10. Reproducing this transcript

- model: large-v3, CTranslate2 **int8**, language `en`, **beam 5**, `condition_on_previous_text=False`,
  `temperature=0.0`, `vad_filter=False`
- **16 chunks** of 113–118 s, quiet-point snapped, 3 s padding
- seed: 89 words of collection and Cross Creek/Dinsmore names, with a leak check by full unprompted
  second pass
- input: the +10.2 dB working copy described in §2 — **not** the raw master

A re-run on the same master with these settings reproduces the raw ASR text; the filed transcript
differs from it only by the corrections in §5, each a line in the JSON's `post_edits`.

## 11. Related material in the collection

- **The George Marshall class, 17 October 1971** — the companion. Ann announces this lecture at 12:10
  of that tape and asks White to talk about John Stockton; he does, from 21:09 here. Read them in
  that order.
- **A.D. White, "Cross Creek records and the Whiskey Rebellion", 15 July 1971** — the same speaker
  four months earlier, in an interview: the informal version of much of this material.
- **"History of George Marshall and other Ministers"** (c. 2001) — Ann Connor's later, expanded
  version, in which she says "a lot of what I have is what Alvin Dinsmore White gave to me". The
  Cross Creek detail, the Stockton academy and Marshall's Cross Creek sermon dates all originate here.
