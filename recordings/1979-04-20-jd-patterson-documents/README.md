# J.D. Patterson — the 64-page typed transcript of the 1979 interview (papers, no audio)

A **papers-only item**: no sound recording belongs to this folder. It holds the typed transcript of the
J.D. Patterson interview — a library-bound typescript of 64 pages, read page-by-page from the scan — and
the vocabulary seed and ASR prompt that were built from it for the two cassette sides.

| | |
|---|---|
| **Document** | "James Douglass Patterson (And His Canine Friend, Trixie)" — oral interview, typed transcript |
| **Subject** | James Douglass Patterson, born 14 March 1904, of Patterson Road, Bethel Park, Pennsylvania |
| **Interviewer** | June Ellington |
| **Typist** | Mrs. T. R. Stump |
| **Recorded** | 20 April 1979 (stated on the typescript's own first page) |
| **Extent** | 64 PDF pages = 2 front-matter pages + 60 printed pages + a captioned photograph + a blank |
| **Words** | 18,639 of document text (18,906 with the transcription's front matter) |
| **Status** | Transcribed from the page images by reading; the two audio sides of the same interview are filed separately |

---

## 1. What the documents are

Four files, all carried here:

1. **`transcript-booklet.md`** (100,357 bytes, 18,639 words of document text) — the whole typescript, page by page, with a
   `## Page N` heading for each PDF page. The typescript alternates **Q.** and **J.** turns (281 and 284 of
   them) with occasional `June:` / `Jim:` at the head. It begins with the dedication page — an oval
   photograph of a small child beside a dog, captioned "JAMES DOUGLASS PATTERSON (And His Canine Friend,
   Trixie), Son of Mr. and Mrs. R. M. Patterson, and Grandson of James Douglass, Sr., Library" — and the
   interview starts on printed page 1.
2. **`transcription-seed.md`** (revision 2, 1,472 words) — the vocabulary and prompt seed for ASR of the
   two cassette sides, rebuilt from this transcription rather than from machine OCR so the spellings are
   the ones the pages carry: *Sampson* (not "Simpson"), *Foliart* (not "Follart"), *Detling* (not
   "Dotling"). It carries people, places, roads, businesses and terms, each marked *high* (corroborated in
   Upper St. Clair / Bethel Park sources), *document* (read from this transcript) or *low* (uncertain
   reading — check the page image).
3. **`transcription-seed.json`** — the same seed in machine-readable form: 39 people, 39 places, 7 roads,
   13 businesses, 13 terms, plus a 650-character `asr_prompt`.
4. **`whisper-initial-prompt.txt`** — that prompt as it was actually passed to the engine (651 bytes): the
   interview's identity, the place names (Patterson Road, Boyer Road, Brush Run Road, Irishtown Road,
   Logan Road, McMurray Road, McLaughlin Run Road, Thomas Road, South Park Road, Fort Couch Road, Bethel
   Church Road, Wiltshire, Rutherford Acres, Brookside, Fifeshire, Beadling, Peters Creek Church, Bethel
   Presbyterian) and the family names (Patterson, Fife, Douglas, Phillips, Foliart, Baldesberger, Stilley,
   Neff, Walters, Hultz, McCune, McMillan, Espy, Johnston, Ellington, Stump).

**A seed is a hypothesis generator, not evidence.** It biases the decoder so that "Fife" is not written
"Fyffe" and "Irishtown" not "Irish Town"; it must never be used to overwrite what a tape says. That rule is
stated in the seed file itself, and it is why the seed is filed with the document that produced it.

The three PDFs are **not** in this repository (8.8 MB, 310 KB and 318 KB); they stay on the archive NAS:

| file | size | sha256 (first 12) |
|---|---|---|
| `James Douglass Patterson - Library Booklet (64 pages).pdf` (the 600 dpi scan) | 8,774,636 B | `095519a3d987` |
| `… - transcript (typeset).pdf` | 309,781 B | `787c38f1b3aa` |
| `… - transcript (facsimile).pdf` | 317,921 B | `e571a00081c9` |

## 2. How the date is established

From the document, in print, twice:

> "Oral interview with Mr. J. D.Patterson, April 20, 1979
> Interviewed by June Ellington. Typist, Mrs. T. R. Stump" — printed page 1

and again in the running head of later pages: "Oral Interview - Mr. J. D. Patterson - April 20, 1979
(continued)". 20 April 1979 was a **Friday**.

This matters beyond this folder: the two cassette sides give only "April 20th" and state **no year**. The
typescript is the document that fixes 1979 for them, which is why `metadata.json` here records the full
date and the two audio items cite this folder in their `date_source`.

The source scan is dated 2026-10-21, and the collection folder 2026-10-18; both are digitisation dates.

## 3. How it was transcribed — and why not OCR

**By reading the page images, page by page.** The front matter says so plainly, and the reason is recorded
there too: an earlier tesseract pass over the same scan **scrambled line order**, substituted real names
("Peters Creek" became "Peters Greek") and silently dropped others — *Brush Run Road*, *Sampson*, *Detling*
never appeared at all. None of that is visible in the output as an error; it reads like prose. So the text
here is a human reading of the page images, and the earlier OCR is not reused anywhere.

**The typist's errors are preserved, not corrected.** Where the typescript prints a wrong or unusual
spelling it stays as typed, and the intended reading is recorded once in a section headed "Appendix A —
editorial notes" — which the front matter points to but which **is not in the document**: the 64 pages end
with a blank page and contain no appendix. That is a gap in the source, recorded here rather than filled in.

**Pagination.** The typescript's own printed numbers run 1–60; the PDF has 64 pages, so **PDF page =
printed page + 2**. The `## Page N` headings in `transcript-booklet.md` are PDF pages; citations to "printed
page N" are two lower.

## 4. What it covers

The same interview as the two cassette sides, and much more of it. A page map of the parts read for this
record:

- **Printed page 1** — the interview opens in the room: "I am June Ellington, and I here visiting with
  J. D. Patterson, or Jim Patterson"; he corrects her to "J. D."; 57 Boyer Road, and the Patterson Road
  house he was born in; his parents, **Etta Douglas** and **Richard Miller Patterson**
- **Printed page 1** — the Irishtown school story: a teacher struggling to explain a canyon, and a boy who
  had been shown one "over in Wilson's woods"
- **Printed page 7** — the old schoolroom: the windows, the seats along the side and back, "a big old coal
  heater in that back corner"
- **Printed page 24** — the Fife connection: Myra, who married Lawrence Fife, and Wiltshire Drive
- **Printed page 27** — the Johnstons of Bethel Church and their three boys, Bob, Jack and Jim
- **Printed page 33** — Taylorstown: $100 a month for eight months, the $10-a-month give-back, "$720.00" a
  year
- **Printed page 38** — "In 1916 when we came back from the west": two rooms down, a large room over
- **Printed page 39** — the 1916–17 building room by room: the cloakroom, the 7th and 8th grade room, the
  stairway, the high school room and the auditorium above
- **Printed page 41** — Bethel, Hillcrest, and the schools the children went to after
- **Printed page 42** — the war years: Liberty Bonds sold at the high school, and the music
- **Printed page 45** — Route 19 and the farms: "Was there the Higby farm, or the Stilleys?"

**Its extent does not match the tapes.** The two cassette sides hold about 8,700 words of transcript
between them; this typescript is 18,639. Whether it transcribes a longer recording than the two surviving
sides, a different sitting, or the same conversation with more of the room's talk, **is not established** —
the typescript is not time-stamped and the tapes are not paginated. Anyone reconciling the two should start
from that gap rather than assume the tapes are complete.

## 5. What is uncertain

- **The Appendix A it references does not exist** in the document, so the typist's errors are preserved
  without the key that was meant to explain them.
- **Relation to the audio** — as above, the typescript is more than twice the length of the two sides.
- **Place-name spellings that conflict** between the typescript and the tapes: the typescript's "Higby" and
  "Hilary" against the tapes' "Higbee" and "Hildy". The transcription keeps the typescript's spelling; the
  audio transcripts keep theirs. Neither has been forced onto the other.
- **The photograph on the dedication page** is described, not reproduced: a child beside a dog, captioned
  "Trixie". Nothing in the text identifies the child beyond the caption.
- **The scan file name** (`20261021153321.pdf`) is a timestamp, not a title; the booklet has no title page
  beyond the dedication.

## 6. Rights

No release is recorded for the typescript or for the interview it records. `metadata.json` carries
`rights.status: "unknown"` for that reason: the collection was digitised for the Historical Room by John
Decker in 2026, but `docs/RIGHTS.md` requires a release per item, and none is on file. The companion tape
side (`unknown-jd-patterson-side-b`) adds a further wrinkle — it announces that the recording is the
property of the **Upper St. Clair Historical Society** and for non-profit use only.

## 7. Files here

| file | what it is |
|---|---|
| `transcript-booklet.md` | The 64-page typescript, page by page. **Start here.** |
| `transcription-seed.md` | The vocabulary/prompt seed (revision 2) built from it |
| `transcription-seed.json` | The same seed as structured lists, with the ASR prompt |
| `whisper-initial-prompt.txt` | The prompt exactly as passed to the engine |
| `metadata.json` | Date and its source, speakers, rights; `kind: "documents"`, `sides: []` |
| `checksums.sha256` | sha256 of every file in this folder |
| `README.md` | This file |

There is no audio here and none is missing: this item is paper. The sound recordings of the same interview
are `unknown-jd-patterson-side-a` and `unknown-jd-patterson-side-b`.

## 8. Citing it

> Patterson, James Douglass. *Oral interview with Mr. J. D. Patterson* (typescript, 60 pp.). Interview by
> June Ellington, 20 April 1979; typed by Mrs. T. R. Stump. Historical Room, Bethel Presbyterian Church:
> scanned 21 October 2026. Transcription, 18,639 words.

Cite the **printed page number** (PDF page − 2) as well as the heading, since the two differ by two.

## 9. Related material in the collection

- **`unknown-jd-patterson-side-a`** and **`unknown-jd-patterson-side-b`** — the two cassette sides of this
  interview, transcribed from the audio. Both take their year from this typescript.
- **1971-07-15 A.D. White** — a different interview in the same room; the Stilley, Fife and Gilfillan
  families appear in both collections.
