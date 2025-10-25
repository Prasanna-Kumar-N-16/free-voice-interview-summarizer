const TOKEN_KEY = 'vis_token'

// Local demo auth (no server): store a fake token
export function login({ username, password }) {
  if (!username || !password) throw new Error('Enter username and password')
  const token = btoa(`${username}:${Date.now()}`)
  localStorage.setItem(TOKEN_KEY, token)
  return token
}
export function logout() { localStorage.removeItem(TOKEN_KEY) }
export function isAuthed() { return Boolean(localStorage.getItem(TOKEN_KEY)) }