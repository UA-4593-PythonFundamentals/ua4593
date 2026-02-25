def check_age_parity(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    if age % 2 == 0:
        return "парне"
    else:
        return "непарне"


age_input = input("Введіть ваш вік: ")
try:
    age = int(age_input)
    result = check_age_parity(age)
    print(f"Ваш вік ({age}) є {result} числом.")
except ValueError as e:
    print(f"Помилка: {e}")
