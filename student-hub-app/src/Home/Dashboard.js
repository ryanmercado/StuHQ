import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage';
import { useNavigate } from 'react-router-dom';
import '../assets/styles/Global.css'; 
import '../assets/styles/Dashboard.css';
import Grayson from '../assets/images/Drinkard.jpeg';
import Charlie from '../assets/images/Charlie.jpeg';
import Ryan from '../assets/images/Mercado.jpeg';
import RecipeIcon from '../assets/images/RecipeIcon.png'
import CalendarIcon from '../assets/images/CalendarIcon.png'
import ResumeIcon from '../assets/images/ResumeIcon.png'

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
            <div className='features-container'>
                <div className='feature-box'>
                    <img src={CalendarIcon} alt={'Life Planner'} className='feature-image' />
                    <h3 className='feature-title'>{'Life Planner'}</h3>
                    <p className='feature-description'>{'The Life Planner is a tool to help you manage your busy schedule. Enter dates and times for important events to make sure you never lose track. Also, the Life Planner comes with a built-in To-Do List to keep you on top of all your tasks.'}</p><br></br>
                    <Link to={'/calendar'} className='feature-button'>View Calendar</Link>
                </div>
                <div className='feature-box'>
                    <img src={RecipeIcon} alt={'Recipe Hub'} className='feature-image' />
                    <h3 className='feature-title'>{'Recipe Hub'}</h3>
                    <p className='feature-description'>{'The Recipe Hub serves as a central location to manage your inventory, maintain your grocery list, and store delicious recipes! Get started by adding a recipe, creating a grocery list, or adding your current stock.'}</p><br></br>
                    <Link to={'/recipeLanding'} className='feature-button'>Manage Recipes</Link>
                </div>
                <div className='feature-box'>
                    <img src={ResumeIcon} alt={'Resume Builder'} className='feature-image' />
                    <h3 className='feature-title'>{'Resume Builder'}</h3>
                    <p className='feature-description'>{'The Resume Builder is a state of the art resume technology that uses a Large Language Model to generate business resumes. Enter all relevant information, and enjoy a professional resume tailored specifically to you!'}</p><br></br>
                    <Link to={'/resumeLanding'} className='feature-button'>Create Resume</Link>
                </div>
               
            </div>
        </div>

    );
};

export default Landing;