#!/usr/bin/env python3
"""Gate: every recording is complete, checksummed, audio-free and schema-shaped.

Pure stdlib (no jsonschema on this box) — the schema is read and the subset it uses is enforced
explicitly, so a schema change that check.py does not understand fails loudly as UNSUPPORTED.
"""
import argparse, hashlib, json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = json.load(open(ROOT / "schema" / "recording.schema.json"))
AUDIO = {".m4a", ".mp3", ".wav", ".flac", ".aif", ".aiff", ".ogg", ".opus", ".mp4", ".mov"}
fails, checks = [], 0


def fail(rec, msg):
    fails.append(f"{rec}: {msg}")


def check_type(rec, path, value, spec):
    global checks
    checks += 1
    t = spec.get("type")
    ok = {
        "string": lambda v: isinstance(v, str),
        "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
        "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
        "boolean": lambda v: isinstance(v, bool),
        "array": lambda v: isinstance(v, list),
        "object": lambda v: isinstance(v, dict),
    }.get(t)
    if ok is None:
        fail(rec, f"UNSUPPORTED schema type {t!r} at {path}")
        return False
    if not ok(value):
        fail(rec, f"{path} should be {t}, got {type(value).__name__}")
        return False
    if t == "string":
        if len(value) < spec.get("minLength", 0):
            fail(rec, f"{path} shorter than {spec['minLength']}")
        if "pattern" in spec and not re.search(spec["pattern"], value):
            fail(rec, f"{path} does not match {spec['pattern']}")
        if "enum" in spec and value not in spec["enum"]:
            fail(rec, f"{path}={value!r} not in {spec['enum']}")
    if t == "number" and "exclusiveMinimum" in spec and value <= spec["exclusiveMinimum"]:
        fail(rec, f"{path} must be > {spec['exclusiveMinimum']}")
    if t == "integer" and "minimum" in spec and value < spec["minimum"]:
        fail(rec, f"{path} must be >= {spec['minimum']}")
    return True


def walk(rec, value, spec, path=""):
    if not check_type(rec, path or "$", value, spec):
        return
    if spec.get("type") == "object":
        props = spec.get("properties", {})
        for key in spec.get("required", []):
            if key not in value:
                fail(rec, f"{path}.{key} is required")
        if spec.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    fail(rec, f"{path}.{key} is not in the schema")
        for key, sub in props.items():
            if key in value:
                walk(rec, value[key], sub, f"{path}.{key}" if path else key)
    if spec.get("type") == "array":
        item = spec.get("items", {})
        if len(value) < spec.get("minItems", 0):
            fail(rec, f"{path} needs at least {spec['minItems']} item(s)")
        for i, v in enumerate(value):
            walk(rec, v, item, f"{path}[{i}]")


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_recording(d):
    rec = d.name
    meta_p = d / "metadata.json"
    if not meta_p.is_file():
        return fail(rec, "no metadata.json")
    try:
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return fail(rec, f"metadata.json is not valid JSON: {e}")
    walk(rec, meta, SCHEMA)
    if meta.get("id") and meta["id"] != rec:
        fail(rec, f"metadata id {meta['id']!r} does not equal the folder name")

    # text files exist, transcripts are not empty, no audio anywhere
    for side in meta.get("sides", []):
        for key in ("transcript", "srt", "notes"):
            rel = side.get(key)
            if not rel:
                continue
            p = d / rel
            if not p.is_file():
                fail(rec, f"missing {key} file {rel}")
            elif p.stat().st_size == 0:
                fail(rec, f"{key} file {rel} is empty")
        t = d / side["transcript"]
        if t.is_file() and len(t.read_text(encoding="utf-8").split()) < 50:
            fail(rec, f"transcript {side['transcript']} looks empty ({len(t.read_text().split())} words)")

    for p in d.rglob("*"):
        if p.is_file() and p.suffix.lower() in AUDIO:
            fail(rec, f"audio file in repo: {p.relative_to(d)} (see docs/AUDIO.md)")

    cs = d / "checksums.sha256"
    if not cs.is_file():
        fail(rec, "no checksums.sha256 (run bin/gen_checksums.py)")
    else:
        for line in cs.read_text().splitlines():
            if not line.strip():
                continue
            digest, _, name = line.partition("  ")
            p = d / name
            if not p.is_file():
                fail(rec, f"checksum lists a missing file: {name}")
            elif sha256(p) != digest:
                fail(rec, f"checksum mismatch: {name}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir")
    a = ap.parse_args()
    dirs = [pathlib.Path(a.dir)] if a.dir else sorted((ROOT / "recordings").iterdir())
    dirs = [d for d in dirs if d.is_dir()]
    if not dirs:
        print("FAIL no recordings")
        return 1
    for d in dirs:
        check_recording(d)
    print(f"{len(dirs)} recording(s), {checks} schema checks, {len(fails)} failure(s)")
    for f in fails:
        print("  FAIL", f)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
