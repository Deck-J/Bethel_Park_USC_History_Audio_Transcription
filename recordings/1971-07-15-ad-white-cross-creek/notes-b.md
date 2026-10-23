# Alvin Dinsmore White — Cross Creek records and the Whiskey Rebellion — Side B — transcription record

Recording stem: `Alvin Dinsmore White - Cross Creek Records and the Whiskey Rebellion (15 July 1971)`.
This note covers **Side B** only; Side A's documents are still pending (see "Status" at the end).

## What this is

**Side B of the A.D. White interview, 20 m 15 s of speech** (the capture is 1 h 35 m 22 s; see
"Cropping" — the rest is dead tape). It is the tail of the same conversation whose Side A opens:

> "The interview which follows was recorded on July the 15th, a Thursday evening, 1971, at Hickory,
> Pennsylvania, and is a record of the interview of Mr. A.D. White and his wife by Ann Conner and
> John Conner." (Side A, 0:10–0:30 — a narrator's slate added when the tape was copied)

**The date is carried over from Side A's slate**, not stated on Side B. 15 July 1971 was a Thursday,
which is what makes the slate credible.

Content, in order: how the county history volume was compiled and what was left out; the *Custer —
hero or butcher* magazine piece and how attitudes change ("history is always changing and being
rediscovered"); books seen in the Pennsylvania room of the Carnegie Library; a swap that brought the
Washington County atlas into the collection; a wish list for the Historical Room — the **Latimer** and
**Sam Green** histories, "both of those books mention Reverend Clark and his part in the Whiskey
Rebellion"; the Latimer copy that disappeared and the one a minister at Mount Prospect Church handed
over; then a long stretch on the **Jones** family and elders, ending in family chatter ("if you're
going to serve these people some ice cream cake").

## Cropping — 75 minutes of the capture is dead tape

The 56 MB capture is **5,721.69 s**. Most of it is not a recording:

| window | 10 s mean / peak | reading |
|---|---|---|
| 0:00 – 19:00 | −22 to −28 dB / −2 to −9 dB | speech |
| 20:10 – 20:13 | −22.8 dB / −2.7 dB | speech continues to the last word |
| **20:13.5** | last audio (max −24.5 dB at 20:13, −53.8 dB at 20:14) | **speech ends** |
| 20:20 – 1:35:22 | −76 to −91 dB mean, −43 to −51 dB peaks | tape hiss floor |

Every 60 s block after 20:60 was measured: **none exceeds −45 dB mean**, i.e. there is no buried
speech, no second session and nothing after the tail. Crop = **0 – 1,215 s** (a 1.5 s pad after the
last word). **Removed: 4,506.7 s (1 h 15 m 07 s) = 78.8 % of the file.** The original `Side B.m4a`
is kept untouched (md5 `3a61e43d4b270826c1a48fc88ffa6cfb`); the crop is a derivative.

## Audio and processing

- Source: ALAC, 48 kHz, stereo, 16-bit, 78 kbps, 5,721.69 s, mean −31.1 dBFS, peak −1.9 dBFS.
- Cropped master: `… - Side B (cropped 20m15s).m4a` — ALAC stream copy, 1,215.06 s, peak unchanged.
- Stereo pair: **delayed duplicate** — 2.57 dB apart (ch1 hotter), r = 0.955–0.996 at a **constant
  −2-sample lag** (16 kHz; 6 samples at 48 kHz). Handled the same way as Side A: ch0 delayed 6 samples,
  then summed 0.5/0.5. Measured on the summed mono: mean −24.5 dBFS, peak −3.0 dB.
- **No gain applied** (the level is in the archive's band, unlike the 1971 George Marshall tape) and
  **no denoise** — the source is lossless.
- Portable copy: `… - Side B (portable).mp3`, mono 64 kbps, full 20:15 — nothing speech-bearing cut.

## Two engines, both run on this side

Both used the same 11 chunk boundaries (quiet-point snapped, 120 s) and the same seeded prompt
(the archive's standing name list).

| | CPU — faster-whisper large-v3 int8, beam 5 | GPU — openvino-genai large-v3 int8, greedy |
|---|---|---|
| words | 2,570 | 2,598 |
| mean word probability | **0.8789** (8.05 % below 0.5) | n/a — this engine reports none |
| wall-clock | 470 s (**2.6× realtime**) | **140 s (8.7× realtime)** |
| word timings | yes (per word, with probability) | yes (per word, no probability) |
| agreement | reference | **WER 0.1128 vs CPU** (88.7 % word agreement) |

**Word-timing check**: 2,383 of the 2,570 CPU words matched a GPU word; start-time difference
**median 0.000 s, p75 0.020 s, p90 0.140 s** — the GPU timings are as good as the CPU engine's.
The residual WER is real text divergence (names, book titles, the messy opening), not a timing
artefact.

**Which one is filed**: the CPU transcript (`… - Side B.txt/.srt/.json`), because it carries per-word
probabilities and is the same engine as Side A. The GPU run is validation: it proves the Arc can
produce an archive-shaped transcript with word timings, 3.4× faster.

## Document set (built after the transcript)

`… - Side B.txt` is the labelled transcript (WHITE / INTERVIEWER / UNKNOWN), and the `.docx` and `.md`
are built from it with `make_docx.py` and `make_md.py` — identical arguments, then checked:
`verify_md_docx.py --dir .` reports **MATCH** (85 paragraphs, 2,641 words, 87 label runs).
`reconcile_md_json.py` reports DRIFT for **three words** ("at", "happened", "if") that come from
joining run-on ASR fragments — a merge, which no `post_edit` can express. Ten proper-name and title
corrections are recorded as `post_edits` in the JSON (Caldwell's Atlas, Latimer, Sam Green, Reverend
Clark, Whiskey Rebellion, Gilfillan, Hill Church, James Espy Jr., the Custer headline, "twenty").

## Files in this folder

| file | what it is |
|---|---|
| `Side A.m4a`, `Side B.m4a` | the captures exactly as received (untouched) |
| `… - Side B (cropped 20m15s).m4a` | lossless crop of Side B, 0–1,215 s |
| `… - Side B.txt / .srt / .json` | CPU transcript (speaker labels not yet applied) |
| `… - Side B (portable).mp3` | mono 64 kbps listening copy |

## Open items

- **Speaker labels are not applied yet.** Side B is White and Ann Connor (with the wife and others in
  the closing exchange); the labels need a read-through against the audio, the same pass Side A is
  waiting on.
- **Unresolved names**: `Latimer` (a county history; also heard as "the Latimers"), `Sam Green`
  (probably the county history author), `William Jones` / `William Jones Jr.`, "the Colorado Atlas of
  Washington County" (almost certainly **Caldwell's Atlas of Washington County**, 1876 — *unconfirmed*),
  and the *Custer* magazine article (title not stated).
- **Side A status**: transcribed on both engines (CPU 3,833 words / mean_p 0.9086; GPU 9.1× realtime,
  WER 0.0634) with nine cold passes over the garbled stretches; the corrected text, labels, `.docx`/
  `.md`, NOTES and the README index entry are **not yet built**.
