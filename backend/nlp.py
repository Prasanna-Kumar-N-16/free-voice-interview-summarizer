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


def extract_questions(text: str) -> List[str]:
    sents = split_sentences(text)
    return [s for s in sents if s.endswith("?")]


def extract_qa(text: str, max_answer_sents: int = 3) -> List[Dict[str, str]]:
    sents = split_sentences(text)
    qa_list = []
    for i, s in enumerate(sents):
        if s.endswith("?"):
            # Collect next 1..max_answer_sents as the answer blob
            ans_sents = []
            for j in range(1, max_answer_sents + 1):
                if i + j < len(sents) and not sents[i + j].endswith("?"):
                    ans_sents.append(sents[i + j])
                else:
                    break
            qa_list.append({
                "question": s,
                "answer": " ".join(ans_sents).strip()
            })
    return qa_list