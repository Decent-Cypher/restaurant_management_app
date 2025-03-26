import React, { useState } from 'react';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loggedIn, setLoggedIn] = useState(false);
  const [error, setError] = useState('');

  const handleDinerLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/diner-login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        credentials: 'include',
        body: new URLSearchParams({ username, password })
        // or JSON if you prefer, but then handle CSRF
      });
      const data = await response.json();
      if (data.success) {
        setLoggedIn(true);
        setError('');
      } else {
        setError(data.error || 'Unknown error');
        setLoggedIn(false);
      }
    } catch (err) {
      console.error(err);
      setError('Request failed');
    }
  };

  return (
    <div>
      <h2>Diner Login</h2>
      <form onSubmit={handleDinerLogin}>
        <input 
          type="text" 
          placeholder="Your username"
          value={username} 
          onChange={(e) => setUsername(e.target.value)} 
        /><br/>
        <input 
          type="password" 
          placeholder="Your password"
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
        /><br/>
        <button type="submit">Login</button>
      </form>
      {error && <p style={{color:'red'}}>{error}</p>}
      {loggedIn && <p>You are logged in!</p>}
    </div>
  );
};

export default LoginForm;
