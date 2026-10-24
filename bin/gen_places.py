#!/usr/bin/env python3
"""Build docs/PLACES.md — a finding aid to the places named across the collection.

The same shape as the names index, and built on the same reading side (`bin/indexlib.py`), so both see
identical text: every place named, how often, and a link to the line where it is mentioned.

Detection is deliberately conservative. A candidate is a place if it ends in a place word (Road, Creek,
Township, Church, Mill…), or is one of the known local places below. That keeps person names out, at the
cost of missing a settlement named only once in passing — and the places named in the collection are
mostly repeated, so the loss is small.

Two things this index will not do: decide which of two spellings is right (the transcripts carry the
speaker's own), or resolve a place that no longer exists. Those are in the recording's notes.
"""
import re
import sys
from collections import defaultdict

import indexlib

ROOT = indexlib.ROOT
OUT = ROOT / "docs" / "PLACES.md"

# Place words: a capitalised run ending in one of these is a place.
ROAD_WORDS = {"Road", "Street", "Avenue", "Ave", "Lane", "Drive", "Trail", "Pike", "Boulevard",
              "Boul", "Court", "Place", "Square", "Alley", "Highway", "Route", "Turnpike"}
WATER_WORDS = {"Creek", "Run", "Hollow", "Branch", "Fork", "Lake", "Pond", "River", "Springs",
               "Run's", "Millrace"}
SETTLE_WORDS = {"Township", "County", "Borough", "City", "Village", "Park", "Heights", "Hills",
                "Valley", "Ridge", "Junction", "Station", "Crossing", "Point", "Landing"}
SITE_WORDS = {"Church", "Cemetery", "Graveyard", "School", "Academy", "Seminary", "College",
              "University", "Mill", "Bridge", "Farm", "Manse", "Hall", "Inn", "Tavern", "Store",
              "House", "Barn", "Works", "Furnace", "Mine", "Hospital", "Library", "Hotel", "Bank",
              "Theater", "Theatre", "Station", "Center", "Centre", "Building", "Club", "Park"}

SUFFIX = {}
for w in ROAD_WORDS:
    SUFFIX[w] = "Roads and streets"
for w in WATER_WORDS:
    SUFFIX[w] = "Waterways"
for w in SETTLE_WORDS:
    SUFFIX[w] = "Settlements and townships"
for w in SITE_WORDS:
    SUFFIX.setdefault(w, "Buildings, churches and sites")

# Known places that carry no place word of their own.
KNOWN_SINGLE = {
    "Bethel": "Settlements and townships", "Hickory": "Settlements and townships",
    "Canonsburg": "Settlements and townships", "Chartiers": "Waterways",
    "Snowden": "Settlements and townships", "Beadling": "Settlements and townships",
    "Bridgeville": "Settlements and townships", "Venetia": "Settlements and townships",
    "Rutherford": "Settlements and townships", "Brookside": "Settlements and townships",
    "Irishtown": "Settlements and townships", "Library": "Settlements and townships",
    "Midway": "Settlements and townships", "Taylorstown": "Settlements and townships",
    "Princeton": "Settlements and townships", "Clifton": "Settlements and townships",
    "Brightwood": "Settlements and townships", "Hillcrest": "Settlements and townships",
    "Pittsburgh": "Settlements and townships", "Homestead": "Settlements and townships",
    "McDonald": "Settlements and townships", "Oakdale": "Settlements and townships",
    "Sturgeon": "Settlements and townships", "Noblestown": "Settlements and townships",
    "Lawrence": "Settlements and townships", "Dormont": "Settlements and townships",
    "Baldwin": "Settlements and townships", "Brentwood": "Settlements and townships",
    "Whitehall": "Settlements and townships", "Elizabeth": "Settlements and townships",
    "Clairton": "Settlements and townships", "Glassport": "Settlements and townships",
    "McKeesport": "Settlements and townships", "Mingo": "Settlements and townships",
    "Peters": "Settlements and townships", "Cecil": "Settlements and townships",
    "Canton": "Settlements and townships", "Allegheny": "Settlements and townships",
    "Sodom": "Settlements and townships", "Hastings": "Buildings, churches and sites",
    "Charleroi": "Settlements and townships", "Donora": "Settlements and townships",
}

# Multi-word places without a place word ("Stone Manse" has one, "Gill Hall" does not).
KNOWN_MULTI = {
    "Gill Hall": "Buildings, churches and sites",
    "Stone Manse": "Buildings, churches and sites",
    "Oliver Miller Homestead": "Buildings, churches and sites",
    "Bethel Academy": "Buildings, churches and sites",
    "Cross Creek": "Waterways",
    "South Park": "Settlements and townships",
    "Mt. Lebanon": "Settlements and townships",
    "Mount Lebanon": "Settlements and townships",
    "Upper St. Clair": "Settlements and townships",
    "Bethel Park": "Settlements and townships",
    "Bower Hill": "Settlements and townships",
    "Old Washington Road": "Roads and streets",
}

# Spellings that are the same place. The Patterson typescript prints a closed *e* that reads as *o*
# (its own Appendix A documents the habit), so "Bothol" is Bethel. Variants are listed in the document
# under "Spelling variants collapsed" with their counts, so the merge is visible rather than silent.
VARIANTS = {
    "Bothol": "Bethel",
    "Bothol Church": "Bethel Church",
    "Bothol Church Road": "Bethel Church Road",
    "Bethel. Church": "Bethel Church",
}

LEAD = re.compile(r"^(?:The|A|An|In|At|On|To|From|Near|By|Of|And|But|So|Then|There|Here|Back|Up|Down|"
                  r"Over|Along|Around|Across|Toward|Towards|Past|Between|Into|Through|Off|Out)\s+")
# no "of"/"the" connectors: "Hugh Lee of Cross Creek" must yield "Cross Creek", not the whole phrase
RUN_RE = re.compile(r"\b((?:[A-Z][\w'’.-]*)(?:\s+[A-Z][\w'’.-]*){0,3})")


ABBREV = {"St.", "Mt.", "Rt.", "Dr.", "Mr.", "Mrs.", "Ms.", "Sr.", "Jr.", "Rev.", "No."}


def _cut_sentence(words):
    """Drop anything before a sentence-ending full stop: "Bethel. Patterson Road" -> "Patterson Road"."""
    for i, w in enumerate(words):
        if w.endswith(".") and w not in ABBREV:
            return words[i + 1:]
    return words


def classify(phrase):
    """Return the section for a candidate, or None if it does not look like a place."""
    words = phrase.split()
    if len(words) >= 2 and phrase in KNOWN_MULTI:
        return KNOWN_MULTI[phrase]
    if len(words) == 1:
        return KNOWN_SINGLE.get(phrase)
    last = words[-1]
    if last in SUFFIX:
        return SUFFIX[last]
    return None


def hits_for(path):
    for line_no, line in indexlib.iter_lines(path):
        for m in RUN_RE.finditer(line):
            phrase = m.group(1).strip().rstrip(",.;:—-")
            phrase = LEAD.sub("", phrase).strip()
            words = phrase.split()
            # longest useful suffix: "Brush Run Road" is one place, "In Brush Run" is not
            words = _cut_sentence(words)
            if not words or any(re.fullmatch(r"[A-Z]\.", w) for w in words):
                continue                      # initials are people, not places
            for start in range(len(words)):
                cand = " ".join(words[start:])
                if len(cand.split()) > 4:
                    continue
                sec = classify(cand)
                if sec:
                    yield line_no, cand, sec
                    break


def main():
    mentions = defaultdict(list)
    sections = {}
    for folder, meta, path in indexlib.iter_transcripts():
        for line_no, phrase, sec in hits_for(path):
            mentions[phrase].append((folder.name, path.name, line_no))
            sections.setdefault(phrase, sec)

    # collapse spelling variants into their canonical place, remembering what was merged
    collapsed = {}
    for variant, canonical in VARIANTS.items():
        if variant in mentions:
            collapsed[variant] = (canonical, len(mentions[variant]))
            mentions[canonical].extend(mentions.pop(variant))
            sections.setdefault(canonical, sections.get(variant, "Settlements and townships"))

    rows = {name: hits for name, hits in mentions.items() if len(hits) >= 2}
    by_section = defaultdict(list)
    for name, hits in rows.items():
        by_section[sections[name]].append((name, hits))
    for v in by_section.values():
        v.sort(key=lambda r: r[0].lower())

    order = ["Settlements and townships", "Roads and streets", "Waterways",
             "Buildings, churches and sites"]
    total = sum(len(h) for h in rows.values())

    lines = [
        "# Places",
        "",
        "A finding aid to **where these transcripts say things happened**: settlements, roads, creeks,",
        "churches, mills and the sites around Bethel Park and Upper St. Clair. Generated by",
        "`bin/gen_places.py` over the same text the names index reads, so the two cannot disagree about",
        "what a transcript says.",
        "",
        f"**{len(rows)} places, {total} mentions**, each linked to the line where it appears. Grouped by",
        "kind: settlements, roads, waterways, then buildings and sites.",
        "",
        "**What this is not.** Not a gazetteer and not a map. A place is indexed when it ends in a place",
        "word or is one of the known local names, so a settlement named once in passing can be missed;",
        "spellings are the speakers' own and are not corrected here. Several of these roads and mills no",
        "longer exist, and some were renamed — the recording's notes say where that is known.",
        "",
        "People have their own index: [`NAMES.md`](NAMES.md). Conflicting accounts of the same event are",
        "in [`NOTES-ON-SOURCES.md`](NOTES-ON-SOURCES.md).",
        "",
    ]
    for sec in order:
        if not by_section.get(sec):
            continue
        lines += [f"## {sec}", "", "| place | mentions | recordings |", "|---|---|---|"]
        for name, hits in by_section[sec]:
            lines.append(f"| **{name}** | {len(hits)} | {len({h[0] for h in hits})} |")
        lines.append("")

    if collapsed:
        lines += [
            "## Spelling variants collapsed",
            "",
            "The transcripts keep the speaker's and the typist's own spellings, so one place can appear",
            "under two forms. These are merged above, and listed here so the merge is visible:",
            "",
            "| as printed in the source | indexed as | mentions merged | why |",
            "|---|---|---|---|",
        ]
        for variant, (canonical, n) in sorted(collapsed.items()):
            lines.append(f"| {variant} | **{canonical}** | {n} | the Patterson typescript prints a closed "
                         f"*e* that reads as *o*; its Appendix A records the habit and the restoration |")
        lines += [
            "",
            "This is a spelling correction of a *machine's* fault, not of a speaker's: the tape says Bethel,",
            "the typewriter printed Bothol. See `recordings/1979-04-20-jd-patterson-documents/` →",
            "`appendix-a-editorial-notes.md`.",
            "",
        ]

    lines += ["## Where each place appears", ""]
    for sec in order:
        for name, hits in by_section.get(sec, []):
            lines.append(f"### {name}")
            by_rec = {}
            for folder, fname, n in hits:
                by_rec.setdefault(folder, {}).setdefault(fname, []).append(n)
            for folder in sorted(by_rec):
                bits = [indexlib.links(folder, fname, sorted(set(ns)))
                        for fname, ns in sorted(by_rec[folder].items())]
                lines.append(f"- [{folder}](../recordings/{folder}/) — " + "; ".join(bits))
            lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(rows)} places, {total} mentions, "
          f"{len(order)} sections")
    return 0


if __name__ == "__main__":
    sys.exit(main())
