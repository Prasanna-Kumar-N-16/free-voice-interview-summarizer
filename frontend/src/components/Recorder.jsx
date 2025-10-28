import { useRef , useState } from "react";
import { uploadAudio } from "../api"

export default function Recorder({ onDone }) {
    const [recording, setRecording] = useState(false)
    const [uploading,setUploading] = useState(false)
    const mediaRef = useRef(null)
    const chunksRef = useRef([])

    const start = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true})
        const mr = new MediaRecorder(stream)

        chunksRef.current = []

        mr.ondataavailable = e => {
            if (e.data.size ) chunksRef.current.push(e.data) }
        }

        mr.onstop = async () => {
            const blob = new Blob(chunksRef.current, {type: "audio/webm"})
            const file = new File([blob], 'recording-${Date.now()}.webm' , { type:"audio/webm"})
            setUploading(true)
            try {
                const out = await uploadAudio(file)
                onDone?.(out)
            }catch(err){
                alert(err)
            }finally(
                setUploading(false)
                stream.getTracks().forEach( t => t.stop())
            )
        }
        mediaRef.current = mr
        mr.start()
        setRecording(true)
    }
}