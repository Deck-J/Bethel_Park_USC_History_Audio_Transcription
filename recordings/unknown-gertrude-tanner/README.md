# Gertrude Tanner — Brookside and the women's club (1985)

Oral history recorded for the Historical Room at Bethel Presbyterian Church, Bethel Park,
Pennsylvania: on its sixtieth anniversary, the last surviving charter member of the Brookside women's
club is asked to talk about the club and the place it was founded in — and she brings the minutes book
with her and reads from it as she speaks.

| | |
|---|---|
| **Speaker** | Gertrude Tanner, charter member of the club since 1925 |
| **Introduced by** | An unidentified librarian, labelled `HOST` |
| **Recorded** | **1985** — the calendar date is unknown (see §1) |
| **Length** | **20 m 13 s** (1,212.843 s), one continuous side |
| **Words** | 2,251 spoken words in 53 labelled paragraphs (51 `GERTRUDE TANNER`, 2 `HOST`), counted from the filed transcript with the speaker labels excluded |
| **Status** | Transcribed, corrected, labelled, verified; master held on the archive NAS |

The talk is in three parts: **Brookside before it was a suburb** — the fort on old Fort Couch Road, the
Couch family, the Indian street names, the Freehold Real Estate Company's parcels about 1900;
**her own arrival** as a bride in 1923, the carriage house, the pigeons, the Model T; and **the club**,
from the book club that preceded it to Mrs. Edna Cully's proposal in 1925.

---

## 1. How the date is established — and why the folder says `unknown`

**No calendar date can be established, so `metadata.json` records `date: "unknown"` and this folder
keeps the `unknown-` prefix.** What *can* be established is the **year, 1985**, and it rests on the
tape's own arithmetic, twice over:

- **1925 + 60 = 1985.** At 15:46: "way back in 1925, and it's exactly 60 years old today."
- **1923 + 62 = 1985.** At 9:48: "I have lived there 60 years, plus the two in the little carriage
  house, making 62 years", after "I came here as a bride in 1923" (3:26).

Two independent statements, one year. The **opening slate** is where a date would normally come from,
and it is **partly unintelligible**: five cold passes over 0:04–0:24 return "This is the 22nd of May,
1965 / 365 / 22nd and Bank, 365, the … library room". The year in the slate cannot be trusted against
the arithmetic — 1965 would make the club forty, not sixty — so the year is 1985 and "22 May" is
recorded as **probable only**. It is shown in brackets in the transcript (`22nd of [May], 1985`) so
that no reader mistakes an editorial reading for a spoken word. The filename carries no date at all.

`2026-10-18` in the archive folder name is the **digitisation** date, not the recording date.

## 2. The physical recording and its capture

| | |
|---|---|
| Master file | `Gertrude Tanner Lecture.m4a` |
| Format | ALAC 48 kHz stereo 16-bit, 154.9 kb/s |
| Duration | **1,212.842667 s (20 m 13 s)** |
| Size | 23,481,203 bytes |
| sha256 | `eadab1df7547dc445dda2c85683c58507605fab36af888cc4f67e50237ac3b9e` |
| md5 (capture record) | `0b119e0b2683b4bb4d9734e64237078f` |
| Mean level | **−45.5 dBFS** |
| Peak | **−18.6 dBFS** |
| Integrated loudness | **−39.2 LUFS**, LRA 20.9 LU |

Measured here with `ffmpeg` (`volumedetect`, `ebur128`) on the master as held on the NAS; the figures
agree with the archive's record.

**The file was recorded at two different levels**, and this is the one thing about the audio that
governs everything else:

| stretch | mean | peak |
|---|---|---|
| 0:00 – 11:10 | −54 to −60 dB | −28.5 to −42 dB |
| 11:20 – 19:05 | −40 to −47 dB | −18.6 to −25 dB |
| 19:05 – 20:13 | −65 to −74 dB | room tone only |

Region A measures **−56.4 dBFS RMS / −55.4 LUFS** and region B **−41.8 dBFS RMS / −40.5 LUFS** — a
**14.9 LU step**, arriving gradually between 11:10 and 11:40 as someone turned the record level up. A
single uniform gain cannot serve both halves: aimed at the archive target it would leave the first
eleven minutes 15 dB under the second. So the gain is **two-region**: **+36.4 dB** from 0:00 to 11:12,
ramped linearly in dB to **+21.5 dB** by 11:40, and held to the end.

**Gain only — no denoise, no EQ, no resampling.** The pre-limiter peak on the floated intermediate was
**+6.9 dBFS**, so a true-peak limiter (`alimiter=limit=0.87`) catches the loudest transients — her
voice at 0:18.9 and again at 17:33. Measured after: **−19.1 LUFS integrated, −1.1 dBTP**, LRA 8.9 LU,
both regions sitting at the same RMS for the first time. **No clipping was introduced**, and this was
checked twice: the first intermediate was written as 16-bit PCM, which silently hard-clipped the
+6.9 dBFS pre-limiter signal; it was rebuilt as float32, and the finished master was then tested for
flat tops (286 samples at the maximum, longest run 3 samples — a limiter, not a clipper).

**There is nothing to denoise.** Only 0.01 % of the energy is above 8 kHz and 84.8 % sits between 300
and 3400 Hz: the source is band-limited, PA- or telephone-grade. Region A's noise floor is around
−61 dBFS, which after +36 dB sits near −25 dB — audible as a steady bed under the first eleven
minutes, and left in, because removing it would also remove signal the transcriber used.

**Stereo.** A delayed duplicate: ch1 stronger by 1.2–1.6 dB in every window, correlation 0.85–0.99 at a
**constant 7-sample (0.146 ms) lag**. Equal-weight summation would comb-filter, so the channels were
summed with the lag compensated — `(ch0 delayed 7 samples + ch1)/2`. The 1.2 dB gap is far too small
for weighting to matter and too small to justify dropping either channel.

## 3. What was done to it (the method)

1. **Measured the two recording levels** with a 60-second block sweep before deciding anything; a
   single gain would have been the wrong answer here.
2. **Established the stereo lag** rather than assuming zero, then summed with compensation.
3. **Chunked on quiet points**: **10 chunks** of about 120 s, each boundary snapped to the quietest
   10 ms frame within ±5 s of its target (116.35, 235.06, 355.02, 475.18, 595.07, 715.01, 835.23,
   955.33, 1075.87 s), with **10 s of overlap**. Never a whole-file pass. Audio decoded by ffmpeg to
   float32 arrays — PyAV in this build rejects the `metadata_errors` kwarg faster-whisper passes.
4. **Seeded the prompt with 417 characters** of Bethel Township names — Brookside, Bethel Park,
   Chartiers, the Stone Manse, Coverdale, Nathan Couch, Riggs, Croco, McCully, Patterson, and the rest
   — **with the speaker's own name deliberately left out**, so that a self-introduction could not be
   manufactured by the prompt.
5. **Checked for prompt leak and collapse** by re-transcribing the same ten boundaries with no prompt:
   per-chunk word counts differ by 0–3 words (241/240, 238/245, 257/261, 306/306, 300/298, 250/249,
   282/282, 258/259, 276/278, 138/138), no segment is built out of seed tokens, and no chunk head
   returned a politeness formula over real dialogue.
6. **Recovered two seams the seeded pass lost** from the unprompted pass: "brother who was living on
   Brookside Boulevard" at 3:40, and "Great big wide oak beams lay right on the dirt, and the walls were
   plastered with mud, horse hair, and lime" at 13:55. Both are in the document and recorded in
   `post_edits`; nothing was deleted from the raw segments.
7. **Removed three tail hallucinations** — "Thank you." at 19:20, 19:50 and 20:12, sitting in room tone
   22 s or more after the last word, with `no_speech_prob` 0.74–0.98. Recorded as a deletion.
8. **Corrected and recorded every correction** in `post_edits`.
9. **Read it end to end**: both merged passes in full (141 and 168 segments) and the finished 53
   paragraphs, plus targeted cold re-transcription of six doubtful windows.
10. **Built the documents from the labelled text** and verified them (53/53 paragraphs, 2,355/2,355
    words, 53/53 labels), then checksummed the folder.

## 4. Engine, and what it measured

| | |
|---|---|
| Engine | faster-whisper **large-v3**, CTranslate2 **int8**, beam 5, 12 CPU threads |
| Version | faster-whisper 1.2.1 |
| Chunks | 10, quiet-point snapped, 10 s overlap |
| Seeded prompt | 417 characters, speaker's name omitted |
| Segments | 141 |
| ASR words | 2,231; document 2,251 spoken words |
| Mean per-word probability | **0.921** (4.84 % of words below 0.5; 8.83 % below 0.7) |
| Weakest stretches | minute 0 (the off-mic slate: 18 % of words below 0.5), 6:00–7:00, 10:00–11:00 |
| Strongest | 11:40 to the end, 0–4 % per minute |

This is the cleanest tape in the collection by per-word probability, and the reason is audible: once
the record level comes up at 11:40 the talk runs clean, and the difficulty is concentrated in the
eleven quiet minutes at the head.

## 5. Corrections made (35, all reversible)

Each is a `post_edits` entry with the raw form, the replacement, the reason and a certainty — 30
certain, 5 probable. The substantive ones:

| heard | changed to | basis | certainty |
|---|---|---|---|
| "the 17th day of 365 … my name will be the librarian" | "the 22nd of [May], 1985 … in the library room" | five cold passes; the year fixed by the 60/62-year arithmetic | probable |
| "his dream and mr couch a mr couch" | "And Mr. Couch, or Mr. Couch" | the unprompted pass at the same timings | certain |
| "the court coach" | "the **Fort Couch**" | the fort is named in the previous sentence | certain |
| "over in the stone house there" | "over in the **Stone Manse**" | "stone manse" at beam 5 and beam 1, two gains, unprompted | probable |
| "Washington, VA" | "Washington, **PA**" | the Castle Shannon–Washington interurban ran to Washington, Pennsylvania | certain |
| "the three-hole real estate in Pittsburgh" | "the **Freehold** Real Estate in Pittsburgh" | the Freehold Real Estate Company, 311 Fourth Avenue, which platted Brookline and adjoining plans 1904–1916; "three-hole" is not English | probable |
| "Arapaho" | "**Arapahoe**" | the street-name spelling | probable |
| "down Mohawk" | "down Mohawk **Road**" | the street; "Road" is audible in the unprompted pass | certain |
| "our Model G Ford" | "our Model **T** Ford" | she says Model T at 9:20, and a 1923 Ford is a Model T | certain |
| "away from the dusk of the road" | "away from the **dust** of the road" | sitting out on a veranda away from road dust | certain |
| "keifer / kefir pear" (×3) | "**Kieffer** pear" | the pear variety | certain |
| "had the top turned off" | "had the top **torn** off" | the unprompted pass | certain |
| "the Walpole Farm" | "the **Walden** Farm" | four cold passes at beam 5 and beam 1, two gains | probable |
| "It had almost been built before the war" | "**Some houses** had been built before the war" | sense; both the audition probe and the unprompted pass read "some houses" | probable |
| "as soon as 22 and 3 came" | "as soon as **'22 and '23** came" | the years after the First World War | certain |
| "the stowing part" | "the **stone** part" | the stone house Nathan Couch built | certain |
| "the arts own it and live in it" | "the **Otts** own it and live in it" | the Otts are the family she names at 2:00 | certain |
| "Thank you." ×3 (19:20, 19:50, 20:12) | removed | hallucinations over room tone | certain |

The remaining entries are sentence breaks, capitalisation and the stitching of ASR fragments into
readable sentences. Stutters and self-corrections are left exactly as spoken.

## 6. Left as heard — the honest gaps

Nine readings are listed as unresolved in the JSON, and one identification question is bigger than a
reading:

- **Whether Gertrude Tanner is Gertrude Heck**, the keeper of the Get-Together Club minutes in the
  Anna T. Connor Papers at the Heinz History Center. A charter member of a Brookside women's club,
  holding the minutes book as she talks, is a real coincidence of subject and object — which is why the
  question is recorded rather than dismissed. But **"Tanner" is not a mishearing of "Heck"** (the two
  are acoustically unrelated), Heck would be a maiden name and nothing on the tape says so, no record
  of a Charles or Gertrude Tanner of Bethel Park was found in obituary or genealogy indexes, and the
  club is never named on the tape as the "Get-Together Club". **Not asserted.**
- **The day and month in the opening slate** — "22nd of May" is the best of five passes; the year is
  established, the date is not.
- **The librarian's own name** — "my name is … the librarian" is unintelligible in every pass.
- **"the main one of the rain roads"** (4:36) — possibly "run roads" or "railroad"; neither is
  supported strongly enough to correct.
- **"Mrs. Edna Cully"** (16:43) — four cold passes agree on Cully; the archive's McCully family is a
  possible source, but "Mc" is never heard.
- **"I couldn't say the word Raccoon Park"** (12:00) — a stumble, or a self-correction to "Raccoon
  Creek"; left as heard.
- **"over at this old stone land"** (3:01) — "stone house" would fit the sense, but that is not what
  the model returns.
- **"Almeda"** (13:23) — the Martin daughter's given name as heard; not checked against a record.
- **Charles Tanner's dams.** She says he built the Raccoon Park lake in Beaver County and the one at
  Shawnee Lake outside Bedford. Raccoon Creek State Park's dam is an earth dam of 1948 and Shawnee
  State Park is in Bedford County, but **no record naming Tanner as the builder was found**. The claim
  is hers, and is transcribed as hers.

## 7. What is on the tape — outline with timestamps

- **0:06** The librarian: "the 22nd of [May], 1985, in the library room of the Bethel Presbyterian
  Church, with Gertrude Tanner"
- **0:41** She begins: the club, and the area — old Fort Couch Road, the Indian trail, the fort by the
  stream
- **1:27** Mr. Couch and the land for the fort; his son **Nathan Couch**, the log cabin and the stone
  house on what became the **Martin farm**
- **2:00** The **Otts** on Kennebec Road
- **2:14** The fort dated to about **1750**; travel by horseback and wagon
- **3:13** How she knows: she came as a bride, and the old people told her
- **3:43** About 1900, the talk of a streetcar or interurban from Castle Shannon to Washington, and the
  **Freehold Real Estate Company** buying parcels and whole farms
- **4:22** The streets named for Indian tribes — Kennebec, Arapahoe, Seneca — and the boulevard
- **4:53** Her husband's brother's house; coming down Mohawk Road; the spring she first saw Brookside
- **5:52** The two big houses with porches facing Brookside; verandas, rugs, oil lamps
- **6:40** Trees planted rather than cut; the **Kieffer pear**
- **7:20** The carriage houses; one with the top torn off; the one she could rent
- **8:41** Charles, an officer in the First World War; the pigeons and the grain
- **9:20** Her father's **Model T Ford**; two years in the carriage house
- **9:48** "60 years, plus the two … making 62 years"; never a moving van
- **10:17** The war over; building starting again; "as soon as '22 and '23 came"
- **11:16** Charles Tanner's **earth dams** for the state — Raccoon Park in Beaver County
- **12:13** **Shawnee Lake** outside Bedford; "a real memorial for our family"
- **13:06** The **Walden farm** purchase; the two daughters, Margaret and Almeda
- **13:51** The old stone house: oak beams on the dirt, mud, horse hair and lime
- **14:05** The bank gutted and rebuilt it; the Otts own it today
- **14:39** What Nathan Couch would make of Fort Couch Road now
- **15:17** The club: "I'll make that a little shorter because you can read the minutes" — the minutes
  book in her hand
- **15:46** "Way back in 1925, and it's exactly 60 years old today"
- **16:23** The book club before it, and **Mrs. Riggs**
- **16:42** **Mrs. Edna Cully** arrives in 1925 and proposes a women's club; the bylaws
- **17:11** Organized to introduce neighbours to each other; the last charter member
- **17:48** The departments: drama, garden, the choral group
- **18:16** The men's civic organization, meeting at the Brookside trolley stop
- **18:43** "It was the women's club — it still exists, and that is what we're celebrating today"

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The transcript: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt` | The same text as 142 timed cues, for playback or captioning |
| `notes-a.md` | The archive's working record, verbatim: measurements, chunks, cold passes, every judgement |
| `metadata.json` | The record of record: date and its source, speakers, master with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

The **audio master is not here** (see `docs/AUDIO.md`): it is held on the archive NAS, two copies,
identified above by sha256. It was found loose at the archive root as `Gertrude Tanner lecture.m4a`,
untranscribed, and moved into its own folder with the md5 verified either side of the move.

**On the side letter.** This is one continuous file with no side letter of its own; it is filed as side
`A` so that the collection's `transcript-a.md` naming holds. That is a naming convention, not a claim
that the cassette is labelled A.

## 9. Citing it

> Tanner, Gertrude. *Brookside and the women's club*. Talk to the Brookside Women's Club on its
> sixtieth anniversary, 1985. Historical Room, Bethel Presbyterian Church: digitised 18 October 2026.
> Transcript, 2,251 words.

Cite the year as **1985** and the day only as uncertain. Cite the timestamp for anything quoted — the
transcript keeps the tape's own timebase, so a claim can always be checked against the master.

## 10. Reproducing this transcript

- model: large-v3, CTranslate2 **int8**, language `en`, **beam 5**, `condition_on_previous_text=False`,
  `temperature=0.0`, `vad_filter=False`, word timestamps
- **10 chunks** of about 120 s, quiet-point snapped, 10 s overlap
- seed: 417 characters of Bethel Township vocabulary, one alternative only, **speaker's name omitted**,
  with a leak check by unprompted re-pass at the same boundaries
- input: the aligned, summed, two-region-gained working copy described in §2 — not the raw stereo
  master

A re-run on the same master, engine and settings reproduces the raw ASR text; the filed transcript
differs from it only by the corrections in §5 and the deletion in §3.

## 11. Related material in the collection

- **Ann Connor's Bethel lectures and classes (1971, 1977, 1983, c. 2001)** — the same Historical Room
  project, from the church's side of the hill: Bethel, the Stone Manse, Chartiers and the families.
  This tape is the Brookside side of the same story, told by a neighbour rather than the church's
  historian.
- **The Anna T. Connor Papers** (Heinz History Center) — which include the minutes of the Get-Together
  Club kept by a Gertrude Heck, and are the reason the identification question in §6 is recorded rather
  than closed.
