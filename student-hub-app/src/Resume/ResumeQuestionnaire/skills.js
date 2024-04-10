import React, { useState, useEffect } from 'react';
import './style.css';
import secureLocalStorage from 'react-secure-storage';

const Skills = ({ handleValidation }) => {
  const [skills, setSkills] = useState(Array(6).fill(''));
  const [requiredSkillsCount, setRequiredSkillsCount] = useState(6);
  const usr_id = secureLocalStorage.getItem("usr_id");
  const [isSubmittable, setIsSubmittable] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);


  useEffect(() => {
    validateSubmit();
    validateFields();
  }, [skills]);

  const validateSubmit = () => {
    const areAllSkillsValid = skills.every(skill => skill.trim() !== '');
    if(areAllSkillsValid){
      setIsSubmittable(true);
    } else {
      setIsSubmittable(false);
    }
  }

  const validateFields = () => {
    const areAllSkillsValid = skills.every(skill => skill.trim() !== '');
    if(!areAllSkillsValid)
      handleValidation(false);
    
  };
  const handleSubmit = async () => {
    try {
      // Initialize counter for successfully submitted skills
      let submittedSkillsCount = 0;
  
      // Iterate over skills array and make API call for each skill
      for (const skill of skills) {
        const formData = {
          user_id: usr_id,
          name: skill
        };
  
        // Example API call with fetch:
        const response = await fetch('http://localhost:5000/api/addResumeTechnicalSkill', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData),
        });
  
        // Check if the response is successful
        if (response.ok) {
          const data = await response.json();
          console.log('Skill added:', data);
          // Increment counter for successfully submitted skills
          submittedSkillsCount++;
        } else {
          throw new Error('Failed to add skill');
        }
      }
      // console.log('submitted: ', submittedSkillsCount)
      // console.log('skills: ', skills.length)
      // Check if all skills are submitted
      if (submittedSkillsCount === skills.length) {
        // Set isSubmitted to true only if all skills are submitted
        setIsSubmitted(true);
        handleValidation(true);
      }
      // Probably need an else that handles the case where not all skills are submitted and allows user to try again, states will need to be reset

    } catch (error) {
      console.error('Error adding skill:', error);
      // You can handle errors here if needed
    }
  };
  
  

  const handleSkillsChange = (index, value) => {
    const updatedSkills = [...skills];
    updatedSkills[index] = value;
    setSkills(updatedSkills);
  };

  const handleAddSkill = () => {
    const updatedSkills = [...skills, ''];
    setSkills(updatedSkills);
    setRequiredSkillsCount(prevCount => prevCount + 1);
  };

  const handleRemoveSkill = (index) => {
    const updatedSkills = [...skills];
    updatedSkills.splice(index, 1);
    setSkills(updatedSkills);
    setRequiredSkillsCount(prevCount => prevCount - 1);
  };

  return (
    <div className="skills-form">
      <h1>Skills</h1>
      {skills.map((skill, index) => (
        <div key={index} className="skill-input-container">
          <label htmlFor={`skill${index + 1}`}>Skill {index + 1}:</label>
          <div className="skill-input">
            <input
              type="text"
              id={`skill${index + 1}`}
              value={skill}
              onChange={(e) => handleSkillsChange(index, e.target.value)}
            />
            
            {index > 5 && (
              <button className="remove-skill-btn" onClick={() => handleRemoveSkill(index)}>
                Remove
              </button>
            )}
            
          </div>
          
        </div>
        
      ))}
      <button className="add-skill-btn" onClick={handleAddSkill}>
                Add new skill
              </button>
      <br />
      <br />
      {/* Submit button */}
      {isSubmittable && !isSubmitted && (
        <button className="resume-button" onClick={handleSubmit}>Submit</button>
      )}
    </div>
  );
};

export default Skills;
