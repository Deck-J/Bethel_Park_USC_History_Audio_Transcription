# History of George Marshall and other Ministers — transcription record (2026-10-19)

## What this is

A 31 min 44 s talk by **Ann Connor** in the Historical Room at Bethel Presbyterian Church,
Bethel Park, Pennsylvania, on the succession of Bethel's ministers: John McMillan as founder,
John Clark, William Woods, and — the bulk of the recording — **Rev. George Marshall**, third
pastor. She works from memory and from documents in the room: Marshall's will and library
list, his tombstone in the cemetery, the Tidball land deed, and a letter Marshall wrote on
14 May 1851 while travelling to Europe. It ends with the letter read aloud to the audience.

It is a room recording made to an audience, not an interview. It is *not* a tour of the room
(the c. 2001 A/B cassettes are); the displays are only pointed at.

## Dating — UNKNOWN on the tape; c. 2001 assumed by the archive

**The recording states no date and its label carries none.** Nothing in the audio names a
year for the talk: no anniversary, no "this year", no reference to a present-day event that
can be anchored. Checked specifically for the anniversary formula the needlepoint tape used
("Today is November the 6th, 1977 … the 201st birthday") — it is not here.

Per John Decker, the working assumption is **c. 2001**, the same era and the same speaker as
the Ann Connor Sides A and B cassettes in this folder, which date themselves by the 225th
anniversary (1776 + 225 = 2001). That is an **assumption, not evidence from this tape**, and
it is recorded as such in the document byline and footer. The 1851 letter she reads is period
content, not a date for the recording.

Conflict check: nothing on the tape contradicts c. 2001. She refers to the Marshall farmhouse's
present owners and to a program she gave "last week". No conflict to flag — but no
corroboration either.

## Speaker

- **ANN** — Ann Connor, per the archive. The tape never states her name; the identification is
  archive-supplied. Same speaker as the A/B cassettes (same register, same first-person
  references to the historical room and to "Maddie").
- **AUDIENCE** — one unidentified audience member, **one turn only**, at 29:58: Ann says
  "It's basically about a dollar today, so that was expensive"; the audience member answers
  "Of course, maybe they were hauling it 50 miles"; Ann replies "Well, he doesn't indicate
  that." Attribution is **by content, not by voiceprint**: a fundamental-frequency comparison
  was made (186 Hz median on the objection vs 205–216 Hz on Ann either side) but the margin is
  inside Ann's own range across the recording, so pitch does not settle it. The dialogue
  structure does: she answers it.
- No interviewer is audible. The questions in the text ("Are you familiar with this at all?",
  "Are you aware that…") are Ann putting questions to the room.

## Source and measurements

- `History of George Marshall and other Ministers.m4a` — ALAC, 48 kHz, 2 ch, 16-bit,
  **1904.213 s (31:44.2)**, 75,371,783 B, added 2026-10-18 22:56. MD5
  `198d5633a0dc95e812faaf8488d83fe4`.
- Mean **−31.2 dBFS**, peak **−3.4 dBFS**. Even across the file: 16 two-minute blocks all
  peak −3.4 to −7.5 dBFS, mean −28.7 to −33.2 dBFS.
- Speech runs **00:09.6 – 31:50.3**; the last ~53 s is room tone at −50 to −87 dB with no
  speech. Digital silence (exact zeros) makes up 18 % of the file in 186 gaps of ≥0.5 s, but
  only **16 gaps reach 1.5 s** and most of those are in that tail — the talk itself is
  continuous.

### Stereo measurement and decision

Measured on six 30 s windows:

| t | ch0 | ch1 | gap | raw corr | best lag | corr at lag |
|---|---|---|---|---|---|---|
| 60 s | −28.6 | −32.6 | 3.9 dB | 0.878 | −5 samples | 0.9950 |
| 240 s | −29.4 | −33.3 | 3.9 dB | 0.885 | −5 | 0.9960 |
| 480 s | −30.3 | −34.1 | 3.8 dB | 0.893 | −5 | 0.9948 |
| 900 s | −30.5 | −34.2 | 3.7 dB | 0.841 | −5 | 0.9932 |
| 1400 s | −31.6 | −35.9 | 4.4 dB | 0.869 | −4 | 0.9928 |
| 1800 s | −25.8 | −30.4 | 4.7 dB | 0.847 | −5 | 0.9921 |

A constant ~4 dB gap with r = 0.99 at a fixed 5-sample (0.104 ms) lag is a **delayed
duplicate** — the same programme on two feeds, not two different signals. So the channels were
**summed with the lag compensated, weighted 2:1 toward the stronger channel**
(`0.6667*L` delayed 5 samples `+ 0.3333*R`). Dropping ch1 would have thrown away a near-perfect
second copy; an equal sum would have added the weaker feed's noise at full weight.

### Processing (gain only, no denoise)

```
channelsplit -> adelay=5S on L -> pan=mono|c0=0.6667*c0+0.3333*c1 -> volume=+12dB -> alimiter(limit=0.89)
```

Result **−19.5 dBFS mean, −1.0 dBFS max**. No denoise: the source is lossless ALAC, and the
8 kHz+ band measures **0.00 %** of total energy (3–8 kHz 0.39 %) — the capture is band-limited,
so there is no hiss to filter and filtering would only take signal from the transcriber.

## Transcription

- **Whisper large-v3** (Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads), `en`,
  `beam_size=5`, `condition_on_previous_text=False`, `temperature=0.0`, word timestamps,
  `vad_filter=False`, `no_speech_threshold=0.6`.
- **16 chunks** of ~120 s, boundaries snapped to the quietest 10 ms frame within ±5 s. Every
  boundary landed in digital silence. Never a whole-file pass.
- `initial_prompt` seeded with the corroborated names only: Bethel, John McMillan, John Clark,
  George Marshall, C. W. Wycoff, Murray C. Reiter, Bethel Academy, Oliver Miller Homestead,
  Mingo Creek, Canonsburg, Chartiers, Dido, Doddridge, Princeton Theological Seminary,
  Peter Croco, Karla Strobl, Coverdale, Lebanon Church, Pigeon Creek, Jefferson College,
  Washington College.
- **Prompt-leak check: clean.** Every seeded name that appears in the output is spoken in
  context (McMillan, Clark, Marshall, Dido, Bethel Academy, Lebanon, Pigeon Creek, Coverdale).
  Wycoff, Reiter, Croco, Strobl, Doddridge, Princeton, Mingo Creek, Oliver Miller and
  Chartiers **do not occur in this recording at all** — this talk stops at Marshall and never
  reaches the later ministers. No window needed re-transcribing unprompted, and no segment
  was deleted for leakage.

### Quality

- 260 segments, **3,819 words**, **mean per-word probability 0.9601**,
  **2.07 % of words below 0.5**.
- **One** 30 s window below 0.80: **31:00–31:30 (0.603)**, the closing 40 s where the talk
  runs out into room tone. Everything before 31:00 is ≥ 0.80. The lowest-probability tokens
  are segment-initial function words ("And", "The", "So,"), the surname "Dom" twice, and
  "Language," at 17:55.
- **One hallucinated segment removed**: "Thank you." at **31:28.5**, 37 s after speech ended,
  over room tone measured at −67 dB. A second unprompted pass also produced a "Thank you." but
  at a different timestamp (31:26.3) — the signature of filler generation, not speech. The
  "Thank you." at **30:50** is kept: it sits at the exact end of the talk and reads as the
  speaker closing. (It could equally be an audience member; left on ANN.)

## Names and words corrected (all 20 in the JSON `post_edits`)

| # | as transcribed | corrected | why | certainty |
|---|---|---|---|---|
| 1 | "**Matt** Anthony Wayne" | **Mad** Anthony Wayne | the general's nickname; "Matt" is ASR | certain |
| 2 | "**Cannonsburg** Academy" | **Canonsburg** Academy | town name (FACT-CHECK #18) | certain |
| 3 | "Thomas and Elizabeth **Tidbalt**" | **Tidball** | she names William Tidball a minute later | certain |
| 4 | "between the **marshals** and members" | the **Marshalls** | family name | certain |
| 5 | "during **Reverend Wood's** pastorate" | **Reverend Woods's** | William Woods, named earlier | certain |
| 6 | "the allegheny **cordage** railroad" | the **Allegheny Portage Railroad** | the Lemon House and the canal/rail hybrid she describes | certain |
| 7 | "a picture of the **lemon house**" | the **Lemon House** | proper name, Allegheny Portage Railroad | certain |
| 8 | "**He paid them $25,000**" | He paid them **25 cents** | she is reading the letter: 50 cents asked, 25 cents paid | certain |
| 9/10 | "**Jenny Lynn**" (×2) | **Jenny Lind** | Lind sang at Castle Garden; the letter's 1851 date fits | certain |
| 11 | "brown shipley and company liverpool england" | **Brown, Shipley and Company, Liverpool, England** | capitalisation only | certain |
| 12 | "where the **Dons** live today" | the **Doms** | same family as "Dom home"; spelling normalised to the majority ASR form — the surname itself is **unverified** | probable |
| 13 | "the Louisiana **purchase**" | **Purchase** | proper noun | certain |
| 14 | "his participation. In the Whiskey Rebellion" | "his participation **in** the Whiskey Rebellion" | a full stop landed at a segment seam; the sentence continues | certain |
| 15 | "the old **The** log meeting house" | "the old log meeting house" | duplicated "The" at a seam | certain |
| 16 | "**Tidball, who** the trustees" | "Tidball **to** the trustees" | "the sale … by Thomas and Elizabeth Tidball to the trustees" | certain |
| 17 | "if there was any serious objection to it **than it was to be reserved**" | "**then it was to be removed**" | the organ was on trial for a month and to be removed if objected to — "reserved" is the opposite | probable |
| 18 | "any of you know. That house, but it's…" | "any of you know **that house**, but it's…" | one clause split by a full stop | certain |
| 19 | "And books in those days were extremely**...**" | "…extremely **expensive and valuable**." | truncated at a chunk boundary; recovered by an unprompted pass over 1300–1332 s | certain |
| 20 | "Washington Presbytery, **Came** to Bethel" | "…**came** to Bethel" | mid-sentence capital from a segment start | certain |

**Punctuation restored, no words changed** — two passages came back from Whisper as
unpunctuated runs (05:07–05:55 the Temperance Movement / William Woods; 26:55–27:55 the canal
boat). Full stops and commas were inserted at the clause boundaries she speaks; the words are
untouched. Flagged separately from the word edits in the JSON.

Mechanical: Whisper's doubled words collapsed ("period. period.", "Academy. Academy.",
"place. place.", "that that", "of of", "this this"); sentence starts capitalised; a decimal
point ("1.30") and abbreviations ("Jr.") no longer trigger a false capital. Hesitations and
false starts left as spoken ("he studied under the, I believe he was…"; "pastor of, third
pastor of").

## Left as heard / unresolved (not guessed)

- **The family in the Marshall farmhouse** — "where the **Doms** live today", "**Mrs. Dom**,
  who owns the Marshall home now". ASR gave "Dons" and "Dom" for the same person; the true
  surname is unverified and "Dom" is a normalisation, not a finding.
- **"Alex Ringsoe"** (30:35) — "you may tell Alex Ringsoe if you see him. I gather Alex
  Ringsoe wasn't at the reservation." No match found.
- **"John McCabe's barn"** (23:12) — where Marshall's trunk was kept.
- **"Alvin Dinsmore White"** (24:42) — who gave Ann her Marshall material.
- **"Mansfield Brown and White, George B. White, Lewis Hutchison Jr. and mother"** (28:22) —
  fellow passengers named in the letter; not checked.
- **"Which you love to hear Jenny Lind for $1"** (29:25) — reads as a rhetorical "wouldn't you
  love to hear…", but the words do not support a safe rewrite.
- **"he was the founder and for many years the Language, Hebrew, he taught Hebrew and Latin"**
  (17:55) — garbled; **two independent passes agree on the words**, so it is her phrasing, not
  an ASR artefact. Probably a lost word ("the linguist").
- **"Plain Truth"** (02:47) — the part of Coverdale where Clark's land lay.
- **"I should have Jane here"** (22:42), **"I'm in the process of transcribing Maddie typing it
  out"** (24:11) — colleagues named in passing.

## History note — the minister sequence

The tape's own sequence is **McMillan (founder) → Clark (first pastor) → Woods (second) →
Marshall (third)**. She is explicit: "on the death of John Clark came our second pastor,
William Woods", and "he became … third pastor of Bethel Presbyterian Church". That is
consistent with Marshall's dates (b. 23 Dec 1806, preaching at Bethel from 11 Jul 1832,
d. 30 Apr 1872 — *Cyclopedia of Biblical, Theological and Ecclesiastical Literature* and a
family record).

It is **not** consistent with the briefing note for this job, which lists Clark second and
Marshall third without Woods. **The tape and the record are right; the briefing list omits
Woods.** Nothing in the transcript was changed to fit the briefing.

Other names she states that were checked: Dr. **John Stockton** of Cross Creek (confirmed —
Stockton was pastor at Cross Creek and opened its academy in 1828, which is where Marshall
taught); **Thomas Cadoux** (confirmed in the sibling A/B transcript as Marshall's travelling
companion); **Peg and Fred Bolander** (confirmed in the A/B transcript). The third meeting
house in **1855** and the first organ in **1866** were not independently checked.

## Portable copy — not a condensation

`History of George Marshall and other Ministers.mp3` — mono 64 kbps
48 kHz, 1852.0 s (30:52), 14,816,492 B.

Measured before building it: 16 silent gaps ≥1.5 s, **41.4 s total**, of which 25.7 s lies
after 30:58 and another 6.7 s before she starts. Inside the talk there are only **four** pauses
of ≥1.5 s, **7.50 s altogether**; collapsing each to 0.5 s would save **5.5 s — 0.29 %** of the
recording. **There is no meaningful dead space to condense**; the only real dead space is the
**53.7 s silent tail** after she stops speaking, of which **52.2 s** is removed here
(1904.2 s → 1852.0 s, 2.74 %). So this is a straight transfer copy with
the tail cut, not a condensed edit, and no word or pause inside the talk was touched.

## Files

| File | What |
|---|---|
| `History of George Marshall and other Ministers.txt` | corrected transcript, 130 paragraphs, 3,789 words, ANN/AUDIENCE labels |
| `History of George Marshall and other Ministers.srt` | 535 cues, word-timed, monotonic, 00:00:09.6 – 00:30:50.2 |
| `History of George Marshall and other Ministers.json` | raw segments + per-word timings/probabilities, stereo measurements, prompt, chunk table, `post_edits`, dropped segment, unresolved list |
| `History of George Marshall and other Ministers.docx` | built from the `.txt`; ANN blue, AUDIENCE red — 129 ANN runs + 1 AUDIENCE run in `document.xml` |
| `History of George Marshall and other Ministers.mp3` | mono 64 kbps, tail removed |

The `.txt` is the source of truth; the `.docx` is a build product. Rebuild with
`make_docx.py … --main-speaker ANN --secondary AUDIENCE`.
