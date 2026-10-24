# The transcription environment these transcripts were made in — nothing more.
#
# Why a container at all: the engine decides the words. A different faster-whisper, a different
# CTranslate2, a different numpy, or a different base image produces a different transcript from the
# same audio, and "it was transcribed on the NAS" is not a reproducible statement without them pinned.
# The base is pinned by DIGEST (a tag is a moving label); the three packages are pinned by version.
#
# What is deliberately NOT baked in: the model and the audio. The model is ~3 GB and the masters are
# held outside this repository (see ../docs/AUDIO.md); both are mounted, so one copy serves every run
# and the image stays small enough to rebuild on a whim.
#
# Measured environment for the filed transcripts (2026-10-23):
#   image      whisper-worker:v0.3   id e7f129822531   (also tagged v0.3-2026-10-21)
#   engine     faster-whisper 1.2.1 / CTranslate2 4.8.3 / numpy 2.5.4
#   model      large-v3, CTranslate2 int8, compute_type=int8, language=en, beam_size=5
#   threads    14 of 16 (OMP/OPENBLAS), ~1.6x realtime on the archive NAS
FROM python:3.13-slim@sha256:cf50a4f6ac4f026458b08d5222023d700ac806410dff5e9ca8728fa44f2b850f

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    OMP_NUM_THREADS=14 \
    OPENBLAS_NUM_THREADS=14

# ffmpeg for decode and level measurement; ca-certificates for the one-off model download.
RUN apt-get update \
 && apt-get install -y --no-install-recommends ffmpeg ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# The three packages that decide the output. Bumping any of them is a new transcription, not an upgrade.
RUN pip install --no-cache-dir \
        faster-whisper==1.2.1 \
        ctranslate2==4.8.3 \
        numpy==2.5.4

# Named mount points, so a bare `docker run` reports them instead of failing on a missing path.
VOLUME ["/media", "/out", "/models", "/scripts"]

WORKDIR /work
CMD ["python", "/scripts/transcribe_chunked.py", "--help"]
