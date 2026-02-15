def get_day_of_week():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        user_input = input("Enter a number (1-7): ")
        number = int(user_input)

        if number in days:
            print(f"Day {number} is {days[number]}.")
        elif number >= 8 or number <= 0:
            print("Error: There are only 7 days in a week. Please enter a number between 1 and 7.")

    except ValueError:
        print("Error: Invalid input. Please enter a numerical value.")

def main():
    get_day_of_week()

if __name__ == "__main__":
    get_day_of_week()