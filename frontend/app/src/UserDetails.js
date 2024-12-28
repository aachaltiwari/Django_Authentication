import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './UserDetails.css';

function UserDetails() {
  const [userDetails, setUserDetails] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    navigate('/login');
  };

  useEffect(() => {
    const fetchUserDetails = async () => {
      setError(null);
      try {
        const response = await fetch('http://localhost:8000/auth/users/me/', {
          method: 'GET',
          headers: {
            Authorization: `Aachal ${localStorage.getItem('access')}`,
          },
        });

        if (!response.ok) {
          if (response.status === 401) {
            throw new Error('Unauthorized. Please log in.');
          }
          throw new Error('Failed to fetch user details');
        }

        const data = await response.json();
        setUserDetails(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchUserDetails();
  }, []);

  return (
    <div className="userdetails-container">
      <h2>User Details</h2>
      {error && <p className="error">{error}</p>}
      {userDetails && (
        <div>
          <p>Username: {userDetails.username}</p>
          <p>Email: {userDetails.email}</p>
          <p>First Name: {userDetails.first_name}</p>
          <p>Last Name: {userDetails.last_name}</p>
          <p>Phone Number: {userDetails.phone_number}</p>
        </div>
      )}
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default UserDetails;
