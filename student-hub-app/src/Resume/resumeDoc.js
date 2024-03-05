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

  const handleCreateResume = () => {
    setIsResumeReady(true);
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
