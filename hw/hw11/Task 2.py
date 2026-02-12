def get_day(num_string):
    # Dictionary mapping numbers to days
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
        number = int(num_string)
        if 1 <= number <= 7:
            return f"Day {number} is {days[number]}."
        else:
            return "Error: Please enter a number between 1 and 7"
        
    except ValueError:
        return "Error: Invalid input. Please enter a numerical value\n"

if __name__ == "__main__":
    while True:
        user_input = input("Enter a number (1-7) for the day of the week: ")
        result = get_day(user_input)
        print(result)
        if "Error" not in result:
            break