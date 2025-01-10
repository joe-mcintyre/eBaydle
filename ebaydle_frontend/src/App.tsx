import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          5247839 <code> _ _ _code_ _ _ </code> jkwedaf 
        </p>

        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <code>typescript gun</code>
        </p>
        <a
          className="App-link"
          href="http://localhost:3000"
          target="_blank"
          rel="noopener noreferrer"
        >
          #RELOAD#
        </a>
        <a
            className="App-link"
            href="#"
            onClick={() => (window.location.href = 'http://localhost:3000')}
        >
          #RELOAD IN PAGE#
        </a>

</header>
    </div>
  );
}

export default App;
