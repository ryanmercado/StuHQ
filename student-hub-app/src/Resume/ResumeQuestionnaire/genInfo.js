import React, { useState } from 'react';
import './style.css';

const GenInfo = ({handleValidation}) => {
    // Need a state for each field
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');

    // This is where we validate that all fields are filled out

  const validateFields = () => { 
    if (firstName.trim() !== '' && lastName.trim() !== '') {
      handleValidation(true);
      //Store/Jsonify Values at this point?
    } else {
      handleValidation(false);
    }
  };

  // Need a function to handle the change of each field
  const handleFirstNameChange = (e) => {
    setFirstName(e.target.value);
    validateFields();
  };

  const handleLastNameChange = (e) => {
    setLastName(e.target.value);
    validateFields();
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
