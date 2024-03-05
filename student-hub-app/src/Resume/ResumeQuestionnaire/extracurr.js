import React, { useState, useEffect } from 'react';
import './style.css';

const Extracurr = ({ handleValidation }) => {
  const [extracurriculars, setExtracurriculars] = useState(Array(3).fill(''));
  const [requiredExtracurricularsCount, setRequiredExtracurricularsCount] = useState(3);

  useEffect(() => {
    validateFields();
  }, [extracurriculars]);

  const validateFields = () => {
    const areAllExtracurricularsValid = extracurriculars.every(activity => activity.trim() !== '');
    handleValidation(areAllExtracurricularsValid);
    // You can add submission logic here if needed
  };

  const handleExtracurricularsChange = (index, value) => {
    const updatedExtracurriculars = [...extracurriculars];
    updatedExtracurriculars[index] = value;
    setExtracurriculars(updatedExtracurriculars);
  };

  const handleAddExtracurricular = () => {
    const updatedExtracurriculars = [...extracurriculars, ''];
    setExtracurriculars(updatedExtracurriculars);
    setRequiredExtracurricularsCount(prevCount => prevCount + 1);
  };

  const handleRemoveExtracurricular = (index) => {
    const updatedExtracurriculars = [...extracurriculars];
    updatedExtracurriculars.splice(index, 1);
    setExtracurriculars(updatedExtracurriculars);
    setRequiredExtracurricularsCount(prevCount => prevCount - 1);
  };

  return (
    <div className="extracurr-form">
      <h1>Extracurricular Activities</h1>
      {extracurriculars.map((activity, index) => (
        <div key={index} className="extracurricular-input-container">
          <label htmlFor={`extracurricular${index + 1}`}>Extracurricular {index + 1}:</label>
          <div className="extracurricular-input">
            <input
              type="text"
              id={`extracurricular${index + 1}`}
              value={activity}
              onChange={(e) => handleExtracurricularsChange(index, e.target.value)}
            />
            {index > 2 && (
              <button className="remove-extracurricular-btn" onClick={() => handleRemoveExtracurricular(index)}>
                Remove
              </button>
            )}
          </div>
        </div>
      ))}
      <button className="add-extracurricular-btn" onClick={handleAddExtracurricular}>
        Add New
      </button>
    </div>
  );
};

export default Extracurr;
