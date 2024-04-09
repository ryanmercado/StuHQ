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
                    <h3>Welcome to</h3>
                    <img src={logo} alt="Logo" className="logo" />
                </div>
                <br></br>
                <h1>Please choose an option:</h1>
                <div className="global-button-group">
                    <Link to="/login">
                        <button className="login-button">Login</button>
                    </Link>
                    <Link to="/signup">
                        <button className="signup-button">Sign Up</button>
                    </Link>
                </div>
            </div>
        </div>
    );
};

export default Landing;
