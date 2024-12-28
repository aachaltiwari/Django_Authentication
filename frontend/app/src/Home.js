import React from 'react';
import './Home.css';

function Home() {
  return (
    <div className="home-container">
      <h1>Welcome to the Authentication System</h1>
      <p>Manage your login, registration, and user details efficiently.</p>
      <div className="buttons">
        <a href="/login" className="btn">Login</a>
        <a href="/register" className="btn">Register</a>
        <a href="/userdetails" className="btn">User Details</a>
      </div>
    </div>
  );
}

export default Home;