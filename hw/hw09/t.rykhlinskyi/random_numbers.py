from random import randint

sec_num = randint(1, 100)

attempts = 10

user_input = int(input("Guess the number between 1 and 100: "))

while attempts > 0:
    if user_input < sec_num:
        print("Too low!")
    elif user_input > sec_num:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number!")
        break
    attempts -= 1
    if attempts > 0:
        user_input = int(input(f"Try again! You have {attempts} attempts left: "))
    else:
        print(f"Sorry, you've used all your attempts. The number was {sec_num}.")