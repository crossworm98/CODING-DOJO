import React from "react";
import { useEffect, useState } from 'react';
import axios from 'axios';
import { BrowserRouter, Link, Switch, Route } from "react-router-dom";
import People from "./components/people"
// import Number from "./components/number";
// import Home from "./components/home";


function App() {
  const [category, setCategory] = useState("planets");
  const [id, setId] = useState(0);
  const [starwarsinfo, setStarwarsInfo] = useState({});
  
  const handleSubmit = e => { 
    e.preventDefault();
    console.log("form submitted");
    axios.get(`https://swapi.dev/api/${category}/${id}`)
      .then(response => {
        console.log(response);
        setStarwarsInfo(response.data);
        })
      .catch(err => console.log(err))
  }

  
  
  return (
    <>
      <div>
        <form onSubmit={handleSubmit} >
          <h1></h1>
          <h1>Search For: </h1>
          <select onChange={ e => setCategory(e.target.value)} >
            <option value="planets">Planets</option>
            {/* <option value="species">Species</option>
            <option value="vehicles">Vehicles</option>
            <option value="starships">Starships</option>
            <option value="films">Films</option> */}
            <option value="people">People</option>
            {/* <option value="root">Root</option> */}
          </select>
          
          <h1>ID: <input type="id" onChange={ e => setId(e.target.value)}/></h1>
          <input type="submit" value="Search" />
        </form>
      </div>
      <p>
        <Link to='/people/${id}'>Home</Link>
        {" | "}
        <Link to="/about">About</Link>
      </p>
      <Switch>
  
        <Route path="/people/:id">
            {/* people component in here */}
            {/* pass in starwarsinfo via props */}
            <People info={starwarsinfo}>
              
            </People>
        </Route>
      </Switch>

    </>
  );
}

export default App;
