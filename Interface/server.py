"""
class LoginSystem:

    def __init__(self):
        self.users = {"Freeflow@gmail.com": "test"}

    def login(self):
        while True:
            username = input("Please enter your user id: ")
            password = input("Please enter your password: ")
            if len(username) <= 5 and len(password) >= 8 and self.check_system(username, password):
                print("Logging In")
                break
            else:
                # TODO Disallow infinite retries to get it right
                print("Error! Max Length is 5 chars.")

    def check_system(self, name, password):
        try:
            expected_password = self.registered_user[name]
        except KeyError:
            # Or try to add a new user to the system here
            return False

        if password != expected_password:
            return False

        return True
"""

users = {'john': 'pass1', 'sarah': 'pass2', 'bob': 'pass3'}

username = input("Enter username: ")

if username in users:
    password = input("Enter password: ")
    if password == users[username]:
        print("Login success")
    else:
        print("Password is off")
else:
    print("Username is off")
    
    
    
#!/usr/bin/python3
"""from flask import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"

@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
"""