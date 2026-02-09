import re

def check_password_validity(password):
    if not (6 <= len(password) <= 16):
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[$#@]", password):
        return False

    return True


user_input = input("Input password: ")

if check_password_validity(user_input):
    print("Password valid!")
else:
    print("Password invalid")