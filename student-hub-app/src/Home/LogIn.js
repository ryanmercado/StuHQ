
import React, { useState } from 'react';
import {useNavigate} from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage'
import { Link } from 'react-router-dom';
import '../assets/styles/Login.css'; 
import '../assets/styles/Global.css'; 
import logo from '../assets/images/StuHQlogo.png'; 
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircleExclamation } from '@fortawesome/free-solid-svg-icons';



const LogIn = () => {
    const navigate = useNavigate();
    const [username, setUsernameValue] = useState('');
    const [password, setPasswordValue] = useState('');
    const [loginFailed, setLoginFailed] = useState(false);

    const handleSubmit = async (e) => {
        const formData = {
            username: username,
            password: password,
        }
        const jsonData = JSON.stringify(formData)
        e.preventDefault();
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:5000/api/login");
        xhr.setRequestHeader("Content-Type", "application/json"); 
        xhr.onload = () => {
          if (xhr.status === 200) { 
            const response = JSON.parse(xhr.response)
            console.log(response)
            if (response.result === 'login successful') {
                secureLocalStorage.setItem('usr_id', response.usr_id)
                navigate('/dashboard');
            }
            else if (response.result === 'login failed') {
                setLoginFailed(true);
            }

          }
        };
        xhr.send(jsonData);
        setPasswordValue('')
    };

    return (
        <div className='global-container'>
            <div className='login-content'>
                <h2>Login to</h2>
                <img src={logo} alt="Logo" className="logo" />
                <form  onSubmit={handleSubmit}>
                <br></br>
                    <label style={{display: 'block', textAlign: 'left'}}>
                        Username:
                        <input className= 'input-field'
                            type="username"
                            name="username"
                            value={username}
                            onChange={(e) => setUsernameValue(e.target.value)}
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
                    <br />
                    <div className="global-button-group">
                        <button className='login-button' type="submit">Login</button>
                        <Link to="/">
                            <button className="home-button">Home</button>
                        </Link>
                    </div>
                </form>
                {loginFailed && ( 
                        <div className='failed-message'>
                            <FontAwesomeIcon icon={faCircleExclamation} /> Login Failed
                        </div>
                    )}
            </div>
        </div>
    );
};

export default LogIn;

