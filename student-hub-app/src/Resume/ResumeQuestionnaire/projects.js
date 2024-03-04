import React, { useState, useEffect } from 'react';

const Projects = ({ handleValidation }) => {
  const [projectDetails, setProjectDetails] = useState('');

  useEffect(() => {
    validateFields();
  }, [projectDetails]);

  const validateFields = () => {
    if (projectDetails.trim() !== '') {
      handleValidation(true);
      //API
    } else {
      handleValidation(false);
    }
  };

  const handleProjectDetailsChange = (e) => {
    setProjectDetails(e.target.value);
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
