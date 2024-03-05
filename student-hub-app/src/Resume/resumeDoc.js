import React, { useState, useEffect } from 'react';
import './style/resume.css';
import DefaultPopup from './defaultPopup';
import { useNavigate } from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage';

const ResumeDoc = () => {
  const navigate = useNavigate();
  const usr_id = secureLocalStorage.getItem('usr_id');
  const [isResumeReady, setIsResumeReady] = useState(false);
  const [showPopup, setShowPopup] = useState(true);

  const handleCreateResume = async () => {
    
    try {
      const response = await fetch('/api/generate_resume', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_id: 1 })
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
      {(
        <div>
          <button className="create-resume-btn" onClick={handleCreateResume}>
            Create Resume
          </button>
          {!isResumeReady && showPopup && <DefaultPopup handleClose={handlePopupClose} />}
        </div>
      )}
    </div>
  );
};

export default ResumeDoc;
