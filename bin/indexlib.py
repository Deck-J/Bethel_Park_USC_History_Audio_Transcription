#!/usr/bin/env python3
"""Shared reading side of the two generated indexes (names and places).

Both indexes must see exactly the same text and the same normalisation, or they disagree about what a
transcript says. This module is the single place that decides what counts as a line of transcript and
what counts as prose in it.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/Deck-J/Bethel_Park_USC_History_Audio_Transcription/blob/main"

# Speaker labels at the head of a line: WHITE:, INTERVIEWER:, ANN:, Q., J., June:, Jim:
LABEL_RE = re.compile(r"^(?:[A-Z][A-Z _'\-]{1,}|Q|J|June|Jim|Ann|Rev)\.?:\s*")


def iter_transcripts():
    """Yield (folder, metadata, path) for every transcript-like file in the repository."""
    for folder in sorted((ROOT / "recordings").iterdir()):
        if not folder.is_dir():
            continue
        meta_p = folder / "metadata.json"
        if not meta_p.is_file():
            continue
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
        for f in sorted(folder.glob("*.md")):
            if not (f.name.startswith("transcript-") or f.name.startswith("appendix-")):
                continue
            yield folder, meta, f


def iter_lines(path):
    """Yield (line_number, prose) for each line worth indexing.

    Strips the speaker label and bold markers, drops editorial [brackets] and any line that is a
    heading, table, rule, filename or URL — so neither index mistakes markup for speech.
    """
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip().lstrip("*> ").strip()
        line = re.sub(r"\*\*|__", "", line)
        line = LABEL_RE.sub("", line)
        line = re.sub(r"\[[^\]]*\]", " ", line)
        if not line or line.startswith(("#", "|", "---")):
            continue
        if ".md" in line or "http" in line or "README" in line:
            continue
        yield i, line


def links(folder, fname, lines, limit=4):
    """Markdown links to the first `limit` mentioned lines, plus a count of the rest."""
    shown = lines[:limit]
    parts = [f"[{fname} L{n}]({REPO_URL}/recordings/{folder}/{fname}#L{n})" for n in shown]
    more = f" +{len(lines) - limit} more" if len(lines) > limit else ""
    return ", ".join(parts) + more


def write_index(out_path, header_lines, rows, key_label="name"):
    """Rows: (entry, hits) with hits = [(folder, fname, line_no)]."""
    lines = list(header_lines)
    lines += ["", f"| {key_label} | mentions | recordings |", "|---|---|---|"]
    for entry, hits in rows:
        lines.append(f"| **{entry}** | {len(hits)} | {len({h[0] for h in hits})} |")
    lines += ["", "## Where each one appears", ""]
    for entry, hits in rows:
        lines.append(f"### {entry}")
        by_rec = {}
        for folder, fname, n in hits:
            by_rec.setdefault(folder, {}).setdefault(fname, []).append(n)
        for folder in sorted(by_rec):
            bits = [links(folder, fname, sorted(set(ns)))
                    for fname, ns in sorted(by_rec[folder].items())]
            lines.append(f"- [{folder}](../recordings/{folder}/) — " + "; ".join(bits))
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return len(rows), sum(len(h) for _, h in rows)
