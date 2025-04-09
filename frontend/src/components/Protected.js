import React, { use, useState } from 'react';

const Protected = () => {
  const [error, setError] = useState('');
  const [m, setM] = useState('');

  const getProtected = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/protected', {
        method: 'GET',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        credentials: 'include',
      });
      const data = await response.json();
      if (data.message) {
        setM(data.message);
        setError('');
      } else {
        setError(data.error || 'Unknown error');
        setM('');
      }
    } catch (err) {
      console.error(err);
      setError('Request failed');
    }
  };

  return (
    <div>
      {error && <p style={{color:'red'}}>{error}</p>}
      <button onClick={getProtected}>Get Protected Content</button>
      <p>{m}</p>
    </div>
  );
};

export default Protected;
