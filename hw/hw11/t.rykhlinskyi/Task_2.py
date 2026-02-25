def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    return days.get(number, "Invalid number! Please enter a number from 1 to 7.")

try:
    user_input = input("Enter a number (1-7): ")
    num = int(user_input)
    print(get_day_of_week(num))
except ValueError:
    print("Error: You must enter a numerical value.")