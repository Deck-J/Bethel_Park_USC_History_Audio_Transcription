# Allegheny County — the geology and coal-mining history of the South Hills (date unknown)

A talk in two sides, given by one unnamed older man — a former miner ("all the ones that were there
when I worked in 1933, and here before World War II") who is also an assured local geologist — working
through a set of maps, photographs and slides in the Historical Room at Bethel Presbyterian Church.

**Side A** is the mining history of the South Hills, read off the rocks: the Pennsylvanian reference
section at the cliff opposite the Point (Rogers, 1840), the county's Conemaugh and Monongahela
formations, the Pittsburgh seam and the Redstone and Waynesburg seams above it, Ohiopyle and
McConnells Mill, the Bureau of Mines experimental mine at Bruceton, the Wabash and B&O railroads at
Curry, the Snowden post office renamed Broughton, the Horning mine and *Black Fury*, Montour No. 10 at
Library, Triphammer Road, and finally why South Park could be bought — the coal lay deeper there.

**Side B** opens in the middle of the *previous* speaker's talk, on the mill on Cochran Mill Road, and
hands over at 1:01 to the same geologist, who starts again from first principles: the three rock types
and the acid-clay soil problem, coal and its sulfur, iron carbonate, the fossils, William Maclure and
the first geological map of North America, the National Pike, the I-79 cut at Heidelberg, the Peters
Creek watershed, the Amity anticline and its hundred gas wells, building stone and brick, and the
Alliance and Hopewell furnaces — closing with an artist's impression of the coal swamp 300 million
years ago.

| | |
|---|---|
| **Speaker** | One unidentified man, a former miner and local geologist; the tape never states his name |
| **Room** | More than one listener: "this lady has already told you more of the history than I knew about it" (A, 15:44), **Grace** is asked whether she can see (B, 10:52), **Jim** is asked to hold the fossil up to the light (B, 7:53). Two audience questions are labelled `AUDIENCE` |
| **Recorded** | **Date unknown** — see §1 |
| **Length** | Side A 21 m 25 s (1,284.78 s) + Side B 30 m 59 s (1,859.16 s) = **52 m 24 s** |
| **Words** | 6,661 (2,608 + 4,053) in 91 labelled turns |
| **Status** | Transcribed 2026-10-20/21, corrected, labelled, verified; masters held on the archive NAS |

Neither side carries a title. "The geology and coal-mining history of the South Hills" describes the
contents and is drawn from the talk itself.

---

## 1. How the date is established — and why it is not

**It isn't, on either side.** No date is spoken, neither filename carries one, and neither source JSON
does: both read `date_recorded: "UNKNOWN"`, with a note that the content places the talk after 1970 and
probably after 1990. The archive README's row for the geology lecture records **UNKNOWN** as well.

What the tape supports is a **bound, not a date**:

- the mines around him are "long since closed down", and he remembers several of them running;
- "all the ones that were there when I worked in **1933** before World War II" — memory, so the talk is
  decades later;
- a Consol research laboratory at Library, and the Bureau of Mines building as a landmark in the
  present tense.

That is the reasoning recorded in `notes-a.md` and `notes-b.md`. It is written as reasoning and not as
a date, and `metadata.json` carries `date: "unknown"` with the folder named `unknown-…` for that
reason alone.

## 2. The two masters, and every audio file in the source folder

| | Side A | Side B |
|---|---|---|
| Master file | `Allegheny County Geological and Mining lecture.m4a` | `Allegheny County Geological and Mining lecture - B side.m4a` |
| Format | ALAC 48 kHz stereo 16-bit | ALAC 48 kHz stereo 16-bit |
| Duration | **1,284.778667 s (21 m 25 s)** | **1,859.157333 s (30 m 59 s)** |
| Size | 51,772,077 bytes | 82,684,034 bytes |
| **sha256** | `61b1a7aa8fe2b918dcdb5dab72cb9c16b694a0a10464c7045c3139406f2c5bf7` | `081ac80b90c332ff74087053d040faa43ce89e72fe93cd338249e37a7e8d94d8` |
| md5 (capture record) | `c53f4c245364d68736414c3e1c2c64b5` | `d79e72d9daf3e0bb70a9ec917e2ba948` |
| Mean level | **−21.3 dBFS** (measured) | **−21.7 dBFS** (measured) |
| Peak | **−1.2 dBFS** (measured) | **−1.9 dBFS** (measured) |
| Last speech | 1,200 s; last 84.8 s at RMS −83.0 dBFS, peak −49.6 dBFS | last cue 30:30.8; the file runs on 28 s beyond it |

Hashes, durations, channel counts and levels were **recomputed from the files** for this record
(`hashlib.sha256`, `ffprobe`, `ffmpeg volumedetect` / `astats`); the md5s are the figures the
transcription JSONs carry.

**Every audio file in the source folder is accounted for:**

| file | what it is | measured |
|---|---|---|
| `Allegheny County Geological and Mining lecture.m4a` | **master, Side A** (as received) | 51,772,077 B, 1,284.78 s, ALAC stereo |
| `Source original/Allegheny County Geological and Mining lecture.m4a` | the untouched capture as received — **byte-identical** to the master above | 51,772,077 B, same sha256 `61b1a7aa…` |
| `Allegheny County Geological and Mining lecture.mp3` | 192 kbps stereo listening copy of Side A | 30,835,789 B, 1,284.75 s |
| `Allegheny County Geological and Mining lecture (portable).mp3` | mono 64 kbps transfer copy of Side A, full length, nothing cut | 10,278,733 B, 1,284.75 s |
| `Allegheny County Geological and Mining lecture - B side.m4a` | **master, Side B** (received as `B side.m4a`, renamed; samples untouched) | 82,684,034 B, 1,859.16 s, ALAC stereo |
| `Allegheny County Geological and Mining lecture - B side.mp3` | 192 kbps stereo listening copy of Side B | 44,619,884 B, 1,859.10 s |

Only the two `.m4a` masters are recorded in `metadata.json`. The MP3s are derivatives; the portable
copy of Side A is a straight transfer, not a condensation.

**Stereo, and two different findings.** On Side A no channel comparison was needed or made: the capture
is a mono-sourced digital file in a stereo container and the ASR ran on the full master decoded to
16 kHz mono. On Side B the pair is the same programme on two feeds — 1.0–1.2 dB apart, correlation
0.97–0.99 at a constant 4–6 sample lag in every block measured — so the channels were **summed**
(`0.5 × c0 + 0.5 × c1`) rather than one being used. Levels on Side B run −25 dB mean early and −20 dB
from about twelve minutes: he moves nearer the microphone, or the room fills.

**Nothing was cropped or processed.** Both masters are the captures as received: no denoise, no gain,
no remux. The A side's silence after 1,200 s is why the ASR run stopped there; nothing was lost.

## 3. What was done to them (the method)

Both sides were transcribed under **identical conditions**, so they can be compared:

1. **Chunked at ~120 s** (16 chunks per side), boundaries snapped to the quietest 10 ms frame; decoded
   by ffmpeg to float32 numpy arrays, because PyAV in this build rejects the `metadata_errors` kwarg
   faster-whisper passes.
2. **No `initial_prompt` at all** — unseeded, on both sides. This recording has no seed-leak question
   because it has no seed; the names had to be recovered from the audio and the local record instead
   (see §5).
3. **Cold passes** on every doubtful passage: on Side A, **18 windows × 3 settings** (beam 5, beam 1,
   beam 5 + VAD) = 54 transcriptions; on Side B, **16 windows × 3** = 48. Every verdict in the
   FACT-CHECK files names what the passes returned.
4. **One window was re-run, not restarted**, on Side B: a run was killed mid-job after its result was
   lost, and the script resumed from the log by skipping windows already written. The window was the
   projector-and-lights exchange, which the ASR had flattened to repeated "Don't" and which the re-run
   recovered as audible dialogue — carried as a bracketed stage direction, since the voices do not
   separate.
5. **Stutters collapsed** ("the the" → "the", repeated segment heads), lone lowercase "i" → "I".
   Nothing else was tidied: hesitations and false starts are left as spoken.
6. **Correct, and log the correction** in each side's `post_edits` with pattern, count, certainty and
   reason — see §5.

## 4. The engines, and what they measured

Both sides: **Whisper large-v3**, Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads,
English, `beam_size=5`, `condition_on_previous_text=False`, word timestamps, `vad_filter=False`.

| | Side A | Side B |
|---|---|---|
| ASR segments | 176 | 334 |
| Words (ASR) | 2,622 | 4,066 |
| Mean word probability | **0.8524** | **0.8534** |
| Words below 0.5 | **9.88 %** | **9.69 %** |
| Filed document | 32 turns, 2,608 words | 59 turns, 4,053 words |
| Timed cues | 175, to 19:59.96 | 334, to 30:30.80 |

Side A's cues stop at 19:59.96 although the file runs 21:24.8, because the run stopped at 1,200 s where
speech ends. The archive also holds a **both-sides** `.srt` — A's 175 cues unchanged, then B's 334
offset by 1,284.778667 s and renumbered: 509 cues, monotonic, with a **91.9 s gap** at the join (the A
side's silent tail plus the 7.1 s before B's first word). It is a derived file and is not in this
repository.

## 5. Corrections made (Side A 48, Side B 56, all reversible)

Each is an entry in the side's JSON `post_edits` with the pattern, the replacement, how many times it
occurs, a certainty marker and the reason. Two habits of this capture drove most of them:

1. **"Coal" collapses to *pole / foal / foam*, and "seam" to *scene / seed*.** Once the cold passes
   returned "coal" and "seam" in the identical sentences, every instance could be fixed together.
2. **"Snowden" collapses to *god / Godden / drowden*.** The post-office story — Snowden renamed
   Broughton so mail would stop going to the other Curry, Pennsylvania — only reads once the name is
   put back.

The readings that needed the local record rather than the audio:

| heard | corrected to | side | basis | certainty |
|---|---|---|---|---|
| "Ponybaugh Formation" | **Conemaugh** | A | northern Allegheny County is Conemaugh, with no workable coal — exactly what he describes | probable |
| "Longahail" / "Palonga hill" | **Monongahela** | A | the southern formation, two to three workable seams | certain |
| "Pittsburgh pole seam", "workable foal" | **coal** | A | cold passes give "coal" in the same sentences | certain |
| "halfway between Hawkinsville and Brewstone" | **Hawkins Mill and Bruceton** | A | no Hawkinsville in the county; Bruceton is the Bureau of Mines mine | probable |
| "drowden … but god really was the name of the post office" | **Snowden** | A | Snowden was the post office and the township, renamed South Park in 1966 | certain |
| "the horny farm … the morning mine", "Hoarding" | **Horning** | A | Horning farm, Horning mine and patch town | certain |
| "redstone seam … near Bondville" | **Brownsville** | A | Redstone coal is named for Redstone Creek at Brownsville; Fort Burd stood above it | probable |
| "the amity and the climb" (A) | left as heard; B supplies the sense — the **Amity arch**, an anticline | A/B | B: "named from Amity, down in Washington County", and "the Amity arch or anticline" | probable |
| "Cochrane View" (A) | left as heard; identified by B as **Cochran Mill Road** | A/B | B names the mill, one mile south of the Bureau of Mines | probable |
| "Crawford's Mills" | **Cochran's Mill** | B | the mill on Cochran Mill Road, over Lick Run | certain |
| "his name was matur", "McClure" | **William Maclure** | B | the "father of American geology"; first map of the United States, 1809 | certain |
| "Freiburg School of Mines" | **Freiberg** | B | Bergakademie Freiberg, Saxony | certain |
| "a stone arch at Grasmere" | **Grantsville** | B | the Casselman River Bridge, 1813–14, on the National Road | certain |
| "the old economy" | **Old Economy** | B | Old Economy Village, Ambridge | certain |

**Where the audio beat the books:** the theatre is written **"Carroll Theater"** because all three cold
passes return it twice, while the Western Pennsylvania Coalfields survey says only that *Black Fury*
was "shown at the nearby Broughton Theater". The tape is the primary source, so his words stand and the
discrepancy is recorded, not corrected.

**Where his memory and the record disagree, the transcript keeps his words** and the FACT-CHECK records
the difference: Broughton School "1927" against 1929; the strike "1937" against a 1927 cold pass and a
documented 1928; the Pittsburgh Coal Company "headquarters" at Library, which was downtown; the *Black
Fury* "novel" before the film, when the novel is 1966; and "closed for two years ago … opened last
December", which fits no documented date for Montour No. 10 (closed 1957).

## 6. Left as heard, and defects found in the source material

**Side A — 9 unresolved readings**, listed in the JSON and in `notes-a.md`:

- **"A lot of stars at Bob Zanesburg"** (3:20) — stable across every cold pass and meaningless; there
  is no Zanesburg in Pennsylvania. A permanent gap, left as heard.
- **"Dawson's tiny fort"** (15:23) — cold passes give "Dawson's Piney Fort" / "Goss's Piney Fort".
- **"two old firefighters"** near Houston (8:30) — probably two old openings or drifts, not recoverable.
- **"McElhaney and Siklum to get me, and Martin"** (6:26) — the old mining families; not recoverable.
- **"first Hawkins Mill"** (16:13) — read as Hawkins Mill, the mill in the photograph; not independently
  found, though Side B places Hawkins Mill on the Amity gas line.
- **"owned by the kidu family"** (15:51) — cold passes give Kidu / Kidoo / Cadoux; no such mine or
  family in the county mine indexes.
- **"this tree fork, overlaid by thick sandstone"** (5:08) — "Freeport" is the likely word (the
  Allegheny Formation's workable beds are Clarion, Kittanning and Freeport) but no pass returns it
  cleanly.

**Side B — 8 unresolved readings**, including "the rocks of the tail masons" (17:08), "Chippenham Road"
(19:41, no such road on OpenStreetMap), the unrecoverable feature in "this is typical screen which we're
only going through prairie" (22:21), and "Instead of early settlers, we had early virgins" (29:38) —
which all three passes hear, and the room laughs.

**Three defects in the source documentation**, recorded rather than smoothed over:

1. **A count that does not match the file.** `notes-a.md` says "44 corrections are applied"; the JSON's
   `post_edits` array holds **48** entries, and the FACT-CHECK file carries more than either. The array
   is the fuller record and is what `metadata.json` counts.
2. **A provenance header that contradicts its own file.** The Side B `.md` header says its "timecodes
   run on the meeting clock, 21:24.8 after the A side", but the shipped `.srt` and `.md` both start at
   **00:00:07** — they are 0-based on the B-side file, as `notes-b.md` says. Only the archive's
   `(both sides).srt` carries the meeting clock. The cues were not altered; the header sentence is
   wrong.
3. **A handover the transcript does not carry.** `notes-b.md` describes the opening handover as "Okay,
   thank you, Martha. Thank you, Bob."; the filed text has only **"Okay, thank you."** at 1:01. Nothing
   was added to the transcript to match the note.

## 7. What is on the tape — outline with timestamps

**Side A (21 m 25 s)**

- **0:15** The cliff opposite the Point, and **Professor Rogers** in 1840 naming the reference section
- **0:59** A **geologic map of Allegheny County** — Conemaugh to the north, Monongahela to the south
- **2:04** The first mines opposite the Point; the move along the hill as the seams were worked out
- **2:51** **The Pittsburgh coal seam** — six feet or more, under four states
- **4:03** The **Redstone** seam, and the **Waynesburg** above it (4:35)
- **5:08** The Allegheny Formation's thin seams, and the tree fork under thick sandstone
- **5:40** Ohiopyle and McConnells Mill
- **6:12** **The government mine** at Bruceton; the families who left the farms for it (6:26)
- **8:30** Two old openings north of Houston; the Wabash and B&O; **Brownsville Road** (9:13)
- **10:13** **Broughton** — the Snowden post office renamed; the brick school and **Ida Miller**
  (10:29)
- **11:20** **The Horning mine** — the 1926 explosion, the strike, Musmanno, *Black Fury* and Paul Muni
- **12:37** The Currys, the Gibson farm, the only working farm he knows of
- **13:47** Brick kilns; **the largest mine, at Library** (13:58) and its research centre
- **15:04** **Piney Fork**, Triphammer Road and the forge (15:23), **Catfish Run** (15:44)
- **16:38** Gas wells on the hill; **Coventry** and 2,000 acres with no mines (17:18)
- **18:47** Applause — "Amen."; **19:14** "Thank you."

**Side B (30 m 59 s)**

- **0:07** The previous speaker, mid-sentence: **Cochran's Mill**, the Whiskey Rebellion, Tom the Tinker
  filling the footholds, the mill torn down in 1978
- **1:01** Handover — "Okay, thank you."
- **1:21** The three rock types: **shale** (1:44), the miners' "slate", and the clay it weathers to
- **4:00** **Limestone**, roasted with charcoal to lime for the acid soil; the three types summed up
  (4:54)
- **5:02** **Coal**, and its sulfur; **iron carbonate** "pancakes" (6:45)
- **7:00** The fossils — ferns, *Calamites*, and a tree trunk held up for the room
- **9:32** The slides; lights off; **"Can you see it, Grace?"** (10:52); Joe at the projector
- **11:07** The most famous early settler: **William Maclure** (11:52), **Freiberg** (12:25), the first
  geological map of North America (12:42), and the **National Pike** as the only road on it (14:14)
- **15:01** Why Pittsburgh was not on the Pike; the Casselman arch at **Grantsville**
- **16:54** Rye and buckwheat, and the soils that suited them; **"What does the deep blue represent?"**
  (17:04)
- **18:15** A rough sketch of the area; the **Peters Creek** watershed; **Piney Fork** (19:05)
- **19:55** **The Amity anticline** — more than 100 gas wells; **"the gas that's trapped on top of the
  arch?"** (20:42)
- **22:14** The feature in the slide he cannot name; **building stone** (23:11); brick, kilns and the
  **shot tower** (25:35)
- **26:26** The first blast furnace west of the Alleghenies; **Alliance Furnace** (26:33); cannonballs
  for Wayne (27:27); **Hopewell Furnace** and its richer ore
- **29:33** An artist's impression of the coal swamp 300 million years ago — "instead of early
  settlers, we had early virgins", and the room laughs

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md`, `transcript-b.md` | The transcripts: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt`, `transcript-b.srt` | The same text as timed cues (175 and 334), 0-based on each side's file |
| `notes-a.md`, `notes-b.md` | The working notes: measurements, engine settings, the cold passes, every judgement call — with the FACT-CHECK tables appended verbatim |
| `metadata.json` | The record of record: date (unknown) and the search behind that, speakers, both masters with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

The masters are **not** here (see `docs/AUDIO.md`): they are held on the archive NAS, identified above
by sha256.

## 9. Citing it

> *The geology and coal-mining history of the South Hills*. Talk in the Historical Room, Bethel
> Presbyterian Church, Bethel Park, Pennsylvania, date unknown; two sides, 52 m 24 s; digitised
> 18 October 2026. Transcript, 6,661 words.

The speaker is unidentified, so there is no name to cite. Give the side (A or B) with the timestamp —
the two sides have separate timebases, and only the archive's `(both sides).srt` runs on one clock.

## 10. How this text got here

The transcripts in this folder are the archive's filed transcripts, **copied unchanged** from
`Allegheny County Geological and Mining lecture.md` and `… - B side.md`, with their `.srt` files and
their transcription records. Nothing was re-transcribed for this repository and no word was altered in
the copying; the corrections in §5 had already been applied and logged in the source JSONs by the
archive. `bin/check.py` verifies the copies against `checksums.sha256`.

## 11. Related material in the collection

- **Gertrude Tanner lecture** — another Historical Room talk to a seated audience, same room, same era
- **Ann Connor, John McMillan lecture** — the church's own history, delivered in the same way
- **A.D. White, Cross Creek records and the Whiskey Rebellion** — the Whiskey Rebellion and Oliver
  Miller, from the other end of the county's history
