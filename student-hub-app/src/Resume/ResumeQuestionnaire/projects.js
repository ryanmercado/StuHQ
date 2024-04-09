import React, { useState, useEffect } from 'react';
import './style.css'; // Assuming the CSS file is named Projects.css
import secureLocalStorage from 'react-secure-storage';

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
  const usr_id = secureLocalStorage.getItem("usr_id");
  const [isSubmittable, setIsSubmittable] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    validateFields();
    validateSubmit();
  }, [projects]);

  const validateSubmit = () => {
    const areAllProjectsValid = projects.every(project => {
      return (
        project.title.trim() !== '' &&
        project.date.trim() !== '' &&
        project.descArr.trim() !== ''
      );
    });
    setIsSubmittable(areAllProjectsValid);
  }

  const validateFields = () => {
    const areAllProjectsValid = projects.every(project => {
      return (
        project.title.trim() !== '' &&
        project.date.trim() !== '' &&
        project.descArr.trim() !== ''
      );
    });
    if(!areAllProjectsValid)
      handleValidation(areAllProjectsValid);
    // You can add submission logic here if needed
  };

  const handleSubmit = async () => {
    let submittedProjectsCount = 0;
    for (const project of projects) {
      const formData = {
        user_id: usr_id,
        title: project.title,
        who_for: project.whoFor,
        date: project.date,
        desc_arr: JSON.stringify([project.descArr])
      };

      // Example API call with fetch:
      const response = await fetch('http://localhost:5000/api/addResumeProject', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      // Check if the response is successful
      if (response.ok) {
        const data = await response.json();
        console.log('Project added:', data);
        submittedProjectsCount++;
      } else {
        console.error('Failed to add project:', response);
      }
    }
    if (submittedProjectsCount === projects.length) {
      setIsSubmitted(true);
      handleValidation(true);
    }
  }

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
      <br />
      <br />
      {/* Submit button */}
      {isSubmittable && !isSubmitted && (
        <button className='resume-button' onClick={handleSubmit}>Submit</button>
        )}

    </div>
  );
  
};

export default Projects;
