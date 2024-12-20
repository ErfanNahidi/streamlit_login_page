import bcrypt
import sqlite3

class User:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def encryption(self):
        """Hash password using bcrypt."""
        salt = bcrypt.gensalt(rounds=15)
        hashed_password = bcrypt.hashpw(self.password.encode(), salt)
        return hashed_password

    def check_username(self):
        """Check if the username is already taken."""
        conn = sqlite3.connect("user.db")
        cur = conn.cursor()
        sql = "SELECT COUNT(*) FROM user WHERE username =?"
        cur.execute(sql, (self.username,))
        count = cur.fetchone()[0] > 0
        conn.close()
        if count:
            return False
        return True

    def store_user(self, hashed_password):
        """Store user credentials in the database."""
        conn = sqlite3.connect("user.db")
        cur = conn.cursor()
        sql = "INSERT INTO user (username, password) VALUES (?, ?)"
        cur.execute(sql, (self.username, hashed_password))
        conn.commit()
        conn.close()

    @staticmethod
    def login(username, password, wrong_time):
        """User login process."""
        if wrong_time < 3:
            conn = sqlite3.connect('user.db')
            cur = conn.cursor()
            sql = "SELECT * FROM user WHERE username = ?"
            cur.execute(sql, (username,))
            user_data = cur.fetchone()  # fetchone() returns a tuple
            conn.close()

            if user_data:
                hashed_password = user_data[1]  # user_data[1] is the password column
                result = bcrypt.checkpw(password.encode(), hashed_password)
                if result:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    @staticmethod
    def check_password_strength(password):
        """Check the strength of the password."""
        if len(password) < 8:
            return False
        has_letters = any(char.isalpha() for char in password)
        has_numbers = any(char.isdigit() for char in password)
        if not has_letters or not has_numbers:
            return False
        return True
