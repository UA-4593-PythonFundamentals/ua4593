import re

def check_password(str):
    check_lenght(str)

def check_lenght(str):
    if len(str) >= 6 and len(str) <=16:
        check_a_z(str)
    else:
        print ("The password's length should be from 6 to 16")

def check_a_z(str):
    if re.search("[a-z]",str):
        check_A_Z(str)
    else:
        print ("The password should have at least one a-z character")

def check_A_Z(str):
    if re.search("[A-Z]",str):
        check_numbers(str)
    else:
        print ("The password should have at least one A-Z character")

def check_numbers(str):
    if re.search("[0-9]",str):
        check_special_symbol(str)
    else:
        print ("The password should have at least one number 0-9")
    
def check_special_symbol(str):
    if re.search(r"[\$\#\@]",str):
        print("The password matches the requirements")
    else:
        print ("The password should have at least one special character, e.g. $,#,@")