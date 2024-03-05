import React, { useState, useEffect } from 'react';
import './style.css';

const Jobs = ({ handleValidation }) => {
  const [jobHistory, setJobHistory] = useState([
    {
      company: '',
      role: '',
      startDate: '',
      endDate: '',
      location: '',
      duties: ['', '']
    },
    {
      company: '',
      role: '',
      startDate: '',
      endDate: '',
      location: '',
      duties: ['', '']
    }
  ]);

  useEffect(() => {
    validateFields();
  }, [jobHistory]);

  const validateFields = () => {
    const areAllJobsValid = jobHistory.every(job => {
      return (
        job.company.trim() !== '' &&
        job.role.trim() !== '' &&
        job.startDate.trim() !== '' &&
        job.endDate.trim() !== '' &&
        job.location.trim() !== '' &&
        job.duties.every(duty => duty.trim() !== '')
      );
    });
    handleValidation(areAllJobsValid);
    // You can add submission logic here if needed
  };

  const handleJobChange = (index, field, value) => {
    const updatedJobHistory = [...jobHistory];
    updatedJobHistory[index][field] = value;
    setJobHistory(updatedJobHistory);
  };

  const handleDutyChange = (jobIndex, dutyIndex, value) => {
    const updatedJobHistory = [...jobHistory];
    updatedJobHistory[jobIndex].duties[dutyIndex] = value;
    setJobHistory(updatedJobHistory);
  };

  const handleAddJob = () => {
    const newJob = {
      company: '',
      role: '',
      startDate: '',
      endDate: '',
      location: '',
      duties: ['', '']
    };
    setJobHistory(prevJobHistory => [...prevJobHistory, newJob]);
  };

  const handleAddDuty = (jobIndex) => {
    const updatedJobHistory = [...jobHistory];
    updatedJobHistory[jobIndex].duties.push('');
    setJobHistory(updatedJobHistory);
  };

  return (
    <div className="jobs-form">
      <h1>Job History</h1>
      {jobHistory.map((job, jobIndex) => (
        <div key={jobIndex} className="job-container">
          <label>Job {jobIndex + 1}:</label>
          <input
            type="text"
            value={job.company}
            placeholder="Company Name"
            onChange={(e) => handleJobChange(jobIndex, 'company', e.target.value)}
          />
          <input
            type="text"
            value={job.role}
            placeholder="Your Role"
            onChange={(e) => handleJobChange(jobIndex, 'role', e.target.value)}
          />
          <input
            type="text"
            value={job.startDate}
            placeholder="Start Date"
            onChange={(e) => handleJobChange(jobIndex, 'startDate', e.target.value)}
          />
          <input
            type="text"
            value={job.endDate}
            placeholder="End Date"
            onChange={(e) => handleJobChange(jobIndex, 'endDate', e.target.value)}
          />
          <input
            type="text"
            value={job.location}
            placeholder="Location"
            onChange={(e) => handleJobChange(jobIndex, 'location', e.target.value)}
          />
          {job.duties.map((duty, dutyIndex) => (
            <input
              key={dutyIndex}
              type="text"
              value={duty}
              placeholder={`What you did ${dutyIndex + 1}`}
              onChange={(e) => handleDutyChange(jobIndex, dutyIndex, e.target.value)}
            />
          ))}
          <button onClick={() => handleAddDuty(jobIndex)}>Add Duty</button>
        </div>
      ))}
      <button onClick={handleAddJob}>Add Job</button>
    </div>
  );
};

export default Jobs;
