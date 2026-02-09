import re

a = "0123456789"
b = "abcdefghijklmnopqrstuvwxyz"
c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d= "!@#$%^&*()"

symbols = a + b + c + d 
max_lenght = 16
min_lenght = 6

def check_validity_password(password):
    if len(password) < min_lenght:
        return False
    if len(password) > max_lenght:
        return False 
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[!@#$%^&*()]", password):
        return False
    return True

password = input("Введіть пароль: ")
print("Ви ввели: ", password)

if check_validity_password(password):
    print("Пароль дійсний")
else:
    print("Пароль не відповідає вищезазначеним вимогам") 

