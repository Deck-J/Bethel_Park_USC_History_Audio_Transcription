# Allegheny County Geological and Mining lecture — transcription record

Recording stem: `Allegheny County Geological and Mining lecture`. Every file in this folder carries that stem; this note is the
working record behind the document.

## What this is

A **21 m 25 s (1,284.78 s) talk on the geology and coal-mining history of the South Hills of
Allegheny County**, given by an older man — a former miner ("all the ones that were there when I
worked in 1933, and here before World War II") who is also an assured local geologist — working
through a set of maps, photographs and slides. He is describing, in order: the Pennsylvanian
reference section at the cliff opposite the Point (Rogers, 1840); a geologic map of Allegheny
County and its Conemaugh / Monongahela / Allegheny formations; the Pittsburgh coal seam and the
Redstone and Waynesburg seams above it; the Freeport sandstone problem; Ohiopyle and McConnells
Mill; the U.S. Bureau of Mines experimental mine at Bruceton; the railroads (Wabash, B&O) and
Brownsville Road at Curry; the Snowden post office renamed Broughton; Broughton School and the
Miller homestead; the Horning mine (1926 explosion, the 1930s strike, *Black Fury*); the Gibson
patch; Montour No. 10 at Library; Triphammer Road and the forge on Piney Fork; and finally why
South Park could be bought — the coal lay deeper there.

**Speaker.** One voice carries the talk. He refers to "this lady" (who had spoken earlier) and to
"Don" in the third person, so at least two other people were present, but no second voice separates
cleanly in the ASR and none is labelled. The tape never states his name. **Date: unknown** — no
date on the tape or the filename. Content places it after 1970 (mines closed, "before World War II"
as memory, a Consol research laboratory at Library) and probably after 1990.

## The source

`Allegheny County Geological and Mining lecture.m4a` — ALAC, 48 kHz, 2 channels, 51,772,077 bytes, 1,284.778667 s
(md5 `c53f4c245364d68736414c3e1c2c64b5`, identical to `Source original/Allegheny County Geological and Mining lecture.m4a`).
Lossless capture, so the master is unchanged as received: no denoise, no gain, no remux.

- The **last 84.8 s carries no speech**: 1,200-1,285 s measures -84.3 dB mean / -47.4 dB max. The ASR
  run stopped at 1,200 s for that reason and nothing was lost.
- The applause-and-thanks tail at 1,058-1,108 s is real audio (-39.8 dB mean, -6.6 dB peak) — it is
  applause, and the only words recovered there are "Amen. / Thank you."

## Method

- **Whisper large-v3** (Systran faster-whisper 1.2.1, CTranslate2 int8, 14 CPU threads), English,
  beam 5, `condition_on_previous_text=False`, word timestamps, **no initial prompt** (unseeded).
- Chunked at ~120 s (16 chunks), boundaries snapped to the quietest 10 ms frame, decoded by ffmpeg to
  float32 numpy arrays (PyAV in this build rejects the `metadata_errors` kwarg faster-whisper passes).
- Quality: 176 segments, 2,622 words, **mean word probability 0.852**, 9.9 % of words below 0.5.
- **Cold pass:** 18 windows (the doubtful passages) re-transcribed with `initial_prompt=None` at
  beam 5, beam 1 and beam 5 + VAD — 54 transcriptions in all. Every verdict in
  `FACT-CHECK - Allegheny County Geological and Mining lecture.md` names what the passes returned.
- Stutters collapsed (`the the` -> `the`), lone lowercase `i` -> `I`. Nothing else tidied: hesitations
  and false starts are left as spoken.

## What the cold pass changed, and what it refused to change

44 corrections are applied and each one is logged in `Allegheny County Geological and Mining lecture.json` -> `post_edits` with
its pattern, replacement, count, certainty and reason. Three habits of this capture drove most of them:

1. **"Coal" collapses to pole / foal / foam, and "seam" to scene / seed.** Once the cold passes
   returned "coal" and "seam" in the identical sentences, every instance could be fixed together.
2. **"Snowden" collapses to "god" / "Godden" / "drowden".** The post-office story — Snowden renamed
   Broughton so mail would stop going to the other Curry, Pennsylvania — only reads once the name is
   put back.
3. **Names resolve to real places only with the local record.** Conemaugh (not "Ponybaugh"),
   Monongahela (not "Longahail"/"Palonga hill"), Brownsville (not "Bondville"), Bruceton (not
   "Brewstone"), Horning (not "Hoarding"/"morning"/"horny"), Musmanno, Nuremberg, Paul Muni,
   Triphammer Road, Lindhart, Gibson.

**Where the audio beat the books:** the theatre is written **"Carroll Theater"** because all three
cold passes return it twice; the Western Pennsylvania Coalfields survey says only that *Black Fury*
was "shown at the nearby Broughton Theater". The tape is the primary source, so his words stand and
the discrepancy is recorded, not corrected.

**Where his memory and the record disagree, the transcript keeps his words** and the FACT-CHECK
records the difference: Broughton School "1927" against 1929; the strike "1937" against a 1927 cold
pass and a documented 1928; the Pittsburgh Coal Company "headquarters" at Library, which was
downtown; the *Black Fury* "novel" before the film, when the novel is 1966; and "closed for two
years ago … opened last December", which fits no documented date for Montour No. 10 (closed 1957).

## Files

| File | What it is |
|---|---|
| `Allegheny County Geological and Mining lecture.txt` | the transcript, one labelled turn per paragraph (source of truth) |
| `Allegheny County Geological and Mining lecture.srt` | timed subtitles, cue per ASR segment, corrected |
| `Allegheny County Geological and Mining lecture.json` | provenance: raw segments + word probabilities (untouched), `paragraphs`, `post_edits` |
| `Allegheny County Geological and Mining lecture.docx` / `.md` | the document, both built from the `.txt` with identical arguments |
| `Allegheny County Geological and Mining lecture.mp3` | 192 kbps stereo listening copy |
| `Allegheny County Geological and Mining lecture (portable).mp3` | mono 64 kbps transfer copy, full length, nothing cut |
| `Allegheny County Geological and Mining lecture.m4a` | the master, unchanged |
| `Source original/` | the untouched capture as received (same md5) |
| `FACT-CHECK - Allegheny County Geological and Mining lecture.md` | every doubtful reading, its verdict and its source |

## Rebuild

The `.txt` is the source of truth; the `.docx`/`.md` are build products. After any transcript edit,
rebuild both from the `.txt` rather than editing the document:

```bash
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_docx.py \
  "Allegheny County Geological and Mining lecture.txt" "Allegheny County Geological and Mining lecture.docx" \
  --title "Bethel Presbyterian Church" --subtitle "Historical Room - Oral History" \
  --byline "LECTURER | geology and coal-mining talk | 21 min 24 s | date unknown" \
  --main-speaker LECTURER
python3 /opt/data/skills/media/archival-voice-transcription/scripts/make_md.py \
  "Allegheny County Geological and Mining lecture.txt" "Allegheny County Geological and Mining lecture.md" --verify-docx "Allegheny County Geological and Mining lecture.docx" \
  --title "Bethel Presbyterian Church" --subtitle "Historical Room - Oral History" \
  --byline "LECTURER | geology and coal-mining talk | 21 min 24 s | date unknown" \
  --main-speaker LECTURER
```

Verification run at build time: `verify_md_docx.py` -> MATCH (32 paragraphs, 2,644 words both
containers, 32 label runs); `make_md.py --verify-docx` -> MATCH.

## Unresolved

Listed in the JSON `unresolved` and in the FACT-CHECK: "A lot of stars at Bob Zanesburg" (3:20, a
permanent gap), "Cochrane View" (15:2x), "Dawson's tiny fort", "two old firefighters" near Houston,
the old family names "McElhaney and Siklum to get me, and Martin", "the amity and the climb" (gas
line), "first Hawkins Mill", and the "Kidu" family mine at Catfish Run.

## Settled by the B side (added when the other side arrived)

The second side of the same meeting was transcribed later and is filed as
`… - B side` with its own NOTES and FACT-CHECK. It closes three of the gaps listed above:

- **"Cochrane View" (15:2x)** -> **Cochran Mill Road**. The B side names the mill, places it one mile
  south of the Bureau of Mines building and dates its demolition to 1978, which is exactly where
  Cochran Mill Road runs; the NRHP stone arch bridge on that road carries it over Lick Run.
- **"the amity and the climb" (gas line)** -> **Amity** and the **fold axis**. The B side has "named
  from Amity, down in Washington County" and "the Amity arch or anticline", with more than 100 gas
  wells drilled along it from Finleyville past Hawkins Mill and Century III Mall to Homestead.
- **"first Hawkins Mill"** -> confirmed as a place on that same gas line, so the A-side reading stands.

See `(both sides).srt` for both sides on one continuous timeline (A's 175 cues, then the B side's
334 offset by this side's 1,284.778667 s; 509 cues, monotonic, 91.9 s gap at the join).

---

# Appendix — the FACT-CHECK, copied verbatim

`FACT-CHECK - Allegheny County Geological and Mining lecture.md` lives in the archive folder and is
reproduced here in full so that every doubtful reading, its verdict and its source travel with the
transcript. Nothing in it has been edited.

# FACT-CHECK — Allegheny County Geological and Mining lecture

Stem: `Allegheny County Geological and Mining lecture`. Every reading below was checked against published geology, local
mining history or a gazetteer, and against three cold re-transcriptions of the passage
(beam 5, beam 1, beam 5 + VAD, `initial_prompt=None`). "Applied" means the correction is in
`Allegheny County Geological and Mining lecture.txt`, and is logged in `Allegheny County Geological and Mining lecture.json` -> `post_edits`.

Verdict key: **CERTAIN** (sentence cannot mean anything else) · **PROBABLE** (sense is clear and
the substitute fits the register, but the audio is stable on the wrong word) · **GAP** (re-listened;
nothing recoverable).

## Formations and seams

| Heard | Corrected to | Verdict | Basis |
|---|---|---|---|
| "Ponybaugh Formation" | **Conemaugh Formation** | PROBABLE | Northern Allegheny County is Conemaugh, "generally not mineable" with thin seams — exactly what he describes. All three cold passes return "Ponybaugh", so this is a reading from the geology, not from the sound. [PA DEP ch.2](https://files.dep.state.pa.us/mining/District%20Mining/DistrictMinePortalFiles/Beneficial_Use/10_CHAPT_2/Chapter_2_final.pdf) |
| "Longahail Formation" | **Monongahela Formation** | CERTAIN | Southern half of the county, two-to-three workable seams. [Monongahela Group](https://en.wikipedia.org/wiki/Monongahela_Group) |
| "Palonga hill formation" | **Monongahela formation** | CERTAIN | "Palonga hill" is Monongahela. Its top is the Waynesburg coal — which is what he says next. |
| "Pittsburgh pole seam", "workable foal", "this lone single pole", "the pole is a little deeper" | **coal** | CERTAIN | The model renders "coal" as *pole / foal / foam* throughout this capture; cold passes give "coal" in the same sentences. [Pittsburgh coal seam](https://en.wikipedia.org/wiki/Pittsburgh_coal_seam) |
| "third big scene", "two chains" | **seam** | CERTAIN | Same substitution class. |
| "the Waynesburg fall" | **the Waynesburg coal** | CERTAIN | Waynesburg coal (No. 11) marks the top of the Monongahela Group. [USGS DMT08](https://ngmdb.usgs.gov/Info/dmt/docs/DMT08_McColloch-J.pdf) |
| "redstone seam … near Bondville … a fort in the Indian days" | **Redstone seam … near Brownsville** | PROBABLE | Redstone coal is named for Redstone Creek at Brownsville; Fort Burd (1759) stood on the hill above the town. The audio is stable on "Bondville". [USGS Geolex](https://ngmdb.usgs.gov/Geolex/Units/Redstone_3510.html) · [Brownsville](https://en.wikipedia.org/wiki/Brownsville,_Pennsylvania) |
| "tree fork … overlaid by thick sandstone" (Allegheny Formation) | left as heard | GAP | The Allegheny Formation's workable beds are Clarion, Kittanning and Freeport; "Freeport" is the likely word (cold passes give "streetport"), but no pass returns it cleanly. Not changed. [USGS Bull. 873](https://pubs.usgs.gov/bul/0873/report.pdf) |
| "ohio pond" / "mcconnell's hill" | **Ohiopyle** / **McConnells Mill** | CERTAIN / PROBABLE | Ohiopyle's falls pour over Pottsville sandstone. McConnells Mill is a different rock story — a glacial-outburst gorge in Slippery Rock Creek, not a basal-Pennsylvanian ledge — so the comparison is his, and mildly wrong. [DCNR](https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/mcconnells-mill-state-park/history) |

## Places, mines and roads

| Heard | Corrected to | Verdict | Basis |
|---|---|---|---|
| "halfway between Hawkinsville and Brewstone" | **halfway between Hawkins Mill and Bruceton** | PROBABLE | Cold passes 2/3 return "Hawkins Mill"; no Hawkinsville exists in Allegheny County. Bruceton is the U.S. Bureau of Mines Experimental Mine, opened 1910 on land leased from Pittsburgh Coal. [Experimental Mine](https://en.wikipedia.org/wiki/Experimental_Mine,_U.S._Bureau_of_Mines) |
| "the government mine … started in the early 1900s … now a National Historical Mining … landmark" | **U.S. Bureau of Mines Experimental Mine, Bruceton** | CERTAIN | Opened 1910; NRHP 1974; now the Bruceton Research Center (NETL/NIOSH/MSHA). He is right that it can be visited — on open days, not daily. [NIOSH](https://www.cdc.gov/niosh/bulletin/2021/bruceton-research-center.html) |
| "the wabash railroad", "the bno", "the V&O" | **the Wabash Railroad**, **the B&O** | CERTAIN (B&O) | Cold passes return "B&O" twice and "bno" once. The Wabash here is the Wabash Pittsburgh Terminal Railway (1904), later the Pittsburgh & West Virginia — "the Wabash" locally. [Wabash Pittsburgh Terminal](https://en.wikipedia.org/wiki/Wabash_Pittsburgh_Terminal) |
| "Brodsville Road" | **Brownsville Road** | CERTAIN | The road through Curry and Broughton. |
| "Curry Station" | left as heard | AMBIGUOUS | Curry was Pittsburgh Terminal Railroad & Coal Co.'s No. 5 patch on Brownsville Road, so a station there is plausible, but no source names one. [Pittsburgh Coalfield survey](https://coalcampusa.com/westpa/pittsburgh/misc/pittmisc2.htm) |
| "a large general store there called Pines" | left as heard | GAP | No Pines/Pyne store found in Curry. Library had a Champion Store Inc. company store. |
| "drowden … but god really was the name of the post office" | **Snowden** | CERTAIN | Snowden was the post office and the township (renamed South Park in 1966); the model dropped the name to "god"/"Godden" in every pass. |
| "there was a quarry Pennsylvania" | **there was a Curry, Pennsylvania** | PROBABLE | Broughton was originally Curry — renamed to end confusion with Curry Hollow and the Curry in Blair County. The audio says "quarry" in all passes; the postal story he tells is otherwise exactly right. [Broughton](https://en.wikipedia.org/wiki/Broughton,_Pennsylvania) |
| "Perry gets its name from the Hurry Farm" | "**Perry** gets its name from the **Curry farm**" | GAP / PROBABLE | 2/3 passes keep "Perry", one gives "Curry Farm". The family is Curry; "Perry" itself is not a place near South Park and is left as heard. |
| "the horny farm … the morning mine", "Hoarding" | **Horning** | CERTAIN | Horning farm, Horning mine and patch town. [Horning](https://en.wikipedia.org/wiki/Horning,_Pennsylvania) |
| "another mine on the Linhart" | **Lindhart** | PROBABLE | Cold passes: "Lindhart" 3, "Linhart" 2. No published spelling found. |
| "the Jason farm, the Gibson" | **the Jason farm, the Gibson** (patch town) | CERTAIN | Gibson was a coal patch — mine opened by the Hillman Gas Coal Co. c.1921. "Intermitted" is **intermarried** (all three passes). [Pittsburgh Coalfield survey](https://coalcampusa.com/westpa/pittsburgh/misc/pittmisc2.htm) |
| "over a library" | **over at Library** (Montour No. 10) | CERTAIN | Pittsburgh Coal Co. opened Montour No. 10 and its mining town in 1919; closed 1957, briefly reopened in the 1970s; Consol ran a research laboratory at Library into the 21st century. [Library / Montour No. 10](https://coalcampusa.com/westpa/pittsburgh/library/library.htm) |
| his claim that the mine was "the headquarters of the Pittsburgh Coal Company" | left as spoken | DISCREPANCY | Pittsburgh Coal's headquarters were downtown; Montour No. 10 was a mine and patch, not a head office. Recorded in NOTES rather than changed — it is what he said. |
| "when that mine closed for two years ago … opened that just last december" | left as heard | GAP | The arithmetic does not work for any documented date (Montour No. 10 closed 1957; the Consol lab ran into the 2000s). Left as spoken. |
| "Tripham" / "where Tip Amber Road goes down" | **Triphammer Road**, from the triphammer of the forge | CERTAIN | The VAD pass returns "where tip amber road goes down"; a triphammer was the forge hammer that gives the road its name. [Triphammer / Piney Fork](https://pghbridges.org/glassport/0586-4459/triphammer_pineyfork.htm) |
| "catfish run comes into a piney fork" | **Catfish Run comes into Piney Fork** | CERTAIN | Catfish Run empties into Piney Fork above the Bethel Park–South Park sewage plant. [Peters Creek Watershed](https://www.phms.peterscreek.org/BP-SPSewagePlant.html) |
| "owned by the kidu family" | left as heard ("Kidu") | GAP | Passes give Kidu / Kidoo / Cadoux. No such mine or family found in the county mine indexes. |
| "first Hawkins Mill" | **Hawkins Mill** | PROBABLE | Same name as in the Bruceton sentence; the mill in the photograph. |
| "the amity and the climb" (gas line) | left as heard | GAP | No Amity or Climb pipeline serving South Park found. Amity, Washington County, exists and may be the word behind it. |
| "built around 1927" (Broughton School) | left as spoken | DISCREPANCY | The district's Broughton School was erected in **1929** (demolished 2014). He says 1927; a spoken number is not corrected. Cold passes also hear "Godwin School", but the school in Broughton is documented as Broughton School. [South Park School District](https://en.wikipedia.org/wiki/South_Park_School_District) |
| "no lines on it … the pole is a little deeper" | **no mines on it … the coal is a little deeper** | CERTAIN | Coal deeper under the South Park tract is why the county could buy 2,013 acres of farmland in the late 1920s (dedicated 1927). [South Park ecological assessment](https://acparksfoundation.org/wp-content/uploads/2020/03/South-Park-Ecological-Assessment-Full.pdf) |

## People and the Black Fury story

| Heard | Corrected to | Verdict | Basis |
|---|---|---|---|
| "Michael Moussoumano", "judge at the loonberg trial" | **Michael Musmanno**, **Nuremberg** | CERTAIN | Presiding judge at the Nuremberg Einsatzgruppen trial, 1947. [Musmanno](https://en.wikipedia.org/wiki/Michael_A._Musmanno) |
| "wrote a novel about that strike called Black Fury … movie that started Paul Munich" | **Black Fury**, film 1935, **starring Paul Muni** | CERTAIN (film) / DISCREPANCY (novel) | The 1935 Warner film starred Paul Muni and used Horning miners as extras. Musmanno's *Black Fury* **novel** appeared in 1966, not before the film — his earlier treatment was the short story "Jan Volkanik". [Black Fury (novel)](https://en.wikipedia.org/wiki/Black_Fury_(novel)) |
| "shown in the Carroll Theater down in Broughton" | **left as "Carroll Theater"** | KEPT | All three passes return "Carroll Theater", twice in the same passage — this is what he said. The mining survey records the film as "shown at the nearby Broughton Theater", i.e. in Broughton; it does not name the house. Audio outranks the secondary source. [Horning](https://coalcampusa.com/westpa/pittsburgh/horning/horning.htm) |
| "1926 they had a terrible explosion … 1937 they had a strike" | 1926 explosion confirmed; **strike: 1927** | PARTLY | The Feb 3, 1926 explosion killed 19 miners and a boss. Cold passes give 1927 for the strike, not 1937. Left as heard and flagged. |
| "when I worked in 3-3" | **when I worked in 1933** | CERTAIN | The VAD pass returns "when I worked in 1933, and here before World War II". |

## Still open after the full cold pass

- **"A lot of stars at Bob Zanesburg"** (3:20) — stable across all passes and meaningless; there is
  no Zanesburg in Pennsylvania (only Zanesville, Ohio). PERMANENT GAP, left as heard.
- **"goes over to Cochrane View"** (15:2x) — passes give Cochrane View / Cocteau Hill / Cockrell
  Hill / Cawthorne Hill. Unstable, no place found. Left as heard.
- **"Dawson's tiny fort"** — passes give "Dawson's Piney Fort" / "Goss's Piney Fort". Left as heard.
- **"two old firefighters"** (near Houston) — passes give "two old fire fighters" / "two old fair
  one"; probably two old openings or drifts, not recoverable.
- **"McElhaney and Siklum to get me, and Martin"** (the old families) — not recoverable.


