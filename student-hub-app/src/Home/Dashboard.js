import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage';
import { useNavigate } from 'react-router-dom';


function Landing() {
    const usr_id = secureLocalStorage.getItem('usr_id')
    const navigate = useNavigate();

    
    useEffect(() => {
        if (usr_id === null) {
            navigate("/");
        }
    }, []);

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
            <Link to="/calendar">
                <button>Life Planner</button>
            </Link>
        </div>
    );
};

export default Landing;