import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ReactDOM from 'react-dom/client';
import './index.css';
import RecipeBookPage from './pages/RecipeBookPage'
import App from './App';
import reportWebVitals from './reportWebVitals';


createRoot(document.getElementById('root')).render(
    <Router>
        <Routes>
//          <Route path = "/" element = {<LandingPage />}/>
            <Route path = "/" element = {<RecipeBookPage />}/>
        <Routes>
    <Router>
);



//const root = ReactDOM.createRoot(document.getElementById('root'));
//root.render(
//  <React.StrictMode>
//    <App />
//  </React.StrictMode>
//);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
