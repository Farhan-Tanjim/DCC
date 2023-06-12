import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

def login(username, password):
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    user = cursor.fetchone()

    if user is None:
        print("User not found")
        return False

    if user[1] == password:
        print("Login successful")
        return True
    else:
        print("Invalid password")
        return False

username = input("Enter your username: ")
password = input("Enter your password: ")

if login(username, password):
    print("User Logged In")
else:
    print("Error Occured")

conn.close()