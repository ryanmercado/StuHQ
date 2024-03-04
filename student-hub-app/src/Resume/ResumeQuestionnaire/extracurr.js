import React, { useState, useEffect } from 'react';

const Extracurr = ({ handleValidation }) => {
  const [extracurriculars, setExtracurriculars] = useState('');

  useEffect(() => {
    validateFields();
  }, [extracurriculars]);

  const validateFields = () => {
    if (extracurriculars.trim() !== '') {
      handleValidation(true);
    } else {
      handleValidation(false);
    }
  };

  const handleExtracurricularsChange = (e) => {
    setExtracurriculars(e.target.value);
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
