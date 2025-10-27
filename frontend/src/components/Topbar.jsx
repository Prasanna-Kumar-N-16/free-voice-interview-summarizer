export default function Topbar({ title, actions }) {
    return (
        <header className="sticky top-0 z-30 bg-white/80 backdrop-blur border-b border-gray-200">
            <div className="container-app h-14 flex items-center justify-between">
                <h1 className="text-lg font-semibold">{title}</h1>
                <div className="flex items-center gap-2">{actions}</div>
            </div>
        </header>
    )
}