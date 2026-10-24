<!-- Two working records from the source folder are carried here in order: 'NOTES - JD Patterson - Side B.md'
     and 'FACT-CHECK - JD Patterson - Side B.md'. Delimiter below. -->

# JD Patterson, Side B — transcription record (2026-10-21)

## What this is

The **second side of the same interview** as `JD Patterson - Side A`: **JD Patterson** talking to
**June Ellington**, recorded in Bethel Park on **20 April 1979** (subject, date and interviewer supplied by the
archive; the tape itself states no year). Side B opens mid-question — "What was his first name? Was it
Samuel?" — so it is continuous with Side A, not a separate recording.

Where Side A was Patterson's teaching career and the 1930-31 Stilley shooting, Side B is **the Fife family
and the ground it stood on**: who married whom, which farmhouse was built when, where each descendant lives
now, the streetcar stops along the Washington interurban (Cremona, Fifeshire, Valley Farm, Paris Lake), the
neighbours along Brookside and Old Washington Road (Hultz, Boyer, Fulliart, Espy, Phillips, Cheeseman,
Wilhals, Hayes, McNary), and the talk around the Klan's meeting place above Clifton. It ends with the
tape's own announcement: **"This is a recording of oral history to be the property of Upper St. Clair
Historical Society and will only be used by non-profit."** That is worth noting: the collection sits in
Bethel Presbyterian's Historical Room, but the recording states Upper St. Clair's ownership.

## Source and measurements

- `JD Patterson - Side B.m4a` — ALAC, 48 kHz, 2 ch, 104,071,166 bytes, **1,866.240 s (31 min 06 s)**,
  md5 `38a3a40c621d274521b8b74b741e56e6`. Received as `JD Patterson Side B.m4a` in the collection root;
  renamed to the archive stem, samples untouched.
- Level: mean **−22.9 dBFS**, peak **−0.6 dBFS**, even across the side (60 s blocks −21.1 to −25.6 dBFS).
- **Stereo:** the channels are 0.2–0.5 dB apart with r = 0.98 at a constant 1–3 sample lag on every window
  measured (120 s, 700 s, 1400 s, 1800 s) — one programme on two feeds, so they were **summed**
  (`pan=mono|c0=0.5*c0+0.5*c1`).

## Method

- **Whisper large-v3 in the `whisper-worker:v0.2` container** (faster-whisper 1.2.1 / ctranslate2 4.8.3 /
  numpy 2.5.4 on python 3.13 — the versions Side A was transcribed with), 14 CPU threads, int8, `en`,
  beam 5, `condition_on_previous_text=False`, word timestamps. Chunked at ~120 s (16 chunks), boundaries
  snapped to the quietest 10 ms frame.
- **Seeded prompt:** the subject, interviewer and the local names (Bethel, Chartiers, Peters Township,
  Mount Lebanon, Fort Couch Road, Castle Shannon, Canonsburg, Mingo Creek, McMillan).
- **The seed echoed over 0–20 s** — the whole prompt came back as a segment, covering whatever was said
  under it. That window was re-transcribed **unprompted** (cold pass `w01`, three settings, all three
  returning the same dialogue) and the recovered text replaced the echo. The raw echo is kept in the JSON
  (`segments[0].raw_asr`, `prompt_leak`) so the record shows both what the model printed and what was said.
- **Quality:** 522 segments, **4,081 words**, mean word probability **0.9333**, 3.81 % of words below 0.5.
- **Cold passes:** 23 windows over every doubtful passage × three settings (beam 5, beam 1, beam 5 + VAD) =
  **69 transcriptions**, run through the same container.
- **50 corrections** applied, each logged in `post_edits` with pattern, count, certainty and reason.
  7 readings remain unresolved and are listed in the FACT-CHECK.

## Speaker labels — and how far they go

Two voices plus the tape announcement. **92 turns: JD 77, JUNE 14, ANNOUNCEMENT 1** - one turn per
paragraph, deliberately not merged: joining consecutive same-speaker paragraphs turned ten minutes of the
interview into a single wall of text that read as garbled even where every word was right.

- **JUNE** is labelled where her words are unambiguous — a question, a name-check, an aside to the room
  ("You don't know when that house was built, do you?", "What was the connection there?", "Is that thing
  running?").
- **Her one-word acknowledgements inside Patterson's stretches stay under JD.** The ASR runs them together
  and no diarisation separates them; a guess there would put her name on his sentences, and the skill's rule
  is that a wrong label is worse than none. That limitation is stated rather than hidden.
- **ANNOUNCEMENT** is the closing ownership statement — neither speaker.

## What this side adds to Side A

- **The Fife family is now documented** where Side A only mentioned the name: Thompson Fife (grandson of
  John Fife, Sr., who came from **Fifeshire, Scotland**, in 1766) built the **William T. Fife house** on Old
  Washington Road in 1832; William T. lived in it 1842–1928 and it received a Pittsburgh History & Landmarks
  plaque — which is the "bronze plaque" he mentions. The other houses he dates (Albert Fife after 1900, the
  Jim Fife place in the 1870s–80s) belong to the same family cluster.
- **The stop names are real**: Cremona, Fifeshire, Valley Farm and Paris Lake all appear in the Pittsburgh
  Railways Washington-interurban stop list, which is what settles his readings.
- **Hultz** (the peach-orchard family on Fort Couch Road) is a stop and family name on that line — not
  "Haltz"/"Holtz" as the ASR has it.
- Corroborates Side A's names: **Espy** (Thomas Espy's Civil War sword, now with J. Walter Phillips),
  **Hulse Boyer**, **Cheeseman**, **Gilfillan**, **McNary**.

## Timecodes: two clocks

- **`JD Patterson - Side B.srt` is 0-based** for this file alone.
- **`JD Patterson (both sides).srt` is the interview clock**: Side A's 516 cues unchanged, then Side B's 522
  cues offset by Side A's exact duration (**2,156.288 s**) and renumbered — 1,038 cues, monotonic, no
  overlaps. The join gap is **313.2 s**, which is Side A's 294.4 s of silent tail plus the 18.8 s before
  Side B's first cue; it is tape, not a dropout.

## Deliverables

| File | What |
|---|---|
| `JD Patterson - Side B.txt` | 28 labelled turns (source of truth) |
| `JD Patterson - Side B.srt` | 522 cues, corrected, 0-based |
| `JD Patterson - Side B.json` | raw segments + word probabilities, `paragraphs`, `post_edits`, `prompt_leak`, `unresolved` |
| `JD Patterson - Side B.docx` / `.md` | the document (JD blue, JUNE and ANNOUNCEMENT red) |
| `JD Patterson - Side B.mp3` | 192 kbps stereo listening copy |
| `JD Patterson - Side B.m4a` | the master, unchanged (was `JD Patterson Side B.m4a`) |
| `JD Patterson (both sides).srt` | both sides on one continuous timeline |
| `FACT-CHECK - JD Patterson - Side B.md` | every doubtful reading, its verdict and its source |

## Rebuild

```bash
cd /opt/data/repos/whisper-worker
bin/transcribe.sh "JD Patterson - Side B.m4a" /opt/data/staging/jdp_b --stem "JD Patterson - Side B" \
  --channel sum --chunk 120 --prompt-file seed.txt
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_docx.py \
  "JD Patterson - Side B.txt" "JD Patterson - Side B.docx" \
  --title "Bethel Presbyterian Church" --subtitle "Historical Room — Oral History" \
  --byline "JD Patterson | interview 20 April 1979 | interviewer June Ellington | second side" \
  --main-speaker JD --secondary JUNE --secondary ANNOUNCEMENT
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_md.py \
  "JD Patterson - Side B.txt" "JD Patterson - Side B.md" --verify-docx "JD Patterson - Side B.docx" \
  --title "Bethel Presbyterian Church" --subtitle "Historical Room — Oral History" \
  --byline "JD Patterson | interview 20 April 1979 | interviewer June Ellington | second side" \
  --main-speaker JD --secondary JUNE --secondary ANNOUNCEMENT
```

Verification at build time: `verify_md_docx.py` → **MATCH** (92 paragraphs, 4,173 words, 92 label runs);
`make_md.py --verify-docx` → MATCH; `reconcile_md_json.py` → **DOCUMENTED-IN-NOTE** (50 post_edits, one
place-name token explained by the provenance note).


## Revised after John's note (2026-10-21)

Two things came out of a careful re-listen of the passage around "the dog woman":

1. **Pymatuning, not "Pima Tuning".** "Norman and Kenny live up around Pymatuning Dam" — Pymatuning
   Reservoir sits on the Pennsylvania-Ohio line north of Pittsburgh, and John identified it from the
   family's whereabouts. Corrected (CERTAIN, his knowledge).
2. **The paragraph was a wall of text, and that is what read as "off".** The builder had been merging
   consecutive same-speaker paragraphs into single turns, so this passage arrived as one ~600-word
   block. It is now one turn per paragraph — 92 turns, and the Fife-descendants passage reads in the
   short exchanges it actually was.
3. **"Catherine, the dog woman" — settled by ear, not by argument.** Nine passes (beam 5/10/1, prompted
   and unprompted) all return "dog" at p 0.93–0.99, and the token is 220 ms. I offered Dodge/Dague as
   surname alternatives on the strength of his habit of naming women by married name; **John listened to
   the extracted clip and hears "dog woman" too**, so the reading stands exactly as spoken. What the
   phrase *means* — a nickname, a kennel, an occupation — is not in the audio, and the transcript makes
   no claim about it. Recorded in the JSON `operator_confirmations` and in the FACT-CHECK so a later
   pass does not "correct" it.


## Street-name seeded run (2026-10-21, John's request)

Re-transcribed the whole side with a second, street-name seed built from **OpenStreetMap**: 2,566 distinct
road names in the Bethel Park / Upper St. Clair box, curated to 26 roads plus the stop and dam names that
appear in the audio (88 words of prompt). Run in the same pinned container, `--prompt-file`, chunk 120.

Result: **not adopted as the base transcript**, and the reason matters more than the run.

- It produced **4,111 words at mean p 0.9347** — statistically the same as the unseeded 4,092 / 0.9333.
- The seed did not echo at the head (checked), but it **biased the one road that was genuinely in doubt**:
  "Bar Hill Road" became "Bower Hill Road" because Bower Hill was in the prompt. It also degraded one
  passage to "a lot of fiefs" where the audio says "fives"/"Fifes". A seed that changes a reading in the
  direction of the seed is a hypothesis, not evidence.
- What it did usefully was **cross-check the real names**: Baptist Road, Bethel Church Road, Bower Hill Road,
  Brookside Boulevard, Clifton Boulevard, Drake Road, Logan Road, Old Washington Road, South Park Road,
  Waterdam Road, Fifeshire, Cremona, Paris Lake and Valley Farm all occur in the audio and exist in OSM.

**"Bar Hill" resolved separately.** Six unprompted cold passes hear "Bar Hill Road"; John hears "Bauer Hill";
OpenStreetMap's road there is **Bower Hill Road** (with Old Bower Hill Road alongside). One road, three
spellings — the transcript now carries the OSM form and the FACT-CHECK records all three, so a reader can
find it under any of them.

## The note now sits in the transcript itself

At John's request, the "dog woman" reading carries an editorial note **inside the turn**, in square brackets,
so a reader meets it where the words are rather than in this file:

> JD: Isabel has one daughter, Catherine, the dog woman. [The words are clear on the tape and were confirmed by
> ear. What "dog woman" refers to - a nickname, a kennel, or an occupation - is not stated, and nothing is
> assumed here.]

The same text is in the document's provenance note, and the JSON records it twice: `editorial_notes` (the
bracket and why it exists) and `operator_confirmations` (who confirmed the reading, when, on what evidence).
Bracketed editorial text is not speech: it is not in the `.srt`, and `reconcile_md_json.py` accounts for it as
documented-in-note rather than as transcript drift.


---

<!-- ===== 'FACT-CHECK - JD Patterson - Side B.md' begins ===== -->

# FACT-CHECK — JD Patterson, Side B

Stem: `JD Patterson - Side B`. Every reading below was checked against the Fife family's published history,
the Pittsburgh Railways Washington-interurban stop list, local place-name records, and three cold
re-transcriptions of the passage (beam 5, beam 1, beam 5 + VAD, `initial_prompt=None`, 23 windows / 69
passes). Verdict key: **CERTAIN** (the record settles it, or the sentence cannot mean anything else) ·
**PROBABLE** (sense clear, substitute fits, audio stable on the wrong word).

## Readings corrected

| Heard | Corrected to | Verdict | Basis |
|---|---|---|---|
| "Bar Hill Road" | **Bower Hill Road** | PROBABLE | Six unprompted cold passes hear 'Bar Hill Road'; John hears it as 'Bauer Hill'; OpenStreetMap lists Bower Hill Road (and Old Bower Hill Road) through Upper St. Clair and Bethel Park. One road, three spellings - the OSM form is used and both spoken forms are recorded. |
| "Pima Tuning Dam" | **Pymatuning Dam** | CERTAIN | Pymatuning Reservoir/dam, on the PA-OH line north of Pittsburgh - identified by John from the family genealogy; the ASR hears 'Pima Tuning Dam'. |
| "billy five" | **Billy Fife** | PROBABLE | Cold passes 2/3: 'a Billy Fife told me'; the family name is Fife. |
| "the men had the planet" | **the men had to plan it** | CERTAIN | Cold passes 3/3: 'the men had to plan it'. |
| "J. was killed in 1925" | **Jay was killed in 1925** | CERTAIN | Cold passes 3/3 'Jay was killed'; the earlier list has 'Jay had one son'. |
| "jackfife" | **Jack Fife** | CERTAIN | Cold passes: 'has Jack Fife up here on Bar Hill Road'. |
| "Ruth Fred Agers" | **Ruthfred Acres** | CERTAIN | Ruthfred Acres, Bethel Park: named for Fred and Ruth Brown, laid out in the 1940s. |
| "Rutherford Acres" | **Ruthfred Acres** | CERTAIN | Same place; cold pass garbles it to 'Rutherford'. |
| "Bill Stute" | **Bill Stuth** | PROBABLE | Cold passes 3/3 'Bill Stuth'. |
| "Tip, Carolyn, married" | **Pip, Carolyn, married** | PROBABLE | Cold passes 3/3 'Pip'. |
| "Fife Shire" | **Fifeshire** | CERTAIN | Fifeshire is a Pittsburgh Railways stop on the Washington interurban between Clifton and Valley Farm; the family came from Fifeshire, Scotland. |
| "five shire" | **Fifeshire** | CERTAIN | Same stop. |
| "the Haltz Fives" | **the Hultz Fifes** | PROBABLE | Hultz is a real stop and family name on the line (Pittsburgh Railways: 'Hultz' between Santa Barbara and Bethel Village); 'Fives' is the family, Fife. |
| "the lawrence fives" | **the Lawrence Fifes** | PROBABLE | Same reading: the Lawrence Fifes' farm. |
| "Al Phyfe house" | **Al Fife house** | CERTAIN | Cold passes 3/3 'the Al Fife house'. |
| "Albert Phyfe" | **Albert Fife** | CERTAIN | Cold passes 3/3 'Albert Fife'. |
| "Sam Phyfe" | **Sam Fife** | CERTAIN | Cold passes: 'Sam Fife, Bill's father'. |
| "Mary McCabe Phyfe" | **Mary McCabe Fife** | CERTAIN | Same person. |
| "Albert Fyfe house" | **Albert Fife house** | CERTAIN | Same house. |
| "John Fyfe's house" | **John Fife's house** | CERTAIN | Same family. |
| "Fyfe Drive" | **Fife Drive** | CERTAIN | Cold pass: 'at the end of Fife Drive'. |
| "the Jim Pfeiffer" | **the Jim Fife** | CERTAIN | Cold passes 3/3 'the Jim Fife'. |
| "Parris Lake" | **Paris Lake** | CERTAIN | Paris Lake is a Pittsburgh Railways stop west of the county line. |
| "Alpheis was still living" | **Al Fife was still living** | PROBABLE | Cold passes: 'Al Fife / Alpheis was still living in the big house'. |
| "Was it Barney or Nathaniel?" | **Was it Fanny or Nathaniel?** | CERTAIN | The answer is 'Nathaniel ... Fanny, they called him'. |
| "a lot of fives" | **a lot of Fifes** | CERTAIN | The family. |
| "Gilphillians" | **Gilfillans** | CERTAIN | Cold passes 3/3 'Gilfillans'; a sister married a Gilfillan. |
| "odd villas hall" | **Odd Fellows hall** | PROBABLE | Cold passes 2/3 'the odd-fellas hall' — the Odd Fellows hall at Clifton. |
| "Petersburg Church" | **Peters Creek church** | PROBABLE | Cold passes give 'peter's pick / petersburg church'; Peters Creek Church is the real congregation. |
| "Wilty Fife" | **Wiltie Fife** | CERTAIN | The family's own form of Will T. Fife; cold passes give 'Wiltie'. |
| "the william james five house" | **the William James Fife house** | CERTAIN | Same house. |
| "mrs frank five" | **Mrs. Frank Fife** | CERTAIN | Same person. |
| "the dr fight farm" | **the Dr. Fife farm** | CERTAIN | Cold pass: 'the Dr. Fife farm'. |
| "the old Dr. Dr. Fife Place" | **the old Dr. Fife place** | CERTAIN | Repeated segment head collapsed. |
| "Holtz Fife" | **Hulse Fife** | CERTAIN | Cold passes: 'It's Hulse Fife'; Hulse is his first name, used three times. |
| "the Holtzes" | **the Hultzes** | PROBABLE | Cold passes keep 'Holtzes'; the stop and family name on the line is Hultz. |
| "The Haltzes" | **The Hultzes** | PROBABLE | Same family. |
| "Will Haltz" | **Will Hultz** | PROBABLE | Same family. |
| "Harry Haltz" | **Harry Hultz** | PROBABLE | Same family. |
| "James Halsboyer" | **James Hulse Boyer** | CERTAIN | The passage is about Hulse Boyer, so his sons are Hulse Boyer. |
| "Doris McNeary" | **Doris McNary** | CERTAIN | She is 'Doris McNary' a few lines earlier. |
| "on Port Couch Road" | **on Fort Couch Road** | CERTAIN | Fort Couch Road, at Route 19. |
| "was the Fullert place" | **was the Fulliart place** | CERTAIN | He spells it out: F-U-L-L-I-A-R-T, then says 'Fullert'. |
| "Carolyn." | **Caroline.** | PROBABLE | Cold passes 2/3 give Caroline; he then says 'Carrie'. |

## Where his memory and the record disagree (transcript keeps his words)

| He said | The record |
|---|---|
| the Will T. Fife house and its "bronze plaque" | Confirmed: the William T. Fife House on Old Washington Road was built in 1832 by Thompson Fife, lived in by William T. Fife 1842-1928, and received a **Pittsburgh History & Landmarks Foundation plaque** in late 2016. |
| "John T. ... and William James had both been in the Civil War" | The 62nd Pennsylvania roster carries **William J. Fife** (b. Sept 1841 near Mont Clair, d. 1923, clerk of session at Bethel Presbyterian for 40+ years), **James Espy Fife** (d. Falmouth, Va., 1862) and **Johnston A. Fife** — several Fifes served; his pairing is close but the names in the roster differ. |
| "he died there about 1923, 1922 or three" | William J. Fife's obituary (Canonsburg Daily Notes, 29 March 1923) matches 1923. |
| the Fife farms' ages ("1870s or 80s", "after 1900") | Plausible against the published house history; no contradicting record found, and his hedges are kept as spoken. |

## Confirmed by the operator (not a correction)

| Reading | Confirmed | What it means |
|---|---|---|
| **"Catherine, the dog woman"** (4:11.7) | John listened to the extracted clip (248.9-252.7) on 2026-10-21 and hears "dog woman" too. | The reading stands exactly as spoken. Nine ASR passes agree (p 0.93-0.99) and the token is 220 ms, so it was never an acoustic doubt - only a plausibility doubt. What the phrase means (a nickname, a kennel, a job) is **not in the audio**, and the transcript makes no claim about it. Recorded so a later pass does not "correct" it to Dodge or Dague. |

## Unresolved (left as heard)

- 'Pima Tuning Dam' (4:25) - no such dam; every pass returns the same syllables. Left as heard.
- 'Bar Hill Road' (4:14) - the road he means is not identified; 'Barr Hill' was checked and not found.
- 'Isabel Hemlinger, the pianist' (3:48) - all three passes agree on the name, but no Hemlinger/Henninger could be corroborated in Bethel Park records.
- 'Catherine, the dog woman' (4:09) - the words are clear, the meaning (a kennel? a nickname?) is not.
- 'Hamels Mortuary' (26:12) - no funeral home of that name found; the hill above Clifton is identifiable, the business is not.
- 'Earl married a swim girl' (28:51) - probably a surname (Swaim?), but no pass returns it cleanly.
- 'Hayes River' (30:06) - the place Genevieve's husband came from is not recoverable.
- 'and Genevieve married a Hayes ... they used them' (30:06) - the clause after 'Hayes' is lost.
- 'Attention.' (14:18) - a single unintelligible word between two exchanges.
- 'It's a different, they're distantly related' (4:36) - the sentence about the other Fife family starts in the middle; kept as spoken.
