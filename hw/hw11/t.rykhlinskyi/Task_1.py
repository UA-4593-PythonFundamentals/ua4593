def process_age(age):
   
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age % 2 == 0:
        return "The age is even"
    else:
        return "The age is odd"

try:
    user_input = input("Enter your age: ")
    age = int(user_input)
    result = process_age(age)
    print(result)
except ValueError as e:
    print(f"Error: {e}")