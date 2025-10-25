const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

async function http(url, opts = {}) {
  const res = await fetch(`${API_BASE}${url}`, opts)
  if (!res.ok) throw new Error(await res.text())
  return res.json()
}

export async function uploadAudio(file) {
  const form = new FormData()
  form.append('file', file)
  return http('/upload-audio', { method: 'POST', body: form })
}

export async function extractQuestions({ text, transcript_id }) {
  return http('/extract-questions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, transcript_id })
  })
}

