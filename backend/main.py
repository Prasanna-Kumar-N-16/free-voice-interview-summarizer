from __future__ import annotations
import io
import os
from typing import Optional, List, Dict

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import whisper  # OpenAI Whisper (local)

from nlp import extract_questions, extract_qa
from db import get_engine, insert_transcript, fetch_transcript

# ---------- App & CORS ----------
app = FastAPI(title="Voice Interview Summarizer", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Whisper model (lazy) ----------
_MODEL = None


def get_model():
    global _MODEL
    if _MODEL is None:
        model_name = os.environ.get("WHISPER_MODEL", "tiny")  # "tiny" or "base"
        _MODEL = whisper.load_model(model_name)
    return _MODEL

# ---------- DB ----------
ENGINE = get_engine()

# ---------- Schemas ----------
class TextIn(BaseModel):
    text: Optional[str] = None
    transcript_id: Optional[int] = None
    max_answer_sents: Optional[int] = 3

class TranscriptOut(BaseModel):
    transcript: str
    transcript_id: Optional[int] = None

class QuestionsOut(BaseModel):
    questions: List[str]

class QAItem(BaseModel):
    question: str
    answer: str

class QAOut(BaseModel):
    items: List[QAItem]


# ---------- Helpers ----------

def resolve_text(payload: TextIn) -> str:
    if payload.text:
        return payload.text
    if payload.transcript_id is not None:
        t = fetch_transcript(ENGINE, payload.transcript_id)
        if t is None:
            raise HTTPException(status_code=404, detail="Transcript not found")
        return t
    raise HTTPException(status_code=400, detail="Provide 'text' or 'transcript_id'")


# ---------- Routes ----------
@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload-audio", response_model=TranscriptOut)
async def upload_audio(file: UploadFile = File(...)):
    # Read bytes
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Empty file")

    # Whisper expects an audio file path or bytes; we pass a BytesIO
    audio_bytes = io.BytesIO(content)

    model = get_model()
    # Transcribe (language auto-detect)
    try:
        result = model.transcribe(audio_bytes, fp16=False)
        transcript = result.get("text", "").strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription failed: {e}")

    tid = insert_transcript(ENGINE, file.filename, transcript)
    return TranscriptOut(transcript=transcript, transcript_id=tid)


@app.post("/extract-questions", response_model=QuestionsOut)
async def api_extract_questions(payload: TextIn):
    text = resolve_text(payload)
    qs = extract_questions(text)
    return QuestionsOut(questions=qs)


@app.post("/extract-qa", response_model=QAOut)
async def api_extract_qa(payload: TextIn):
    text = resolve_text(payload)
    max_ans = payload.max_answer_sents or 3
    items = [
        {"question": x["question"], "answer": x["answer"]}
        for x in extract_qa(text, max_answer_sents=max_ans)
    ]
    return QAOut(items=items)