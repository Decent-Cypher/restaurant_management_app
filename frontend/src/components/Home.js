import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [feedback, setFeedback] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/feedback/')
      .then(response => {
        setFeedback(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the feedback!', error);
      });
  }, []);

  return (
    <div>
      <h1>hello bro</h1>
      <ul>
        {feedback.map(item => (
          <li key={item.id}>{item.comment} - {item.rating}</li>
        ))}
      </ul>
    </div>
  );
};

export default Home;