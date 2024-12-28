import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './Home';
import Login from './Login';
import Register from './Register';
import UserDetails from './UserDetails';
import './App.css';

function App() {
  return (
    <Router>
      <div className="menu">
        <Link to="/home" className="home-button">Home</Link>
      </div>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/userdetails" element={<UserDetails />} />
      </Routes>
    </Router>
  );
}

export default App;

