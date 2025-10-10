FROM python:3.11-slim

# System deps for whisper/ffmpeg/spacy
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg build-essential libsndfile1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm

# Copy source
COPY . .

# Env: choose tiny/base
ENV WHISPER_MODEL=tiny

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]