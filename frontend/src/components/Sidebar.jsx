import { NavLink } from 'react-router-dom'

const base = 'flex items-center gap-3 rounded-xl px-3 py-2 font-medium'

export default function Sidebar() {
  const cls = ({ isActive }) =>
    isActive ? `${base} bg-white text-gray-900` : `${base} text-white/80 hover:text-white hover:bg-white/10`
  return 
}