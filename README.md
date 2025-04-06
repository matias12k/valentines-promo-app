# Valentines Giveaway App

## Overview
This project is a Full Stack application designed for a Valentine's Day giveaway hosted by a hotel. It allows users to register, verify their email, and participate in a random draw for a prize. The application is built using Django with Django REST Framework for the backend and Vue.js (or Nuxt.js) for the frontend.

## Project Structure
The project is divided into two main parts: the backend and the frontend.

### Backend
- **Django**: The backend is built using Django, which provides a robust framework for building web applications.
- **Django REST Framework**: This is used to create RESTful APIs for the application.
- **Celery**: Used for handling asynchronous tasks, such as sending verification emails.
- **Redis**: Acts as a message broker for Celery.

### Frontend
- **Vue.js/Nuxt.js**: The frontend is developed using Vue.js or Nuxt.js, providing a reactive user interface.
- **Axios**: Used for making HTTP requests to the backend API.

## Features
1. **User Registration**: Users can register with their name and email. A verification email is sent upon registration.
2. **Email Verification**: Users can verify their email using a token sent to their inbox.
3. **Password Setup**: Verified users can set their password to complete their account creation.
4. **Admin Login**: An admin interface allows hotel staff to log in and manage the giveaway.
5. **Winner Selection**: The admin can randomly select a winner from verified participants and notify them via email.

## Installation
### Backend
1. Navigate to the `backend` directory.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start the Django server:
   ```
   python manage.py runserver
   ```

### Frontend
1. Navigate to the `frontend` directory.
2. Install the required packages:
   ```
   npm install
   ```
3. Start the Nuxt.js development server:
   ```
   npm run dev
   ```

## Usage
- Access the application through the frontend URL (usually `http://localhost:3000`).
- Users can register, verify their email, and set their password.
- Admins can log in to manage the giveaway and select a winner.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.