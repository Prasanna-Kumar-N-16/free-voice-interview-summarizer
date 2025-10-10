from __future__ import annotations
from typing import List, Dict
import spacy

# Lazy-load model (so container start is fast)
_nlp = None

def get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp


def split_sentences(text: str) -> List[str]:
    nlp = get_nlp()
    doc = nlp(text)
    # Keep raw sentence text
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]

