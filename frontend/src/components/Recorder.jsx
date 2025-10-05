import React, { useState, useEffect } from 'react';

const Recorder = () => {
    const [isRecording, setIsRecording] = useState(false);
    const [mediaRecorder, setMediaRecorder] = useState(null);
    const [audioChunks, setAudioChunks] = useState([]);

    useEffect(() => {
        if (mediaRecorder) {
            mediaRecorder.ondataavailable = event => {
                setAudioChunks(prev => [...prev, event.data]);
            };

            mediaRecorder.onstop = () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                const audioUrl = URL.createObjectURL(audioBlob);
                const audio = new Audio(audioUrl);
                audio.play();
                setAudioChunks([]);
            };
        }
    }, [mediaRecorder, audioChunks]);

    const startRecording = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const recorder = new MediaRecorder(stream);
        setMediaRecorder(recorder);
        recorder.start();
        setIsRecording(true);
    };

    const stopRecording = () => {
        mediaRecorder.stop();
        setIsRecording(false);
    };

    return (
        <div>
            <h2>Audio Recorder</h2>
            {isRecording ? (
                <button onClick={stopRecording}>Stop Recording</button>
            ) : (
                <button onClick={startRecording}>Start Recording</button>
            )}
        </div>
    );
};

export default Recorder;