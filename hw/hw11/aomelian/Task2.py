days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

def day_week(day):
    if day > 7 or day <= 0:
        raise ValueError("You can only enter numbers from 1 to 7")
    else:
        return days_of_week[day]

if __name__ == "__main__":
    state = True
    while state:
        try:
            i = int(input())
            result = day_week(i)
            print(result)
            state = False
        except ValueError as e:
            if "numbers" in str(e):
                print(f"Error: {e}")
            else:
                print("Please, enter a valid data")
            state = True


