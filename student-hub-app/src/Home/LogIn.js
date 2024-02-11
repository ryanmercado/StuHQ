// Login.js

import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

const LogIn = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });
    const [loginFailed, setLoginFailed] = useState(false);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        try{
            const response = await fetch('http://localhost:5000/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            
            const data = await response.json();

            if (response.data.result === 'login successful') {
                history.push('/dashboard')
            }else{
                setLoginFailed(true)
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
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input
                        type="username"
                        name="username"
                        value={formData.username}
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
                <button type="submit">Login</button>
            </form>
            {loginFailed && <div style={{ color: 'red' }}>Login failed</div>}
        </div>
    );
};

export default LogIn;

