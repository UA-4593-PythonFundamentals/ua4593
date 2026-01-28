import re


def validate_password(password):
    """
    Validate password according rules.
    Args:
        password (str): The password to validate
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if len(password) < 6:
        return False, "Password must be at least 6 characters long"
    
    if len(password) > 16:
        return False, "Password must be at most 16 characters long"
    
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter [a-z]"
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter [A-Z]"
    
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit [0-9]"
    
    if not re.search(r'[$#@]', password):
        return False, "Password must contain at least one special character [$#@]"
    
    return True, "Password is valid"


def main():
    print("=" * 10)
    print("Password Validator")
    print("=" * 10)
    print("\nPassword requirements:")
    print("- At least 1 lowercase letter [a-z]")
    print("- At least 1 uppercase letter [A-Z]")
    print("- At least 1 digit [0-9]")
    print("- At least 1 special character [$#@]")
    print("- Minimum length: 6 characters")
    print("- Maximum length: 16 characters")
    print("=" * 50)
    
    while True:
        password = input("\nEnter a password to validate: ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        is_valid, message = validate_password(password)
        
        if is_valid:
            print(f"success: {message}")
        else:
            print(f"error: {message}")


if __name__ == "__main__":
    main()

