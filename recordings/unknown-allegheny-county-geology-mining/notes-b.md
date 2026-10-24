# Allegheny County Geological and Mining lecture (B side) — transcription record

Recording stem: `Allegheny County Geological and Mining lecture - B side`. Every file for this side
carries that stem; this note is the working record behind the document.

## What this is

The **second side of the same meeting**. It opens in the middle of the *previous* presenter's talk —
the mill on Cochran Mill Road, the Whiskey Rebellion, Tom the Tinker filling up the mill's footholds,
the mill torn down in 1978 — which ends with a handover: "Okay, thank you, Martha. Thank you, Bob."
From 1:09 the geologist who gives the A side takes over again and works through: the three rock types
(shale, sandstone, limestone) and the acid-clay soil problem; coal and its sulfur; iron carbonate
"pancakes"; the fossils (ferns, *Calamites*, a tree trunk held up for the room); William Maclure and
the first geological map of North America; the National Pike and the Casselman arch; why Pittsburgh's
rocks make poor soil and the county a coal basin; the I-79 cut at Heidelberg and the Benwood
limestone; the stream map of the Peters Creek watershed; the 12 Mile House; the Amity anticline and
its hundred gas wells; salt licks; building stone, brick and the shot tower; Alliance Furnace and
Hopewell Furnace; and closes with an artist's impression of the coal swamp 300 million years ago.

**Speaker.** The same unnamed man as the A side — the former miner turned local geologist. The room
speaks too: two audience questions are labelled `AUDIENCE`, "Joe" runs the slide projector, "Grace"
is asked whether she can see, "Jim" holds up the fossil, and "Martha" and "Bob" are thanked at the
handover. No other voice separates cleanly in the ASR, so nothing further is labelled rather than
guessed. **Date: unknown**, as on the A side (no date on the tape or the filename; content puts it
after 1970 and probably after 1990).

## The source

`Allegheny County Geological and Mining lecture - B side.m4a` — ALAC, 48 kHz, 2 channels, 82,684,034
bytes, 1,859.157333 s (30 min 59 s), md5 `d79e72d9daf3e0bb70a9ec917e2ba948`. Received as
`B side.m4a`; renamed to the archive stem, samples untouched (no denoise, no gain, no remux).

- The stereo pair is the same programme on two feeds: 1.0-1.2 dB apart with 0.97-0.99 correlation at
  a constant 4-6 sample lag in every block measured. It is not a delayed duplicate at a 3 dB
  difference, so the two channels were **summed** (`pan=mono|c0=0.5*c0+0.5*c1`) rather than using one.
- Levels run -25 dB mean early, -20 dB from about 12 minutes: he moves nearer the microphone, or the
  room fills.

## Method

- **Whisper large-v3** (Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads), English,
  beam 5, `condition_on_previous_text=False`, word timestamps, **no initial prompt** — the same recipe
  as the A side, so the two sides are transcribed under identical conditions.
- Chunked at ~120 s (16 chunks), boundaries snapped to the quietest 10 ms frame; ffmpeg decodes to
  float32 numpy (PyAV in this build rejects the `metadata_errors` kwarg faster-whisper passes).
- Quality: 334 segments, 4,066 words, **mean word probability 0.853**, 9.7 % of words below 0.5.
- **Cold pass:** 16 windows (every doubtful passage) re-transcribed with `initial_prompt=None` at
  beam 5, beam 1 and beam 5 + VAD — 48 transcriptions. One window's run was killed mid-job and
  resumed from the log rather than restarted; the script skips windows already written.
- 56 corrections applied, each logged in `post_edits` with pattern, count, certainty and reason.
  8 readings remain unresolved and are listed in the FACT-CHECK.
- One cold-pass window was re-run after the first attempt's result was lost: the projector-and-lights
  exchange, which the ASR had flattened to repeated "Don't", and which the re-run recovered as
  audible dialogue (carried as a bracketed stage direction, since the voices do not separate).
- Stutters and repeated segment heads collapsed; hesitations ("uh", "um") left as spoken.

## Timecodes: two clocks, both documented

- **`- B side.srt` is 0-based** for the B-side audio alone, so a cue time matches the file you play.
- **`(both sides).srt` is the meeting clock**: the A side's 175 cues unchanged, then the B side's 334
  cues offset by the A side's exact duration (1,284.778667 s) and renumbered — 509 cues, monotonic,
  no overlaps across the join. The join leaves a **91.9 s gap** (21:31.9 against the A side's last cue
  at 19:59.98): that is the A side's silent 84.8 s tail plus the 7.1 s before the B side's first word.

## Files

| File | What it is |
|---|---|
| `… - B side.txt` | the transcript, one labelled turn per paragraph (source of truth) |
| `… - B side.srt` | timed subtitles, cue per ASR segment, corrected, 0-based |
| `… - B side.json` | provenance: raw segments + word probabilities (untouched), `paragraphs`, `post_edits`, `unresolved` |
| `… - B side.docx` / `.md` | the document, both built from the `.txt` with identical arguments |
| `… - B side.mp3` | 192 kbps stereo listening copy |
| `… - B side.m4a` | the master, unchanged (was `B side.m4a`) |
| `… (both sides).srt` | both sides on one continuous timeline for citing |
| `FACT-CHECK - Allegheny County Geological and Mining lecture - B side.md` | every doubtful reading, its verdict and its source |

## Rebuild

The `.txt` is the source of truth; `.docx`/`.md` are build products. After any transcript edit,
rebuild both from the `.txt`:

```bash
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_docx.py \
  "Allegheny County Geological and Mining lecture - B side.txt" \
  "Allegheny County Geological and Mining lecture - B side.docx" \
  --title "Bethel Presbyterian Church" --subtitle "Historical Room - Oral History" \
  --byline "LECTURER | rocks, soils, water and early industry of the South Hills | 30 min 59 s | date unknown" \
  --main-speaker LECTURER --secondary AUDIENCE
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_md.py \
  "Allegheny County Geological and Mining lecture - B side.txt" \
  "Allegheny County Geological and Mining lecture - B side.md" \
  --verify-docx "Allegheny County Geological and Mining lecture - B side.docx" \
  --title "Bethel Presbyterian Church" --subtitle "Historical Room - Oral History" \
  --byline "LECTURER | rocks, soils, water and early industry of the South Hills | 30 min 59 s | date unknown" \
  --main-speaker LECTURER --secondary AUDIENCE
```

Verification at build time: `verify_md_docx.py` -> MATCH (59 paragraphs, 4,110 words, 59 label runs,
57 `LECTURER` + 2 `AUDIENCE`); `make_md.py --verify-docx` -> MATCH; `reconcile_md_json.py` ->
**JSON-CONSISTENT** (56 post_edits applied, 8 unresolved).

## What this side settles on the A side

- The A side's unresolved **`Cochrane View`** is **Cochran Mill Road** — the B side names the mill and
  puts it one mile south of the Bureau of Mines building, which is where Cochran Mill Road runs.
- The A side's **`the amity and the climb`** is the **Amity** line of gas wells and the fold axis
  (`anticline`) they were drilled along: this side has "named from Amity, down in Washington County"
  and "the Amity arch or anticline".
- **Hawkins Mill** (A side: "first Hawkins Mill") is confirmed as a place on that same gas line.
- The A side's coal-for-"pole" and coal-for-"corn" substitution class is confirmed again here.

---

# Appendix — the FACT-CHECK, copied verbatim

`FACT-CHECK - Allegheny County Geological and Mining lecture - B side.md` lives in the archive folder
and is reproduced here in full so that every doubtful reading, its verdict and its source travel with
the transcript. Nothing in it has been edited.

# FACT-CHECK — Allegheny County Geological and Mining lecture (B side)

Stem: `Allegheny County Geological and Mining lecture - B side`. Every reading below was checked
against published geology, local mining, iron-making or place-name history, and against three cold
re-transcriptions of the passage (beam 5, beam 1, beam 5 + VAD, `initial_prompt=None`, 16 windows /
48 passes). "Count" is how many times the string occurs in the transcript; the correction is in
`.txt`, `.docx`, `.md` and `.srt`, and is logged in the JSON `post_edits`.

Verdict key: **CERTAIN** (sentence cannot mean anything else, or the source settles it) ·
**PROBABLE** (the sense is clear and the substitute fits, but the audio is stable on the wrong word).

## Readings corrected

| Heard | Corrected to | Verdict | Basis |
|---|---|---|---|
| "Crawford's Mills" | **Cochran's Mill** | CERTAIN | The mill is on Cochran Mill Road, one mile south of the Bureau of Mines; the NRHP stone arch bridge there carries Cochran Mill Road over Lick Run. The A side's unresolved 'Cochrane View' is the same name. |
| "Cochrane still paid" | **Cochran still paid** | CERTAIN | Same family/place as Cochran's Mill (cold passes 2/3 'Cochran'). |
| "his name was matur" | **his name was William Maclure** | CERTAIN | William Maclure (1763-1840), 'father of American geology': Scottish, made a fortune and retired early, first geologic map of the United States 1809, crossed the Alleghenies about 50 times, settled at New Harmony, Indiana. |
| "if McClure or his settlers" | **if Maclure or his settlers** | CERTAIN | Same person; ASR renders the name two ways. |
| "what McClure didn't know" | **what Maclure didn't know** | CERTAIN | Same person. |
| "Freiburg School of Mines" | **Freiberg School of Mines** | CERTAIN | Bergakademie Freiberg, Saxony - the mining school of the period. 'Freiburg' is the ASR spelling of a different city. |
| "the old economy" | **Old Economy** | CERTAIN | Old Economy Village, Ambridge, Beaver County - the Harmony Society's third settlement. |
| "a full gate at Cumberland" | **a toll gate at Cumberland** | PROBABLE | The National Road's toll gate stood where the road began, at Cumberland, Maryland; cold passes give 'pole gate' / 'full gate'. |
| "a stone arch at Grasmere" | **a stone arch at Grantsville** | CERTAIN | The Casselman River Bridge, Grantsville, Garrett County, Maryland (1813-14): an 80 ft stone arch, the largest in America when built, on the National Road. |
| "the full freedom the full reposition" | **the period of coal deposition** | PROBABLE | Cold passes give 'coal repetition' / 'full reposition'; the sentence closes the coal-forming period. |
| "milwaukee hill and clarendon" | **the Monongahela at Clairton** | CERTAIN | Peters Creek discharges into the Monongahela River at Clairton; cold passes give '... and clareton'. |
| "snowden and lard up" | **Snowden and Library** | PROBABLE | Cold pass gives 'snowden and lard up'; the two places on Peters Creek are Snowden and Library. |
| "Atkins Run" | **Catfish Run** | PROBABLE | Catfish Run is a named Piney Fork tributary running through South Park park, past the meeting place; no 'Atkins Run' exists in the watershed. Cold passes give 'cactus run'. |
| "Bronzeville Road" | **Brownsville Road** | CERTAIN | Brownsville Road runs through Curry and Broughton; the A side has the same reading. |
| "Stanleyville" | **Finleyville** | CERTAIN | Finleyville, Washington County, at the south end of the gas line; cold passes 2/3 give 'finleyville'. |
| "Century Three Mall" | **Century III Mall** | CERTAIN | Century III Mall, West Mifflin. |
| "named from anarchy down in Washington" | **named from Amity, down in Washington County** | PROBABLE | Amity, Washington County, is an old village with surviving early buildings; cold passes give 'amity' 2/3, and another window gives 'the Emity arch'. |
| "those were gasoline" | **those were gas wells** | CERTAIN | Cold passes: 'those were gas wells' in the same exchange. |
| "a salt mix there for the buffalo" | **a salt lick there for the buffalo** | PROBABLE | He is explaining the name of Lick Run; cold passes give 'salt lake' / 'salt mix'. |
| "block mavericks" | **blockhouses** | CERTAIN | Blockhouses stood outside the fort; 'block mavericks' is not a word. |
| "mustard ball" | **musket ball** | CERTAIN | Musket balls, cast at the shot tower. |
| "first rest of the alligators" | **first west of the Alleghenies** | PROBABLE | Alliance Furnace (1789, Jacob's Creek) was the first iron furnace west of the Alleghenies; every cold pass garbles the phrase. |
| "This is the Williams Alliance Furnace over in the Westmoreland County near Jacob Street" | **This is the ruins of Alliance Furnace over in Westmoreland County near Jacob's Creek** | PROBABLE | Cold passes 3/3 give 'the ruins of Alliance Furnace ... near Jacob Street'. Alliance Furnace stood on Jacob's Creek, Fayette County - he says Westmoreland; the reading is kept and the county flagged. |
| "oakwell 12th Village" | **Hopewell Furnace Village** | PROBABLE | All three passes hear 'Oakwell Village ... Berks County'. The Berks County iron plantation that outlasted the rest, supplied Washington's army, and is a restored national historic site with costumed guides is Hopewell Furnace (1771-1883). |
| "that's my brother john barry was a metro just retired" | **that's, my brother John was a metallurgist, retired** | CERTAIN | Cold passes: 'My brother John was a metallurgist, retired'. |
| "telemiting horse tail" | **Calamites horsetail** | CERTAIN | Calamites, the tree-sized horsetail whose jointed stems he is holding; the A side has the same fossil as 'calamities'. |
| "wind spread of four or three feet" | **wingspread of four or three feet** | CERTAIN | Wingspan of the Carboniferous dragonfly (Meganeura). |
| "in birch county pennsylvania" | **in Berks County, Pennsylvania** | CERTAIN | The Daniel Boone Homestead is at Birdsboro, Berks County. |
| "mudstone or steel stone" | **mudstone or siltstone** | CERTAIN | Siltstone - the fine clastic rock between shale and sandstone. |
| "gray middle limestone" | **gray marine limestone** | PROBABLE | The middle unit of the cyclothem is the marine limestone. |
| "The most common rock type here is scale" | **The most common rock type here is shale** | CERTAIN | Shale; he goes on to say the miners called it slate, which shale is not. |
| "raised such things as lye and buckwheat" | **raised such things as rye and buckwheat** | CERTAIN | Rye and buckwheat were the frontier crops on acid clay soil. |
| "that dashing line" | **that dashed line** | CERTAIN | A dashed line on the map marks the fold axis. |
| "this corn around here is quite good" | **this coal around here is quite good** | CERTAIN | He is discussing the coal's sulfur content; 'coal' collapses to 'corn' in this capture too. |
| "right underneath the pole there" | **right underneath the coal there** | CERTAIN | Same coal-for-pole collapse the A side documents. |
| "right under the thin, thin core" | **right under the thin, thin coal** | PROBABLE | Thin coal seam above the clay. |
| "This is aphid right here" | **This is pyrite right here** | PROBABLE | Iron sulfide in a sulfur ball is pyrite; 'aphid' is the ASR form. |
| "some of the layers are dark green glasses" | **some of the layers are dark, glassy** | PROBABLE | Vitrain - the bright glassy coal bands. |
| "record all these streams here are abrading the peter's creek" | **all these streams here are a tributary of Peters Creek** | PROBABLE | The sentence introduces the stream map; the cold pass opens 'corner in the lower right corner there going past snowden ... and it flows into ... clareton'. |
| "of the early sellers settlers" | **of the early settlers** | CERTAIN | Stutter collapsed. |
| "It was torn It was torn down" | **It was torn down** | CERTAIN | Repeated segment head collapsed. |
| "Okay, thank you. Thank you." | **Okay, thank you.** | CERTAIN | Handover thanks collapsed. |
| "Bureau of Mines building and It was torn down" | **Bureau of Mines building, and it was torn down** | CERTAIN | Sentence boundary restored. |
| "There were a few other smaller gas mills" | **There were a few other smaller gas wells** | CERTAIN | He is talking about gas wells on the arch. |
| "Washington County, D.C., a little village" | **Washington County — a little village** | CERTAIN | The D.C. is an ASR artefact; Amity is in Washington County, Pa. |
| "how it gets this lame" | **how it gets its name** | CERTAIN | Cold passes 2/3 give 'how it gets its name'. |
| "the sellers needed" | **the settlers needed** | CERTAIN | Settlers, not sellers. |
| "have a sponge like that today in the comics" | **have swamps like that today in the tropics** | PROBABLE | Cold pass beam5+vad: 'we have swamps like that today in the tropics'; modern swamps are the living analogue he means. |
| "are now exceeded is" | **are now extinct** | CERTAIN | Cold passes: 'all these different species of trees are now extinct'. |
| "with the growth line that's calamities" | **with the growth line — that's Calamites** | CERTAIN | Calamites, the fossil horsetail. |
| "followed followed by 51" | **followed by 51** | CERTAIN | Repeated word collapsed. |
| "The third type is limestone, store, which would" | **The third type is limestone stone, which would** | PROBABLE | 'store' is the ASR form of 'stone'. |
| "it's It's really smooth" | **it's really smooth** | CERTAIN | Repeated segment head collapsed. |
| "from someplace. place." | **from someplace.** | CERTAIN | Repeated word collapsed. |

## Where his memory and the record disagree (transcript keeps his words)

| He said | The record |
|---|---|
| Alliance Furnace is "over in the Westmoreland County near Jacob's Creek" | Alliance Furnace (1789) stood on Jacob's Creek in **Fayette County**, about two miles above its mouth on the Youghiogheny. It was the first iron furnace west of the Alleghenies, and it supplied shot for General Anthony Wayne's 1794 campaign — exactly as he describes. [Pioneer iron industry in Western Pennsylvania](https://journals.psu.edu/wph/article/download/1553/1401/1401) |
| "the first brick building around here was 1764 in a blockhouse" | His date is unverified; the point he is making (a kiln needs several buildings to be worth firing) is sound. |
| "I believe it is 1794" of the National Road, after saying 1790 | The National Road was authorised in 1806 and begun at Cumberland in 1811; the Casselman arch is 1813-14. The "1794" appears to belong to the Brownsville Road / Red Stone Road he mentions next. Left as spoken. |
| "they produced armaments for George Washington in the Revolution" of Hopewell | Hopewell Furnace did supply iron for the Revolution; the National Park Service dates its operation 1771-1883. |
| "Instead of early settlers, we had early virgins" | All three cold passes return "virgins" and the room laughs: kept as spoken. The intended word is not recoverable. |

## Recovered from a failed read

The projector-and-lights exchange at 9:38-10:42 came back from the ASR as six repetitions of "Don't."
A cold pass over the same 64 seconds recovers audible dialogue — "if you turn that light off", "keep
the lights on", "try it again", "oh, now I have it", "we'll have to see it in just a minute", "very
good", "that's better". More than one voice is involved and they do not separate, so the recovered
words are carried as a bracketed stage direction instead of being attributed to a speaker.

## Unresolved (left as heard)

- 'the rocks of the tail masons' (17:08) - all cold passes give 'tail masons / tail mazes'; no formation or group name matches. Probably the top of the coal measures, left as heard.
- 'So that's the center of your addition, stack addition' (17:25) - no reading recovers this; the word after 'center of your' is lost.
- 'Chippenham Road' (19:41) - all three passes agree on the name, but no such road appears in South Park or Jefferson Hills on OpenStreetMap; the 12 Mile House stood at Brownsville Road's junction with it. Left as heard.
- 'this is typical screen which we're only going through prairie' (22:21) - unintelligible; he is naming the feature in the slide.
- 'to give you an idea of the weapon and the seminal' (19:01) - the words after 'idea of the' are not recoverable.
- 'Instead of early settlers, we had early virgins' (29:38) - all three passes hear 'virgins' and the room laughs; left as spoken.
- 'a Morgan-bound sandstone was built as a step-barring house in 1831' (23:32) - 'Morgan Run sandstone' is a probable reading of the stone, but the house's name is not recoverable; the 1831 / demolished-1878 dates stand.
- 'This is across from the South Park Contra building' (24:25) - the building's name is not recoverable.

