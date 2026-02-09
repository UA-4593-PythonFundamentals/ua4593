import re

def pass_is_valid(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'
    return re.search(pattern, password) != None

password = input("Type your password: ")
if pass_is_valid(password):
    print("Password is valid!")
else:
    print("Password is not valid!")
