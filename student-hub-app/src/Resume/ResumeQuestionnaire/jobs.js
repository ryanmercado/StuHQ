import React, { useState, useEffect } from 'react';

const Jobs = ({ handleValidation }) => {
  const [jobHistory, setJobHistory] = useState('');


  useEffect(() => {
    validateFields();
  }, [jobHistory]);

  const validateFields = () => {
    if (jobHistory.trim() !== '') {
      handleValidation(true);
    } else {
      handleValidation(false);
    }
  };

  const handleJobHistoryChange = (e) => {
    setJobHistory(e.target.value);
  };

  return (
    <div>
      <h1>Job History</h1>
      <label htmlFor="jobHistory">Job History:</label>
      <input
        type="text"
        id="jobHistory"
        value={jobHistory}
        onChange={handleJobHistoryChange}
      />
    </div>
  );
};

export default Jobs;
