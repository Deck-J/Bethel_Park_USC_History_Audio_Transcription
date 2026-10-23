#!/usr/bin/env python3
"""Write checksums.sha256 for one recording folder (sorted, relative names)."""
import hashlib, pathlib, sys

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

d = pathlib.Path(sys.argv[1]).resolve()
out = []
for p in sorted(d.rglob("*")):
    if p.is_file() and p.name != "checksums.sha256":
        out.append(f"{sha256(p)}  {p.relative_to(d).as_posix()}")
(d / "checksums.sha256").write_text("\n".join(out) + "\n")
print(f"wrote {d/'checksums.sha256'} ({len(out)} files)")
