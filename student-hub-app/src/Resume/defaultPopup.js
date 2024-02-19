import React from 'react';
import './style/defaultPopup.css';
import GenInfo from './ResumeQuestionnaire/genInfo';
import Skills from './ResumeQuestionnaire/skills';
import Jobs from './ResumeQuestionnaire/jobs';
import Projects from './ResumeQuestionnaire/projects';
import Extracurr from './ResumeQuestionnaire/extracurr';


const DefaultPopup = ({ handleClose }) => {
  return (
    <div className="popup">
      <div className="popup-content">
        <span className="close" onClick={handleClose}>
          &times;
        </span>
        <p>This is the popup content.</p>
      </div>
      <span className="arrow arrow-left">&#10094;</span>
      <span className="arrow arrow-right">&#10095;</span>
    </div>
  );
};

export default DefaultPopup;
