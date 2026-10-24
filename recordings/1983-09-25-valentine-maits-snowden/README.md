# Ruth Valentine, Miller Maits and Jean Snowden — remembering Bethel (25 September 1983)

A Historical Room session at Bethel Presbyterian Church, Bethel Park, Pennsylvania, recorded on
**25 September 1983**: an unnamed moderator reads the church's history aloud and hands over in turn to
three of the congregation's oldest members, who talk about what they themselves remember.

| | |
|---|---|
| **Speakers** | Ruth Valentine · Miller Maits · Jean Snowden |
| **Moderator** | An unnamed man, labelled `HOST`; never identifies himself |
| **Recorded** | Sunday, 25 September 1983 — date from the archive's capture record, corroborated loosely by the tape (see §1) |
| **Length** | 25 m 59.98 s (1,559.98 s), one continuous capture |
| **Words** | 3,073 in the filed transcript |
| **Status** | Transcribed, corrected, labelled; one reading pass, no second engine; audio master held on the archive NAS |

This is a **meeting, not an interview**: the moderator introduces each speaker by name, reads the
history, and takes about a third of the tape himself. The last ~1 m 40 s is the meeting breaking up,
with chatter away from the microphone.

---

## 1. How the date is established

**The tape states no date.** The date is **filename-supplied**: the source JSON records it as
user-supplied by John Decker, written `9-25-83` on the original capture (`recorded.source`). That is
a filename, not a slate — weaker evidence than a date read onto the tape.

One internal detail is consistent with it. The moderator closes with

> "over 200 years now of history, almost 206 or 207 years, I guess, this year."

Bethel was founded on 5 November 1776; 1776 + 206 = 1982 and 1776 + 207 = 1983. That fits 1983 and
excludes nothing near it, but it does not prove the day or the month. **25 September 1983 was a
Sunday**, which fits a Historical Room session held before the morning service — the tape ends with
someone asking when the service starts and being told "It's quarter to 11 now."

Nothing on the tape contradicts 25 September 1983. **2026-10-18** in the archive's collection folder
name is the digitisation date, not the recording date.

## 2. The physical recording and its capture

| | |
|---|---|
| Master file | `Valentine, Maits and Snowden (25 September 1983).m4a` |
| Format | ALAC 48 kHz stereo 16-bit (lossless) |
| Duration | 1,559.978667 s (25 m 59.98 s) |
| Size | 58,020,991 bytes |
| sha256 | `cacd4b6a06676be4ebc5d8c23930a478403e35d386574f5c274a22ea532180c7` |
| md5 | `913bdf2b51aa75586d7cd6931b03403f` — recomputed here, identical to the md5 in the source JSON |
| Mean level | −23.1 dBFS |
| Peak | −4.3 dBFS |
| Bit rate | 298 kbps |

Duration, format, sample rate, channel count, size, sha256, md5, mean level and peak were measured on
the master for this record. The source JSON gives −19.0 dBFS mean and −1.0 dBFS peak for the
**processed working copy**, after the +3.78 dB of gain it applied; −23.1 + 3.78 = −19.3 dB, so the two
sets of figures describe the same signal before and after that gain. The gain was applied to a
working copy only — the master is untouched.

**Digitisation.** The source JSON carries no per-item digitisation date. 2026-10-18 is the
collection's date per the archive README and folder name, and the master's NAS mtime is 2026-10-19
23:22 EDT. Which of those is the capture date is not established; the metadata records the collection
date and says so.

**Stereo.** The source JSON records a **delayed duplicate**: a constant 4-sample (0.083 ms) lag at
r = 0.96–0.996 across nine 30-second windows, channel 1 stronger by 2–3 dB through the body of the
tape. The working copy was summed `(2·ch1 + ch0)/3` with the lag compensated, then gained +3.78 dB.
That measurement was made during transcription and is reported from the JSON; it was **not**
re-measured for this package.

**No denoise, deliberately.** The source is band-limited — the JSON records essentially nothing above
2.4 kHz, with the >8 kHz band at 0.0000–0.0001 % of total energy. There is no hiss to filter, only
signal to lose.

## 3. What was done to it (the method, as the source notes record it)

1. **Chunked, never whole-file.** 13 chunks of ~120 s, boundaries snapped to the quietest 10 ms
   frame within ±5 s of each target.
2. **Seeded prompt**, corroborated names only, including the three participants' surnames. The
   **leak check came back clean**: "Valentine", "Maits" and "Snowden" do not occur anywhere in the
   output. The one seeded name that does appear early, "Fort Tidball", was confirmed by an
   un-prompted re-transcription of 0–45 s, which produced the same words.
3. **Speaker attribution by dialogue structure first**, then pitch as a check: who is addressed, who
   answers, who introduces whom. Pitch was used to confirm that a label covers one voice — not to
   name anyone.
4. **Every change recorded** in the source JSON's `post_edits`: 33 entries with the raw form, the
   replacement, the reason and the certainty.

## 4. The engine, and what it measured

| | |
|---|---|
| Engine | Whisper **large-v3**, Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads |
| Decoding | `en`, `beam_size=5`, `condition_on_previous_text=False`, `temperature=0.0`, `no_speech_threshold=0.6`, `vad_filter=False`, word timestamps |
| Audio path | ffmpeg → float32 numpy arrays (PyAV in this build rejects the `metadata_errors` kwarg faster-whisper passes) |
| Segments | 238 |
| Words | 3,073 in the filed transcript (the source JSON counts 3,108 on the segment level — a counting-method difference, not a text difference) |
| Mean per-word probability | **0.9403** |
| Words below 0.5 | 3.54 % (6.76 % below 0.7) |

Only **one** engine was run. There is no second-engine cross-check and no WER figure for this item.

Every 30-second window below 0.80 mean probability lies **after 24:30**, in the post-meeting chatter;
the formal remarks are 0.80 and above throughout.

## 5. Speaker attribution, and how sure it is

| label | evidence |
|---|---|
| `RUTH VALENTINE` | Moderator: "Thank you, Ruth" (6:23), immediately after she stops. She reads her own cradle-roll certificate: "Ruth Elizabeth Douglas … born on the 26th day of December, 1913". **First name certain; surname not on the tape.** |
| `MILLER MAITS` | Named twice independently — by the moderator at 6:29 ("The next person is Miller Maits … a descendant of the Oliver Miller family") and by Ruth at 4:46. **The only one of the three surnames the tape says aloud.** |
| `JEAN SNOWDEN` | Moderator at the hand-over: "Jean, why don't you take over" (16:52); referred to again at 23:14. **First name certain; surname not on the tape.** |
| `HOST` | Unnamed moderator, median f0 150 Hz across four blocks — 45 Hz below the two women and 37 Hz above Maits, which is what rules him out as one of the three. |
| `UNIDENTIFIED` | After 24:20 only: off-microphone chatter that cannot be attributed. |

**Ruth and Jean cannot be separated acoustically** — 206 Hz against 208 Hz, timbre similarity 0.989.
The split rests entirely on the moderator naming each woman as she takes the floor, and on their
self-descriptions being incompatible (Ruth's certificates run 1914–1929; Jean had been a member 33
years with a toddler in 1950).

**One judgement call, flagged not resolved.** From 15:47 the moderator says he will "turn this over
to Gene for a few minutes", then speaks for another minute himself before actually handing over at
16:52. That minute is labelled `HOST` because its pitch is identical to his other blocks (150.9 Hz
against 150.0 and 150.9) and 45 Hz below Jean's — but if the hand-over took effect when announced,
those lines are Jean's and the label is wrong. The audio cannot settle it.

## 6. Corrections and what is left as heard

**Substantive `post_edits`** (33 in all):

| heard | changed to | basis | certainty |
|---|---|---|---|
| "turn up a child and away should go" | "Train up a child in the way he should go" | Proverbs 22:6, printed on the certificate she reads | certain |
| "Mary Wyckoff", "mary wycroft" | Mary Wycoff | the 1951 history has 111 "Wycoff", no "Wyckoff"; she is named cradle-roll superintendent | certain |
| "murray c ryder" | Murray C. Reiter | the pastor's signature on the certificate; Reiter installed May 1914, her baptism June 1914 | certain |
| "Mrs. Ryder taught the class" | Mrs. Reiter | the same name as the signature — the pastor's wife | probable |
| "principally cannonsburg" | Canonsburg | town name | certain |
| "a general neville", "pastor clark" | General Neville, Pastor Clark | the Whiskey Rebellion figures in the history he reads | certain |
| "their own legionary society" | their own missionary society | the subject of the passage | probable |
| "called Pigeon Creek. / Creek. Our church" | "called Pigeon Creek. Our church" | duplicated fragment across a chunk seam | certain |
| "Thank you." (×2, 25:39 and 25:58) | removed | hallucinations over verified silence after speech ended | certain |

Mechanical work alongside: doubled words and stray fragments across chunk seams ("put his hands upon
/ upon them", "active and / and dedicated", "the three / Three groups"), sentence case, and one
hallucinated "Noah?" dropped at 6:50. Hesitations and false starts were left alone.

**Left as heard — the honest gaps.** Eleven items are listed as unresolved in the source JSON; the
substantive ones:

- **"Fort Tidball"** (0:13–0:26) — where Ruth was born, "off Logan Road, below the church". Reproduced
  identically by an un-prompted pass, so it is what she says, but no such fort or place-name was
  found. Possibly a local name for a Tidball family property.
- **"they called the fire tire"** (3:02) — the small room where the beginners' class met.
- **Names read off certificates, none corroborated**: "Elsie McConkie" and "Mr. Kravitz" (3:33–3:42),
  "H. E. Pellett" (3:58), "Isabel Hemlinger" (5:55), and the play title "Home Came Ted" (5:55).
- **"Mr. Yarnell"** (11:29) — a pastor whose pastorate ran "up through 1960"; not checked against the
  1951 history, which ends before him.
- **Three broken clauses**: "We can't sit or stand on our path, but we have to go forward" (22:39),
  "So you know why we had to build the little children" (21:57), "I keep seeing something more"
  (16:23).
- **Chatter after 24:20** — intelligible, unattributable, partly left in because it is on the tape.
- **The date is filename-supplied** (§1), and the **surnames of two of the three speakers are not on
  the tape at all**; they come from the filename and map onto the participants in speaking order,
  which is an inference.
- **Rights.** Public-domain status rests on the collection-level release in `docs/RIGHTS.md`; no
  per-item release document is in the source folder.
- **Not re-measured here:** the stereo lag/correlation figures and the per-window probability table,
  quoted from the source JSON.

## 7. What is on the tape — outline with timestamps

- **0:13** **Ruth**: born in "Fort Tidball", off Logan Road below the church
- **0:57** The cradle-roll certificate: enrolled 28 March 1914, born 26 December 1913, signed Mary
  Wycoff and Henry Harley, motto Proverbs 22:6
- **2:10** Baptised by **Reiter** in June 1914 — "one of the first"; promoted to the beginners'
  department, 1917, Mrs. Reiter's class by the stairway
- **3:20** Promotion certificates 1923 and 1929; superintendents named; the **Lightbearers**
- **4:24** The **Tom Thumb Wedding** — 30 children under seven; **Miller Maits** was in it
- **5:30** Christian Endeavor, the plays, "Nothing but the Truth" and "Home Came Ted"
- **6:23** The moderator thanks Ruth and introduces **Miller Maits**, a descendant of the Oliver
  Miller family
- **7:30** **Maits**: arrowheads turned up by the plough, the spring, the old wooden bridge and a
  bent-pin fishing line
- **9:18** The moderator's **history of the buildings**: a log church of 1779 across the road, torn
  down 1826 for a brick church on the present site, 1855, and the present church of 1910, its bricks
  carrying the earlier ones forward
- **11:01** The **1909 Easter Sunday tornado** that took the roof off, as Edna Croco told it
- **11:38** Only **six pastors** in 175 years, up through Mr. Yarnell's pastorate (to 1960)
- **12:37** The **Whiskey Rebellion**, 1794: Pastor Clark pleads with the men, **General Neville**'s
  house at Bower Hill (13:28), Major McFarlane killed
- **13:50** McMillan at the **Hill Church** from 1775, and at **Pigeon Creek** (13:59)
- **14:26** What the buildings cost: $6,000 in 1855, $30,000 in 1910, $55–60,000 to dig the basement,
  $247,000 in 1951
- **15:36** The oldest grave: **Elizabeth Kitto**, 1784
- **15:55** First woman deacon 1947, first woman elder 1963 (16:00) — "backward, perhaps, is a better
  word"; **Samuel Fife** and the trees of Bethel
- **16:52** **Jean** takes over on the **women's organisations**
- **17:05** The three bodies: **Ladies Aid Society**, the missionary societies, the **Fannie Dietrich
  Society** (1887); 1785, linen dyed with new-mown hay for the seminary students' suits (17:43)
- **18:27** Chicken dinners and oyster suppers for the 1910 building; what the Ladies' Aid bought
- **19:39** The first missionary society, **1822** — 106 members, 44 of them women, all offices held
  by men; the women's own society from **1840**
- **21:04** The three merged in **1945** into the UPW; "we've only been members for 33 years"
- **21:57** The building phases they have lived through; 70 children in the kindergarten room
- **23:14** The moderator's close: women's talents wasted for years; "almost 206 or 207 years"
- **24:09** The meeting breaks up — "It's quarter to 11 now"

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The transcript: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt` | The same text as timed cues (234), for playback or captioning |
| `notes-a.md` | The archive's working notes: measurements, engine settings, attribution evidence, every judgement call |
| `metadata.json` | The record of record: date and its source, speakers, master with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

`transcript-a.md`, `transcript-a.srt` and `notes-a.md` are **byte-for-byte copies** of the archive's
files of the same stem, taken on 2026-10-23. Nothing was edited for this repository; the "Side A"
label in `metadata.json` names the single file, not a cassette side.

The audio master is **not** here (see `docs/AUDIO.md`): it is held on the archive NAS, identified
above by sha256.

## 9. Citing it

> Valentine, Ruth; Maits, Miller; and Snowden, Jean. *Remembering Bethel*. Historical Room session,
> Bethel Presbyterian Church, 25 September 1983. Historical Room, Bethel Presbyterian Church:
> digitised 18 October 2026. Transcript, 3,073 words.

Cite the timestamp for anything quoted. Two cautions for a careful citation: the surnames
"Valentine" and "Snowden" are **not spoken on the tape**, and the moderator is unidentified.

## 10. Reproducing this transcript

- model: large-v3, CTranslate2 **int8**, language `en`, **beam 5**, 14 threads
- `--chunk-seconds 120`, snapped to quiet points: **13 chunks**
- seed: the archive's corroborated name list, with a leak check (clean)
- input: the 2:1 channel sum, lag-compensated, gained +3.78 dB — the working copy, not the raw master

A re-run on the same master, engine and settings reproduces the raw ASR text; the filed text differs
from it by the 33 `post_edits` in the source JSON, each revertible in one line.

## 11. Related material in the collection

- **`1983-09-25-ann-connor-john-mcmillan`** — Ann Connor's lecture, recorded the **same day**. The
  two agree on the ministers' names and on the 1776 founding; they **differ on when McMillan began
  preaching here** — this panel says 1775, the lecture says he was ordained in June 1776 after
  arriving in 1775. Neither is corrected here; the disagreement is worth knowing about.
- **`1977-11-06-ann-connor-bethel-needlepoint`** — Ann Connor in 1977 on the same families, with a
  needlepoint demonstration.
- **`1971-07-15-ad-white-cross-creek`** — A.D. White's interview, the collection's other long
  first-hand account.
