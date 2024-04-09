import React, { useState, useEffect } from 'react';
import './style/resume.css';
import DefaultPopup from './defaultPopup';
import { useNavigate } from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage';
import QuestionIcon from '../assets/images/QuestionIcon.png'
import ResumeIcon from '../assets/images/ResumeIcon.png'
import DeleteIcon from '../assets/images/DeleteIcon.png'

const ResumeDoc = () => {
  const navigate = useNavigate();
  const usr_id = secureLocalStorage.getItem("usr_id");
  const [isResumeReady, setIsResumeReady] = useState(false);
  const [showPopup, setShowPopup] = useState(false);

  const handleCreateResume = async () => {
    //For trying to pull file from backend, does not work yet
    try {
      const response = await fetch('/api/generate_resume', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: usr_id })
      });
  
      if (!response.ok) {
        throw new Error('Failed to generate resume');
      }
  
      // Assuming the response contains the PDF file, you can handle it here
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      window.open(url); // Open the PDF in a new tab
    } catch (error) {
      console.error('Error generating resume:', error);
    }
  };

  const handleExampleData = async () => {
    try {
      const response = await fetch('/api/fill_example_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: usr_id })
      });
  
      if (!response.ok) {
        throw new Error('Failed to fill with example data');
      }
  
      console.log('Example data filled successfully');
    }
    catch (error) {
      console.error('Error filling with example data:', error);
    }
  };

  const handleDeleteResume = async () => {
    try {
      const response = await fetch('/api/deleteResume', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: usr_id })
      });
  
      if (!response.ok) {
        throw new Error('Failed to delete resume');
      }
  
      console.log('Resume deleted successfully');
    } catch (error) {
      console.error('Error deleting resume:', error);
    }
  };

  const handlePopupClose = () => {
    setShowPopup(false);
  };

  useEffect(() => {
    if (usr_id === null) {
      navigate("/");
    }
  }, [usr_id, navigate]);

  return (
    <div className="body">
      <div className = 'resume-dashboard-container'>
        <h2 className='dash-title'>Welcome to your StuHQ Resume Builder!</h2>
        <div className='features-container'>
          <div className = 'feature-box'>
            <img src={QuestionIcon} alt={'Recipe Hub'} className='feature-image' />
            <h3 className='feature-title'>{'Open Questionnaire'}</h3>
            <p className='feature-description'>{'To begin on your Resume creation journey, you will first have to fill out 5 pages worth of questions that will populate your generated resume. Be warned though, if you do not fill out and submit every field on every page, the Resume will not properly be created. To get started click the following button.'}</p><br></br>
            <button className ="feature-button" onClick={() => setShowPopup(true)}>
              Open Questionnaire
            </button>
            </div>
          <div className = 'feature-box'>
            <img src={ResumeIcon} alt={'Resume Builder'} className='feature-image' />
            <h3 className='feature-title'>{'Build and Download Resume'}</h3>
            <p className='feature-description'>{'Once you have filled out all the fields on the questionnaire, you can then generate your resume. This resume will be a professional resume tailored specifically to you! Click the following button to generate your resume, and you will be redirected to a pdf of your new Resume!'}</p><br></br>
            <button className ="feature-button" onClick={handleCreateResume}>
              Create Resume
            </button>
            </div>
          <div className = 'feature-box'>
            <img src={DeleteIcon} alt={'Delete Resume'} className='feature-image' />
            <h3 className='feature-title'>{'Delete Resume Info'}</h3>
            <p className='feature-description'>{'If you would like to delete all of your resume information so you can start over, you can do so by clicking the following button. Be warned, once you delete your resume information, you will have to start the questionnaire from the beginning. Make sure to click this before filling with example data.'}</p><br></br>
            <button className ="delete-resume-btn" onClick={handleDeleteResume}>
              Delete Resume Info
            </button>
            </div>
        </div>
        <br></br>
        <button className = 'feature-button' onClick={handleExampleData}> Fill with Example Data</button>
      </div>
      
      {!isResumeReady && showPopup && <DefaultPopup handleClose={handlePopupClose} />}
    </div>
  );
};

export default ResumeDoc;
