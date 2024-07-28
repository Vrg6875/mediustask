import React from 'react';
import './App.css';

import {Header} from "./mycomponents/Header";

import {Footer} from "./mycomponents/footer";

import {Todos} from "./mycomponents/todos";

import {Todo} from "./mycomponents/todo"; // Adjusted filename

function App() {
  return (
    <>
      <Header/> 
      <Footer/>
      <Todos/>
      <Todo/>

    </>
  );
}

export default App;
