import React from 'react';
import "./navbar.css";
import { Link, useLocation } from "react-router-dom";
import logo from '../assets/images/StuHQlogo.png'; 


const Navbar = () => {

    return (
        <nav className='nav'>
            <Link to='/dashboard' className='site-title'>
                <img src={logo} alt="Logo" className="nav-bar-logo" />
            </Link>
            <ul>
                <CustomLink to="/calendar">Calendar</CustomLink>
                <CustomLink to="/recipeLanding">Recipes/Groceries</CustomLink>
                <CustomLink to="/resumeLanding">Resume Builder</CustomLink>
            </ul>
        </nav>
    );
};

export default Navbar;

function CustomLink({ to, children, ...props }) {
    const location = useLocation();
    const path = location.pathname;

    return (
        <li className={path === to ? "active" : ""}>
            <Link to={to} {...props}>
                {children}
            </Link>
        </li>
    )
};