import React, { useState } from "react";
import './App.css';

function App() {
  const [newTodo, setnewTodo] = useState("");
  const [todos, setTodos] = useState([]);
  //HANDLERS//
  const handlenewtodoSubmit = (event) => {
    event.preventDefault();
    //SUBMIT VALIDATIONS//
    if (newTodo.length == 0) {return;}
    //END//
    const todoItem = {
      text: newTodo,
      complete: false
    }
    setTodos([...todos, todoItem]);
    setnewTodo("");
  }
  const handletodoDelete = (delindx) => {
    const filteredTodos = todos.filter((todo, i) => {
      return i != delindx;
    })
    setTodos(filteredTodos);
  }
  const handlecheckBox = (indx) => {
    const updatedTodos = todos.map((todo, i) => {
      if (indx == i) {
        // todo.complete = !todo.complete;
        const updatedTodo = {... todo, complete: !todo.complete};
        return updatedTodo;
      }
      return todo;
    })
    setTodos(updatedTodos);
  }
  //END HANDLERS//
  //RENDER//
  return (
    <div className="App">
      <form onSubmit={(event) => {
        handlenewtodoSubmit(event);
      }}>
        <input value={newTodo} type="text" onChange={(event) => { setnewTodo(event.target.value) }}></input>
        <div>
          <button type="submit">Add</button>
        </div>
      </form>
      <hr />
      {
        todos.map((todo, i) => {
          const todoClasses = ["bold"];
          if (todo.complete){
            todoClasses.push("line-through", "bold")
          }

          return <div style={{paddingTop: "15px"}} key={i}>
            <input onChange={(event) => {handlecheckBox(i);}} checked={todo.complete} type="checkbox" />
            <span className={todoClasses.join(" ")}>{todo.text}</span>
            <button style={{marginLeft: "15px"}} onClick={(event) => {handletodoDelete(i)}}>Delete!</button>
          </div>;
        })
      }
    </div>
  );
}

export default App;
