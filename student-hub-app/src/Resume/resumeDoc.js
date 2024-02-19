import React, { useState } from 'react';
import './style/resume.css';
import DefaultPopup from './defaultPopup';

const ResumeDoc = () => {
  const [isResumeReady, setIsResumeReady] = useState(false);
  const [showPopup, setShowPopup] = useState(true);

  const handleCreateResume = () => {
    setIsResumeReady(true);
  };

  const handlePopupClose = () => {
    setShowPopup(false);
  };

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
