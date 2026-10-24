# Ann Connor — the 201st anniversary: Bethel needlepoint and the Miller homestead (6 November 1977)

A Sunday-school talk at Bethel Presbyterian Church, Bethel Park, Pennsylvania, recorded on **6 November
1977** — the day after the 201st anniversary of the founding of Bethel and Lebanon churches — followed
by a demonstration of the needlepoint and corn-husk work made for the Oliver Miller Homestead. The
first forty minutes are a talk to children; the last ten are two women working lace at a table.

| | |
|---|---|
| **Speaker** | Ann Connor (surname from the family/archive; never spoken on the tape) |
| **Also heard** | Visiting adults (`INTERVIEWER`) and children answering questions (`CHILD`) |
| **Recorded** | Sunday, 6 November 1977 — **stated on the tape in its first sentence** (see §1) |
| **Length** | 44 m 35.8 s (2,675.80 s), one continuous capture |
| **Words** | 5,890 in the filed transcript |
| **Status** | Transcribed, corrected, labelled from content; one reading pass, no second engine; audio master held on the archive NAS |

This is a **talk, not an interview** — Ann speaks throughout, with the children answering questions in
the style of a class — until the needlepoint demonstration at the end, where a second woman's voice
takes part and the recording becomes an overlapping conversation.

---

## 1. How the date is established

**The tape dates itself**, in the first line of the recording:

> "Today is November the 6th, 1977. We mark this as the 201st birthday of Bethel and Lebanon churches."

It is not a copyist's slate but the speaker's own opening statement, and it is internally consistent:
she gives the founding as **5 November 1776**, and 1776 + 201 = 1977. **6 November 1977 was a Sunday**,
which fits a Sunday-school class.

"Bethel and Lebanon churches" is corroborated in the church's own history: the Eastern Division was
renamed Lebanon and the Western Division Bethel between October 1785 and April 1786.

Two other dates in the material are **not** the recording date: **2026-10-18** is when the file was
added to the archive (its mtime is 2026-10-18 16:48 EDT, which the source notes also record), and the
filed document's header reads "digitised 2026-10-19", which the notes elsewhere treat as the
transcription date. **The two digitisation dates in the source are not reconciled**; `metadata.json`
records 2026-10-18, the file's own timestamp, and says so.

## 2. The physical recording and its capture

| | |
|---|---|
| Master file | `Ann Connor - History of Bethel Needlepoint.m4a` |
| Format | ALAC 48 kHz stereo 16-bit (lossless) |
| Duration | 2,675.797333 s (44 m 35.8 s) |
| Size | 78,391,869 bytes |
| sha256 | `fce6464dbd8cfaa4cbdcc77a5f539def0bbadb08b230bb1a6aef6ada4ecc190f` |
| md5 | `283850bb88ac5c5723f5ea7da5091e9c` — computed here; the source notes give no md5 to compare against |
| Mean level | −40.7 dBFS |
| Peak | −3.3 dBFS (a handling bump at about 34:00) |
| Bit rate | 234 kbps |

Duration, format, sample rate, channel count, size, sha256, md5, mean level and peak were measured on
the master for this record. The level figures agree with the source notes exactly.

**It is the quietest master in this set** — −40.7 dBFS mean, 17 dB below the 1983 panel beside it.
The source notes record that it is uneven: 60-second block peaks run from −22.4 dBFS to −3.3, the
latter at a bump on the microphone or table around 34:00. The archive's listening MP3 carries gain and
a limiter; the master does not.

**Stereo.** The source JSON records the channels as a **delayed duplicate**: ch0 −40.5 dB RMS against
ch1 −40.9, correlation 0.92 at zero lag rising to **0.978 at a constant −3-sample lag** (0.0625 ms).
The working copy was summed with the offset compensated, `(c0[:-3] + c1[3:]) / 2`, discarding no
channel. That measurement was made during transcription and is reported from the JSON; it was **not**
re-measured for this package.

**No denoise.** The JSON records energy above 8 kHz at 0.002–0.08 % of the total (3–8 kHz at 0.2–1.2 %),
which is codec and deck roll-off rather than hiss, so gain only was applied to the working copy.

**The tail is silence.** The last ~2 m 50 s (41:45–44:36) measures −57 to −85 dBFS with no speech.

## 3. What was done to it (the method, as the source notes record it)

1. **Chunked, never whole-file.** 23 chunks of ~120 s, each boundary snapped to the quietest 10 ms
   point within ±5 s.
2. **Seeded prompt**, corroborated nouns only: Reiter, Croco, Wycoff, Karla Strobl, Coverdale mission,
   McMillan, John Clark, George Marshall, Bethel Academy, Mingo Creek, Chartiers, Canonsburg,
   Doddridge, Oliver Miller Homestead.
3. **Prompt-leak check, and repair.** Four windows came back as echoed seed text over real speech
   (11:40–12:42, 25:48–26:42, 27:48–28:32, 35:55–36:25). Each was re-transcribed with **no** prompt and
   spliced back; the 35:55–36:25 span was partly unrecoverable and is marked `[unclear]` where no pass
   resolved it. The final text contains none of the seed list.
4. **Hallucinations over silence removed.** Six "Thank you" segments in the silent tail were verified
   against −57 to −85 dBFS room tone and dropped, with the measurement recorded in the JSON.
5. **Corrected by sense.** 47 `post_edits` entries in the source JSON, each naming the raw form, the
   replacement, the reason and the certainty. The 31 substantive ones are tabulated in the source
   notes.

## 4. The engine, and what it measured

| | |
|---|---|
| Engine | Whisper **large-v3**, Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads |
| Decoding | `en`, `beam_size=5`, `condition_on_previous_text=False`, `compression_ratio_threshold=2.4`, `vad_filter=False`, word timestamps |
| Segments | 415 (342 timed cues) |
| Words | 5,890 in the filed transcript (the source JSON counts 5,922 at the segment level — a counting-method difference) |
| Mean per-word probability | **0.918** |
| Words below 0.5 | 5.3 % |

None of the 30-second windows averaged below 0.68. Only **one** engine was run: no second-engine
cross-check, no WER figure.

The weak stretches are the two-voice, off-microphone lace conversation from 35:55 to 41:45, which is
also where the labels become least certain.

## 5. Corrections (47 `post_edits` entries, all reversible)

The substantive ones — this transcript needed sense corrections as much as name corrections, because
the subject is domestic craft:

| heard | changed to | basis | certainty |
|---|---|---|---|
| "John MacMillan" | John McMillan | the same sentence spells it McMillan | certain |
| "corn needle mush" | cornmeal mush | food list; "needle" has no sense | certain |
| "pull the house down" | pull the **husk** down | husking Indian corn | certain |
| "decorate the homestay" | homestead | misheard | certain |
| "screw some of that mint" | **strew** some of that mint | mint strewn on the floor | certain |
| "the indent hanging" | the **Indian** hanging | the corn-husk Indian doll | certain |
| "the Fidball family" | the **Tidball** family | Mary Tidball Miller, Oliver Miller's wife | certain |
| "lauren wilder" | **Laura** Wilder | Laura Ingalls Wilder | certain |
| "Cornelius Wycock" | Cornelius **Wycoff** | fourth pastor, Dr C. W. Wycoff (1951 history) | certain |
| "Reverend Ryder" | Reverend **Reiter** | Rev. Murray C. Reiter, fifth minister | certain |
| "Throbel", "Carla" | **Karla Strobl** | Presbyterial missionary at Coverdale | certain |
| "Cogardale" (×2) | **Coverdale** | the Coverdale mission | certain |
| "Preston Wolf" (×4) | Preston **Wolfe** | Columbus author of *History of the Wolfe Family* (1936) | certain |
| "any teeth in the building" | any **heat** in the building | the next line is foot warmers | certain |
| "be wiggling on a figure" | **whittling** on a figure | whittling | certain |
| "the Lynn Peter" | the **Indian Peter** | she has just named him Indian Peter | probable |
| "a little brief like this" | a little **braid** like this | the braided corn-husk mat | probable |
| "a corner theme that I made" | a **corner scene** | the piece she made | probable |
| "a much layered chair" | a much-**loved** chair | sense | probable |
| "Peter's Township / Peter's Creek" | **Peters** Township / **Peters** Creek | place names | certain |
| "all over cromwell" | all over **Oliver Cromwell** | name | certain |

Mechanical work alongside: stutters collapsed ("visitors visitors", "the the"), month names and
proper nouns capitalised, a stray "Thanks." and a duplicated "ourselves" at a chunk seam removed.
Hesitations and false starts were left as spoken.

## 6. Left as heard — the honest gaps

- **"And Chuck is a Bavakian."** (29:20) — almost certainly a remark about Karla Strobl's nationality
  ("Czech… she's a Bohemian", Prague-born), but the words do not support a safe rewrite. The filed
  document's provenance note says "Czechoslovakian (not Bohemian, per the family)" — that is the
  family's correction of the historical fact, not of what the tape says.
- **"he may not have made his performance"** (18:26) — a boy's playthings; sense unrecoverable.
- **"it's like an operating thing"** (21:35) — the communion token, described for children.
- **"so you had to Here, before the elders"** (22:06) — a verb is missing; not guessed.
- **Lace terms that could not be corroborated**: "the jabotnik" (33:25), "father plates", "learned
  washing". Left as heard.
- **35:55–41:45, the needlepoint conversation** — two women working lace, overlapping, off-mic. Parts
  are intelligible ("two stitches and a picot"), parts are not; one 16-second span is marked
  `[unclear - overlapping conversation]`. **Treat this stretch as indicative, not quotable.**
- **The speaker labels are inferred, not diarized.** No diarization was run: `ANN`, `INTERVIEWER` and
  `CHILD` come from content, and mixed-speaker segments are left on Ann's line. Where two adults
  overlap at the end, the attribution is a guess.
- **The surname is not on the tape.** "Ann Connor" is family/archive attribution; the Oliver Miller
  Homestead Associates' published history names her as Anna (Thomas) Connor, which is consistent with
  the content but is not something the recording says.
- **The head of the tape may be clipped.** The talk opens mid-programme ("Today is November the 6th,
  1977…") with no introduction of the speaker; whether anything preceded it is unknown.
- **Two dates for digitisation** in the source, unreconciled (§1).
- **Rights.** Public-domain status rests on the collection-level release in `docs/RIGHTS.md`; no
  per-item release document is in the source folder.
- **Not re-measured here:** the stereo lag/correlation, the 60-second block sweep and the MP3's
  loudness — quoted from the source JSON and notes.

## 7. What is on the tape — outline with timestamps

- **0:09** "Today is November the 6th, 1977… the 201st birthday of Bethel and Lebanon churches";
  visitors — descendants of Mary Miller — coming to the homestead that day
- **1:27** **5 November 1776**: John McMillan arrives, stops at **Oliver Miller**'s; the Millers, ten
  children, the youngest **Mary**
- **2:41** The scene she made of McMillan's arrival; the horse, the black cape
- **3:05** McMillan's **saddlebags**; what he carried — Bible, ink pen, **journal**; the journal entry
  for 5 November 1776 at Peters Creek, five children baptised (3:48)
- **4:43** Pioneer sharing, and the food for that day: oat cakes, cornmeal mush, **corn dodgers** (5:15)
- **5:47** **Preston Wolfe** of Columbus, Ohio, descendant of Mary Miller; the book he wrote and the jug
  brought from Northern Ireland
- **7:56** The costume she will wear — long shift, short gown, apron, bonnet
- **8:25** The **bicentennial quilt**, the two Marys on the windowsill (9:08), Oliver Miller's will
- **9:59** The Christmas decorations they will make next week
- **10:10** The Depression, making rather than buying, and why the items are given away
- **11:49** "What is a sample?" — a child answers
- **12:13** Visitors from Japan, Germany and France
- **13:26** The **red ear of corn** and Delaware Indian luck
- **13:41** The **corn-husk broom**, the dirt floor, the border marked in the dirt, the **mint strewn**
  at the door
- **15:29** **Indian Peter** — the Christian Indian who warned the settlers; the family he stayed with;
  **Peters Township** and **Peters Creek** named for him (17:30)
- **18:29** Boys' toys and **whittling**; the Heritage Day wood carver, 11 December (18:43)
- **19:27** The **braided corn-husk** mat, rugs, baskets, hats
- **20:12** **Laura Ingalls Wilder**, and why the books are not just girls' stories
- **21:32** The **communion token** — who could take communion, and the token struck for the 200th
  anniversary
- **23:47** Signing a sheet to welcome Preston Wolfe
- **24:46** The portrait of the fourth pastor, **Cornelius Wycoff**
- **25:37** The first log church, the land bought from **Nathan Couch** for $5, **Fort Couch Road**
- **26:13** The **handbell** rung for the tape; no heat, so the **foot warmer** (27:19) and the split-log
  bench
- **28:24** **John Clark**'s pulpit chair — the oldest furniture they have
- **28:58** **Karla Strobl**, who came from Czechoslovakia in the 1920s for the **Coverdale** mission
- **29:28** **Reverend Marshall**'s chair and desk — schoolmaster and third pastor; **Bethel Academy**
  (29:42), the forerunner of the local high school; the **Marshall Corner** (30:05)
- **32:29** The lace: a pattern said to be Oliver Cromwell's baby clothes; the **Swedish wedding crown**
  (32:43)
- **35:52** Two stitches and a **picot** — the demonstration proper, two voices overlapping
- **41:45–44:36** Room tone; the tape was left running

## 8. Files here

| file | what it is |
|---|---|
| `transcript-a.md` | The transcript: labelled, corrected, readable. **Start here.** |
| `transcript-a.srt` | The same text as timed cues (342), for playback or captioning |
| `notes-a.md` | The archive's working notes: measurements, engine settings, leak repair, every judgement call |
| `metadata.json` | The record of record: date and its source, speakers, master with sha256, rights |
| `checksums.sha256` | sha256 of every file in this folder, checked by `bin/check.py` |
| `README.md` | This file |

`transcript-a.md`, `transcript-a.srt` and `notes-a.md` are **byte-for-byte copies** of the archive's
files of the same stem, taken on 2026-10-23. Nothing was edited for this repository; the "Side A"
label in `metadata.json` names the single file, not a cassette side.

The audio master is **not** here (see `docs/AUDIO.md`): it is held on the archive NAS, identified
above by sha256. The archive's 41 m 17 s MP3 is a listening copy with the silent tail removed; it is
not the master and is not used for this transcript.

## 9. Citing it

> Connor, Ann. *The 201st anniversary: Bethel needlepoint and the Miller homestead*. Talk for the
> Sunday school, Bethel Presbyterian Church, 6 November 1977. Historical Room, Bethel Presbyterian
> Church: digitised 18 October 2026. Transcript, 5,890 words.

Cite the timestamp for anything quoted. Two cautions: the surname is not spoken on the tape, and the
last six minutes are an overlapping conversation whose speaker labels are inferred.

## 10. Reproducing this transcript

- model: large-v3, CTranslate2 **int8**, language `en`, **beam 5**, 14 threads
- `--chunk-seconds 120`, snapped to quiet points: **23 chunks**
- seed: the archive's corroborated name list, with a leak check and four un-prompted splices
- input: the lag-compensated channel sum described in §2 — not the raw stereo master

A re-run on the same master, engine and settings reproduces the raw ASR text; the filed text differs
from it by the 47 `post_edits` in the source JSON, each revertible in one line.

## 11. Related material in the collection

- **`1983-09-25-ann-connor-john-mcmillan`** — the same speaker six years later, giving the formal
  lecture on McMillan.
- **`1983-09-25-valentine-maits-snowden`** — the 1983 panel, where **Miller Maits** speaks about the
  same Oliver Miller homestead these decorations were made for.
- **`1971-07-15-ad-white-cross-creek`** — A.D. White on the Miller family, the still at the Stone
  Manse and the Whiskey Rebellion.
