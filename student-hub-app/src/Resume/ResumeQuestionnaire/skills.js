import React, { useState, useEffect } from 'react';

const Skills = ({ handleValidation }) => {
  const [skills, setSkills] = useState('');

  useEffect(() => {
    validateFields();
  }, [skills]);

  const validateFields = () => {
    if (skills.trim() !== '') {
      handleValidation(true);
      // CALL API AND WRITE TO DB
    } else {
      handleValidation(false);
    }
  };

  const handleSkillsChange = (e) => {
    setSkills(e.target.value);
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
