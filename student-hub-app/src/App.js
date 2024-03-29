import React from 'react';
import { createRoot } from 'react-dom/client';
import { Route, Routes, useLocation  } from 'react-router-dom';
import ReactDOM from 'react-dom/client';
import './assets/styles/index.css';
import reportWebVitals from './reportWebVitals';
import LogIn from './Home/LogIn';
import SignUp from './Home/SignUp';
import Landing from './Home/Landing';
import ScrollPane from './Calendar/ScrollPane.js';
import Dashboard from './Home/Dashboard.js'
import ResumeDoc from './Resume/resumeDoc';
import RecipeLanding from './Recipe/RecipeLanding.js';
import RecipeList from './Recipe/RecipeList.js';
import StockList from './Recipe/StockList.js';
import GroceryList from './Recipe/GroceryList.js';
import Navbar from './Navbar/Navbar.js';
import secureLocalStorage from 'react-secure-storage';

function App() {
    const location = useLocation();
    const excludedRoutes = ['/signup', '/login', '/'];
    const shouldRenderNavbar = !excludedRoutes.includes(location.pathname);
    
    return (
        <>
        {shouldRenderNavbar && <Navbar />}
        <Routes>
            <Route path="/signup" element={<SignUp />} />
            <Route path="/login" element={<LogIn />} />
            <Route path="/" element={<Landing />} />
            <Route path="/calendar" element={<ScrollPane />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/recipeLanding" element={<RecipeLanding />} />
            <Route path="/resumeLanding" element={<ResumeDoc />} />
            <Route path='/grocery-list' element={<GroceryList />} />
            <Route path='/recipe-list' element={<RecipeList />} />
            <Route path='/stock-list' element={<StockList />} />
        </Routes>
        </>
    );
}

export default App;