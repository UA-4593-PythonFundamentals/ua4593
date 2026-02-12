# -*- coding: utf-8 -*-

def get_weekday(number):
    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П’ятниця",
        6: "Субота",
        7: "Неділя",
    }

    if number not in days:
        raise ValueError("Число має бути від 1 до 7!")
    return days[number]

def main():
    try:
        try:
            user_input = input("Введіть число від 1 до 7, щоб дізнатися день тижня: ")
            number = int(user_input)
        except EOFError:
            # Non-interactive run: use a fixed sample input.
            number = 1

        day = get_weekday(number)
        print(f"День тижня для числа {number} — {day}.")
    except ValueError as ve:
        print(f"Помилка: {ve}")

if __name__ == "__main__":
    main()
