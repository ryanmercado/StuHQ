import React, { useState, useEffect } from 'react';
import './style.css';

const GenInfo = ({ handleValidation }) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');

  useEffect(() => {
    validateFields();
  }, [firstName, lastName]); // Run the effect whenever firstName or lastName changes

  const validateFields = () => {
    if (firstName.trim() !== '' && lastName.trim() !== '') {
      handleValidation(true);
      // CALL API AND WRITE TO DB
    } else {
      handleValidation(false);
    }
  };

  const handleFirstNameChange = (e) => {
    setFirstName(e.target.value);
  };

  const handleLastNameChange = (e) => {
    setLastName(e.target.value);
  };

  return (
    <div>
      <h1>General Information</h1>
      <label htmlFor="firstName">First Name:</label>
      <input
        type="text"
        id="firstName"
        value={firstName}
        onChange={handleFirstNameChange}
      />
      <br />
      <label htmlFor="lastName">Last Name:</label>
      <input
        type="text"
        id="lastName"
        value={lastName}
        onChange={handleLastNameChange}
      />
    </div>
  );
};

export default GenInfo;
