import React, { useState, useEffect } from 'react';
import './style.css';
import secureLocalStorage from 'react-secure-storage';

const Extracurr = ({ handleValidation, handleClose }) => {
  const [extracurriculars, setExtracurriculars] = useState([{ activity: '', month: '', year: '' }, { activity: '', month: '', year: '' }, { activity: '', month: '', year: '' }]);
  const usr_id = secureLocalStorage.getItem("usr_id");
  const [isSubmittable, setIsSubmittable] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    validateSubmit();
    validateFields();
  }, [extracurriculars]);

  const validateSubmit = () => {
    const areAllExtracurricularsValid = extracurriculars.every(activity => activity.activity.trim() !== '' && activity.month !== '' && activity.year !== '');
    setIsSubmittable(areAllExtracurricularsValid);
  }

  const validateFields = () => {
    const areAllExtracurricularsValid = extracurriculars.every(activity => activity.activity.trim() !== '' && activity.month !== '' && activity.year !== '');
    if (!areAllExtracurricularsValid)
      handleValidation(false);
  };

  const handleSubmit = async () => {
    try {
      let submittedExtracurricularsCount = 0;

      for (const activity of extracurriculars) {
        const formData = {
          user_id: usr_id,
          title: activity.activity,
          desc: activity.month + ' ' + activity.year,
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
        handleClose();
      }

    } catch (error) {
      console.error('Error adding extracurricular:', error);
    }
  };

  const handleExtracurricularsChange = (index, field, value) => {
    const updatedExtracurriculars = [...extracurriculars];
    updatedExtracurriculars[index][field] = value;
    setExtracurriculars(updatedExtracurriculars);
  };

  const handleAddExtracurricular = () => {
    const updatedExtracurriculars = [...extracurriculars, { activity: '', month: '', year: '' }];
    setExtracurriculars(updatedExtracurriculars);
  };

  const handleRemoveExtracurricular = (index) => {
    const updatedExtracurriculars = [...extracurriculars];
    updatedExtracurriculars.splice(index, 1);
    setExtracurriculars(updatedExtracurriculars);
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
              value={activity.activity}
              onChange={(e) => handleExtracurricularsChange(index, 'activity', e.target.value)}
            />
            <label htmlFor={`month${index + 1}`}></label>
            <select
              id={`month${index + 1}`}
              value={activity.month}
              onChange={(e) => handleExtracurricularsChange(index, 'month', e.target.value)}
            >
              <option value="">Select Month</option>
              <option value="January">January</option>
              <option value="February">February</option>
              <option value="March">March</option>
              <option value="April">April</option>
              <option value="May">May</option>
              <option value="June">June</option>
              <option value="July">July</option>
              <option value="August">August</option>
              <option value="September">September</option>
              <option value="October">October</option>
              <option value="November">November</option>
              <option value="December">December</option>
            </select>
            <select
              id={`year${index + 1}`}
              value={activity.year}
              onChange={(e) => handleExtracurricularsChange(index, 'year', e.target.value)}
            >
              <option value="">Select Year</option>
              {Array.from({ length: 101 }, (_, index) => (
                <option key={index} value={1950 + index}>{1950 + index}</option>
              ))}
            </select>
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
      <br />
      <br />
      {/* Submit button */}
      {isSubmittable && !isSubmitted && (
        <button className="resume-button" onClick={handleSubmit}>Submit</button>
      )}
    </div>
  );
};

export default Extracurr;
