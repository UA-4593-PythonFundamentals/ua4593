import re

def check_validity(password):
    """
    Checks the validity of a user's password.
    Returns error messages or a success confirmation.
    """
    errors = []
    regs = {
        r'[A-Z]': 'Password must contain at least one uppercase letter',
        r'[a-z]': 'Password must contain at least one lowercase letter',
        r'[0-9]': 'Password must contain at least one number between 0 and 9',
        r'[$#@]': 'Password must contain at least one of the following characters: $, #, @'
    }

    if len(password) < 6 or len(password) > 16:
        errors.append(f'Password length must be between 6 and 16 characters. The length of your password is {len(password)}.')

    for reg, message in regs.items():
        if not re.search(reg, password):
            errors.append(message)

    if errors:
        return f'Error!\n{"\n".join(errors)}'
    return 'Success! Your password is valid and saved!'

password = input('Please enter your password: ')

print(check_validity(password))