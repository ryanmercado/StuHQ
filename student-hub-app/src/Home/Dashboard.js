import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage';
import { useNavigate } from 'react-router-dom';
import '../assets/styles/Global.css'; 
import '../assets/styles/Dashboard.css';
import Grayson from '../assets/images/Drinkard.jpeg';
import Charlie from '../assets/images/Charlie.jpeg';
import Ryan from '../assets/images/Mercado.jpeg';


function Landing() {
    const usr_id = secureLocalStorage.getItem('usr_id')
    const navigate = useNavigate();

    
    useEffect(() => {
        if (usr_id === null) {
            navigate("/");
        }
    }, []);

    return (
        <div className='dashboard-container'>
            <h2 className='dash-title'>Welcome to your StuHQ Dashboard!</h2>
            <div className='columns-container'>
                <div className='column'>
                    <img src={Grayson} alt="Recipe Hub" />
                    <Link to="/recipeLanding">
                        <button className='global-button'>Recipe Hub</button>
                    </Link>
                    <p className='column-blurb'>The Recipe Hub serves as a central location to manage your inventory, maintain your grocery list, and store delicious recipes! Get started by adding a recipe, creating a grocery list, or adding your current stock.</p>
                </div>
                <div className='column'>
                    <img src={Ryan} alt="Resume Builder" />
                    <Link to="/resumeLanding">
                        <button className='global-button'>Resume Builder</button>
                    </Link>
                    <p className='column-blurb'>The Resume Builder is a state of the art resume technology that uses a Large Language Model to generate business resumes. Enter all relevant information, and enjoy a professional resume tailored specifically to you!</p>
                </div>
                <div className='column'>
                    <img src={Charlie} alt="Life Planner" />
                    <Link to="/calendar">
                        <button className='global-button'>Life Planner</button>
                    </Link>
                    <p className='column-blurb'>The Life Planner is a tool to help you manage your busy schedule. Enter dates and times for important events to make sure you never lose track. Also, the Life Planner comes with a built in To-Do List to keep you on top of all your tasks.</p>
                </div>
            </div>
        </div>
    );
};

export default Landing;