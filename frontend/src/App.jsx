import React from 'react';
import Recorder from './components/Recorder';
import Tabs from './components/Tabs';
import './styles.css';

const App = () => {
    return (
        <div className="app">
            <h1>Welcome to the Application</h1>
            <Tabs />
            <Recorder />
        </div>
    );
};

export default App;