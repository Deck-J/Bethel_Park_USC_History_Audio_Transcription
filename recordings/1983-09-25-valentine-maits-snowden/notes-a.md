# Valentine, Maits and Snowden (25 September 1983) — transcription record

Recording stem: `Valentine, Maits and Snowden (25 September 1983)`. Every file in this folder
carries that stem; this note is the working record behind the document.

## What this is

A 25 m 59 s (1,559.98 s) recording of a Historical Room session at Bethel Presbyterian Church,
Bethel Park, Pennsylvania, held on **25 September 1983**. It is a four-voice meeting, not an
interview: an unnamed moderator introduces each of three older members in turn, reads the
church's history aloud, and hands over to each. **Ruth Valentine** reads her own Sunday-school
certificates (cradle roll 1914, promotion 1917, 1923, 1929); **Miller Maits** — a descendant of
the Oliver Miller family — talks about the Miller homestead and the early roads; **Jean
Snowden** describes the women's organisations, the Ladies Aid Society and the missionary
society, and how the three groups merged in 1945. The moderator closes on the church being
"almost 206 or 207 years" old.

The last ~1 m 40 s is post-meeting chatter away from the microphone (from 24:20).

## Date, and what the date rests on

- **25 September 1983 — supplied by the archive** (John Decker, written `9-25-83` on the
  original capture), not stated anywhere on the tape.
- **Internal corroboration:** the moderator's closing "over 200 years now of history, almost
  206 or 207 years, I guess, this year". Bethel was founded 5 November 1776, so 1776 + 206 =
  1982 and 1776 + 207 = 1983 — consistent with, and mildly corroborative of, the supplied date.
- **Conflict: none.** The tape states no date of its own and nothing in it contradicts
  25 September 1983. The 1983 date is recorded as filename-supplied throughout.

## Speaker attribution and the evidence for it

Four voices were found. The method was dialogue structure first (who is addressed, who answers,
who introduces whom), then cepstral median f0 per block as a check that a label covers one
voice. Pitch was **not** used to name anyone.

| Label | Voice | Evidence | Confidence |
|---|---|---|---|
| `RUTH VALENTINE` | female, median f0 206 Hz | Moderator: "Thank you, Ruth" (06:23), immediately after she stops. She reads her own certificate: "Ruth Elizabeth Douglas … born on the 26th day of December, 1913". | first name certain; **surname not on tape** |
| `MILLER MAITS` | male, median f0 113 Hz — the lowest voice on the tape | Named twice independently: by the moderator ("The next person is Miller Maits … a descendant of the Oliver Miller family", 06:29–06:41) and by Ruth ("Miller Maits back there was [in the Tom Thumb wedding]", 04:46). | high — the only filename surname the tape says aloud |
| `JEAN SNOWDEN` | female, median f0 208 Hz | Moderator at the hand-over: "Jean, why don't you take over and tell us about some of the women's activities" (16:52); referred to again at the close ("As Gene points out", 23:14). ASR renders both "Jean" and "Gene"; the voice is female and the topic is the women's organisations. | first name certain; **surname not on tape** |
| `HOST` | male, median f0 150 Hz (four blocks: 150.0 / 150.9 / 150.9 / 147.2 Hz, sd 14 — one man) | The unnamed moderator. Introduces each speaker, reads the church history, speaks for about a third of the tape. Never names himself. | unnamed; remains unidentified |

**Surname caveat.** `Valentine` and `Snowden` come from the filename only — neither appears in
the audio. Ruth's maiden name, from the certificate she reads, is **Douglas**, so Valentine is a
married name. `MAITS` is the family spelling of a surname the tape pronounces "Mates". The three
filename surnames map onto the three participants in speaking order, which is a filename
inference, not spoken evidence.

**Ruth vs Jean cannot be separated acoustically** — median f0 206 Hz vs 208 Hz, timbre
similarity 0.989, the closest pair on the tape. The split rests entirely on the moderator
addressing each by name at the point she takes the floor, and on their self-descriptions being
incompatible (Ruth's certificates from 1914–1929; Jean a member 33 years with a toddler in 1950).
The moderator (150 Hz) is 45 Hz below both and 37 Hz above Maits, which is what rules him out as
one of the three named speakers.

### The one flagged judgement call — 15:47 to 16:52

The moderator says he will "turn this over to Gene for a few minutes", then speaks for another
minute himself ("In preface, I might say that in 1947, we elected our first woman deacon … Our
Samuel Fife … That's something I have not been aware of"), and only then hands over: "Jean, why
don't you take over." That minute is labelled `HOST` because its pitch is identical to his other
blocks (150.9 Hz, sd 14.0, against 150.0 and 150.9 elsewhere) and 45 Hz below Jean's — but if the
hand-over took effect at 15:51 as announced, those lines are Jean's opening remarks and the label
is wrong. Flagged rather than resolved: the audio cannot separate two speakers at the same pitch.

## Source and measurement

- `Valentine, Maits and Snowden (25 September 1983).m4a` — ALAC, 48 kHz, 2 ch, 16-bit,
  1,559.978667 s, 58,020,991 bytes, md5 `913bdf2b51aa75586d7cd6931b03403f`.
- **Stereo: delayed duplicate.** Measured on nine 30 s windows: a constant 4-sample (0.083 ms)
  lag at r = 0.96–0.996, ch1 2–3 dB stronger through the body of the tape. Summed with the lag
  compensated, weighted 2:1 toward ch1 — an equal-weight sum would have added the weaker feed's
  noise at full weight, and dropping ch0 would have discarded a near-perfect second copy.
- **Processing: gain only, no denoise.** `channelsplit -> ch1 delayed 4 samples ->
  mono = (2*ch1 + 1*ch0)/3 -> gain +3.78 dB`. Result −19.0 dBFS mean, −1.0 dBFS peak. The source
  is band-limited (nothing measurable above 2.4 kHz; the >8 kHz band is 0.0000–0.0001 % of total
  energy), so there is no hiss to filter — only signal to lose.

## Transcription

- Whisper **large-v3** (Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads), `en`.
- **13 chunks** of ~120 s, boundaries snapped to the quietest 10 ms frame within ±5 s of each
  target. Never a whole-file pass. `beam_size=5`, `condition_on_previous_text=False`,
  `temperature=0.0`, `no_speech_threshold=0.6`, `vad_filter=False`, word timestamps.
- Audio decoded by ffmpeg to float32 numpy arrays; PyAV in this build rejects the
  `metadata_errors` kwarg faster-whisper passes, so the array path is used deliberately.
- `initial_prompt` seeded with corroborated names only (Bethel, McMillan, Clark, Woods,
  Marshall, Wycoff, Reiter, Bethel Academy, Oliver Miller Homestead, Mingo Creek, Canonsburg,
  Chartiers, Dido, Doddridge, Princeton Theological Seminary, Croco, Strobl, Coverdale, Tidball,
  Wolfe, Stilley, Webb Murray; Valentine, Maits, Snowden).
- **Prompt-leak check: clean.** `Valentine`, `Maits` and `Snowden` do not occur in the output at
  all. The one seeded name that appears in the opening seconds, "Fort Tidball", was confirmed by
  an unprompted re-transcription of 0–45 s, which produced "I was born in Fort Tidball"
  identically. No window needed the un-prompted splice.

### Quality

- 238 segments, **3,108 words**, **mean per-word probability 0.9403**, **3.54 % of words below
  0.5** (6.76 % below 0.7).
- Every 30 s window below 0.80 mean probability lies **after 24:30**, in the post-meeting
  chatter. The formal remarks are 0.80 and above throughout — the weakest of those are 24:30
  (0.688), 25:00 (0.767) and 25:30 (0.614, 4 words).

## Corrections applied (33 `post_edits`)

All are recorded in the JSON `post_edits` list with their raw ASR form, reason and certainty, so
each can be checked against the raw segment it replaced. The substantive ones:

| # | As transcribed | Corrected | Why | Certainty |
|---|---|---|---|---|
| 1 | "turn up a child and away should go" | "Train up a child in the way he should go" | Proverbs 22:6, printed as the motto on the cradle-roll certificate she reads aloud | certain |
| 2 | "Mary Wyckoff / mary wycroft" | Mary Wycoff | Bethel spelling: the 1951 history has 111 "Wycoff", zero "Wyckoff"; she is named cradle-roll superintendent | certain |
| 3 | "murray c ryder" | Murray C. Reiter | signature of the pastor on the certificate; Reiter installed May 1914, matching her baptism in June 1914 | certain |
| 4 | "Mrs. Ryder taught the class" | Mrs. Reiter | same name as the signature above — the pastor's wife, not a separate Ryder family | probable |
| 5 | "principally cannonsburg" | Canonsburg | town name | certain |
| 6 | "a general neville", "pastor clark" | General Neville, Pastor Clark | Whiskey Rebellion figures named in the history he reads | certain |
| 7 | "Edna Croco" | Edna Croco | surname from the Bethel record (Croco, not Kroko/Grokos) | certain |
| 8 | "their own legionary society" | their own missionary society | the women's missionary society is the subject of the passage | probable |
| 9 | "called Pigeon Creek. / Creek. Our church" | called Pigeon Creek. Our church | duplicated fragment across a chunk seam | certain |
| 10 | "Thank you." (×2, 25:39 / 25:58) | removed | hallucinated over room tone after speech ended | certain |

Mechanical repairs applied alongside: doubled words and stray fragments duplicated across chunk
seams collapsed (e.g. "put his hands upon / upon them", "active and / and dedicated",
"the three / Three groups"), sentence case repaired, one hallucinated "Noah?" dropped at 06:50.
Hesitations and false starts were left alone.

## Unresolved (left as heard, not guessed)

1. **"Fort Tidball"** (00:13–00:26) — the place Ruth was born, "off Logan Road, below the church".
   Reproduced identically by an unprompted re-transcription, so it is what she says, but no such
   fort or place-name was found; possibly a local name for a Tidball family property.
2. **"they called the fire tire"** (03:02) — the small room where the beginners' class met, near
   the stairway to the sanctuary.
3. **"Elsie McConkie"** and **"Mr. Kravitz"** (03:33–03:42) — 1923 superintendent names read off
   a certificate; neither spelling corroborated.
4. **"H. E. Pellett"** (03:58) — intermediate-department superintendent, 1929.
5. **"Isabel Hemlinger"** (05:55) — coached the Christian Endeavor plays.
6. **"Home Came Ted"** (05:55) — the title of a second play.
7. **"Mr. Yarnell"** (11:29) — pastor whose pastorate ran "up through 1960"; not checked against
   the 1951 history, which ends before him.
8. **"We can't sit or stand on our path, but we have to go forward"** (22:39) — the figure of
   speech is garbled; left as heard rather than improved.
9. **"So you know why we had to build the little children"** (21:57) — a broken clause.
10. **"I keep seeing something more"** (16:23).
11. **Off-microphone chatter after 24:20** — intelligible but unattributable; some of it is
    left in the transcript because it is on the tape.

## File inventory

| File | What it is |
|---|---|
| `Valentine, Maits and Snowden (25 September 1983).m4a` | the master, as received from the archive; md5 `913bdf2b51aa75586d7cd6931b03403f` |
| `Valentine, Maits and Snowden (25 September 1983).txt` | the transcript: labelled turns, source of truth for both documents |
| `Valentine, Maits and Snowden (25 September 1983).srt` | timed subtitles, speaker label on the first cue of each turn |
| `Valentine, Maits and Snowden (25 September 1983).json` | provenance layer: raw ASR segments, per-word timings and probabilities, stereo measurement, `post_edits`, `unresolved`, `speaker_attribution` |
| `Valentine, Maits and Snowden (25 September 1983).docx` | the filed document, built from the `.txt` |
| `Valentine, Maits and Snowden (25 September 1983).md` | the same document in Markdown |
| `Valentine, Maits and Snowden (25 September 1983).mp3` | mono 64 kbps listening copy, 25:59.93, -16.8 LUFS / -1.7 dBTP |
| `NOTES - Valentine, Maits and Snowden (25 September 1983).md` | this record |

Rebuild the documents only from the `.txt` (see the archive README); never edit the `.docx` or
`.md` by hand, or the next rebuild silently reverts it.
