import React, { useEffect, useState } from 'react';
import './App.css';
import catLogo from './cat-logo.jpg';

function App() {
  const [cats, setCats] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/cats')
      .then(response => response.json())
      .then(data => setCats(data));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
      <img src={catLogo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <table className="table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Breed</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {cats.map(cat => (
            <tr key={cat.id}>
              <td>{cat.name}</td>
              <td>{cat.breed}</td>
              <td>{cat.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;