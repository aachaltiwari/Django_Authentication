# Django Authentication Project

This project provides a simple authentication system using Django and JWT (JSON Web Token). It includes user registration, login, and profile management functionalities. The backend is built with Django and Django Rest Framework, while the frontend is built using React.

### Key Features:
- User registration and login with JWT.
- Secure profile access with token-based authentication.
- User information retrieval (e.g., name, email, and phone number).

## Installation

### Backend Setup

1. Navigate to the **backend/** directory and set up a Python virtual environment:

    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

3. Install the backend dependencies:

    ```bash
    pip install -r backend/requirements.txt
    ```

4. Apply migrations to set up the database:

    ```bash
    python backend/manage.py migrate
    ```

5. Run the Django development server:

    ```bash
    python backend/manage.py runserver
    ```

    The backend will be running at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the **frontend/** directory:

    ```bash
    cd frontend/app/
    ```

2. Install the frontend dependencies:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```

    The frontend will be running at `http://localhost:3000`.

## Usage

Once both the backend and frontend servers are running, you can interact with the authentication system through the React frontend. The system allows you to register, log in, and view your profile.

