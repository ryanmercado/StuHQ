import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ReactDOM from 'react-dom/client';
import './assets/styles/index.css';
import RecipeBookPage from './pages/RecipeBookPage'
import App from './App';
import reportWebVitals from './reportWebVitals';


createRoot(document.getElementById('root')).render(
    <Router>
        <Routes>
            <Route path = "/" element = {<RecipeBookPage />}/>
        </Routes>
    </Router>
);
