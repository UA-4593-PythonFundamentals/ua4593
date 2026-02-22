def check_age(age):

    try:
        age = int(age)
    except Exception:
        print("Incorrect value!")
        return
         
    if age <= 0:
        raise ValueError(f"Incorrect age {age}")
    elif age % 2 == 0:
        print("Your age is even number!")
    else:
        print("Your age is odd number!") 
    
age = input("Please type your age: ")

check_age(age)