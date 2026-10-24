# JD Patterson, Side A — transcription record (2026-10-19)

## What this is

Side A of a 1979 cassette interview with **JD Patterson**, recorded in Bethel Park,
Pennsylvania, on **20 April 1979** by **June Ellington**. Patterson was a schoolteacher
for 40-odd years: Taylorstown, Canton Township (West Washington/Wolfdale), Chartiers
Township High School, Wood River and Alda and Shelton in Nebraska, then Peters Township
for 14 years, with two years' leave in West Virginia. The tape is a teaching-career and
local-history interview, not a tour of the historical room — it ranges over the Bethel
school building of 1916-17, its vocational programme, the graduating classes of 1917-21,
Mount Lebanon and Route 19 before it was built up, and the 1930-31 shooting of Bob Stilley.

**Provenance of the identifying facts.** The subject (JD Patterson), the date (20 April
1979) and the interviewer (June Ellington) were **supplied by the archive**, not read off
the tape. The tape supports the subject and the day: it opens "April 20th, and I'm talking
to A.J. Patterson — J.D. Patterson — J.D. Patterson, I'm sorry", the interviewer correcting
her own mishearing. **The tape states no year.** No conflict was found between the supplied
date and anything said on the recording; the 1979 framing is consistent with a man who was
17 in 1921 (b. c. 1904) speaking about a 1930 killing in the past tense.

## Source and measurements

- `JD Patterson Side A.m4a` — ALAC, 48 kHz, 2 ch, 16-bit, 35:56.288 (2,156.288 s),
  mean −25.1 dBFS, peak 0.0 dBFS.
- Level is even across the file: 36 one-minute blocks all peak −2.3 to −4.7 dBFS,
  mean −23 to −26 dBFS. The single 0.0 dB peak at 22:12 is **12 clipped samples**
  (0.25 ms) — a capture click, not saturation.
- Speech runs 00:09.3 – 31:01.8; the final **294.4 s (4 min 54 s) is digital silence**
  (mean −91 dB), i.e. the tape ran on after the interview stopped.

### Stereo measurement and decision

Measured on three 30 s windows (420 s, 900 s, 1300 s):

| | ch0 | ch1 | gap | raw corr | best lag | corr at lag |
|---|---|---|---|---|---|---|
| 420 s | −23.1 dB | −26.1 dB | 3.1 dB | 0.972 | 1 sample (0.021 ms) | 0.990 |
| 900 s | −22.7 dB | −25.8 dB | 3.1 dB | 0.981 | 1 sample | 0.992 |
| 1300 s | −23.3 dB | −26.2 dB | 3.0 dB | 0.985 | 1 sample | 0.992 |

A constant 3.1 dB gap with r = 0.99 at a fixed one-sample lag is the **delayed-duplicate**
case: the same programme on two feeds, not two different signals. So the channels were
**summed with the lag compensated**, weighted 2:1 toward the stronger channel
(`0.6667*L + 0.3333*R`, L delayed 1 sample) — an equal sum would have added the weaker
feed's noise at full weight, and dropping ch1 entirely would have thrown away a
near-perfect second copy.

### Processing chain (gain only, no denoise)

```
channelsplit -> adelay=1S on L -> 0.6667*L + 0.3333*R -> volume=+4.5dB -> alimiter(-1.5 dBFS, level=disabled)
```

Result: **−18.96 LUFS integrated, −1.41 dBTP**, max sample −1.5 dBFS (from −20.74 LUFS).
No denoise: the source is lossless ALAC and the 8 kHz+ band sits 11.6 dB below the speech
band — that is real tape hiss, and filtering it would remove signal the transcriber uses.

## Transcription

- **Whisper large-v3** (Systran faster-whisper, CTranslate2), int8, 14 CPU threads, `en`.
- **16 chunks**, ~2 min, boundaries snapped to the quietest 10 ms frame within ±5 s.
  Never a whole-file pass. `beam_size=5`, `condition_on_previous_text=False`,
  word timestamps, `vad_filter=False`.
- `initial_prompt` seeded with the corroborated names (Bethel, McMillan, Clark, Marshall,
  Wycoff, Reiter, Bethel Academy, Oliver Miller Homestead, Mingo Creek, Canonsburg,
  Chartiers, Dido, Doddridge, Princeton, Croco, Strobl, Coverdale, Ellington, Patterson).
- **Prompt-leak check: clean.** Every seeded token in the output is spoken — the tape
  really does name "J.D. Patterson" at 00:00:14 and "Bethel" / "Chartiers" in context.
  No window needed re-transcribing unprompted.

### Quality

- 449 segments, **4,333 words**, **mean per-word probability 0.9485**,
  **2.98 % of words below 0.5**.
- Weakest stretches (segment mean < 0.80): 11:16–11:21, 18:48–18:54, 30:52–30:58, plus
  scattered single seconds at 00:26, 00:37, 06:11–06:29, 06:51, 07:20–07:43, 09:54,
  14:23–14:27, 16:49–16:54, 19:55, 20:55–20:58, 21:40–21:48, 22:49, 24:38–24:55,
  27:06, 28:50–29:00. None is longer than five seconds; names and numbers account for
  most of the low scores.
- **Read end to end**, all 73 ASR paragraphs → 194 speaker turns.

## Speaker labels

Two voices only. Labels in the source: `JD` and `JUNE`; both passed to the builder
(`--main-speaker JD --secondary JUNE`). Builder report: `JD=119, JUNE=75`; parsed back
out of `document.xml`: `JD=119, JUNE=75`. No third voice.

## Corrections applied (by sense, with reasons)

| # | As transcribed | Corrected | Reason |
|---|---|---|---|
| 1 | "Shartiers" | Chartiers | same school, named correctly two lines earlier |
| 2 | "which has Jesse Holly" | "Wichas, Jesse Holly" | 1919 graduate list — "which has" is the surname Wichas |
| 3 | "Peter's Township", "at Peter's" | Peters Township, at Peters | township name |
| 4 | "Kenton Township" | Canton Township | speaker self-corrects to "Canton Town" in the next breath |
| 5 | "pod", "pld" | POD, PLD | Problems of Democracy, the course abbreviation |
| 6 | "Alder" | Alda | the Nebraska town he names as "Alda" three lines earlier |
| 7 | "elder schools" | Alda schools | same town: "I took charge of the Alda schools" |
| 8 | "castle shannon" | Castle Shannon | borough name |
| 9 | "Silley" | Stilley | same family, spelled Stilley elsewhere in the passage |
| 10 | "work couch", "Fort Couture", "for couch" | Fort Couch | Fort Couch Road at Route 19 |
| 11 | "the ore farm" | the Orr farm | Howard Orr / Roy McEwen are the subject two sentences earlier |
| 12 | "web murray's" | Webb Murray's | spelled "Webb Murray's" later in the same passage |
| 13 | "trotwood" | Trotwood | Trotwood Acres / West / North |
| 14 | "a miller" | a Miller | surname, "one of the McEwen women marry a Miller" |
| 15 | "mine three" | Mine Three | place name (Phillips School at Mine Three) |
| 16 | "mr hildy" | Mr. Hildy | name and title |
| 17 | "eisenhower school" | Eisenhower School | school name |
| 18 | "Married and I think the second marriage" | "and I think in the second marriage" | ASR turned a false start into a sentence |
| 19 | "anna and I" | "Anna, and I" | the girl's name |
| 20 | "Rob Bob Stilley" | "Rob — Bob Stilley" | self-correction, marked with a dash |
| 21 | "No, two. Two." | "No, two." | duplicated token |
| 22 | "she died in 49" | "she died in '49" | elided year |
| 23 | "graduated in 1917 in 1918" | "graduated in 1917. In 1918" | two years run together |

Mechanical, applied and counted: 8 doubled words collapsed (next, from ×2, 1917, and, the;
"had had" protected as past perfect), 18 proper-noun casing fixes, sentence-initial caps,
lone lowercase `i` → `I`. Hesitations and false starts left alone.

**Kept verbatim:** "A.J. Patterson" at the head — the interviewer misspeaks and corrects
herself; that is the recording, and it is how the name is evidenced.

## Unresolved (left as heard, not guessed)

- **"TITSO subjects"** (14:23) — "He just wouldn't bother preparing lesson plans on all the
  TITSO subjects we should have had more work in." Probably a trade/industrial curriculum
  term; no reading is provable.
- **"J-5"** (28:42) — "some of the Walther boys, J-5, Donald McKeown had been in." A name or
  a service designation; unresolved.
- **"Vernon Mullenauer" / "Leo Molinar"** (19:07, 19:12) — the same family written two ways;
  neither spelling corroborated.
- **"Rausch residence"** (24:45) and "Universal, is it? — Unity, Unitarians, Unitarian" —
  the church now occupying the house is heard but not identified.
- **"it's no longer called from from that new part there that the road kept into"** (20:33) —
  garbled clause at the Hayes Avenue/Route 70 description; the sense (the road was cut by
  Route 70) is clear from the surrounding sentences, the wording is not recoverable.
- **"Mitchell corners"**, **"Emerson … Hugh"** (the two older Stilley brothers), and the
  1920 class list — heard, not corroborated.

## Deliverables

| File | What |
|---|---|
| `JD Patterson - Side A.txt` | 194 labelled turns, plain text |
| `JD Patterson - Side A.srt` | 516 cues; speaker label on the first cue of each turn |
| `JD Patterson - Side A.json` | per-word timings/probabilities, stereo + prompt metadata, `post_edits` |
| `JD Patterson - Side A.docx` | built from the .txt, JD blue / JUNE red |
| `JD Patterson - Side A.mp3` | mono 64 kbps 48 kHz, 30:49.9 |

### Condensed copy — measured

Original 35:56.3 → condensed **30:49.9**. Removed **306.3 s (14.2 %)**, of which
**294.4 s is the silent tail**, 8.9 s the silent head, and 3.0 s one internal gap
(168.7–171.4 s). **Speech removed: none** — six of the ten detected silences were left
intact because a cut inside them would have touched a word's span (the transcript's word
boundaries stretch across those pauses).

## Side B

Marked "side A" and 35:56 long — shorter than a C90 side (nominal 45 min), so either a
shorter cassette or the recording was stopped early. Either way **a B side very likely
exists and has not been supplied**; it should be requested rather than assumed lost.
If it arrives, transcribe with the same recipe and offset its timecodes by 2,156.288 s.

## Reproduce

Scratch workspace: `/opt/data/cache/scratch/jdp` (`transcribe.py`, `edits.py`, `final.py`,
`mkjson.py`, `mkmp3.py`). Audio never left the machine.

## Side B arrived — transcribed 2026-10-21

The other side of the cassette was supplied and is filed as `JD Patterson - Side B` with its own NOTES and
FACT-CHECK. It is continuous with this side (it opens mid-question: "What was his first name? Was it
Samuel?"), so the two now exist on one clock in `JD Patterson - Side B/JD Patterson (both sides).srt` —
this side's 516 cues unchanged, Side B's 522 offset by 2,156.288 s, 1,038 cues, monotonic, 313.2 s gap at
the flip (this side's 294.4 s silent tail plus the head of Side B).

What it settles about **this** document:

- **The Fife family is documented**, where Side A only carried the surname: Thompson Fife built the
  William T. Fife house on Old Washington Road in 1832 (his grandfather John Fife, Sr. came from Fifeshire,
  Scotland, in 1766); William T. lived there 1842-1928, and the bronze plaque he mentions is the Pittsburgh
  History & Landmarks plaque awarded in 2016.
- **Espy** is corroborated: Side B has Thomas Espy's Civil War sword, now with J. Walter Phillips — which
  fixes the surname behind this side's low-confidence readings.
- **Hulse Boyer** appears in both sides with the same story (the man who dropped "Hulse" and went by Jim).
- **The tape's owner is not Bethel.** Side B closes with "This is a recording of oral history to be the
  property of Upper St. Clair Historical Society and will only be used by non-profit." Worth knowing before
  the collection is published anywhere.

