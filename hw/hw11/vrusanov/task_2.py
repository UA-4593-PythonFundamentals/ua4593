days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

user_input = input("Введіть число (1-7): ")
try:
    number = int(user_input)
    if number < 1 or number > 7:
        print("Помилка: число має бути від 1 до 7")
    else:
        print(f"День тижня: {days[number]}")
except ValueError:
    print("Помилка: введено не числове значення")
