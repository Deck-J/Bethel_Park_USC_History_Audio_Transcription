# Edna Croco — remembering Edna Maits and old Bethel (13 September 1983)

A research interview recorded by **Ann Connor** on her way to, and then inside, the home of
**Edna M. Croco** — 83 years old, the last of the "three Ednas", and the woman who could still
describe the third meeting house from the inside: its water cooler, its caretaker, its flowers,
its passing bell, and the Easter wind that lifted the oil chandeliers and took a side off the roof
(1902 is the 1951 history's date for that storm, not hers).

Ann Connor was building the Historical Room. She had Edna Maits's prayer, given at the Miller
Homestead in 1979, and was to read it at the Women's Association meeting the next day; she went to
Edna Croco to gather memories of Mrs. Maits to add to it. What she got was an hour of Bethel's
ordinary life — the Ladies Aid, the schools, the wagon shop at Sodom, cottage prayer meetings, a
Catholic Bible with four kings in it — and, at the end, a friend described.

| | |
|---|---|
| **Speaker** | Edna M. Croco, of Bethel Park, Pennsylvania |
| **Interviewer** | Ann Connor |
| **Recorded** | Tuesday, 13 September 1983 — place not stated on the tape; it opens at the Oliver Miller Homestead and in Ann Connor's car, and the interview continues indoors at Edna Croco's home |
| **Length** | 34 m 20 s (2,059.776 s); last speech at 30:33, then silence |
| **Words** | 2,946 in 132 turns (66 EDNA, 66 ANN CONNOR) |
| **Status** | Transcribed 2026-10-19/20, corrected, labelled, verified; master held on the archive NAS |

The recording carries no title of its own. "Remembering Edna Maits and old Bethel" is a description,
not a label read off the object.

---

## 1. How the date is established

The date is **on the tape**, spoken by Ann Connor in the first eleven seconds:

> "This is Tuesday, September the 13th, 1983, and this is Ann Connor."
> — 0:09, labelled `ANN CONNOR`

**13 September 1983 was a Tuesday**, checked against the calendar rather than assumed, so the
statement is internally consistent. Nothing in the recording contradicts it: the Women's Association
meeting she is preparing for is "tomorrow". The source folder name carries no date, and the file
arrived with none, so nothing was inherited from a neighbouring folder.

Two other dates in the material are **not** the recording date:

- **2026-10-18** in the archive's folder path is the **digitisation** date.
- The dates in Edna Croco's biographical front matter — born 20 September 1899, died May 1988 — are
  from a **genealogy index entry, a secondary source**, and are labelled as such in the transcript
  and in `notes-a.md`. The primary obituary has not been obtained.

## 2. The recording and its capture

| | |
|---|---|
| Master file | `Edna Croco Interview.m4a` |
| Format | ALAC, 48 kHz, 2 channels, 16-bit |
| Duration | **2,059.776 s (34 m 20 s)** |
| Size | 37,145,922 bytes |
| **sha256** | `087265af5bd3e3c958c70fae730ba6bcd2f59f9761fa882b899787e5bdf3dcc3` |
| md5 (capture record) | `4cae6a72735fa9ace86aa92f8cc16c1f` |
| Mean level | **−44.2 dBFS** (measured) |
| Peak | **−9.8 dBFS** (measured) |
| Speech ends | 1,832.9 s (30:33); last 220 s measured at RMS −83.5 dBFS, peak −36.8 dBFS |

The hash and the duration above were **recomputed from the file** for this record (`hashlib.sha256`,
`ffprobe`); the md5 is the figure the transcription JSON carries.

**It is quiet, and the quiet is not a fault.** The first minute is the loudest block and it is Ann
speaking close to the microphone; the interview itself runs 10–20 dB lower. Energy above 8 kHz is
42.7 dB below the passband (3–8 kHz already 21.9 dB down), so the top end is empty because the
capture is band-limited, not because there is hiss in it. **No denoise, no filtering — gain only.**

**A third of the file is literal digital zero** — 710.4 s in 49 runs of a second or more, interleaved
with speech at 20 ms granularity. That is what a voice-actuated or squelch-gated recorder produces.
The audio alone cannot say which mechanism it was; the measurement says only that the gaps are
sample-exact zeros, not a quiet room.

**Stereo.** The archive measured a delayed duplicate: ch0 −45.53 dB, ch1 −43.20 dB (2.33 dB apart)
at a consistent 7–9 sample lag (median 8), correlation 0.973–0.992 against 0.59–0.87 at zero lag.
The working copy was a lag-compensated sum at 48 kHz weighted 0.433/0.567 — proportional to
amplitude, never equal-weight, which would have comb-filtered the top of the speech band.

**The condensed copy.** `Edna Croco Interview (condensed).mp3` is 1,648.11 s (measured), mono 64 kbps at 48 kHz, loudness-normalised from a master that sits at −44 dBFS.
98 silent gaps were cut, 8 skipped as too tight; 625.4 s of 2,059.8 s (30.4 %) was removed, of which
225.8 s is the silent tail and 399.6 s internal pauses. Every cut gap keeps 0.4 s of room tone, no
word overlaps a cut, and three joins were re-transcribed to check that the words either side survived.
It is a listening copy; **the transcripts point at the full-length master**, never at it.

## 3. What was done to it (the method)

1. **Measure before touching.** Duration, levels, per-channel RMS, correlation and lag, and the
   distribution of exact zeros — which is what found the gated recorder.
2. **Align and sum the stereo pair** rather than discarding a channel.
3. **Chunk on quiet points, not on the clock**: 16 chunks of about 120 s, boundaries snapped to the
   quietest 10 ms frame within ±5 s of each target. Never a whole-file pass.
4. **Transcribe twice.** A seeded pass carrying corroborated names (Edna Croco, Bethel Park, Baptist
   Road, Peter Croco, Wilson Croco, McMillan, Clark, Woods, Marshall, Wycoff, Reiter, Chartiers,
   Canonsburg, Mingo Creek, Bethel Academy, Oliver Miller, Doddridge, Princeton Theological Seminary,
   Karla Strobl, Coverdale mission), and a **second pass with `initial_prompt=None`** over the same
   boundaries as a control.
5. **Repair the prompt damage.** The seed did not echo; it *collapsed* — "Thank you for joining us."
   or a single 12-second word over audible speech at 4:00, 4:10, 17:53 and 18:05, with word
   probabilities 0.00–0.15. Those five windows were re-transcribed unprompted and spliced back,
   recovering about 170 words of real dialogue including a whole question-and-answer pair.
6. **Recover the chunk seams.** An **orphan pass** kept a word transcribed in the 4 s overlap when no
   word owned by its own chunk covered that time span: **97 words** recovered across fifteen seams,
   while catching 44 duplicated words.
7. **Correct, and record every correction** in the JSON's `post_edits` — what was heard, what it
   became, why, and whether that is certain or probable.
8. **Label by content, not by pitch.** Both women sit in one band (roughly 150–220 Hz) on one
   microphone; a two-cluster fit would have produced a confident split with no evidence behind it.
9. **Build the documents from the labelled text**, then verify: `verify_md_docx.py` reported MATCH at
   132 paragraphs, 3,146 words and 132 label runs in both containers; `reconcile_md_json.py` located
   and applied all 27 `post_edits`.

## 4. The engine, and what it measured

- **Whisper large-v3**, Systran faster-whisper 1.2.1, CTranslate2 4.8.3 int8, 14 CPU threads, `en`.
- `beam_size=5`, `condition_on_previous_text=False`, `temperature=0.0`,
  `compression_ratio_threshold=2.4`, `vad_filter=False`, word timestamps.
- Audio decoded by ffmpeg to float32 arrays; PyAV in this build rejects the `metadata_errors` kwarg
  faster-whisper passes, so the array path was deliberate.
- Quality: **2,943 words, mean per-word probability 0.8744, 8.29 % of words below 0.5** (16.89 %
  below 0.7) — inside the archive's bar of ≥0.85 mean and <10 % below 0.5. The notes quote 2,947
  words and 0.8738; the small difference is a re-count after the last label rename and is recorded in
  §6 rather than smoothed over.
- Weakest 2-minute blocks: 12:00–14:00 (0.822), 26:00–28:00 (0.818), 18:00–20:00 (0.843),
  28:00–30:00 (0.844) — where the two women overlap or Edna turns from the microphone. Cleanest:
  0:00–2:00 (0.943), 14:00–16:00 (0.909).

## 5. Corrections made (27 `post_edits`)

Each is an entry in the JSON that ships with the archive transcript: find, replace, reason, and a
certain/probable marker. The substantive ones:

| heard | changed to | basis | certainty |
|---|---|---|---|
| "Mrs. Edna Miller **Mates**" (×10), "Edna **Mace**" | **Maits** | 1951 history: Maits ×21, Mates ×0 | certain |
| "She married **Roe and** Mates" | **Rowan** Maits | her husband's given name | probable |
| "**Wilton** Road" (×3) | **Wilson** Road | three of four decodes; the Wilson family | probable |
| "the log house is **on St. John's**" | "the log house is **gone**" | beam-10 decode | probable |
| "three **Edmonds**" | three **Ednas** | the next breath: "Yeah, three Ednas" | certain |
| "**Snowdon**" (×2) | **Snowden** | Snowden Township, now South Park | certain |
| "**Kroko** school" | **Croco** school | the family's one c | probable |
| "**Blanche McKeown**" | "**There was Blanche McEwen**" | 1951 history: "Miss Blanche McEwen of Bethel" | probable |
| "reverend **johnson** … in africa" | **Johnston** | Rev. William C. Johnston, Bethel's missionary, sailed for West Africa 1895 | certain |
| "**Lady's** Aid" | **Ladies** Aid | 1951 history throughout | certain |
| "the **pregnaturians**" | the **Presbyterians** | ASR of Presbyterians | certain |
| "Reverend **Ryder**" | **Reiter** | Dr. Murray C. Reiter, Bethel's fifth minister 1914–1946 | certain |
| "he built **service** and the two **surveys**" | "he built **surreys**, and the two **surreys**" | a surrey is a carriage; they were "just alike" | certain |
| "It was in **1999**" | **1899** | the recording is 1983; the fire precedes a 19 May birth | probable |
| "mr **pellet** … john l **pellet**" | **John L. Poellot** | 1951 history: "Elder John L. Poellot of Bethel" | probable |
| "this is Ann **Conner**" | **Connor** | her own name; archive spelling | certain |
| "whether that was **field hall**" | **Gill Hall** | eleven cold passes; Gill Hall Road above the Cochran Mill valley | probable |
| "the **nexus church**" | the **Methodist church** | the passage is about Methodism up the hill | probable |
| "dr weichmann's bible class" | **Dr. Wycoff's Bible class** | Dr. C. W. Wycoff, Bethel's fourth pastor | certain |
| "**Nelly** Beam" | **Nellie** Beam | as heard twice | certain |

The **Gill Hall** reading is the one proper noun that listening alone would not settle, and it is
carried as *probable*: Millvale is rejected acoustically (no /v/, the second syllable stays `hɔːl`),
Mill Hall is rejected geographically (Clinton County, 200 miles away), and Gill Hall fits both the
sound and the biography — Jefferson United Methodist Church at 310 Gill Hall Road, in what was
Snowden Township, the same Snowden Ann corrects Edna about a minute earlier.

Mechanical repairs — lone lowercase "i", sentence case, doubled words at chunk joins, proper-noun
casing — are applied but not logged as corrections because they change no word. Hesitations and false
starts are left alone.

## 6. Left as heard, and what is still open

The archive's own list of unresolved readings (11 items in the JSON's `unresolved`, 12 in
`meta.unresolved`) is carried in `notes-a.md` and not shortened here. The ones a reader should know:

- **"the white of Bible plans"** (2:33) — as heard; probably the Wycoff Bible Class, but the phrase is
  not recoverable and is not corrected.
- **"King's school"** (12:22) — a school name the next breath supports ("King's school and Bethel
  grade school"), but nothing else does.
- **The year of the Simmons house fire** — heard as 1899 twice at beam 5 and 1909 at beam 10; 1899 is
  written because the fire precedes a 19 May birth in the same year, but the audio is not decisive.
- **"Jacob Morlock"** (7:47) — the caretaker of the third meeting house; not in the 1951 history.
- **"Nellie Beam"** (25:20) — the girl Grandma Wilson raised; no Beam on the 1951 roll.
- **"From down in Capitana?"** (26:29) — a place name the ASR gives three different ways.
- **"John McKay"** (30:23) — a name in a garbled closing sentence, as the recording stops mid-thought.

Three documentation faults in the source material are recorded rather than hidden:

1. **A stale duplicate.** The JSON's `meta.unresolved` still lists *"Dr. Weichmann's Bible class"* as an
   open question, while the same JSON's `post_edits` carries that reading as a **certain** correction
   to "Dr. Wycoff's Bible class" and the filed text reads Wycoff. The top-level `unresolved` list has
   already dropped it; the mirror was not updated.
2. **Word-count drift.** The notes say 2,947 words and mean probability 0.8738; the JSON says 2,943
   and 0.8744; this repository's count of the labelled turns is 2,946. The differences are a handful
   of tokens across a label rename and a rebuild. `metadata.json` carries this repository's count.
3. **The last 25 seconds** are labelled with low confidence: the sentences are garbled and the
   recording stops mid-thought. The labels there are the weakest in the file, as are the turns
   between 1:44 and 4:00, where Ann's narration and Edna's reminiscence run together.

## 7. What is on the tape — outline with timestamps

- **0:09** Ann Connor names herself and the date; the errand — Miller Homestead, the flower show,
  Mrs. Maits's 1979 prayer, the Women's Association meeting "tomorrow"
- **1:44** Edna remembers Edna Maits as a young girl; her grandmother's property below Johnston
  Wilson; the rent collected after Mama died
- **2:33** The Bible class that began with 75 members; Blanche McEwen; "the white of Bible plans"
- **3:30** Dr. Wycoff's Bible class photograph, and the table saved out of the barn for the
  historical room
- **4:21** Ann's account of the drive: the log house on Wilson Road where Edna Maits was born
- **5:07** **The three Ednas** — Ross Patterson the carpenter, and Edna Patterson, Edna Miller,
  Edna Croco
- **6:21** The Simmons house fire, 19 April; Edna Simmons born 19 May; "I'm the last of the three"
- **7:14** **The third meeting house** — the water cooler, the caretaker Jacob Morlock, the well
  below the parsonage
- **8:06** Flowers, and no committee: "furnished by different ones bringing from their gardens"
- **8:48** The **passing bell** — "that means tolling the bell"; Uncle Al at Allegheny Cemetery
- **11:13** Edna and the church: the **Ladies Aid**, and Rev. Johnston in Africa
- **12:22** The schools — King's school, Bethel grade school for 7th and 8th, Snowden; where Edna
  taught
- **14:08** **Rowan Maits** never allowed to join Bethel — his mother was a Baptist — yet an officer
  in the church
- **15:08** Summer Methodism and winter Presbyterianism; the Methodist church up the hill, **Gill
  Hall** at 15:51 (*probable*)
- **16:17** **Cottage prayer meetings**; the Catholic Bible at 16:39 with four kings in it at 17:30;
  Rev. Reiter at the Miller homestead
- **18:20** Wednesday evenings; neighbours, Mr. and Mrs. Boyer at 18:59; Ida and Albert walking
  barefoot from the Stone Manse at 20:02
- **20:55** **John L. Poellot's wagon shop at Sodom** and the two surreys; Grandma Wilson in the
  wrong surrey
- **21:56** Where Sodom was — below Route 19, where McMurray Road meets McLaughlin Run Road
- **23:22** **The Easter 1902 wind** (the year is the 1951 history's, not hers) — four oil chandeliers
  lifted to the rafters at 23:36, "the church was haunted"; "I was only about two years old"
- **24:58** The log house; **Nellie Beam**, raised by Grandma Wilson and never adopted
- **26:46** Keeping in touch by telephone, and the death notices she reads first
- **27:35** What Edna Maits was like as a friend: "she was able to take charge of the situation,
  keep a clear head"
- **29:09** The close — the book, the page, the photograph
- **30:23** Last words; the recording stops at 30:33 and the rest of the file is silence

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The transcript: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt` | The same text as 216 timed cues, for playback or captioning |
| `notes-a.md` | The working notes: measurements, engine settings, the prompt collapse, the orphan pass, every judgement call |
| `metadata.json` | The record of record: date and its source, speakers, master with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

The master is **not** here (see `docs/AUDIO.md`): it is held on the archive NAS, identified above by
sha256.

## 9. Citing it

> Croco, Edna M. *Remembering Edna Maits and old Bethel*. Interview by Ann Connor, 13 September 1983
> (place not stated on the tape). Historical Room, Bethel Presbyterian Church: digitised 18 October
> 2026. Transcript, 2,946 words.

Cite the timestamp for anything quoted — the transcript keeps the tape's own timebase, so a claim can
always be checked against the master.

## 10. How this text got here

The transcript in this folder is the archive's filed transcript, **copied unchanged** from
`Edna Croco Interview.md` with its `.srt` and its transcription record. It was not re-transcribed for
this repository and no word was altered in the copying; the corrections described above had already
been applied and logged in the source JSON by the archive. Run `bin/check.py` to verify the copies
against `checksums.sha256`.

## 11. Related material in the collection

- **Valentine, Maits and Snowden**, 25 September 1983 — twelve days later, a session with three of
  the church's oldest members, Miller Maits among them
- **Ann Connor, John McMillan lecture**, 25 September 1983
- **A.D. White, Cross Creek records and the Whiskey Rebellion**, 15 July 1971 — the Miller homestead,
  the Stone Manse and the Cochran Mill appear there too
