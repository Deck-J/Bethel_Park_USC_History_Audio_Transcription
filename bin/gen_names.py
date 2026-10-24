#!/usr/bin/env python3
"""Build docs/NAMES.md — a finding aid to the people named across the collection.

This is generated, not curated: it reads every transcript in the repository and indexes capitalised
person-name patterns, giving each name the recordings and lines where it appears, with a link to the
line on GitHub. It is a way *into* the transcripts, not an authority on them — the transcripts are the
authority, and a name that survives the filter here has not been checked against any outside record.

Two things keep the noise down:
  * a name must look like one (a capitalised run of 2-3 tokens, or a known surname), and
  * it must occur at least twice, or be named in a recording's metadata (speakers are always included).

Excluded: speaker labels (WHITE:, INTERVIEWER:), the stoplist below, and tokens inside `[brackets]`
(the editors' own annotations).
"""
import json
import pathlib
import re
import sys
from collections import defaultdict

import indexlib                    # shared reading side: same normalisation as the places index

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "NAMES.md"
REPO_URL = "https://github.com/Deck-J/Bethel_Park_USC_History_Audio_Transcription/blob/main"

# Words that start sentences in this material and are not names.
STOP = set("""The A An And But So Well Yes No Oh Now Then There This That These Those He She It They We You I
If When What Why How Who Whom Which Where Because As At In On For To Of With From By About After Before
During Until While Since Though Although However Also Just Only Even Still Yet Not Nothing Something
Anything Everything Everyone Someone Nobody All Both Each Every Few Many Most Some Such Than Too Very
Can Could Did Do Does Had Has Have Is Was Were Will Would Shall Should May Might Must
Mr Mrs Miss Ms Dr Reverend Rev Deacon Elder Pastor Father Sir Lady Lord
Chapter Page Appendix Interview Transcript Note Notes Summary Recording Side Tape
Q J June Jim ANN WHITE INTERVIEWER NARRATOR GUEST UNKNOWN HOST
Between Beside Among Through Against Without Within Along Across Behind Beyond Under Over
January February March April May June July August September October November December
Monday Tuesday Wednesday Thursday Friday Saturday Sunday
Bethel Presbyterian Church Historical Room Library
God Lord Christ Jesus Bible
German English Irish Scotch Scottish American Indian
North South East West Upper Lower Old New
School Church Cemetery Road Street Avenue Hill Creek Run Hollow Station Market Store House Hall
Lane Farm Mill Bridge Field Woods Park Township County City Village Borough
One Two Three Four Five Six Seven Eight Nine Ten Hundred Thousand
University College Seminary Society Association Company
Civil War Revolution Rebellion Christmas Easter Sunday Monday
Yes No Maybe Sure Right Correct Wrong True False
Well So And But Because Since Then
""".split())

NONPERSON = set("""Family Friend State County Church School Company Lumber Boulevard Road Street Avenue
Greenhouses Farm Mill Creek Hollow Station Cemetery Park College University Seminary Society Association
Historical Room Library War History Bible Streetcar Hotel Bank Theater Theatre Restaurant Store Market
Center Centre Building House Hall Inn Tavern Bridge Field Woods Township City Village Borough River Lake
County's Club Committee Board Class Lecture Interview Tape Side Chapter Page Appendix Street Railway Station
""".split())

# Local surnames: every family this collection actually names. A candidate must end in one of these (or
# be one of these alone) to be indexed, which is what keeps places like "Castle Shannon" and "Fort Couch"
# out. Extend it when a new recording brings a new family; the gate cannot check this for you.
SURNAMES = {
    "Connor", "White", "Marshall", "McMillan", "Patterson", "Croco", "Tanner", "Snowden", "Maits",
    "Valentine", "Douglas", "Gilfillan", "Espy", "Latimer", "Green", "Vance", "Miller", "Millar",
    "Lee", "Graham", "Simpson", "Stockton", "Clark", "Woods", "Wycoff", "Reiter", "Tidball", "Wolfe",
    "Strobl", "McCully", "Stilley", "Murray", "Fife", "Phelan", "Neville", "Stump", "Ellington",
    "Baldesberger", "Beadling", "Rutherford", "Poellot", "McDowell", "Sampson", "Foliart",
    "Johnston", "Acheson", "Hanna", "McCormick", "Dinsmore", "McKee", "Lyle", "Baird", "Cochran",
    "Cole", "Waite", "Phillips", "McNary", "McMurray", "McCune", "Wicks", "Stutt", "Edgar", "Walter",
    "Duncan", "Bell", "Cannon", "Carson", "Craig", "Ferguson", "Fulton", "Gibson", "Henderson",
    "Kerr", "Knox", "McClure", "McConnell", "McLaughlin", "Porter", "Reed", "Reid", "Ross",
    "Scott", "Sterrett", "Todd", "Wallace", "Wilson", "Young", "Black", "Brown", "Campbell",
    "Davis", "Evans", "Harris", "Jackson", "Jones", "Kelly", "Moore", "Murphy", "Quinn", "Riley",
    "Taylor", "Thomas", "Walker", "Ward", "Watson", "Wright", "Stop",
}

PLACES = {"Castle Shannon", "Fort Couch", "Drake Stop", "Upper St. Clair", "Bethel Park"}

NAME_RE = re.compile(
    r"\b((?:Mc|Mac|O'|De|Van|Von|St\.? )?[A-Z][a-z]{2,}(?:[-'][A-Z][a-z]+)?)"
    r"(?:\s+((?:[A-Z]\.\s+)*)((?:Mc|Mac|O'|De|Van|Von|St\.? )?[A-Z][a-z]{2,}(?:[-'][A-Z][a-z]+)?))?"
)

LABEL_RE = re.compile(r"^(?:[A-Z][A-Z _]{2,}|Q|J|June|Jim):\s*")


def iter_transcripts():
    for folder in sorted((ROOT / "recordings").iterdir()):
        if not folder.is_dir():
            continue
        meta_p = folder / "metadata.json"
        if not meta_p.is_file():
            continue
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
        for f in sorted(folder.glob("*.md")):
            # transcripts only: notes and READMEs discuss names, they are not where they are mentioned
            if not (f.name.startswith("transcript-") or f.name.startswith("appendix-")):
                continue
            yield folder, meta, f


def line_hits(path):
    """Yield (line_no, candidates) for one transcript file, over indexlib's normalised lines."""
    for i, line in indexlib.iter_lines(path):
        found = []
        for m in NAME_RE.finditer(line):
            first, mid, second = m.group(1), m.group(2) or "", m.group(3)
            if first in STOP:
                continue
            if f"{first} {second}" in PLACES:
                continue
            if second and second not in STOP and second not in NONPERSON and second in SURNAMES:
                found.append(f"{first} {mid.strip() + ' ' if mid.strip() else ''}{second}".strip())
            elif first in SURNAMES and not second:
                found.append(first)
        for n in found:
            yield i, n


def main():
    mentions = defaultdict(list)          # name -> [(folder, file, line)]
    speakers = {}
    for folder, meta, f in indexlib.iter_transcripts():
        for name in (s.get("name") for s in meta.get("speakers", [])):
            if name and not name.lower().startswith("unidentified"):
                speakers.setdefault(name, []).append((folder.name, None, None))
        for line_no, name in line_hits(f):
            mentions[name].append((folder.name, f.name, line_no))

    # keep: >=2 mentions, or a stated speaker; drop possessives/plurals duplicating a base name
    rows = []
    for name, hits in mentions.items():
        if len(hits) < 2 and name not in speakers:
            continue
        files = sorted({(h[0], h[1]) for h in hits if h[1]})
        rows.append((name, hits, files))

    rows.sort(key=lambda r: r[0].lower())

    lines = [
        "# Names",
        "",
        "A finding aid to **who is named** in these transcripts, and where. Generated by",
        "`bin/gen_names.py` from the transcripts themselves, so it can be rebuilt and cannot drift.",
        "",
        f"**{len(rows)} names**, each linked to the lines that mention them. Links open the transcript on",
        "GitHub at that line; where a name appears many times in one recording, the first few are listed.",
        "",
        "**What this is not.** It is not a gazetteer, a genealogy or an authority file. The filter keeps",
        "capitalised name-shaped runs that occur twice or more (plus every stated speaker), so it will miss",
        "a person mentioned once and can occasionally keep a place or a title. The transcripts are the",
        "authority; where a name is uncertain the transcript says so and this index repeats it unchanged.",
        "",
        "Where the collection contradicts itself about a person, see",
        "[`NOTES-ON-SOURCES.md`](NOTES-ON-SOURCES.md).",
        "",
        "## The index",
        "",
        "| name | mentions | recordings |",
        "|---|---|---|",
    ]
    for name, hits, files in rows:
        recs = sorted({h[0] for h in hits})
        lines.append(f"| **{name}** | {len(hits)} | {len(recs)} |")

    lines += ["", "## Where each name appears", ""]
    for name, hits, files in rows:
        lines.append(f"### {name}")
        by_rec = defaultdict(list)
        for folder, fname, line_no in hits:
            by_rec[folder].append((fname, line_no))
        for folder in sorted(by_rec):
            seen = []
            for fname, line_no in by_rec[folder]:
                if fname and (fname, line_no) not in seen:
                    seen.append((fname, line_no))
            shown = [f"[{fname} L{n}]({REPO_URL}/recordings/{folder}/{fname}#L{n})"
                     for fname, n in seen[:4] if fname]
            more = f" +{len(seen) - 4} more" if len(seen) > 4 else ""
            lines.append(f"- [{folder}](../recordings/{folder}/) — {', '.join(shown)}{more}"
                         if shown else f"- [{folder}](../recordings/{folder}/)")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(rows)} names, "
          f"{sum(len(h) for _, h, _ in rows)} mentions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
