import { VFC, useState } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

const App: VFC = () => {
  const [text, setText] = useState('');
  const handleSubmit = (): void => {
    void axios.get('http://127.0.0.1:8000/luck/').then((res) => {
      console.log(res);
    });
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <input type="text" onChange={(e) => setText(e.currentTarget.value)} />
        <button type="button" onClick={handleSubmit}>
          PUSH!
        </button>
      </header>
    </div>
  );
};

export default App;
