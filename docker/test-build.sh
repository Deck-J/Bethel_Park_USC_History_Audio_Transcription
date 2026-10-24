#!/usr/bin/env bash
# Prove the pinned environment builds and imports the exact engine versions. Not part of the repo
# content served to readers - it is the build proof, so it lives next to the Dockerfile.
set -euo pipefail
cd "$(dirname "$0")"
docker build -t oral-history-transcriber:test .
docker run --rm oral-history-transcriber:test \
  python -c "import faster_whisper,ctranslate2,numpy;print('ENGINE_OK',faster_whisper.__version__,ctranslate2.__version__,numpy.__version__)"
