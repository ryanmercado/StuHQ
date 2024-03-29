// SignUp.js
import React, { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage'

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
                  setFailedMessage(response.result)
              }
              else if (response.result === 'a user has already signed up with this email'){
                  setCreatedFailed(true);
                  setFailedMessage(response.result)
              }
              else if (response.result === 'passwords do not match'){
                  setCreatedFailed(true);
                  setFailedMessage(response.result)
  
              }
            }
          };
        xhr.send(jsonData);
        setPasswordValue('')
        setConfirmPasswordValue('')
    };

    return (
        <div>
            <h2>Sign Up</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input
                        type="text"
                        name="username"
                        value={username}
                        onChange={(e) => setUsernameValue(e.target.value)}
                    />
                </label>
                <br />
                <label>
                    Email:
                    <input
                        type="email"
                        name="email"
                        value={email}
                        onChange={(e) => setEmailValue(e.target.value)}
                    />
                </label>
                <br />
                <label>
                    Password:
                    <input
                        type="password"
                        name="password"
                        value={password}
                        onChange={(e) => setPasswordValue(e.target.value)}
                    />
                </label>
                <br />
                <label>
                    Confirm Password:
                    <input
                        type="password"
                        name="confirm_password"
                        value={confirm_password}
                        onChange={(e) => setConfirmPasswordValue(e.target.value)} 
                    />
                </label>
                <br />
                <button type="submit">Sign Up</button>
                {createdFailed && <div style={{ color: 'red' }}>{failedMessage}</div>}
            </form>
        </div>
    );
};

export default SignUp;
