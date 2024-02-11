import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ReactDOM from 'react-dom/client';
import './assets/styles/index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import LogIn from './Home/LogIn';
import SignUp from './Home/SignUp';
import Landing from './Home/Landing';


createRoot(document.getElementById('root')).render(
    <Router>
        <Routes>
            <Route path="/signup" element={<SignUp />} />
            <Route path="/login" element={<LogIn />} />
            <Route path="/" element={<Landing />} />
            <Route path="/recipeLanding" element ={<recipeLanding/>} />
            <Route path="/resumeLanding" element ={<resumeDoc/>} />
            <Route path="/calendarLanding" element ={<calendarLand/>} />

        </Routes>
    </Router>
);
