import React, { useState } from 'react';

const Extracurr = ({ handleValidation }) => {
  const [extracurriculars, setExtracurriculars] = useState('');

  const validateFields = () => {
    if (extracurriculars.trim() !== '') {
      handleValidation(true);
    } else {
      handleValidation(false);
    }
  };

  const handleExtracurricularsChange = (e) => {
    setExtracurriculars(e.target.value);
    validateFields();
  };

  return (
    <div>
      <h1>Extracurricular Activities</h1>
      <label htmlFor="extracurriculars">Extracurriculars:</label>
      <input
        type="text"
        id="extracurriculars"
        value={extracurriculars}
        onChange={handleExtracurricularsChange}
      />
    </div>
  );
};

export default Extracurr;
