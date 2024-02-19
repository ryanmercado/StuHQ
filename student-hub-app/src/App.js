import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ReactDOM from 'react-dom/client';
import './assets/styles/index.css';
import reportWebVitals from './reportWebVitals';
import LogIn from './Home/LogIn';
import SignUp from './Home/SignUp';
import Landing from './Home/Landing';
import CalendarLand from './Calendar/CalendarLand';
import Dashboard from './Home/Dashboard.js'
import ResumeDoc from './Resume/resumeDoc';

function App(){
  return(
      <Router>
          <Routes>
              <Route path="/signup" element={<SignUp />} />
              <Route path="/login" element={<LogIn />} />
              <Route path="/" element={<Landing />} />
              <Route path="/calendar" element={<CalendarLand />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/recipeLanding" element ={<recipeLanding/>} />
              <Route path="/resumeLanding" element ={<ResumeDoc/>} />
          </Routes>
      </Router>
  )
}

export default App;