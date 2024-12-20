# Login System with Streamlit

This project implements a user authentication system using Streamlit and SQLite. It allows users to register, log in, and view a personalized welcome page after logging in successfully. Passwords are securely hashed using bcrypt for added security.

## Features
- User registration with username and password.
- Secure password storage with bcrypt hashing.
- User login functionality with login attempt limit (3 attempts).
- Personalized welcome page after successful login.
- Responsive UI using Streamlit.

## Requirements
- Python 3.x
- streamlit
- bcrypt
- sqlite3

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ErfanNahidi/streamlit_login_page
    cd streamlit_login_page
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run gui.py
    ```

## How it works

1. **Registration:**  
   When users register, their password is securely hashed with bcrypt and stored in an SQLite database. The system checks for existing usernames to prevent duplicates.

2. **Login:**  
   Users can log in by entering their credentials. The password entered by the user is compared to the hashed password stored in the database using bcrypt's `checkpw` function.

3. **Personalized Welcome Page:**  
   After successful login, users are redirected to a personalized page that displays a welcome message with their username.

## File Structure
- **gui.py:** Contains the Streamlit UI and user interface logic.
- **user.py:** Defines the `User` class, which handles user registration, login, password encryption, and validation.
- **database.py:** Manages the SQLite database connection and queries.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


