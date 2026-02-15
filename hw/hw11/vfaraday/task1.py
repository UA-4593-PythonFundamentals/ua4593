def process_age(age):
    try:
        age = int(age)
    except ValueError:
        return "Has to be an integer"

    if age < 0:
        raise ValueError("Age cannot be negative!")

    if age % 2 == 0:
        return "The age is even."
    else:
        return "The age is odd."

def main():
    user_input = input("Please enter your age: ")
    try:
        result = process_age(user_input)
        print(result)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()