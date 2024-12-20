# database.py
import sqlite3
import os
from contextlib import closing

# Establishing a connection to the database
def get_db_connection():
    conn = sqlite3.connect('user.db')
    conn.row_factory = sqlite3.Row  # Using row_factory to access columns as dictionaries
    return conn

# Create the user table if it doesn't exist
def create_table():
    with closing(get_db_connection()) as conn:
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS user (
                    username TEXT PRIMARY KEY,
                    password BLOB
                )
            """)

# Store a new user in the database
def store_user(username, hashed_password):
    with closing(get_db_connection()) as conn:
        with conn:
            conn.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, hashed_password))

# Check if the username already exists in the database
def check_username(username):
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM user WHERE username = ?", (username,))
        return cursor.fetchone()[0] > 0

# Authenticate the user by checking username and password
def login_user(username, password):
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        if user_data and bcrypt.checkpw(password.encode(), user_data["password"]):
            return True
        return False
