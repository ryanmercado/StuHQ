import React, { useState } from 'react';

const Skills = ({ handleValidation }) => {
  const [skills, setSkills] = useState('');

  const validateFields = () => {
    if (skills.trim() !== '') {
      handleValidation(true);
    } else {
      handleValidation(false);
    }
  };

  const handleSkillsChange = (e) => {
    setSkills(e.target.value);
    validateFields();
  };

  return (
    <div>
      <h1>Skills</h1>
      <label htmlFor="skills">Skills:</label>
      <input
        type="text"
        id="skills"
        value={skills}
        onChange={handleSkillsChange}
      />
    </div>
  );
};

export default Skills;
