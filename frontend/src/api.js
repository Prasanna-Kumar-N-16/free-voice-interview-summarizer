import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export async function uploadAudio(file) {
  const form = new FormData();
  form.append("file", file);
  const { data } = await axios.post(`${API_BASE}/upload-audio`, form, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return data; // { transcript, transcript_id }
}

export async function extractQuestions({ text, transcript_id }) {
  const { data } = await axios.post(`${API_BASE}/extract-questions`, { text, transcript_id });
  return data; // { questions: [] }
}

export async function extractQA({ text, transcript_id, max_answer_sents = 3 }) {
  const { data } = await axios.post(`${API_BASE}/extract-qa`, { text, transcript_id, max_answer_sents });
  return data; // { items: [{question, answer}] }
}