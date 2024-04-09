import React, { useState, useEffect } from 'react';
import './style.css';
import secureLocalStorage from 'react-secure-storage';

const Extracurr = ({ handleValidation }) => {
  const [extracurriculars, setExtracurriculars] = useState(Array(6).fill(''));
  const [requiredExtracurricularsCount, setRequiredExtracurricularsCount] = useState(6);
  const usr_id = secureLocalStorage.getItem("usr_id");
  const [isSubmittable, setIsSubmittable] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    validateSubmit();
    validateFields();
  }, [extracurriculars]);

  const validateSubmit = () => {
    const areAllExtracurricularsValid = extracurriculars.every(activity => activity.trim() !== '');
    if(areAllExtracurricularsValid){
      setIsSubmittable(true);
    } else {
      setIsSubmittable(false);
    }
  }

  const validateFields = () => {
    const areAllExtracurricularsValid = extracurriculars.every(activity => activity.trim() !== '');
    if(!areAllExtracurricularsValid)
      handleValidation(false);
  };

  const handleSubmit = async () => {
    try {
      let submittedExtracurricularsCount = 0;

      for (const activity of extracurriculars) {
        const formData = {
          user_id: usr_id,
          title: activity,
          desc: " "
        };

        const response = await fetch('http://localhost:5000/api/addResumeExtracurr', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData),
        });

        if (response.ok) {
          const data = await response.json();
          console.log('Extracurricular added:', data);
          submittedExtracurricularsCount++;
        } else {
          throw new Error('Failed to add extracurricular');
        }
      }

      if (submittedExtracurricularsCount === extracurriculars.length) {
        setIsSubmitted(true);
        handleValidation(true);
      }

    } catch (error) {
      console.error('Error adding extracurricular:', error);
    }
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
          <label htmlFor={`extracurricular${index + 1}`}>Activity {index + 1}:</label>
          <div className="extracurricular-input">
            <input
              type="text"
              id={`extracurricular${index + 1}`}
              value={activity}
              onChange={(e) => handleExtracurricularsChange(index, e.target.value)}
            />
            {index > 5 && (
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
      <br />
      <br />
      {/* Submit button */}
      {isSubmittable && !isSubmitted && (
        <button className="submitButton" onClick={handleSubmit}>Submit</button>
      )}
    </div>
  );
};

export default Extracurr;
