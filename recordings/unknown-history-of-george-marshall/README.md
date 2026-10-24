# Ann Connor — the ministers of Bethel, and George Marshall (date unknown)

A talk given in the Historical Room at Bethel Presbyterian Church, Bethel Park, Pennsylvania, on the
succession of Bethel's ministers: **John McMillan** as founder, **John Clark** as first pastor,
**William Woods** second, and — for the bulk of the recording — **Rev. George Marshall**, third
pastor. Ann Connor works from memory and from the documents in the room: Marshall's will and the list
of his library, his tombstone in the cemetery, the Tidball land deed, and a letter he wrote on
**14 May 1851** on his way to Europe, which she reads aloud at the end.

It is a room recording made to an audience, not an interview and not a tour of the room; the displays
are pointed at rather than walked through.

| | |
|---|---|
| **Speaker** | Ann Connor — per the archive; the tape never states her name |
| **Audience** | One unidentified audience member, one turn at 29:58 |
| **Recorded** | **Date unknown.** Not on the tape, not on the filename, not in the source JSON. See §1 |
| **Length** | 31 m 44 s (1,904.213 s); last speech at 30:50, then 53 s of room tone |
| **Words** | 3,789 in 130 turns (129 ANN, 1 AUDIENCE) |
| **Status** | Transcribed 2026-10-19, corrected, labelled, verified; master held on the archive NAS |

The recording carries no title. "The ministers of Bethel, and George Marshall" is a description of
its contents, not a label read off the object.

---

## 1. How the date is established — and why it is not

**It isn't.** The recording states no date, names no anniversary, and refers to no outside event that
can be anchored in a year. The search was made rather than assumed, and it came back empty:

- the filed transcript, read end to end: no "this year", no anniversary formula, no datable news;
- the `.srt`: nothing;
- the source JSON: `date_recorded` reads `"UNKNOWN (not stated on the tape; c. 2001 assumed by the
  archive)"`, with `date_recorded_basis` saying the same in more words;
- the notes and the archive README's row for this item: both record **UNKNOWN**.

The archive's working assumption is **c. 2001**, supplied by John Decker on the grounds that this is
the same era and the same speaker as the Ann Connor Sides A and B cassettes, which date themselves by
the church's 225th anniversary (1776 + 225 = 2001). That is an **assumption about a neighbour, not
evidence from this tape**, and it is recorded as an assumption wherever it appears. Nothing on the
tape contradicts it — she speaks of a programme she gave "last week", and of the present owners of the
Marshall farmhouse — but nothing corroborates it either.

The **14 May 1851** date she reads out belongs to Marshall's letter. It is period content, not a date
for the recording, and is not used as one.

`metadata.json` therefore carries `date: "unknown"`, and the folder is named `unknown-…` for that
reason alone.

## 2. The recording and its capture

| | |
|---|---|
| Master file | `History of George Marshall and other Ministers.m4a` |
| Format | ALAC, 48 kHz, 2 channels, 16-bit |
| Duration | **1,904.213 s (31 m 44 s)** |
| Size | 75,371,783 bytes |
| **sha256** | `890e4ab6225687f7cb6af612d081272e3418526e74cf900a9d6d9da347953257` |
| md5 (capture record) | `198d5633a0dc95e812faaf8488d83fe4` |
| Mean level | **−31.2 dBFS** (measured) |
| Peak | **−3.4 dBFS** (measured) |
| Speech | 0:09.6 – 30:50.3; last 49 s measured at RMS −66.2 dBFS, peak −37.2 dBFS |

Hash and duration were **recomputed from the file** for this record; the md5 is the figure the
transcription JSON carries.

**Level is even.** Sixteen two-minute blocks all peak between −3.4 and −7.5 dBFS and average −28.7 to
−33.2 dBFS; there is no level step and no second session spliced onto the file. The 8 kHz-and-above
band measures **0.00 %** of total energy (3–8 kHz 0.39 %), so the capture is band-limited and there is
no hiss to filter. **No denoise, no filtering — gain only.**

**Stereo.** Measured on six 30 s windows: ch0 3.7–4.7 dB hotter than ch1, raw correlation 0.84–0.89,
rising to **0.992–0.996 at a constant −5 sample lag** (0.104 ms). A constant gap and near-perfect
correlation at a fixed lag is a **delayed duplicate**, so the channels were summed with the lag
compensated and weighted 2:1 toward the stronger channel:
`0.6667 × L (delayed 5 samples) + 0.3333 × R`, then `+12 dB` and a limiter. Result: −19.5 dBFS mean,
−1.0 dBFS max. No channel was discarded.

**A note on the speech end.** `notes-a.md` prints the last speech as "31:50.3", which is past the end
of a 31 m 44 s file and cannot be right; the `.srt`'s last cue is **30:50.110**, and the last 53 s is
room tone measured at −66 dBFS RMS. The figure used here is the one the timed cues support.

**Nothing was cropped from the master.** The transcription ran on the file as received. The mono
64 kbps copy beside it (`… .mp3`, 1,852.0 s, measured; 14,816,492 B) is a straight transfer with the
53.7 s silent tail removed — measured before it was made: sixteen silent gaps of ≥1.5 s totalling
41.4 s, of which 25.7 s lies after 30:58 and 6.7 s before she starts; inside the talk only four pauses
reach 1.5 s, 7.50 s altogether, so collapsing them would have saved 0.29 % of the runtime. It is not a
condensation and no pause inside the talk was touched.

## 3. What was done to it (the method)

1. **Measure before touching**: duration, levels, a sixteen-block level sweep, per-channel RMS,
   correlation and lag, and the share of exact digital zeros (18 % of the file in 186 gaps of ≥0.5 s —
   but only 16 gaps reach 1.5 s and most are in the tail, because the talk itself is continuous).
2. **Check the stereo relationship** rather than assuming it, then sum with the lag compensated.
3. **Chunk on quiet points**: 16 chunks of about 120 s, boundaries snapped to the quietest 10 ms frame
   within ±5 s. Every boundary landed in digital silence. Never a whole-file pass.
4. **Transcribe with a seeded prompt** carrying corroborated names only — Bethel, John McMillan, John
   Clark, George Marshall, C. W. Wycoff, Murray C. Reiter, Bethel Academy, Oliver Miller Homestead,
   Mingo Creek, Canonsburg, Chartiers, Dido, Doddridge, Princeton Theological Seminary, Peter Croco,
   Karla Strobl, Coverdale, Lebanon Church, Pigeon Creek, Jefferson College, Washington College.
5. **Check the seed for leakage.** Clean: every seeded name that appears in the output is spoken in
   context. Wycoff, Reiter, Croco, Strobl, Doddridge, Princeton, Mingo Creek, Oliver Miller and
   Chartiers **do not occur in this recording at all** — the talk stops at Marshall. No window needed
   re-transcribing unprompted and no segment was deleted for leakage.
6. **Remove hallucination, keep speech.** One segment was dropped: "Thank you." at **31:28.5**, thirty-eight
   seconds after the last words, over room tone measured at −67 dB, and a second unprompted pass produced a
   "Thank you." at a different timestamp (31:26.3) — the signature of filler, not speech. The "Thank
   you." at **30:50** was kept: it sits at the exact end of the talk and reads as the speaker closing
   (it could equally be an audience member; left on ANN).
7. **Restore punctuation where Whisper gave none** — two unpunctuated runs (05:07–05:55, the
   Temperance Movement and William Woods; 26:55–27:55, the canal boat). Full stops and commas were
   inserted at the clause boundaries she speaks; **the words were not touched**, and the restoration is
   flagged separately from the word edits in the JSON.
8. **Correct, and record every correction** in `post_edits` — see §5.
9. **Label the speakers**: `ANN` and `AUDIENCE`. No interviewer is audible; the questions in the text
   ("Are you familiar with this at all?", "Are you aware that…") are Ann putting questions to the room.

## 4. The engine, and what it measured

- **Whisper large-v3**, Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads, `en`.
- `beam_size=5`, `condition_on_previous_text=False`, `temperature=0.0`, word timestamps,
  `vad_filter=False`, `no_speech_threshold=0.6`; 16 chunks, boundaries snapped to the quietest 10 ms
  frame.
- **260 segments, 3,819 words, mean per-word probability 0.9601, 2.07 % of words below 0.5** — well
  inside the archive's bar of ≥0.85 mean and <10 % below 0.5, and the highest of the recordings
  prepared in this batch (the others measure 0.85–0.87).
- One 30-second window falls below 0.80: **31:00–31:30 (0.603)**, where the talk runs out into room
  tone. Everything before 31:00 is ≥ 0.80. The lowest-probability tokens are segment-initial function
  words ("And", "The", "So"), the surname "Dom" twice, and "Language," at 17:55.

## 5. Corrections made (20 `post_edits`)

All twenty are in the JSON that ships beside the archive transcript, each with the raw form, the
correction, the reason and a certainty marker; nineteen rows below because one reading occurs twice.

| # | heard | changed to | basis | certainty |
|---|---|---|---|---|
| 1 | "**Matt** Anthony Wayne" | **Mad** Anthony Wayne | the general's nickname | certain |
| 2 | "**Cannonsburg** Academy" | **Canonsburg** Academy | the town's name | certain |
| 3 | "Thomas and Elizabeth **Tidbalt**" | **Tidball** | she names William Tidball a minute later | certain |
| 4 | "between the **marshals** and members" | the **Marshalls** | family name | certain |
| 5 | "during **Reverend Wood's** pastorate" | **Reverend Woods's** | William Woods, named earlier | certain |
| 6 | "the allegheny **cordage** railroad" | the **Allegheny Portage Railroad** | the Lemon House and the canal/rail hybrid she describes | certain |
| 7 | "a picture of the **lemon house**" | the **Lemon House** | proper name, Allegheny Portage Railroad | certain |
| 8 | "He paid them **$25,000**" | He paid them **25 cents** | she is reading: 50 cents asked, 25 cents paid | certain |
| 9–10 | "**Jenny Lynn**" (×2) | **Jenny Lind** | Lind sang at Castle Garden; the 1851 date fits | certain |
| 11 | "brown shipley and company liverpool england" | **Brown, Shipley and Company, Liverpool, England** | capitalisation only | certain |
| 12 | "where the **Dons** live today" | the **Doms** | same family as "Dom home"; spelling normalised to the majority ASR form — the surname itself is **unverified** | probable |
| 13 | "the Louisiana **purchase**" | **Purchase** | proper noun | certain |
| 14 | "his participation. In the Whiskey Rebellion" | "his participation **in** the Whiskey Rebellion" | a full stop landed at a segment seam | certain |
| 15 | "the old **The** log meeting house" | "the old log meeting house" | duplicated "The" at a seam | certain |
| 16 | "**Tidball, who** the trustees" | "Tidball **to** the trustees" | "the sale … by Thomas and Elizabeth Tidball to the trustees" | certain |
| 17 | "if there was any serious objection to it **than it was to be reserved**" | "**then it was to be removed**" | the organ was on trial for a month and to be removed if objected to — "reserved" is the opposite | probable |
| 18 | "any of you know. That house, but it's…" | "any of you know **that house**, but it's…" | one clause split by a full stop | certain |
| 19 | "And books in those days were extremely…" | "…extremely **expensive and valuable**." | truncated at a chunk boundary; recovered by an unprompted pass over 1300–1332 s | certain |
| 20 | "Washington Presbytery, **Came** to Bethel" | "…**came** to Bethel" | mid-sentence capital from a segment start | certain |

That is twenty edits in nineteen rows: the Jenny Lind reading occurs twice and is logged as edits 9 and 10.

Also applied but not counted as corrections, because no word changed: Whisper's doubled words
collapsed ("period. period.", "Academy. Academy.", "that that", "of of", "this this"), sentence starts
capitalised, a decimal point and "Jr." no longer triggering a false capital. Hesitations and false
starts are left as spoken.

## 6. Left as heard, and one point of history

Eight readings remain unresolved and are listed in the JSON and in `notes-a.md`. The ones a reader is
most likely to trip over:

- **The family in the Marshall farmhouse** — "where the **Doms** live today", "**Mrs. Dom**, who owns
  the Marshall home now". The ASR gave "Dons" and "Dom" for the same person; the true surname is
  unverified, and "Dom" is a normalisation, not a finding.
- **"Alex Ringsoe"** (30:18) — "you may tell Alex Ringsoe if you see him. I gather Alex Ringsoe wasn't
  at the reservation." No match found.
- **"John McCabe's barn"** (22:55) — where Marshall's trunk was kept.
- **"Mansfield Brown and White, George B. White, Lewis Hutchison Jr. and mother"** (28:00) — fellow
  passengers named in the letter; not checked.
- **"Which you love to hear Jenny Lind for $1"** (29:40) — reads as a rhetorical "wouldn't you love
  to hear…", but the words do not support a safe rewrite.
- **"he was the founder and for many years the Language, Hebrew, he taught Hebrew and Latin"**
  (17:55) — garbled, but **two independent passes agree on the words**, so it is her phrasing rather
  than an ASR artefact. Probably a lost word ("the linguist").

**The minister sequence is worth stating plainly**, because it is the spine of the talk and it is
correct: **McMillan (founder) → Clark (first pastor) → Woods (second) → Marshall (third)**. She is
explicit — "on the death of John Clark came our second pastor, William Woods", and Marshall "became …
third pastor of Bethel Presbyterian Church" — and it agrees with Marshall's dates (b. 23 December 1806,
preaching at Bethel from 11 July 1832, d. 30 April 1872). A briefing list seen during the archive's
work omitted Woods; the tape and the record were not changed to fit it.

Unchecked on the tape and left as she says them: the third meeting house in **1855** and the first
organ in **1866**. Her aside that books in those days were "extremely expensive and valuable" is restored from a
truncated chunk (correction 19) and is the only such repair.

## 7. What is on the tape — outline with timestamps

- **0:09** "I generally try to do what I can from memory, but I'm going to do this very quickly"
- **0:16** **John McMillan**, "apostle of Presbyterianism in the West", founder of Bethel and Lebanon;
  the journal entry of 5 November 1776 at the Miller homestead; East and West Peters Creek
- **1:23** **John Clark** — born in New Jersey (place unknown), churches in four states, the Whiskey
  Rebellion, and the land at **Plain Truth** (2:20) left to Jefferson College
- **3:00** Clark's slaves, and **Dido** (3:15), freed by his will; the unaccounted "Dave"
- **4:03** 1794: **Mad Anthony Wayne**, the Louisiana Purchase, and Pittsburgh as the gateway
- **5:16** The **Temperance Movement**; the death of Clark and **William Woods** as second pastor
- **7:55** The **log meeting house** torn down and the first brick meeting house built
- **8:39** **The argument over which hill** — the vote taken by staying put; Woods asks to withdraw
- **10:52** **George Marshall** — born near Milton, Union County; Milton Academy under David
  Kirkpatrick; Dickinson College; Jefferson College in **1828** (11:29)
- **11:44** Teaching at **Cross Creek Academy** to pay his tuition; **Dr. John Stockton** (12:53)
- **13:10** **Mary Lee**, daughter of Hugh Lee, elder at Cross Creek
- **13:57** First sermon **11 July 1832**: "He stood pale and thin like a ghost, but his voice and
  gestures were powerful" (14:04); third pastor
- **14:47** The **Tidball** tract at Oakhurst; Marshall Road; the farmhouse and the Hicks family; the
  Bolanders' Peter Boyer house; "over 100 acres" (17:09)
- **17:16** The **will**, and the inventory he hopes to get; founder of **Bethel Academy**; Hebrew and
  Latin; trustee of Jefferson College (18:05); Western Theological Seminary; the first permanent church
  records
- **19:48** The **third meeting house**, 1855; the first organ, 1866, on a month's trial (20:01);
  the tombstone with an open book
- **21:43** Where the library went ("heavens knows"); his health, "dyspepsia", and the ulcer guess
- **22:50** The **trunk** from John McCabe's barn; the canal-boat family connection
- **24:00** The **summer of 1851** and the European trip with **Thomas Cadoux**
- **25:25** **Marshall's letter of 14 May 1851**, read aloud — the canal boat, the Allegheny Portage
  Railroad and the **Lemon House** (26:53), the 25 cents for the trunk (27:31), Johnstown at two in the
  morning (28:11)
- **29:06** **Jenny Lind** at Castle Garden, 7,000 present, "all for $1" (29:28)
- **29:58** The **audience** objects that they may have been hauling it 50 miles; Ann: "he doesn't
  indicate that"
- **30:12** "Tomorrow we sail, the Lord willing"; **Alex Ringsoe** at 30:18; write care of Brown, Shipley and
  Company, Liverpool
- **30:50** "Thank you." — the talk ends; the tape runs on into room tone

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The transcript: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt` | The same text as 535 timed cues, 00:00:09.6 – 00:30:50.1 |
| `notes-a.md` | The working notes: measurements, stereo table, engine settings, the prompt-leak check, every judgement call |
| `metadata.json` | The record of record: date (unknown) and the search behind that, speakers, master with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

The master is **not** here (see `docs/AUDIO.md`): it is held on the archive NAS, identified above by
sha256.

## 9. Citing it

> Connor, Ann. *The ministers of Bethel, and George Marshall*. Talk in the Historical Room, Bethel
> Presbyterian Church, Bethel Park, Pennsylvania, date unknown (archive working assumption c. 2001);
> digitised 18 October 2026. Transcript, 3,789 words.

Because the date is unknown, cite it as **undated** and give the archive's assumption only in
parentheses, marked as an assumption. Cite the timestamp for anything quoted.

## 10. How this text got here

The transcript in this folder is the archive's filed transcript, **copied unchanged** from
`History of George Marshall and other Ministers.md`, together with its `.srt` and its transcription
record. It was not re-transcribed for this repository and no word was altered in the copying; the
corrections in §5 had already been applied and logged in the source JSON by the archive.
`bin/check.py` verifies the copies against `checksums.sha256`.

## 11. Related material in the collection

- **George Marshall Class**, 17 October 1971 — Ann Connor teaching a class on the same material
- **A.D. White, Cross Creek records and the Whiskey Rebellion**, 15 July 1971 — Cross Creek Academy,
  Stockton and Marshall's letters, from the man who gave Ann much of this material
- **Ann Connor Sides A and B** — the cassettes that carry the 225th-anniversary date behind the c. 2001
  assumption
