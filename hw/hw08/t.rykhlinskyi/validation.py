def validity_check(password):
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    elif len(password) > 16:
        return "Password must be at most 16 characters long."
    elif not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    elif not any(char in '$#@' for char in password):
        return "Password must contain at least one special character from $#@."
    else:
        return "Password is valid."
user_password = input("Enter your password: ")
validation_result = validity_check(user_password)
print(validation_result)