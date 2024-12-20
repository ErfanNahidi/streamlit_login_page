import streamlit as st
from user import User
import database

# Create table if not exists
database.create_table()

# Set up session state to keep track of user login and page
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Login or Register choice
if st.session_state.page == 'login':
    choice = st.radio("Do you want to login or register?", ['Login', 'Register'])

    # Register Section
    if choice == 'Register':
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Register"):
            user = User(username, password)

            if user.check_username():
                if User.check_password_strength(password):
                    hashed_password = user.encryption()
                    user.store_user(hashed_password)
                    st.success("User registered successfully!")
                else:
                    st.error("Password is too weak. (min 8 characters)")
            else:
                st.error("Username already taken.")

    # Login Section
    elif choice == 'Login':
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = User(username, password)
            wrong_time = 0
            if user.login(username, password, wrong_time):
                st.session_state.logged_in = True  # Set user as logged in
                st.session_state.username = username  # Store username in session state
                st.session_state.page = "profile"  # Set the page to profile
            else:
                st.error("Incorrect username or password.")

# Handle the logged-in user's profile page
if st.session_state.page == "profile" and st.session_state.logged_in:
    st.title(f"Welcome {st.session_state.username}!")
    st.write("This is your profile page.")
    
    # Example of a personalized feature
    st.write(f"Welcome to your personalized profile page, {st.session_state.username}!")
    
    # Add more user-specific details here (e.g., user preferences, settings, etc.)
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"  # Reset page to login screen

