from re import search 

def password_check(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not search(r"[A-Z]", password):
        return False
    if not search(r"[a-z]", password):
        return False
    if not search(r"[0-9]", password):
        return False
    if not search(r"[$#@]", password):
        return False
    return True

password = input("Enter your password: ")
if password_check(password):
    print("Strong password")
else:
    print("Weak password")
    print("Try again")

