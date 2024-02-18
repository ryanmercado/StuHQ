import React from 'react';
import { Link } from 'react-router-dom';


function Landing() {
    return (
        <div>
            <h2>Welcome to your StuHQ Dashboard!</h2>
            <p>Please choose an option:</p>
            <Link to="/recipeLanding">
                <button>Recipe Hub</button>
            </Link>
            <Link to="/resumeLanding">
                <button>Resume Builder</button>
            </Link>
            <Link to="/calendarLanding">
                <button>Life Planner</button>
            </Link>
        </div>
    );
};

export default Landing;