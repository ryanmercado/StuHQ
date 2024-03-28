import React, { useState, useEffect } from 'react';
import './style.css'; // Assuming the CSS file is named Projects.css

const Projects = ({ handleValidation }) => {
  const [projects, setProjects] = useState([
    {
      title: '',
      whoFor: '',
      date: '',
      descArr: ''
    },
    {
      title: '',
      whoFor: '',
      date: '',
      descArr: ''
    }
  ]);

  useEffect(() => {
    validateFields();
  }, [projects]);

  const validateFields = () => {
    const areAllProjectsValid = projects.every(project => {
      return (
        project.title.trim() !== '' &&
        project.date.trim() !== '' &&
        project.descArr.trim() !== ''
      );
    });
    handleValidation(areAllProjectsValid);
    // You can add submission logic here if needed
  };

  const handleProjectChange = (index, field, value) => {
    const updatedProjects = [...projects];
    updatedProjects[index][field] = value;
    setProjects(updatedProjects);
  };

  const handleAddProject = () => {
    if (projects.length < 4) {
      const newProject = {
        title: '',
        whoFor: '',
        date: '',
        descArr: ''
      };
      setProjects(prevProjects => [...prevProjects, newProject]);
    }
  };

  const handleDeleteProject = index => {
    if (projects.length > 2 && index >= 2) {
      const updatedProjects = [...projects];
      updatedProjects.splice(index, 1);
      setProjects(updatedProjects);
    }
  };

  return (
    <div className="projects-container">
      <h1>Projects</h1>
      {projects.map((project, projectIndex) => (
        <div key={projectIndex} className="project">
          <h2>Project {projectIndex + 1}</h2>
          <label>Title:</label>
          <input
            type="text"
            value={project.title}
            onChange={(e) => handleProjectChange(projectIndex, 'title', e.target.value)}
          />
          <label>Who For:</label>
          <input
            type="text"
            value={project.whoFor}
            onChange={(e) => handleProjectChange(projectIndex, 'whoFor', e.target.value)}
          />
          <label>Date:</label>
          <input
            type="text"
            value={project.date}
            onChange={(e) => handleProjectChange(projectIndex, 'date', e.target.value)}
          />
          <label>Description Array:</label>
          <textarea
            className="description-input" // Added class name to match the CSS
            value={project.descArr}
            onChange={(e) => handleProjectChange(projectIndex, 'descArr', e.target.value)}
          />
          {projectIndex > 1 && projectIndex <= 3 && (
            <button className="delete-project-button" onClick={() => handleDeleteProject(projectIndex)}>Delete Project</button>
          )}
        </div>
      ))}
      {projects.length < 4 && (
        <button className="add-project-button" onClick={handleAddProject}>Add Project</button>
      )}
    </div>
  );
  
};

export default Projects;
