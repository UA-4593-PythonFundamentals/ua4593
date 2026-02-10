import re

password = input("Enter password: ")

rules = {
    "lowercase": re.search(r"[a-z]", password),
    "uppercase": re.search(r"[A-Z]", password),
    "digit": re.search(r"\d", password),
    "special": re.search(r"[$#@]", password),
    "length": 6 <= len(password) <= 16,
}

if all(rules.values()):
    print("Password is valid")
else:
    print("Password is invalid")