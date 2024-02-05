import React from 'react';
import { Link } from 'react-router-dom';


const Landing = () => {
    return (
        <div>
            <h2>Welcome to StuHQ!</h2>
            <p>Please choose an option:</p>
            <Link to="/login">
                <button>Login</button>
            </Link>
            <Link to="/signup">
                <button>Sign Up</button>
            </Link>
        </div>
    );
};

export default Landing;