# Chess Application

This application is designed to display chess player data retrieved from the Lichess API. It consists of a frontend built with ReactJS, a backend powered by Python with FastAPI, and utilizes a PostgreSQL database for data storage.

## Prerequisites

Ensure you have the following installed on your system:

- Node.js and npm (for running ReactJS)
- Python (for running the backend with FastAPI)
- PostgreSQL (for the database)

## Setup

### Frontend (ReactJS)

1. Navigate to the `frontend` directory:
cd frontend

2. Install dependencies:
npm install

3. Start the React development server:
npm start

4. Access the frontend at `http://localhost:3000` in your web browser.

### Backend (Python with FastAPI)

1. Navigate to the `backend` directory:
cd backend

arduino

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate # For Linux/Mac, use venv\Scripts\activate for Windows


3. Install dependencies:
pip install fastapi uvicorn databases[postgresql]


4. Run the backend server:
uvicorn main:app --reload


5. The backend will be accessible at `http://localhost:8000`

### PostgreSQL Database

1. Ensure PostgreSQL is running.

2. Create a database named `chess_app`:
createdb chess_app

arduino

3. Set up the tables by running the database migration script (if available):
python manage.py migrate

