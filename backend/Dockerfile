ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 1. CPU-only torch in its own layer (the default Linux wheel pulls in gigabytes of CUDA libraries)
RUN pip install torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu

# 2. Everything else; the torch line is dropped so pip doesn't swap the CPU build for the default one
COPY backend/requirements.txt requirements.txt
RUN grep -v '^torch==' requirements.txt > requirements-no-torch.txt \
    && pip install -r requirements-no-torch.txt

# 3. Bake the embedding model into the image so startup never downloads it
ENV HF_HOME=/opt/hf-cache
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
ENV HF_HUB_OFFLINE=1

# 4. Your code last, so code edits don't invalidate the heavy layers above
COPY backend/ backend/

ENV PORT=8080
CMD exec gunicorn --bind 0.0.0.0:${PORT} --workers 1 --threads 8 --timeout 0 backend.app:app
