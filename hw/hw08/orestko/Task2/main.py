from re import search

password = input("Введіть Ваш пароль: ")

length = 6 <= len(password) <= 16
lower = search(r"[a-z]", password) is not None
upper = search(r"[A-Z]", password) is not None
digit = search(r"[0-9]", password) is not None
special = search(r"[$#@]", password) is not None

if length and lower and upper and digit and special:
    print("Пароль правильний.")
else:
    print("Пароль не правильний.")