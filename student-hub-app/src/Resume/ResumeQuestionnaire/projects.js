import React, { useState } from 'react';

const Projects = ({ handleValidation }) => {
  const [projectDetails, setProjectDetails] = useState('');

  const validateFields = () => {
    if (projectDetails.trim() !== '') {
      handleValidation(true);
    } else {
      handleValidation(false);
    }
  };

  const handleProjectDetailsChange = (e) => {
    setProjectDetails(e.target.value);
    validateFields();
  };

  return (
    <div>
      <h1>Projects</h1>
      <label htmlFor="projectDetails">Project Details:</label>
      <input
        type="text"
        id="projectDetails"
        value={projectDetails}
        onChange={handleProjectDetailsChange}
      />
    </div>
  );
};

export default Projects;
