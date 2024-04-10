import React, { useState, useEffect } from 'react';
import './style.css';
import secureLocalStorage from 'react-secure-storage';

const Jobs = ({ handleValidation }) => {
  const [jobHistory, setJobHistory] = useState([
    {
      company: '',
      role: '',
      startDate: '',
      endDate: '',
      location: '',
      duties: ''
    },
    {
      company: '',
      role: '',
      startDate: '',
      endDate: '',
      location: '',
      duties: ''
    }
  ]);
  const usr_id = secureLocalStorage.getItem("usr_id");
  const [isSubmittable, setIsSubmittable] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    validateFields();
    validateSubmit();
  }, [jobHistory]);

  const validateSubmit = () => {
    const areAllJobsValid = jobHistory.every(job => {
      return (
        job.company.trim() !== '' &&
        job.role.trim() !== '' &&
        job.startDate.trim() !== '' &&
        job.endDate.trim() !== '' &&
        job.location.trim() !== '' &&
        job.duties.trim() !== ''
      );
    });
    setIsSubmittable(areAllJobsValid);
  
  }
  const validateFields = () => {
    const areAllJobsValid = jobHistory.every(job => {
      return (
        job.company.trim() !== '' &&
        job.role.trim() !== '' &&
        job.startDate.trim() !== '' &&
        job.endDate.trim() !== '' &&
        job.location.trim() !== '' &&
        job.duties.trim() !== ''
      );
    });
    if (!areAllJobsValid)
      handleValidation(areAllJobsValid);
    // You can add submission logic here if needed
  };

  const handleSubmit = async () => {
    let submittedCount = 0;
    for (const job of jobHistory) {
      const formData = {
        user_id: usr_id,
        company: job.company,
        role: job.role,
        start_date: job.startDate,
        end_date: job.endDate,
        location: job.location,
        desc_arr: JSON.stringify([job.duties]) //This needs to be run through GPT before here
      };

      const response = await fetch('http://localhost:5000/api/addResumeExperience', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Job added:', data);
        submittedCount++;
      } else {
        throw new Error('Failed to add job');
      }
    }
    if (submittedCount === jobHistory.length) {
      setIsSubmitted(true);
      handleValidation(true);
    }

  };

  const handleJobChange = (index, field, value) => {
    const updatedJobHistory = [...jobHistory];
    updatedJobHistory[index][field] = value;
    setJobHistory(updatedJobHistory);
  };

  const handleAddJob = () => {
    if (jobHistory.length < 4) {
      const newJob = {
        company: '',
        role: '',
        startDate: '',
        endDate: '',
        location: '',
        duties: ''
      };
      setJobHistory(prevJobHistory => [...prevJobHistory, newJob]);
    }
  };

  const handleDeleteJob = index => {
    const updatedJobHistory = [...jobHistory];
    updatedJobHistory.splice(index, 1);
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
          <textarea
            className="description-input"
            value={job.duties}
            placeholder={`Give us Job Information to run through GPT`}
            onChange={(e) => handleJobChange(jobIndex, 'duties', e.target.value)}
          />
          {jobIndex >= 2 && (
            <button onClick={() => handleDeleteJob(jobIndex)}>Delete Job</button>
          )}
        </div>
      ))}
      {jobHistory.length < 4 && (
        <button className="add-job-button" onClick={handleAddJob}>Add Job</button>
      )}
      <br />
      <br />
      {/* Submit button */}
      {isSubmittable && !isSubmitted && (
        <button className="resume-button" onClick={handleSubmit}>Submit</button>
        )}
    </div>
  );
};

export default Jobs;
