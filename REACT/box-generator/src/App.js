import './App.css';
import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import ColorForm from './components/form'
import Boxy from './components/boxy'

function App() {
  const [colors, setColors] = useState([]);
  console.log(colors)
  return (
    <div className="App">
      <div>
        <ColorForm setColors={setColors} />
      </div >
      <div className="d-flex justify-content-between">
        {colors.map((color, index) => <Boxy key={index} color={color} />)}
      </div>
    </div>

  );
}

export default App;
