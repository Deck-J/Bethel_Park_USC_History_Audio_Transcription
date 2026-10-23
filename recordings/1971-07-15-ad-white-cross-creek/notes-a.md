# Alvin Dinsmore White — Cross Creek records and the Whiskey Rebellion — Side A — transcription record

Recording stem: `Alvin Dinsmore White - Cross Creek Records and the Whiskey Rebellion (15 July 1971)`.
Companion note: `NOTES - … - Side B.md`.

## What this is

**31 m 12 s** (1,872.0 s) of an interview recorded **15 July 1971 at Hickory, Pennsylvania** — the
slate at the head of the tape says so, and 15 July 1971 was a Thursday:

> "…a record of the interview of Mr. A.D. White and his wife by Ann Conner and John Conner."
> (0:10–0:30, a narrator's slate added when the tape was copied — labelled `NARRATOR`, not a voice
> in the room)

**A.D. White is Alvin Dinsmore White of Hickory**, who lectured in this same series on 31 October 1971
on *Cross Creek and the Dinsmore family* (already in the archive). This is the informal interview
behind that lecture: he brings his own books and notes and reads from them.

Content, in order: the old library books and whether Canonsburg's were taken to W&J College; the
**William Vance case** — married his deceased wife's sister, deprived of communion at Cross Creek,
appealed to the General Assembly in 1821 and again in 1822 and lost both times; communion-season
customs and the guest-minister rotation (Stockton at Cross Creek, Marshall at Bethel, Clark and
McMillan); Jimmy Simpson's three-line diary and the elders holding "society" when the minister was
away; the records of Cross Creek and the merged congregation's refusal to allow any historical
observance; Cross Creek Academy and its teachers; George Marshall's obituaries and Board of Missions
service; then his books — Hugh Lee of Cross Creek, Simpson's annotated centennial volume, the academy
building (1858), and **George Marshall's letter of 27 July 1863** to General James Lee about the death
of Henry Graham, read onto the tape in full, with its postscript about raids and the draft (Morgan's
Raid); and finally the **Whiskey Rebellion**: Oliver Miller, mortally wounded at General Neville's on
16 July 1794, his widow, William Miller the distiller who disappeared, and the still kept at the
**Stone Manse** until the park took it over and Mrs Maits took it from there.

## Dating — 15 July 1971, from the tape

- The slate gives "July the 15th, a Thursday evening, 1971"; 15 July 1971 **was** a Thursday.
- Nothing on the tape contradicts it. Side B carries no date of its own and is dated from this slate.
- `2026-10-18` in the archive folder name is the **digitisation** date, not the recording date.

## Audio and processing

- Source: `Source original/Side A.m4a` — ALAC, 48 kHz, stereo, 16-bit, 355 kbps, 1,872.04 s,
  mean −23.5 dBFS, peak −1.2 dBFS, md5 `7494fde23b36fb686982332a1432efe7`.
- Level is even across the whole side (−21.6 to −25.7 dB mean per minute); no gain applied, **no
  denoise** — the source is lossless.
- Stereo pair: **delayed duplicate** — 2.5–3.2 dB apart (ch1 hotter), r = 0.987–0.992 at a constant
  −2-sample lag (16 kHz; 6 at 48 kHz). The working copy for both engines was ch0 delayed 6 samples and
  summed 0.5/0.5, so both engines saw identical samples.
- The last ~50 s is the tape running down; there is no speech after 30:55.

## Engines — both ran this side

Same 17 chunk boundaries (quiet-point snapped, 120 s) and the same seeded prompt (the archive's
standing name list).

| | CPU — faster-whisper large-v3 int8, beam 5 | GPU — openvino-genai large-v3 int8, greedy |
|---|---|---|
| words | 3,833 | 3,824 |
| mean word probability | **0.9093** (5.5 % below 0.5) | n/a — not reported |
| wall-clock | 1,140 s (1.6× realtime) | 205 s (**9.1× realtime**) |
| agreement | reference | WER **0.0634** (93.7 % word agreement) |

The filed transcript is the CPU one. The GPU run exists as the cross-check and as the engine's
validation (see `whisper-worker/docs/GPU.md`).

**Nine un-prompted cold passes** were run over the stretches that the first pass garbled (0:18–0:42,
3:45–5:20, 6:23–6:45, 21:12–21:40, 21:55–22:31, 24:36–25:02, 28:10–28:32, 28:46–29:08). They settled
"they claim, in fact, that it was an incestuous marriage" (not "I claim … I was incestuous married")
and "the grave is not marked" (not "grade"), and confirmed that the "station at Crosby" reading is
what the tape actually says, twice, in all three passes — left as heard.

## Labels

`WHITE` (the subject), `INTERVIEWER` (Ann Connor and John Connor — the tape does not identify which of
them speaks each question, so the label is shared rather than guessed), `NARRATOR` (the copyist's
slate at the head only). The letter is read by White and is marked `[reading]`; stage marks are not
attributed to anyone.

## Corrections applied (all recorded in the JSON `post_edits`)

Canonsburg (from "Cannonsburg"); Stockton (from "Stockman"/"Stockley"); Cross Creek Academy (from
"Craftsman Academy"/"Cross-Crick's"); **1858** for the academy building (the ASR said 1958, which is
anachronistic — Marshall died in 1868); **Morgan, the Raider** (from "Borgon"; Morgan's Raid, July
1863); "the grave was not marked" (from "grade"); Mrs. **Maits** (from "mates"); the **Stone Manse**
(from "stone man's"); George **Marshall** as the letter's signer (the ASR split it into "George
Martin. Marshall. Marshall, partner."); "at Cross Creek" for Henry Graham's burial (from "in standard
cross"); Reverend Marshall in Simpson's note (from "Marvin Marshall"); "impairment of sight" (from
"site"); and the Vance ruling sentence restored from a cold pass.

## Left as heard / unresolved

- **"the station at Crosby"** — three cold passes agree; almost certainly "the session at Cross
  Creek", but the tape says Crosby and it is not corrected.
- **Armand Denny** (Board of Missions president) — spelling not corroborated.
- **"the wind of the panes knocked out"** (1:57) — garbled; no confident reading.
- **"he was taken in the family of Reverend John Clark; die, daddy, kill, alive; twice married"**
  (26:20) — the tape itself is mangled here; left as heard rather than invented.
- **1958 vs 1858** is a judgement call recorded above; if a Cross Creek Academy source says otherwise,
  the post_edit carries the reason and can be reverted.
- **Douglass/Patterson/Connor**: none of these appear on this side; the standing seed is present in the
  JSON as the prompt, not as content.

## Verification

- `make_docx.py` and `make_md.py` with identical arguments; `verify_md_docx.py --dir .` reports
  **MATCH** for both sides (Side A: 100 paragraphs, 3,884 words, 100 label runs).
- `reconcile_md_json.py`: the transcript is the `.txt` rebuilt from the CPU segments, so the only
  residue is **one word** introduced by joining run-on fragments ("has"), which no `post_edit` can
  express because it is a merge, not a substitution. That is the only reason the verdict is DRIFT
  rather than JSON-CONSISTENT; every proper-name change is a recorded `post_edit` (14 of them).
