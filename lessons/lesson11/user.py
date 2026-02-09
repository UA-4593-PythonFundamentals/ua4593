from my_logging import logging

class UserError(Exception):
    def __init__(self, message):
        super().__init__(message)
        logging.error(f"UserError: {message}")


class User:
    def __init__(self, username, email, age):
        if not username.isalpha():
            raise UserError("Username must contain only alphabetic characters.")
        self.username = username
        if "@" not in email or "." not in email:
            raise UserError("Invalid email address.")
        self.email = email
        if not age.isdigit():
            raise UserError("Age must be a positive integer.")
        age = int(age)
        if age < 0:
            raise UserError("Age cannot be negative.")
        self.age = age

    def get_info(self):
        return f"Username: {self.username}, Email: {self.email} Age: {self.age}"
    
def create_user():
    try:
        username = input("Enter username: ")
        email = input("Enter email: ")
        age = input("Enter age: ")
        user = User(username, email, age)
        print("User created successfully!")
        print(user.get_info())
    except UserError as e:
        print(f"User creation failed: {e}")



