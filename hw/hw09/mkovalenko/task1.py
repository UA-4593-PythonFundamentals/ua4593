import random

random_number = random.randint(1, 100)

attempts = 10

for i in range(attempts):
    user_number = int(input(f"You have {attempts-i} attempts left. Type number: "))

    if user_number == random_number:
        print("You win!")
        break
    elif user_number < random_number:
        print("Guessed number is greater then your. Try again!") 
    elif user_number > random_number:
        print("Guessed number is less then your. Try again!") 
else:
    print("You lose!")