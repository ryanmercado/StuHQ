// SignUp.js

import React, { useState } from 'react';

const SignUp = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        confirm_password: '',
    });

    const[createdFailed, setCreatedFailed] = useState(false);
    const[failedMessage, setFailedMessage] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
            const response = await fetch('http://localhost:5000/api/createAccount', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();

            if (response.data.result === 'account created successfully') {
                
                history.push('/dashboard')

            } else if (response.data.result === 'username already exists'){
                setCreatedFailed(true);
                setFailedMessage = response.data.result;
                
            } else if (response.data.result === 'a user has already signed up with this email'){
                setCreatedFailed(true);
                setFailedMessage = response.data.result;
            } else if (response.data.result === 'passwords do not match'){
                setCreatedFailed(true);
                setFailedMessage = response.data.result;
            }
        }catch (error) {
            console.error('Login error:', error);
        } finally{
            setFormData({
                username: '',
                password: '',
            });
        }
        
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
                        value={formData.username}
                        onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    Email:
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    Password:
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    Confirm Password:
                    <input
                        type="password"
                        name="confirm_password"
                        value={formData.confirm_password}
                        onChange={handleChange}
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
