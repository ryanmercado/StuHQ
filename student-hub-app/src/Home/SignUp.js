// SignUp.js
import React, { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage'
import { Link } from 'react-router-dom';
import '../assets/styles/Global.css';
import '../assets/styles/Login.css'; 
import logo from '../assets/images/StuHQlogo.png'; 
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircleExclamation } from '@fortawesome/free-solid-svg-icons';



function SignUp() {
    const navigate = useNavigate();
    const [username, setUsernameValue] = useState('');
    const [password, setPasswordValue] = useState('');
    const [email, setEmailValue] = useState('');
    const [confirm_password, setConfirmPasswordValue] = useState('');
    const [createdFailed, setCreatedFailed] = useState(false);
    const [failedMessage, setFailedMessage] = useState('');

    const handleSubmit = async (e) => {
        const formData = {
            username: username,
            password: password,
            email: email,
            confirm_password: confirm_password,
        }
        const jsonData = JSON.stringify(formData)
        e.preventDefault();
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:5000/api/createAccount");
        xhr.setRequestHeader("Content-Type", "application/json"); 
        xhr.onload = () => {
            if (xhr.status === 200) { // Handle cases: username taken, pwds don't match, email taken
              const response = JSON.parse(xhr.response)
              if (response.result === 'account created successfully') {
                  secureLocalStorage.setItem('usr_id', response.usr_id)
                  navigate('/dashboard');

              }
              else if (response.result === 'username already exists'){
                  setCreatedFailed(true);
                  setFailedMessage('Username already exists')
              }
              else if (response.result === 'a user has already signed up with this email'){
                  setCreatedFailed(true);
                  setFailedMessage('A user has already signed up with this email')
              }
              else if (response.result === '*Passwords do not match'){
                  setCreatedFailed(true);
                  setFailedMessage("Passwords do not match")
                  
  
              }
            }
          };
        xhr.send(jsonData);
        setPasswordValue('')
        setConfirmPasswordValue('')
    };

    return (
        <div className='global-container'>
            <div className='login-content'>
                <h2>Sign Up</h2>
                <img src={logo} alt="Logo" className="logo" />
                <form onSubmit={handleSubmit}>
                    <label style={{display: 'block', textAlign: 'left'}}>
                        Username:
                        <input className= 'input-field'
                            type="text"
                            name="username"
                            value={username}
                            onChange={(e) => setUsernameValue(e.target.value)}
                        />
                    </label>
                    <br />
                    <label style={{display: 'block', textAlign: 'left'}}>
                        Email:
                        <input className= 'input-field'
                            type="email"
                            name="email"
                            value={email}
                            onChange={(e) => setEmailValue(e.target.value)}
                        />
                    </label>
                    <br />
                    <label style={{display: 'block', textAlign: 'left'}}>
                        Password:
                        <input className= 'input-field'
                            type="password"
                            name="password"
                            value={password}
                            onChange={(e) => setPasswordValue(e.target.value)}
                        />
                    </label>
                    <br />
                    <label style={{display: 'block', textAlign: 'left'}}>
                        Confirm Password:
                        <input className= 'input-field'
                            type="password"
                            name="confirm_password"
                            value={confirm_password}
                            onChange={(e) => setConfirmPasswordValue(e.target.value)} 
                        />
                    </label>
                    <br />
                    <div className="global-button-group">
                        <button className='login-button' type="submit">Sign Up</button>
                        <Link to="/">
                            <button className="home-button">Home</button>
                        </Link>
                    </div>
                    {createdFailed && ( 
                        <div className='failed-message'>
                            <FontAwesomeIcon icon={faCircleExclamation} /> {failedMessage}
                        </div>
                    )}
                </form>
            </div>
        </div>
    );
};

export default SignUp;
