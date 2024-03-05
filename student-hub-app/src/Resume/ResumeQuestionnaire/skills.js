import React, { useState, useEffect } from 'react';
import './style.css';

const Skills = ({ handleValidation }) => {
  const [skills, setSkills] = useState(Array(6).fill(''));
  const [requiredSkillsCount, setRequiredSkillsCount] = useState(6);

  useEffect(() => {
    validateFields();
  }, [skills]);

  const validateFields = () => {
    const areAllSkillsValid = skills.every(skill => skill.trim() !== '');
    if(areAllSkillsValid){
      submitSkills();
    }
    handleValidation(areAllSkillsValid);
    
  };
  const submitSkills = () => {
    //Call API here
    
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
    </div>
  );
};

export default Skills;
