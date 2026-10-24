# Ann Connor — "History of Bethel needlepoint" — transcription record (2026-10-19)

Source: `Ann Connor - History of Bethel Needlepoint.m4a`, 78,391,869 B, added 2026-10-18 16:48.
ALAC 16-bit 48 kHz **stereo**, 2675.797 s (44:35.8). Mean level −40.7 dBFS, peak −3.3 dBFS;
60 s block sweep peaks −3.3 (at 34:00, a handling bump) to −22.4.

## Dating — the tape dates itself: 6 November 1977

First line: *"Today is November the 6th, 1977. We mark this as the 201st birthday of Bethel and
Lebanon churches."* 1776 + 201 = 1977. The A/B cassettes in this folder are c. 2001; **this
recording is not** — it is 26 years older, a Sunday-school talk given the day after the 201st
anniversary, with a needlepoint demonstration afterwards. `2026-10-18` is the digitisation date.
"Bethel and Lebanon churches" is corroborated: Bethel's own history records the Eastern Division
being renamed Lebanon and the Western Division Bethel between Oct 1785 and Apr 1786.

## Speaker

Labelled **ANN** per the family. The tape never states her name. The Oliver Miller Homestead
Associates' published history names her as **Anna (Thomas) Connor**, the teacher who asked to use
the old stone house and later built Bethel's historical room — consistent with the content here
(she describes her husband John, her years as a history teacher, and the homestead's volunteer
group). Surname and given name are family/history-supplied, not spoken.

## Processing

- **Stereo:** ch0 −40.5 dB RMS, ch1 −40.9 dB (0.4 dB apart); correlation 0.92 raw, **0.978 at a
  constant −3-sample lag** (0.0625 ms). A delayed duplicate, not two different feeds → summed with
  the offset compensated: `(c0[:-3] + c1[3:]) / 2`. No channel discarded.
- **No denoise.** Energy above 8 kHz measured 0.002–0.08 % (codec/deck roll-off, no hiss); 3–8 kHz
  0.2–1.2 %. Lossless capture, so gain only — no filter chain was applied before transcription.
- **Whisper large-v3** (Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads), language
  `en`, beam 5, `condition_on_previous_text=False`, `compression_ratio_threshold=2.4`, word
  timestamps, 23 chunks of ~120 s with boundaries snapped to the quietest 10 ms point within ±5 s.
- Seeded prompt (corroborated nouns only): Reiter, Croco, Wycoff, Karla Strobl, Coverdale mission,
  McMillan, John Clark, George Marshall, Bethel Academy, Mingo Creek, Chartiers, Canonsburg,
  Doddridge, Oliver Miller Homestead.
- **Quality:** 415 segments, 5,925 words, mean word probability **0.918**, **5.3 %** of words below
  0.5. No 30 s window averaged below 0.68.

## Prompt leak — repaired, not deleted

Four windows came back as echoed seed text over real speech (11:40–12:42, 25:48–26:42,
27:48–28:32, 35:55–36:25). Each was re-transcribed with **no** prompt and spliced back; the
35:55–36:25 span was partly unrecoverable and is marked `[unclear]` where no pass resolved it.
The final text contains **zero** occurrences of "Names and places", "oral history recording at
Bethel" or any seed list.

The last ~2 min 50 s (41:45–44:36) is room tone at −57 to −85 dB with no speech; six Whisper
"Thank you" segments there were hallucinations over verified silence and were **removed**, with the
measurement recorded in the JSON.

## Words corrected by sense (all are in the JSON `post_edits`)

| # | as transcribed | corrected | why | certainty |
|---|---|---|---|---|
| 1 | "John **MacMillan**" | John **McMillan** | same sentence spells it McMillan | certain |
| 2 | "corn **needle** mush" | **cornmeal** mush | food list; "needle" has no sense | certain |
| 3 | "if you found **in all**" | if you found **one at all** | sense | probable |
| 4 | "when you pull the **house** down" | pull the **husk** down | husking Indian corn | certain |
| 5 | "decorate the **homestay**" | **homestead** | misheard | certain |
| 6 | "she would **screw** some of that mint" | **strew** some of that mint | mint strewn on the floor | certain |
| 7 | "the **indent** hanging" | the **Indian** hanging | the corn-husk Indian doll | certain |
| 8 | "the **Fidball** family" | the **Tidball** family | Mary **Tidball** Miller, Oliver Miller's wife (OMHA) | certain |
| 9 | "**lauren wilder**" | **Laura Wilder** | Laura Ingalls Wilder | certain |
| 10 | "you better **pride** them" | **prize** them | sense: value them | certain |
| 11 | "**Cornelius Wycock**" | Cornelius **Wycoff** | fourth pastor, Dr C. W. Wycoff (1951 history) | certain |
| 12 | "**Reverend Ryder**" | Reverend **Reiter** | Rev. Murray C. Reiter, fifth minister | certain |
| 13 | "**Throbel**" / "**Carla**" | **Karla Strobl** | Presbyterial missionary at Coverdale | certain |
| 14 | "**Cogardale**" (×2) | **Coverdale** | Coverdale mission, Bethel | certain |
| 15 | "**Preston Wolf**" (×4) | **Preston Wolfe** | Columbus author of *History of the Wolfe Family* (1936) | certain |
| 16 | "any **teeth** in the building" | any **heat** in the building | next line is foot warmers | certain |
| 17 | "be **wiggling** on a figure" | be **whittling** on a figure | whittling | certain |
| 18 | "our **rip** carver" | our **wood** carver | the Heritage Day carver | probable |
| 19 | "**in** heritage day" | **at** Heritage Day | preposition | probable |
| 20 | "a little **brief** like this" | a little **braid** like this | braided corn-husk mat | probable |
| 21 | "forerunner of a high school **trip**" | of a high school | "trip" spurious | probable |
| 22 | "the **Lynn Peter**" | the **Indian Peter** | she has just named him Indian Peter | probable |
| 23 | "That's a much **layered** chair" | much-**loved** chair | sense | probable |
| 24 | "all over **cromwell**" | all over **Oliver Cromwell** | name | certain |
| 25 | "**Peter's** Township / **Peter's** Creek" | **Peters** Township / **Peters** Creek | place names | certain |
| 26 | "a **corner theme** that I made" | a **corner scene** that I made | the piece she made | probable |
| 27 | "**You're learning two** back there" | learning **too**, back there | homophone | certain |
| 28 | "going to **be represent**" | going to represent | spurious "be" | certain |
| 29 | "**so I do** you think Preston Wolfe" | So do you think | spurious "I" | certain |
| 30 | "and you know **would that** you remember" | And you know what? Do you remember | garbled question | probable |
| 31 | "**Peter and** instead of killing" | And instead of killing | repeated name at a restart | probable |

Mechanical: stutters collapsed ("visitors visitors", "the the", "it it"); sentence starts,
"October/November/December", "Columbus", "Ohio", "Northern Ireland", "Bedford", "Swedish",
"Indians", "Oliver/Mary/Millers" capitalised; a stray "Thanks." and a duplicated "ourselves" at a
chunk seam removed. Hesitations and false starts left as spoken.

## Left as heard / unresolved (not guessed)

- **"And Chuck is a Bavakian."** (29:20) — almost certainly a remark about Karla Strobl's
  nationality ("Czech… she's a Bohemian", Prague-born) but the words do not support a safe rewrite.
- **"he may not have made his performance"** (18:26) — a boy's playthings; sense unrecoverable.
- **"it's like an operating thing"** (21:35) — the communion token described by a child or Ann.
- **"so you had to Here, before the elders"** (22:06) — a verb is missing; not guessed.
- **"the jabotnik?"** (33:25), **"learn to make father plates"**, **"learned washing"** — lace terms
  I could not corroborate; left as heard.
- **35:55–41:45 needlepoint conversation** — two women working lace, overlapping, off-mic. Parts are
  intelligible ("two stitches and a picot"), parts are not; one 16 s span is marked
  `[unclear - overlapping conversation]`. Treat this stretch as indicative, not quotable.
- **"Nathan Couch"** is correct as transcribed (Nathan Couch, St Clair/Peters Township, land patent
  1786–1788; Fort Couch Road is named for the family).

## Condensation — `Ann Connor - History of Bethel Needlepoint.mp3`

- `silencedetect noise=-55dB:d=1.5` (speech RMS on this capture sits near −44 dB; pauses fall to
  −55…−60 dB). Every gap ≥ 1.5 s shortened to **0.4 s**, keeping 0.2 s each side.
- 48 gaps detected; **14 left untouched** because a transcribed word ran into them (a breath or a
  word tail — cutting there would clip speech). They are listed in the JSON/log.
- 2,675.7 s → **2,476.7 s**, **199.0 s removed (7.4 %)**.
- **Be clear about what that 7.4 % is:** 170.1 s is the silent tail after she stops speaking, and
  28.9 s is one quiet stretch around 30:30–31:12. The conversation itself contains almost no long
  pauses — **~1.1 % of the talk proper was trimmed**, so this is not really a condensed edit of the
  interview; it is the full talk with the dead tail removed.
- Checked: 0 transcribed words overlap any cut; tightest cut-to-word margin 0.48 s; speech-frame
  share 52.5 % → 56.4 % (nothing was lost). Joins at 05:34 and 26:38 re-transcribed cleanly with the
  words either side intact.
- MP3 mono 64 kbps 48 kHz, 19,813,868 B, 41:16.7 — the same profile as `mp3 for transfer/`.
