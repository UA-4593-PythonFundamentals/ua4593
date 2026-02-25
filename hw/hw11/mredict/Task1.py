def check_age(age_value):
    """Function to process the age and handle logic/exceptions."""

    if not age_value.isdigit():
        raise ValueError("Invalid input. Please enter a numeric value for age.")
    else:
        age = int(age_value)
    
    if age < 0:
        raise ValueError("Age cannot be a negative number.")
    
    if age % 2 == 0:
        return f"The age {age} is even."
    else:
        return f"The age {age} is odd."
    
if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter your age: ")
            result = check_age(user_input)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")
            continue
        break
