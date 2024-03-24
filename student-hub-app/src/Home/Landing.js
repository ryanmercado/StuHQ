import React from 'react';
import logo from '../assets/images/StuHQlogo.png'; 
import { Link } from 'react-router-dom';
import '../assets/styles/Landing.css'; 
import '../assets/styles/Global.css'; 

const Landing = () => {
    return (
        <div className='global-container'>
            <div className='landing-content'>
                <div className="welcome-text">
                    <h1>Welcome to</h1>
                    <img src={logo} alt="Logo" className="logo" />
                </div>
                <p>Please choose an option:</p>
                <div className="global-button-group">
                    <Link to="/login">
                        <button className="button">Login</button>
                    </Link>
                    <Link to="/signup">
                        <button className="button">Sign Up</button>
                    </Link>
                </div>
            </div>
        </div>
    );
};

export default Landing;
