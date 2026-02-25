def age_check(number):
    if number < 0:
        raise ValueError("Age cannot be negative")
    return "even" if number % 2 == 0 else "odd"


if __name__ == "__main__":
    state = True
    while state:
        try:
            print("Enter the age: ", end="")
            age = int(input())
            result = age_check(age)
            print(f"The age is {result}")
            state = False
        except ValueError as e:
            if "negative" in str(e):
                print(f"Error: {e}")
            else:
                print("Error: Please enter a valid number")
            state = True
