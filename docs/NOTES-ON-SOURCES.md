# Notes on the sources

Things that are true about this material but do not belong in any single recording's folder: places
where two tapes disagree, where a document and its own tape disagree, and defects in the source files
that were recorded rather than smoothed over.

None of these have been "corrected". Oral history is evidence about what a person remembered, not only
about what happened, and two witnesses contradicting each other is itself a finding. Where a conflict
affects a specific passage, it is also noted in that recording's `README.md` and `notes-*.md`.

## Where the tapes contradict each other

**George Marshall's call to Bethel — 1832 or 1833.** A.D. White (31 October 1971) says Marshall was
called in **1833**; Ann Connor (17 October 1971, and again in *History of George Marshall and other
Ministers*) says **1832**. Both are speaking from records they know well; neither reading has been
harmonised, and the difference may be between the call and the installation rather than a
misremembering. Anyone dating Marshall's pastorate from this collection should cite which tape they are
using.

**When John McMillan began preaching — 1775 or ordained 1776.** The two 1983 recordings disagree: one
has him preaching from **1775**, the other places his ordination in **June 1776**. Both are left as the
speakers said them.

**Ann Connor's own birth year — 1803 or 1806.** Inside the *George Marshall Class* she gives both, in
passing, without noticing. This is a self-contradiction on the tape, not a transcription error.

**The Bethel fire — 1899 or 1909.** In the Edna Croco interview the year is undecided; the passage is
left as heard.

## Where a document and its tape disagree

**The J.D. Patterson typescript is more than twice the interview.** The printed typescript runs 18,639
words; the two tape sides carry 8,698 spoken words (4,491 + 4,207). The typescript says it is the same
interview. Either it includes material from a part of the conversation that was not recorded, or it was
edited up — the difference is unexplained, and the typescript also refers to an **Appendix A** that is
not among the 64 scanned pages. The scan is probably incomplete.

**One tape side announces ownership.** The Patterson Side B cassette states that the recording belongs
to the Upper St. Clair Historical Society and is for non-profit use. The three Patterson items and
*Ann Connor — Sides A and B* are nonetheless published as **public domain** on the rights holder's
release (John Decker), with that announcement recorded in each one's `rights.basis` rather than
silenced. If the Society, or any participant or their family, wants an item changed or removed, that is
honoured without argument — see `RIGHTS.md`.

**Dinsmore, 31 October 1971 — a second file of the same performance.** The source folder holds
`second recording.m4a` (1,858.304 s, a different hash from the master). Measured against the master it
is the same performance with a drifting lag, losing a second by the end — a second capture of one
playback, not a second event. It is not transcribed; only the master is.

## Dates that rest on a filename

Two items have no slate and no spoken date, and their date comes only from the original capture
filename recorded by the digitizer:

- *Ann Connor — the Reverend John McMillan*, `Ann-Connor John McMillian 9-25-83`
- *Valentine, Maits and Snowden*, `9-25-83`

Nothing in either tape would contradict a wrong date, which is why each `date_source` says so plainly.
A cassette label would settle both.

By contrast, four items date themselves on the tape (15 July 1971, 6 November 1977, 13 September 1983,
20 April 1979 by typescript), and two carry a written cassette label (`10.17.71`, `10.31.71`).

## Defects in the source files, recorded not repaired

Found while packaging; all left as they are, with the transcript standing as the authority:

- **Edna Croco:** the transcription JSON's `meta.unresolved` list still carries a "Weichmann" reading
  that a *certain* `post_edit` had already resolved to **Wycoff**. Word counts also drift by a word or
  two between the JSON, the `.md` and the notes (2,943 / 2,946 / 2,947).
- **History of George Marshall:** the notes give the end of speech as "31:50.3", which is past the end
  of a 31:44 file; the cue sheet supports **30:50.3**.
- **Allegheny County Geological and Mining lecture:** Side A's notes claim "44 corrections" while its
  JSON holds **48**; Side B's `.md` header claims meeting-clock timecodes while its `.srt` is 0-based;
  and the notes describe a "thank you, Martha … Bob" handover that the filed text does not contain.
- **John McMillan:** the source is self-contradictory about a trailing "Thank you." at 31:05 — the
  `.srt` has it, the `.md` and `.txt` do not, and the notes list it as both removed and kept. It is
  reproduced as received and should not be quoted.
- **Digitisation dates:** the Needlepoint folder gives two (file mtime 2026-10-18 against "digitised
  2026-10-19" in its document header), and the McMillan `date_digitised` (2026-10-20) is later than the
  collection's capture date with no explanation.

None of these change what was said. All of them change what a reader should trust the surrounding
paperwork for, which is exactly why they are written down here instead of quietly fixed.
