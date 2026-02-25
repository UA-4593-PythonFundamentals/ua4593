def check_age(age):
    
    if age < 0:
        raise ValueError("Вік не може бути від'ємним!")
    return "парний" if age % 2 == 0 else "непарний"

def main():
    try:
        user_input = input("Введіть свій вік: ")
        age = int(user_input)
        result = check_age(age)
        print(f"Ваш вік {result}.")
    except ValueError as ve:
        print(f"Помилка: {ve}")


if __name__ == "__main__":
    main()