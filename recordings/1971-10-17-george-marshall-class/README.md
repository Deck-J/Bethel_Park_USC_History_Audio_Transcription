# Ann Connor — A class on Dr. George Marshall (17 October 1971)

Oral history recorded for the Historical Room at Bethel Presbyterian Church, Bethel Park,
Pennsylvania: the church's collector teaches a Sunday-school class on its third pastor, working from
the objects she has carried in — Marshall's desk, the family Bible, the pulpit Bible, a handbell — and
from the church's first record book.

| | |
|---|---|
| **Speaker** | Ann Connor, teaching the class |
| **Also on the tape** | An unidentified male participant (`GUEST`), who speaks twice during the class and then gives a three-minute account of his own ministry |
| **Recorded** | Sunday, 17 October 1971 |
| **Length** | **30 m 24 s** (1,823.744 s), one continuous file |
| **Words** | 3,554 spoken words in 90 labelled paragraphs (82 `ANN`, 8 `GUEST`), counted from the filed transcript with the speaker labels excluded |
| **Status** | Transcribed, corrected, labelled, verified; master held on the archive NAS |

This is a **class, not a lecture**. She sets homework ("I gave you an assignment last week"), asks the
room a question and counts the answers ("one, two, three, four — Robbie knows, but I don't"), and
hands over to a visitor to describe a photograph ("Would you like to tell them?"). 1971 is the
collection's earliest year, and this tape and the 31 October lecture answer each other: here she
announces that Mr. White will speak at the end of the month; there he does.

---

## 1. How the date is established

The date is written on the **physical cassette label**, `10.17.71`. That is the primary evidence, and
it is the archive's working record that says so — with the digitizer confirming it is a label on the
tape, not an inference from a filename. It is corroborated three ways:

- **The weekday fits.** 17 October 1971 was a **Sunday**, and this is a Sunday-school hour: she refers
  to "as we saw last Sunday with our communion set" and to "an assignment last week".
- **The tape states no date of its own**, and nothing on it contradicts the label.
- **The one forward-looking date on the tape lands exactly.** At 12:10: "And on the 31st of this
  month, Mr. Alvin Dinsmore White is going to come back, and I'm going to ask him to tell you a little
  bit about this man, John Stockton." 31 October 1971 was also a Sunday — the next meeting of this
  class. A label written a year late would put that sentence out of joint.

`2026-10-18` in the archive folder name is the **digitisation** date, not the recording date.

## 2. The physical recording and its capture

| | |
|---|---|
| Master file | `George Marshall Class (17 October 1971).m4a` |
| Format | ALAC 48 kHz stereo 16-bit, 195.8 kb/s |
| Duration | **1,823.744 s (30 m 24 s)** |
| Size | 44,640,137 bytes |
| sha256 | `e64aba5a3afbf134ca3468338c1cfef6ad9a56054f9a0729b7c028c4ca54c92e` |
| md5 (capture record) | `900a30ad9459a04cbb37fc7e07e04760` |
| Mean level | **−42.1 dBFS** |
| Peak | **−12.9 dBFS** |
| Integrated loudness | **−37.6 LUFS**, LRA 14.3 LU |

Measured here with `ffmpeg` (`volumedetect`, `ebur128`) on the master as held on the NAS; the figures
agree with the archive's record (−37.65 LUFS, LRA 14.5).

**It is very quiet, and measurably so.** Roughly **19 dB below the rest of the collection** (which
sits at −16 to −19 LUFS), which is why it sounds faint next to its neighbours. Gain was applied to the
**listening copy only** — a two-pass `loudnorm` to I = −18.1 LUFS with a −2.2 dBTP ceiling, measured
back at −19.29 LUFS, −1.79 dBTP, LRA 8.7 — and **the master is untouched**.

**There is nothing to denoise.** Only 0.012 % of the energy is above 8 kHz and 0.06 % between 3 and
8 kHz: the capture is band-limited to roughly 3 kHz, which is tape and cassette-deck response, not
hiss. A filter here would remove speech and nothing else.

**Stereo.** A delayed duplicate: ch0 −43.23 dBFS, ch1 −41.26 dBFS (1.97 dB apart), correlation
0.9866–0.9906 at a constant +4-sample (0.083 ms) lag, against a raw correlation of 0.883 without
compensation. Summed as `(1·ch0 + 2·ch1)/3` with ch1 shifted back 4 samples; post-sum correlation
against ch1 alone is 0.999, so the sum has not comb-filtered.

**The last three and a half minutes are a separate recording.** Speech stops at 26:47; the level falls
to −61 dBFS by 26:55; at 27:05 a new voice starts **17 dB louder** than the class, and the room tone
changes with it. Everything from 26:47 to 29:09 is the `GUEST`'s account of his own ministry. It is in
the same file and is part of the recording — the tape was evidently restarted, or left running into
another session — so it is transcribed and labelled rather than cut. Anyone citing it should know it
is **not** part of the class discussion.

## 3. What was done to it (the method)

1. **Measured first**: duration, level, a sixty-second level sweep (block peaks −12.9 to −23.8 dBFS,
   block means −34.2 to −47.2 dBFS), spectrum, and the silent tail.
2. **Established the stereo relationship** by measurement, then aligned and summed.
3. **Chunked on quiet points**: **16 chunks** of about 116–124 s, each boundary snapped to the
   quietest 10 ms frame within ±5 s of a 120 s target. Never a whole-file pass. Audio decoded by
   ffmpeg to float32 arrays — PyAV in this build rejects the `metadata_errors` kwarg faster-whisper
   passes, so the array path was used deliberately.
4. **Seeded the prompt** with the general collection seed plus the Bethel/Chartiers vocabulary —
   this is a Bethel Township subject — trimmed to **195 tokens** so nothing was truncated out of the
   tail. The uncertain readings in the review notes were deliberately **not** seeded, and no name was
   added from the filename.
5. **Ran a full second pass with no prompt** over the same 16 boundaries as the leak and collapse
   detector.
6. **Nothing needed splicing.** The prompted pass produced 3,643 words against the plain pass's 3,637,
   and per-chunk counts agree within ±8 words except at chunks 1, 11 and 12. Where they disagreed the
   span was judged on its own words, not on the count: at 2:06 the plain pass's "that in his youth" was
   taken; at 2:17 the plain pass recovered "the Mexican War and" that the prompted pass dropped; at
   22:52 the plain pass recovered "James would have been the oldest son in the family".
7. **Removed three tail hallucinations** — "Thank you." at 29:19, 29:36 and 30:07, emitted over room
   tone at −83 to −90 dBFS, thirty to seventy seconds after speech ends. They are recorded as
   deletions in the JSON, not silently dropped.
8. **Corrected, and recorded every correction** in `post_edits`.
9. **Labelled the speakers** and read the whole file end to end — all 226 segments and all 90
   paragraphs — in order.
10. **Built the `.md` and `.srt` from the labelled `.txt`** and verified them against it.
11. **Checksummed the folder** and kept the master out of the repository.

## 4. Engine, and what it measured

| | |
|---|---|
| Engine | faster-whisper **large-v3**, CTranslate2 **int8**, beam 5, 14 CPU threads |
| Version | faster-whisper 1.2.1 / CTranslate2 4.8.3 |
| Chunks | 16, quiet-point snapped |
| Seeded / plain pass words | 3,643 / 3,637 |
| Segments | 226 |
| Mean per-word probability | **0.8609** (9.77 % of words below 0.5; 17.6 % below 0.7) |
| Weakest stretches | 7:00–9:00, 17:00–18:00, 21:00–23:00 (two voices), 29:00–30:31 |
| Strongest | 20:00–21:00 — she is reading a printed page |

0.8609 is inside the archive's acceptable band but the weakest of the collection's tapes, and that is
a property of the **source**, not the model: the capture has no energy above 3 kHz. The plain pass's
40 extra words in chunk 11 were *invented filler*, not recovery — the reason a word count is not a
quality measure.

## 5. Corrections made (155, all reversible)

Every change from the raw ASR is in the JSON's `post_edits` with its raw form, its replacement, a
reason and a certainty — 62 certain, 84 probable, 9 marked unresolved. The substantive ones:

| heard | changed to | basis | certainty |
|---|---|---|---|
| "the big death of all these dr marshall" | "the big desk that belonged to Dr. Marshall" | three cold passes; the desk is the object the talk opens with | certain |
| "Thomas Marcus", "Elisha McCurdy" | Thomas **Marquis**, Elisha **Macurdy** | real contemporaries of McMillan in the revival she describes | probable |
| "Reverend Mr. Swift" | Reverend Mr. **Woods** | Bethel's second pastor; the sequence McMillan–Clark–Woods | probable |
| "Chancellor of Bethel" | "**pastor** of Bethel" | plain pass | certain |
| "Hessel Academy" | **Bethel** Academy | the academy Marshall founded at Bethel | probable |
| "revelate in the seventh chapter" | "**Revelation**, the seventh chapter" | the text of the Civil War sermon | probable |
| "WSJ" | **W&J** | Washington & Jefferson holds the sermon | certain |
| "Dr. Murray's journal" | Dr. **Marshall's** journal | the book in her hand, named correctly three times elsewhere | certain |
| "the word disembarrassed" | "the word **dysentery**" | the disease that recurs in a church death register | probable |
| "Alvin Hensmore / Hinton / Allison Moore White" | Alvin **Dinsmore** White | one man, three ASR attempts | probable |
| "Crossbridge / Frost Creek / CrossFit / Templeton" | **Cross Creek** | "Cross Creek Church" comes through cleanly three times in the same file | certain |
| "as the death of Dr. Marjorie was passed on" | "at the death of Dr. **Marshall**, and was passed on" | same man throughout | certain |
| "Well, thanks. We're the oldest science team." | "Well, **James would have been the oldest son in the family**." | plain pass; she is listing the six children | certain |
| "a fine breakfast president" | "a fine **brick residence**" | the 1951 history's description of the farmhouse, read aloud | probable |
| "Mr. William McGaughan" | Mr. William **McCully** | attested Bethel surname; plain pass reads McCully | probable |
| "from 1830 to 1760" / "About 18 days" | 1830 to **1860** / "About **1860**" | the academy's dates and closing year | probable |
| "St. Michael Marshall Road" | **Marshall Road** | named for the Marshall farm | probable |
| "Bethel presbytery Presbyterian Church" | **Bethel Presbyterian Church** | ASR artifact | certain |
| "Thank you." ×3 (29:19, 29:36, 30:07) | removed | hallucinated over room tone 30–70 s after speech ends | certain |

Mechanical repairs alongside: one doubled word collapsed at a chunk seam ("because because"),
sentence and proper-noun case restored, `i` → `I`, and `[unclear]` inserted only where no pass
recovered a word.

## 6. Left as heard — the honest gaps

Fifteen readings are listed as unresolved in the JSON. The ones a reader will meet:

- **Ann contradicts herself on Marshall's birth**: "born in 1803" (1:37) and "born in Union County,
  December the 23rd, 1806" (10:13). Both left as spoken; the later, specific date is almost certainly
  the one she meant.
- **This tape and White's 31 October lecture disagree on the call**: she says he preached the first
  Sabbath of **June 1832** and was ordained and installed; White says **1833**, twice. Nothing has been
  harmonised in either transcript.
- **"The other items deal with the [unclear] of Dr. Wycoff"** (4:42) — plaster? portrait? casket?
- **"which is [unclear] for the article"** (7:27) — first sentence of the register description.
- **The tail of the journal-copy sentence** (9:42) is unintelligible in every pass and was not carried
  into the text. This is the one place where the document has less text than the audio.
- **A child's name** between "Anna Margaret" and "the youngest, John Stockton" (16:47). She names five
  of the six children; the sixth is not recoverable.
- **"the white stones meet the marker"** (18:41) — read as "stones"; the phrase stays uncertain.
- **"Jacob Warlock"** (20:02), an 1861 land purchase. Jacob **Morlock** the sexton is named at 26:12;
  whether it is the same family name is unresolved and no substitution was made.
- **The Westinghouse lawyer anecdote** (20:59–21:26) is largely unintelligible and is transcribed as
  heard, with `[unclear]` where a word is missing.
- **Who the `GUEST` is.** Pitch separates him from Ann by nearly an octave (123–142 Hz against
  205–254 Hz), but whether the two interjections and the closing ministry account are the same man is
  **plausible and unproven**: the ranges overlap and the two sit two and a half minutes apart on
  recordings made at different levels. One label, not two.
- **One 26-second passage is attributed with less confidence than the rest.** At 5:24 Ann says "Would
  you like to tell them?" and the reply measures **219 Hz**, inside her own range; nothing in the words
  separates the two women. It is labelled `ANN` because the audio cannot support a different label,
  though the content says it is probably a visitor.

## 7. What is on the tape — outline with timestamps

- **0:21** The desk that belonged to Dr. Marshall, and what it started
- **0:53** What she has already covered — McMillan, John Clark, Mr. Woods — and why Marshall is next
- **1:37** Born in 1803 (contradicted later at 10:13); a pastorate of almost forty years
- **2:22** The Civil War sermon she located at W&J
- **3:12** His wish to prepare young men for the ministry; the historical room's objects
- **3:49** The furniture, the family Bible, the pulpit Bible used from 1850, open at Revelation 7
- **5:04** "Would you like to tell them?" — the visitor describes Marshall's photograph
- **5:40** Items concerning Dr. Wycoff; her hope that the congregation will keep giving
- **6:14** His journal: the church's first record book, and how he kept it
- **8:01** He wrote each entry himself; deaths and their circumstances; whole families of children
- **8:43** Dysentery, and the common communion cup "as we saw last Sunday"
- **9:32** The journal is deteriorating; copies were made through Tom Starkey and Xerox
- **9:55** Born in Union County, 23 December 1806; the oldest of five; his mother Nancy Adams
- **10:42** Milton Academy under the Rev. David Kirkpatrick; Hebrew, Greek, Latin; his health
- **11:30** He could have entered Jefferson College as a senior, but the rules were the rules
- **11:57** To Cross Creek, to study under Dr. John Stockton, boarding with the pastor
- **12:10** The announcement: Mr. White will speak on the 31st about Stockton
- **12:43** Teacher at Cross Creek Academy; the pastor-teacher pattern of his life
- **13:16** The Western Missionary Society, and preparing men for the moving frontier
- **13:40** Mary Lee, daughter of the ruling elder Hugh Lee — and how Mr. White supplied the name
- **15:03** Jefferson College, class of 1831; the call to Bethel, first Sabbath of June 1832
- **15:37** The six children: James Lee, Sarah Agnes Cadoux, Mary Amanda Fife, Anna Margaret, John
  Stockton — and one name lost
- **16:01** James Marshall, who returned the desk and buried his wife and father beside Marshall
- **17:16** Cross Creek five miles from Hickory — and the `GUEST`'s correction, "sort of west"
- **17:57** The white stones, the academy marker, Stockton's house, the church
- **18:31** The academy buildings: a small brick one-story, replaced in 1855 by a two-story building
- **19:36** Open from 1830 to about 1860; the bell moved to the third meeting house
- **19:52** The photograph taken during Dr. Wycoff's pastorate; Marshall had no manse, he had a farm
- **20:52** The old road to Washington; the Westinghouse lawyer anecdote
- **21:47** The assignment: where is this house? Four hands, and "Robbie knows, but I don't"
- **22:15** The farm: bricks made on the premises, the two-story farmhouse, later bought by Mr. Hicks
- **23:38** The 60 acres adjoining Bethel on the east, and the tracts he bought
- **24:39** The farmhouse today, and what Bethel's growth did to the site
- **25:33** The log cabin where the church began, and the house that stands there now
- **26:12** Jacob Morlock the sexton, and the handbells used before the bell was hung
- **27:05** The tape restarts louder: the `GUEST`'s own ministry — 1951, a ship, bugs, Norway
- **28:05** Cambridge, Chinese student work, the housing projects, Coverdale
- **29:01** "In 1959 I came to Bethel Presbyterian Church as associate pastor… On May 1st, 1967, I
  retired." The tape runs on

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The transcript: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt` | The same text as 218 timed cues, for playback or captioning |
| `notes-a.md` | The archive's working record, verbatim: measurements, chunks, cold passes, every judgement |
| `metadata.json` | The record of record: date and its source, speakers, master with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

The **audio master is not here** (see `docs/AUDIO.md`): it is held on the archive NAS, two copies,
identified above by sha256.

## 9. Citing it

> Connor, Ann. *A class on Dr. George Marshall*. Sunday-school class, 17 October 1971. Historical Room,
> Bethel Presbyterian Church: digitised 18 October 2026. Transcript, 3,554 words.

Cite the timestamp for anything quoted — the transcript keeps the tape's own timebase, so a claim can
always be checked against the master. If you are quoting the last three and a half minutes, say so:
that is the `GUEST`, not Ann Connor.

## 10. Reproducing this transcript

- model: large-v3, CTranslate2 **int8**, language `en`, **beam 5**, `condition_on_previous_text=False`,
  `temperature=0.0`, `compression_ratio_threshold=2.4`, `vad_filter=False`, word timestamps
- **16 chunks**, quiet-point snapped
- seed: the general collection seed plus the Bethel/Chartiers vocabulary, 195 tokens, with a leak
  check by full unprompted second pass
- input: the capture as received. The level correction in §2 was applied to the listening copy, **not**
  to the master, and not to the ASR input.

A re-run on the same master with these settings reproduces the raw ASR text; the filed transcript
differs from it only by the corrections in §5 and the deletions in §3.

## 11. Related material in the collection

- **A.D. White, "Cross Creek and the Dinsmore family", 31 October 1971** — the lecture this tape
  announces, delivered two weeks later by the man she describes here as "a historian who has written
  the history of his own church".
- **"History of George Marshall and other Ministers"** (c. 2001) — Ann's later, expanded delivery of
  the same material: the library and the will, the trunk from John McCabe's barn, the Europe trip with
  Thomas Cadoux. None of that is on the 1971 tape — in October 1971 she was still gathering it.
- **A.D. White, "Cross Creek records and the Whiskey Rebellion", 15 July 1971** — the interview that
  first put her in touch with the Cross Creek material.
