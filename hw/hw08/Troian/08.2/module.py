import re

password_reg = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[a-zA-Z0-9$#@]{6,16}$"
)

def check_password(password):
    return bool(password_reg.match(password))

