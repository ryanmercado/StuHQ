import React, { useState } from 'react';
import './style/defaultPopup.css';
import GenInfo from './ResumeQuestionnaire/genInfo';
import Skills from './ResumeQuestionnaire/skills';
import Jobs from './ResumeQuestionnaire/jobs';
import Projects from './ResumeQuestionnaire/projects';
import Extracurr from './ResumeQuestionnaire/extracurr';

const DefaultPopup = ({ handleClose }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const [requiredFlags, setRequiredFlags] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  const nextPage = () => {
    if (currentPage < 5 && requiredFlags) {
      setCurrentPage(currentPage + 1);
    } else {
      setErrorMessage('*Please fill out all required fields before proceeding to the next page.');
    }
  };

  const prevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
      setErrorMessage('');
    }
  };

  const handleSubmit = () => {
    
  };

  const handleValidation = (isValid) => {
    setRequiredFlags(isValid);
    if (isValid) {
        setErrorMessage('');
    } else {
        setErrorMessage('*There are still Required Fields that are not met')
    }
  };

  let pageContent;
  switch (currentPage) {
    case 1:
      pageContent = (
        <GenInfo
          handleValidation={handleValidation}
        />
      );
      break;
    case 2:
      pageContent = (
        <Skills
          handleValidation={handleValidation}
        />
      );
      break;
    case 3:
      pageContent = (
        <Jobs
          handleValidation={handleValidation}
        />
      );
      break;
    case 4:
      pageContent = (
        <Projects
          handleValidation={handleValidation}
        />
      );
      break;
    case 5:
      pageContent = (
        <Extracurr
          handleValidation={handleValidation}
        />
      );
      break;
    default:
      pageContent = <GenInfo/>;
  }

  return (
    <div className="popup">
      <div className="popup-content">
        <span className="close" onClick={handleClose}>
          &times;
        </span>
        {errorMessage && (
          <div className="error-text">
            {errorMessage}
          </div>
        )}
        <div className="page-content">
          {pageContent}
          {currentPage !== 5 && (
            <span className="arrow arrow-right" onClick={nextPage}>
              &#10095;
            </span>
          )}
        </div>
      </div>
      
    </div>
  );
  
};

export default DefaultPopup;
