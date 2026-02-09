import re

errors = []
def validate_password(password):
    if not (6 <= len(password) <= 16):
        errors.append("Password length must be between 6 and 16 characters")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least 1 lowercase letter")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least 1 uppercase letter")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least 1 digit")
    if not re.search(r"[^a-zA-Z0-9]", password):
        errors.append("Password must contain at least 1 special character")
    
    is_valid = len(errors) == 0
    
    if is_valid:
        print("VALID")
    else:
        for error in errors:
            print(error)
    return is_valid, errors

if __name__ == "__main__":
    test_passwords = ["abc", "Abc123!", "password", "Pass1@"]

    for pwd in test_passwords:
        print(f"\nTesting: '{pwd}'")
        validate_password(pwd)