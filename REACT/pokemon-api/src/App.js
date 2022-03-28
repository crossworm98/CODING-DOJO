import { useEffect, useState } from 'react';
import axios from 'axios';
import "bootstrap/dist/css/bootstrap.min.css";
import './App.css';

function App() {
  const [responseData, setresponseData] = useState(null);
  
  useEffect( () => {
    axios.get('https://pokeapi.co/api/v2/pokemon?limit=1500')
      .then(response => {
        console.log(response);
        setresponseData(response.data.results)
        })
      .catch(err => console.log(err))
  }, []);


  return (
    <div className="App">
      <h1>Pokemon!</h1>
      <button className="btn btn-primary btn-lg">Catch them all!</button>
      <ul>
        {
          responseData.map( (item,i) => {
            return <li key={i}>{item.name}</li>
          })
        }
      </ul>
    </div>
  );
}

export default App;
