import React, { useState, useEffect } from 'react';
import './style.css';

const GenInfo = ({ handleValidation }) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');
  const [linkedin, setLinkedin] = useState('');
  const [edu, setEdu] = useState('');
  const [major, setMajor] = useState('');
  const [GPA, setGPA] = useState('');
  const [gradMonth, setGradMonth] = useState(''); 
  const [gradYear, setGradYear] = useState('');

  const usr_id = localStorage.getItem("usr_id");

  useEffect(() => {
    validateFields();
  }, [firstName, lastName, phone, email, linkedin, edu, major, GPA]);

  const validateFields = () => {
    if (
      firstName.trim() !== '' &&
      lastName.trim() !== '' &&
      /^\(\d{3}\) \d{3}-\d{4}$/.test(phone) &&
      /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) &&
      /^\d{2}\/\d{2}$/.test(gradDate) &&
      /^\d\.\d{2}$/.test(GPA) &&
      edu.trim() !== '' &&
      major.trim() !== ''
    ) {
      handleValidation(true);
    } else {
      handleValidation(false);
    }
  };

  const handleSubmit = () => {
    const formData = {
      usr_id,
      lastname: lastName,
      firstname: firstName,
      phone,
      email,
      linkedin,
      edu,
      grad_date: gradDate,
      major,
      GPA
    };

    // Call your API here to write to the database using formData
    console.log("Form data:", formData);
    // Example API call with fetch:
    // fetch('your_api_endpoint', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json',
    //   },
    //   body: JSON.stringify(formData),
    // })
    // .then(response => response.json())
    // .then(data => console.log(data))
    // .catch(error => console.error('Error:', error));
  };

  const handleFirstNameChange = (e) => {
    setFirstName(e.target.value);
  };

  const handleLastNameChange = (e) => {
    setLastName(e.target.value);
  };

  const handlePhoneChange = (e) => {
    const inputValue = e.target.value.replace(/\D/g, ''); // Remove non-digit characters
    let formattedPhone = '';
    
    
    switch (inputValue.length) {
      case 3:
        formattedPhone = inputValue.replace(/^(\d{3})$/, '($1)');
        break;
      case 4:
        formattedPhone = inputValue.replace(/^(\d{3})(\d{1})$/, '($1) $2');
        break;
      case 5:
        formattedPhone = inputValue.replace(/^(\d{3})(\d{2})$/, '($1) $2');
        break;
      case 6:
        formattedPhone = inputValue.replace(/^(\d{3})(\d{3})(\d{0,3})$/, '($1) $2-$3');
        break;
      case 7:
        formattedPhone = inputValue.replace(/^(\d{3})(\d{3})(\d{0,4})$/, '($1) $2-$3');
        break;
      case 8:
        formattedPhone = inputValue.replace(/^(\d{3})(\d{3})(\d{0,4})$/, '($1) $2-$3');
        break;
      case 9:
        formattedPhone = inputValue.replace(/^(\d{3})(\d{3})(\d{0,4})$/, '($1) $2-$3');
        break;
      case 10:
        formattedPhone = inputValue.replace(/^(\d{3})(\d{3})(\d{4})$/, '($1) $2-$3');
        break;
      default:
        if (inputValue.length < 10)
          formattedPhone = inputValue
        
    }
    if (inputValue.length <= 10)
      setPhone(formattedPhone);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleLinkedinChange = (e) => {
    setLinkedin(e.target.value);
  };

  const handleEduChange = (e) => {
    setEdu(e.target.value);
  };

  const handleMonthChange = (e) => {
    setGradMonth(e.target.value);
  };

  const handleYearChange = (e) => {
    setGradYear(e.target.value);
  };

  const handleMajorChange = (e) => {
    setMajor(e.target.value);
  };

  const handleGPAChange = (e) => {
    const enteredGPA = parseFloat(e.target.value);
  
    if ((enteredGPA >= 0 && enteredGPA <= 5)|| e.target.value === '') {
      const formattedGPA = e.target.value.replace(/[^\d.]/g, '').replace(/(\.\d{2}).+/, '$1');
      setGPA(formattedGPA);
    }
  };

  return (
    <div className="gen-info-form">
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
      <br />
      <label htmlFor="phone">Phone:</label>
      <input
        type="tel"
        id="phone"
        value={phone}
        onChange={handlePhoneChange}
      />
      <br />
      <label htmlFor="email">Email:</label>
      <input
        type="email"
        id="email"
        value={email}
        onChange={handleEmailChange}
      />
      <br />
      <label htmlFor="linkedin">Linkedin:</label>
      <input
        type="text"
        id="linkedin"
        value={linkedin}
        onChange={handleLinkedinChange}
      />
      <br />
      <label htmlFor="edu">Education:</label>
      <input
        type="text"
        id="edu"
        value={edu}
        onChange={handleEduChange}
      />
      <br />
      <label htmlFor="gradDate">Graduation Date:</label>
      <div className="grad-date-container">
        <select id="gradMonth" value={gradMonth} onChange={handleMonthChange}>
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
        <select id="gradYear" value={gradYear} onChange={handleYearChange}>
          <option value="">Select Year</option>
          {Array.from({ length: 101 }, (_, index) => (
            <option key={index} value={1950 + index}>{1950 + index}</option>
          ))}
        </select>
      </div>
      <br />
      <label htmlFor="major">Major:</label>
      <input
        type="text"
        id="major"
        value={major}
        onChange={handleMajorChange}
      />
      <br />
      <label htmlFor="GPA">GPA (X.XX):</label>
      <input
        type="text"
        id="GPA"
        value={GPA}
        onChange={handleGPAChange}
      />
      <br />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default GenInfo;
