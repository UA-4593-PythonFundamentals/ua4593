import module

password = input("Enter pasword:")

if(module.check_password(password)):
    print("Password valid!"+"\n"+"Your password: " + password)
else:
    print("Password invalid"+"\n"+"Your password: " + password)