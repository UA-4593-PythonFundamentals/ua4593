
def day_in_writing(day):
    import calendar

    try:
        day = int(day)
    except Exception:
        print("You entered non-numerical data!")
        return

    if day < 1:
        raise ValueError(f"You entered less than 1 value: {day}") 

    try:
        return calendar.day_name[day-1]
    except IndexError:
        print("Incorrect value! You must enter value beetween 1 and 7!")


day = input("Please type the day of the week: ")
day_w = day_in_writing(day)

if not day_w == None: 
    print(f"Day in writing is: {day_in_writing(day)}")