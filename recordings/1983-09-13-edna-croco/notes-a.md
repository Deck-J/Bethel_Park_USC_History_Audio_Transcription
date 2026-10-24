# Edna Croco — interview with Ann Connor (13 September 1983) — transcription record

Recording stem: `Edna Croco Interview`. Every file in this folder carries that stem; this note is
the working record behind the document.

## What this is

A 34 m 20 s (2,059.78 s) recording made by **Ann Connor** on **Tuesday 13 September 1983**. It
opens with Ann alone at the Miller Homestead and then driving, talking into the recorder about the
errand she is on: she has the prayer that **Mrs. Edna Miller Maits** gave at the homestead in 1979,
and she is going to see **Edna Croco** to gather memories of Edna Maits to read at the Women's
Association meeting the next day. From about 4:00 the interview proper is under way in Edna's
house — the third meeting house and its water cooler, its caretaker, the flowers and the passing
bell, Uncle Al's burial, the Ladies Aid and Rev. Johnston in Africa, the schools the two women
attended, Rowan Maits never being allowed to join the church his mother distrusted, summer
Methodism and winter Presbyterianism, cottage prayer meetings, Edna's father and the Catholic Bible
with four kings in it, the wagon shop at Sodom and John L. Poellot's two surreys, what Sodom was and
where, the 1902 wind that took the roof off the third meeting house, and finally what Edna Maits was
like as a friend.

It ends abruptly: Ann says she will take the book along and open it at a page, Edna starts to say
something about a photograph, and the recording stops at 30:33. The remaining 3 m 46 s of the file
is silence.

**This is the sixth recording in the Bethel archive and the first in it to name its own date.** It
is a different kind of document from the other five: not a lecture and not a moderated panel, but a
research interview with a single 83-year-old woman, recorded by the woman who was building the
Historical Room.

## The biographical record — and what it rests on

| | |
|---|---|
| Name | Edna M. Croco |
| Born | **20 September 1899** |
| Died | **May 1988**, aged 88 |
| Age on this recording | 83 — seven days short of her 84th birthday |
| Bethel membership | joined **31 January 1915** (recorded as "Croco, Miss Edna M." on the roll in the 1951 history) |
| Family | Croco of Bethel Park; "Croco, J. Wilson" is on the same 1951 roll; the family farm was on Baptist Road |

**The dates are from a genealogy index entry, which is a SECONDARY source.** The primary obituary
(Pittsburgh Press / Post-Gazette, May 1988) has not been obtained and sits behind a paywall. The
dates are therefore *not* confirmed from a primary record and should be cited as secondary. They are
in the document's front matter, marked as such, and are not part of the transcript turns.

The **year** is independently corroborated from the tape itself. At 23:22 she says she was "only
about two years old" when a wind took one side of the roof off the third meeting house. The 1951
history dates that storm precisely: *"Sunday, March 30, 1902, was Easter… with a deafening roar a
'twister' blew in… and ripped off a large section of the roof"* (Anna M. Wycoff, eyewitness). Two
years before March 1902 is 1899-1900, which fits 20 September 1899 exactly. The same passage in the
history describes the chandeliers being jerked up to the ceiling — which is the detail Edna's father
gave her, and which she recounts at 23:48.

## Date, and what the date rests on

**Tuesday 13 September 1983 — stated on tape**, in the first eleven seconds: *"This is Tuesday,
September the 13th, 1983, and this is Ann Connor."* 13 September 1983 was indeed a Tuesday, so the
statement is internally consistent. Nothing in the recording contradicts it, and the Women's
Association meeting she is preparing for is "tomorrow".

The folder name carries no date and the file arrived with none, so nothing was inherited from the
neighbours. The `2026-10-18` in the archive folder name is the digitisation date.

## Speaker attribution, and why it is content-based

Two voices, labelled `ANN CONNOR` and `EDNA`.

- **Ann Connor.** She names herself at 0:09. She narrates her errand into the
  recorder before the interview begins (1:44–4:00), says "that's on my other tape in the ride that
  I took", "I have the water cooler that was used there", asks every question, and ends by saying
  she will take the book along.
- **EDNA = Edna M. Croco.** The subject. "Just Edna Maits and myself and Edna Simmons"; "I'm the
  last of the three"; the family memories (Grandma Wilson, Daddy, the roof, the surreys).

**Pitch cannot separate them, and was not used to.** Median f0 was measured per segment: both women
sit in one band (roughly 150–220 Hz across the file, with no bimodal split), and they share one
microphone in one room. Fitting a two-cluster model to those values would have produced a
confident-looking split with no evidence behind it. The attribution above rests on what is said —
who asks, who answers, whose father and grandmother are being described.

**The weakest stretch is 1:44–4:00**, where Ann's narration and Edna's reminiscence run together and
only the backchannels ("Okay. And Wilson Road. Yeah. All right.") are unmistakably the second voice.
Turns in that stretch are labelled by content and are recorded as medium confidence in the JSON
`speaker_attribution`. The final 25 seconds are low confidence: the sentences are garbled and the
recording stops mid-thought.

Edna speaks slightly more than Ann — **56/44 by words (Edna 1,662, Ann 1,286)** — so `--main-speaker
EDNA` is the correct colour assignment as well as the correct subject.

## Source and measurement

- `Edna Croco Interview.m4a` — ALAC, 48 kHz, 2 ch, 16-bit, **2,059.776 s**, 37,145,922 bytes,
  md5 `4cae6a72735fa9ace86aa92f8cc16c1f`, **unchanged as received** (md5 verified before and after
  the move out of the archive root).
- Level: mean **−44.2 dBFS**, peak **−9.8 dBFS**. The first minute is the loudest block (mean
  −33.2, peak −10.5) and it is Ann speaking close to the microphone; the interview itself runs
  10–20 dB lower.
- **Energy above 8 kHz is 42.7 dB below the passband** (3–8 kHz is already 21.9 dB down). There is
  nothing to denoise: the top end is empty because the capture is band-limited, not because there
  is hiss in it. **No denoise, no filtering — gain only.**
- **Stereo: delayed duplicate, ch1 stronger.** Measured per channel and per 120 s window: ch0
  −45.53 dB, ch1 −43.20 dB (**2.33 dB apart**), with a consistent **7–9 sample lag** (median 8
  samples = 0.167 ms) at which correlation is **0.973–0.992** (against 0.59–0.87 at zero lag). Both
  channels carry the same programme, ch1 leads in time and is louder. They were summed at 48 kHz
  with the lag compensated and weights 0.433/0.567 (proportional to amplitude). An equal-weight sum
  would have comb-filtered the top of the speech band; using ch1 alone would have thrown away a
  near-perfect second copy.
- **A third of the file is literal digital zero** — 710.4 s of samples that are exactly 0, in 49
  runs of a second or more, interleaved with the speech at 20 ms granularity. That is what a
  voice-actuated or squelch-gated recorder produces, and it explains why the tape sounds empty
  between remarks. The audio alone cannot say which mechanism it was.

## Transcription

- Whisper **large-v3** (Systran faster-whisper 1.2.1, CTranslate2 4.8.3, int8, 14 CPU threads), `en`.
- **16 chunks** of about 120 s, boundaries snapped to the quietest 10 ms frame within ±5 s of each
  target. Never a whole-file pass. `beam_size=5`, `condition_on_previous_text=False`,
  `temperature=0.0`, `compression_ratio_threshold=2.4`, `vad_filter=False`, word timestamps.
- Audio decoded by ffmpeg to float32 arrays. **PyAV in this build rejects the `metadata_errors`
  kwarg** faster-whisper passes, so the array path was used deliberately.
- `initial_prompt` seeded with corroborated names: Edna Croco, Bethel Park, Baptist Road, Peter
  Croco, Wilson Croco, McMillan, Clark, Woods, Marshall, Wycoff, Reiter, Chartiers, Canonsburg,
  Mingo Creek, Bethel Academy, Oliver Miller, Doddridge, Princeton Theological Seminary, Karla
  Strobl, Coverdale mission.
- **A second pass with `initial_prompt=None`** over the same boundaries (16 chunks) as a control. It
  is what found the prompt damage described below; it also supplies the text where the prompted
  pass had nothing usable.

### Prompt leak: the seed did not echo — it collapsed

No segment came back as a verbatim echo of the prompt. What happened instead is the same failure in
a different disguise: **the seeded pass emitted "Thank you for joining us." or a single 12-second
word over speech that is plainly there** — at 4:00, 4:10, 17:53 and 18:05. Word probabilities on
those tokens are 0.00–0.15, and the un-prompted pass over the same audio returns fluent, contextual
dialogue:

| Window | Prompted pass | Un-prompted pass |
|---|---|---|
| 4:00–4:20 | "Thank you … for … joining us." (p 0.00 / 0.06 / 0.05) | "Now, you say that you lived there." / "Well, I better not put this on the tape." / "I was going to ask you who was going to get this bill." |
| 4:10–4:23 | (the same silence) | "Well, I don't know. I don't know anything about that. That's a decision that the Millers have to make." |
| 17:53–17:55 | "you and he" — the word "you" given 12.4 s | "…and he couldn't find it. Well, that's interesting. I didn't realize that." |
| 18:05–18:10 | "for joining us." (p 0.11 / 0.04) | "…but I would guess that since the cottage prayer meetings were held in each other's homes, that the Millers would have been a part of that. And was that during the week that that was held? It was almost certainly a Wednesday evening." |

**Every one of those windows was re-transcribed without the prompt and spliced back. Nothing was
deleted.** The five spliced windows carry about 170 words of real dialogue, including a whole
question-and-answer pair the document would otherwise have lost. Two genuine hallucinations over
digital silence (two "Thank you." and six "you" at 31:06–34:10, where the audio is sample-zero) were
excluded from the transcript and are listed in the JSON.

### Chunk seams: 97 words recovered by an orphan pass

The first merge assigned every word to the chunk whose core region held its midpoint. That is
correct in principle and lost content in practice: where a chunk head hallucinated, the words the
*previous* chunk had transcribed in the 4 s overlap fell outside its own core and had no owner.
Words lost that way included:

- "That was one thing she made me aware of." (3:57)
- "When Uncle Al was buried, he was…" (9:47)
- "I didn't hear Edna ever doing this, but Ida and Albert told me when I took care of them…" (19:52)
- "And I was born in Edna Patterson, Edna Miller, and Edna Croco." (part of 5:51)
- "Well, when did you first know Edna in connection with Bethel Church?" (13:56)

The fix is an **orphan pass**: a word outside its own chunk's core is kept when no word owned by
that core covers its time span. It recovered **97 words** across fifteen chunk seams, and caught 44
duplicated words that the same pass could otherwise have introduced. The transcript was rebuilt from
that timeline, and a coverage check confirms that every word of the raw segments appears in the
document except the 17 explained by the correction table.

### Quality

- **2,947 words**, **mean per-word probability 0.8738**, **8.35 % of words below 0.5** (16.97 %
  below 0.7). That is inside the archive's bar (≥0.85 and <10 %).
- Weakest stretches, by 2-minute block: **12:00–14:00** (0.822), **26:00–28:00** (0.818),
  **18:00–20:00** (0.843), **28:00–30:00** (0.844). These are the passages where the two women
  overlap, or where Edna turns away from the microphone; treat names and dates in them as
  indicative.
- Cleanest: 0:00–2:00 (0.943) and 14:00–16:00 (0.909).
- **Read end to end**: all 132 turns, 3,080 words, twice — once against the prompted pass and once
  against the un-prompted pass — plus a separate pass for misplaced context words.

## Corrections applied

27 logged segment-level edits covering 31 distinct corrections, all in the JSON `post_edits` with
raw form, corrected form, reason and a certain/probable marker (16 of the 27 are certain). The
substantive ones:

| # | As transcribed | Corrected | Why | Certainty |
|---|---|---|---|---|
| 1 | "Mrs. Edna Miller **Mates**" (10×) | **Maits** | 1951 history: "Mrs. Edna Maits", "Mrs. E. M. Maits" — Maits ×21, Mates ×0; the archive's Valentine folder already uses Maits | certain |
| 2 | "Edna **Mace**" / "Mrs. **Mace**" | Maits | same person | certain |
| 3 | "She married **Roe and** Mates" | **Rowan** Maits | her husband's given name, heard as "Roe and" | probable |
| 4 | "**Wilton** Road" (×3) | **Wilson** Road | three of four decodes give Wilson, one at p=0.98; the sentence is about the Wilson family and "Johnston Wilson" | probable |
| 5 | "the Wilton farm was on **Elm Hill**" | "the Wilson farm was on **the hill**" | beam-10 decode: "from where the wilson farm was on the hill" | probable |
| 6 | "the log house is **on St. John's**" | "the log house is **gone**" | beam-10 decode: "the log house is gone but the other house is still there" | probable |
| 7 | "three **Edmonds**" / "Three Edmonds?" | "three **Ednas**" | the next breath: "Yeah, three Ednas" | certain |
| 8 | "**Snowdon**" (×2) | **Snowden** | Snowden Township, now South Park; the archive spells it Snowden (Jean Snowden) | certain |
| 9 | "**Kroko** school" | **Croco** school | the family's one c | probable |
| 10 | "It was called **Blanche McKeown**" | "**There was Blanche McEwen**" | 1951 history: "Miss Blanche McEwen of Bethel", 50 years teaching the Beadling Mission School, and named in a cast list beside Edna Croco; "who else was in there" needs "There was" | probable |
| 11 | "reverend **johnson** … in africa" | **Johnston** | Rev. William C. Johnston, Bethel's missionary, sailed for West Africa 1895 | certain |
| 12 | "**Lady's** Aid" | **Ladies** Aid | 1951 history: "Ladies Aid Society" throughout | certain |
| 13 | "the **pregnaturians**" | the **Presbyterians** | ASR of Presbyterians, in a sentence about Baptists and Bethel | certain |
| 14 | "Reverend **Ryder**" | **Reiter** | Dr. Murray C. Reiter, Bethel's fifth minister 1914–1946 | certain |
| 15 | "he built **service** and the two **surveys**" | "he built **surreys**, and the two **surreys**" | a surrey is a carriage, and the next clause says the two were "just alike"; the 1951 history uses "surrey" | certain |
| 16 | "It was in **1999**" | **1899** | the recording is 1983; the fire precedes a 19 May birth in the same year | probable |
| 17 | "mr **pellet** — john l **pellet**" | **John L. Poellot** | 1951 history: "Elder John L. Poellot of Bethel" — name and initial match | probable |
| 18 | "this is Ann **Conner**" | **Connor** | her own name; the archive spelling | certain |
| 19 | "He always had his **vehicle and seen** the funny side" | "his **way of seeing** the funny side" | sense only; the words as heard are not English | probable |
| 20 | "Well, **faster** along the aisle" | "Well, **passing** along the aisle" | the interviewer's question about the passing bell | probable |
| 21 | "That was the one **that to help** to raise money" | "that **helped** to raise money" | agreement with "was the one" | certain |
| 22 | "she talked uh in **curve**" | "she **taught**, uh, in Cur…" | context: which school she taught at; the name itself is truncated | certain for "taught" |
| 23 | "whether that was **field hall**" | "**Gill Hall**" | eleven cold passes give `[g/m/f]ɪl` + `hɔːl` (see below); Gill Hall Road sits above the Cochran Mill valley and the dialogue says she pointed up the hill | probable |
| 24 | "what they called well the **nexus church**" | "what they called, well, the **Methodist church**" | the passage is about the Methodist church up the hill | probable |
| 25 | "Mrs. **Phillips Surrey**" | "Mrs. **Phillips' surrey**" | possessive and the carriage | certain |
| 26 | "**Edwin Gitche** was born over there" | "**Edna** was born over there" | beam-10 decode: "I didn't know that Edna was born over there" | probable |
| 27 | "**Nelly** Beam" | **Nellie** Beam | spelling of the name as heard twice | certain |

### The Methodist church above the Cochran Mill: Gill Hall (probable)

Row 23 is the one proper noun here that listening alone would not settle, and it was carried as
unresolved until the tape had been chased down properly. Eleven cold passes (no `initial_prompt`, the
same chunk boundaries, temperature 0) returned **Millvale** in none of them and **Mill Hall** in none of
them. What every pass does return is a two-syllable name ending in `hɔːl` with a `[g/m/f]ɪl` head.

- **Millvale is rejected acoustically.** It needs a /v/ and a front diphthong tail. No pass produced
  either, and the second syllable stays a stable `hɔːl` where Millvale would give `-vale`.
- **Mill Hall is rejected geographically.** It is a real congregation — in Clinton County, 200 miles
  from Bethel Park. A name that exists but cannot be in this woman's biography is a mishearing, not a
  reading.
- **Gill Hall fits both tests.** It is a real Jefferson Hills locality: Gill Hall Road runs the ridge
  above the Cochran Mill valley, and Jefferson United Methodist Church at 310 Gill Hall Road has served
  a congregation for more than 175 years. Jefferson Hills was formerly **Snowden Township** — the same
  Snowden as Snowden Road in this interview, in the township Ann already corrects Edna about.
- **The dialogue corroborates it.** "…she pointed up the hill and we were down in the valley there,
  trying to find the old Cochran Mill" — she pointed up the hill, at Gill Hall. The hill is the whole
  point of the anecdote.

Marked **probable**, not certain: the `…ill Hall` shape is high confidence, but the initial consonant
(Gill / Mill / Phil) is exactly what the audio will not pin down. Recorded in `post_edits` against both
document occurrences (15:52 and 16:09), with the raw `segments` left untouched.

Mechanical repairs applied alongside: lone lowercase "i" as the pronoun, sentence case, doubled
words from the merge ("that That"), and casing of proper nouns. Hesitations, false starts and
self-interruptions are left alone ("I was her, well, I don't know").

## Unresolved (left as heard, not guessed)

1. **"Dr. Wycoff's Bible class"** (3:32) and **"the white of Bible plans"** (2:33) — probably the
   **Wycoff Bible Class** of the 1951 history, which records Annie M. Poellot as its teacher for 29
   years, but three decodes all give a name closer to *Wycoff*. The text reads **Wycoff** and the change
   is logged in `post_edits`; the identification of the class, not the reading, is what stays open.
2. **"King's school"** (12:22) — a school name the tape does not support; the next breath names the
   Bethel grade school.
3. **The year of the Simmons house fire** — heard as 1899 (beam 5, twice) and 1909 (beam 10). 1899 is
   written, because the fire precedes a 19 May birth in the same year and Edna was born that
   September, but the audio is not decisive.
4. **"Jacob Morlock"** (7:53) — the caretaker of the third meeting house; not in the 1951 history.
5. **"Nellie Beam"** (25:20) — the girl Grandma Wilson raised; no Beam on the 1951 roll, but "Beam"
   is what is said twice.
6. **"Edna Patterson, Edna Miller, and Edna Croco"** (5:51) — as spoken; the "three Ednas" are
   otherwise named as Edna Maits, Edna Simmons and Edna Croco, so "Edna Patterson" may be a slip or a
   fourth name. Not resolved.
7. **"From down in Capitana?"** (26:29) — a place name the ASR gives three different ways.
8. **"What's on the north side?"** (10:15) — the question as heard; its referent is unclear.
9. **"half of the … Bible plants is in this picture"** (29:37) — the phrase is not recoverable.
10. **"John McKay"** (30:23) — a name in a garbled closing sentence.
11. **"rainfall"** (23:22) — a single word after "took one side of the roof off"; left out of the text
    and recorded here.
12. **"her dad drank so"** (25:34) — the sentence about Nellie Beam's father is as heard; the sense is
    inferable, the wording is not.

## Dead time, and the condensed copy

John's note said the audio seemed to have a lot of dead time. **Measurement says he is right, and
the dead time is real rather than imagined** — but it is not evenly spread:

| Measure | Value |
|---|---|
| Total duration | 2,059.78 s (34:20) |
| Speech ends | **1,832.9 s (30:33)** — the last 226.9 s is tail |
| Literal digital zero | 710.4 s (34.5 % of the file), in 49 runs ≥ 1 s |
| Gaps ≥ 1.5 s below −55 dBFS peak | **106 gaps, 532.5 s (25.9 %)** |
| Of which the tail | 226.9 s (11.0 %) |
| Of which internal thinking pauses | ~305 s (14.8 %) |

For comparison with the rest of the archive: the John McMillan lecture had almost no dead air (a 9 s
head and a 15 s tail, longest internal pause 2.9 s) and its MP3 is a straight conversion; the George
Marshall talk needed only its tail trimmed. **This recording is the first in the archive with a
genuinely large amount of internal dead time** — and the reason is visible in the waveform: the
source contains runs of *exact* digital zeros between utterances, which is a gated or voice-actuated
recorder, not a person pausing quietly.

**What was cut, and what was not.** A gap was cuttable only if **every** 20 ms frame in it peaked
below −55 dBFS — 20–30 dB under the quietest speech — was at least 1.5 s long, and sat at least
0.25 s clear of any word boundary (guard band 0.30 s, plus a 0.20 s margin after the previous word).
Each cut gap keeps **0.4 s**, so the conversation still breathes; nothing is butt-joined.

- Cuts made: **98**. Gaps skipped as too tight: **8**.
- Removed: **625.4 s of 2,059.8 s — 30.4 %**. Of that, **225.8 s is the silent tail** and **399.6 s
  is internal** (19.4 % of the runtime).
- Condensed duration: **1,648.11 s (27:28)**.
- **No word overlaps any cut** (0 violations), and the tightest margin between a cut edge and a word
  edge is **0.250 s**. Three joins were re-transcribed from the condensed file to check that the
  words either side survived intact — "Did you know that that was the case?", "Well, what do you
  remember about Edna in connection with the church?", "Not, I can't think of anybody at this point. /
  I can't think of anybody at this point." — all recovered whole.
- **No speech time was removed.** Every removed second is silent. If anything the copy runs slightly
  faster than the room did; it does not cut a single word.

The file is named `Edna Croco Interview (condensed).mp3` because it genuinely is one. It is mono
64 kbps at 48 kHz, loudness-normalised to −18 LUFS (measured mean −22.7 dBFS, peak −1.5 dBTP) from a
master that sits at −44 dBFS. **The transcript, the `.srt` and the JSON all point at the full-length
master**, never at this copy.

## File inventory

| File | What it is |
|---|---|
| `Edna Croco Interview.m4a` | the master, as received; md5 `4cae6a72735fa9ace86aa92f8cc16c1f` |
| `Edna Croco Interview.txt` | the transcript: 132 labelled turns, source of truth for both documents |
| `Edna Croco Interview.srt` | 216 timed cues, speaker label on the first cue of each turn |
| `Edna Croco Interview.json` | provenance: raw ASR segments (prompted and un-prompted), per-word timings and probabilities, stereo measurement, 27 `post_edits`, 12 `unresolved`, `speaker_attribution` |
| `Edna Croco Interview.docx` | the filed document, built from the `.txt` |
| `Edna Croco Interview.md` | the same document in Markdown |
| `Edna Croco Interview (condensed).mp3` | 27:28 condensed listening copy, mono 64 kbps |
| `NOTES - Edna Croco Interview.md` | this record |

## Verification

```
verify_md_docx.py --dir .      -> 132 docx paras / 132 md blocks / 3146 words both / 132 labels  MATCH
reconcile_md_json.py           -> md-only 3, unexplained 0, orphans 0, labels EDNA+ANN CONNOR, date OK
                                  27 post_edits, all 27 located and applied (0 unresolved edits)
                                  11 unresolved items in the JSON list
                                  VERDICT: DOCUMENTED-IN-NOTE (one word, "them", carried by the note)
```

The JSON carries two unresolved lists: the top-level one (11 items) and `meta.unresolved` (12). The
extra item in the mirror is the Wycoff entry, which is a `post_edits` correction now rather than an open
question; the count in the document's provenance note tracks `meta.unresolved` and this file's list.

Label runs parsed back out of `word/document.xml`: **EDNA 66, ANN CONNOR 66** — equal to the
builder's own count and to the count in the `.txt`. Every part of the `.docx` was parsed with
`xml.etree` before the file was accepted.

## Rebuild

Rebuild the documents only from the `.txt`; never edit the `.docx` or `.md` by hand.

```bash
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_docx.py \
    "Edna Croco Interview.txt" "Edna Croco Interview.docx" \
    --title "Bethel Presbyterian Church" \
    --subtitle "Historical Room - Oral History: Edna M. Croco, 13 September 1983" \
    --byline "Edna M. Croco, spoken with Ann Connor | recorded 13 September 1983 | 34 m 20 s" \
    --note "<the provenance note in the current .md>" \
    --main-speaker EDNA --secondary "ANN CONNOR"
python3 .../make_md.py "Edna Croco Interview.txt" "Edna Croco Interview.md" <same args> \
    --verify-docx "Edna Croco Interview.docx"
```
