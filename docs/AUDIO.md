# Where the audio lives

The masters are **not** in this repository, deliberately:

- a 31-minute ALAC side is ~83 MB and a 95-minute capture ~56 MB; GitHub warns above 1 GB per repo and
  hard-fails on a 100 MB file, so a handful of interviews would break the clone for everyone;
- Git LFS would put a finite quota in front of files that will never change, which is the wrong place
  to spend it;
- the masters are already held twice on the NAS (volume2 archive + the backup set), and the archive
  folder is the authority for them.

`docs/AUDIO.md` in this repo records, per recording: the master's filename, its sha256, its duration and
format, and where it can be obtained on request. When a side is published for download it goes to the
Internet Archive (public-domain, no quota, permanent identifier) and the identifier is recorded in the
recording's `metadata.json` — never a raw file in git.
