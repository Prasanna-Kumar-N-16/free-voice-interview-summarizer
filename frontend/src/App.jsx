import React from 'react';
import Recorder from './components/Recorder';
import Tabs from './components/Tabs';
import './styles.css';

const tabs = [
  { id: 'tab1', label: 'Summary', content: <div>Summary content</div> },
  { id: 'tab2', label: 'Questions', content: <div>Questions content</div> },
];

const App = () => {
    return (
        <div className="app">
            <h1>Welcome to the Application</h1>
            <Tabs tabs={tabs} />
            <Recorder />
        </div>
    );
};

export default App;