from random import randint

def guess_number():
    number_to_guess = randint(1, 100)
    attempts = 10

    print("Guess number from 1 to 100.")
    
    for i in range(attempts):
        print(f"Remaining attempts: {attempts - i}")
        user_input = input(f"Enter your number: ")
        if user_input.isdigit() and 1 <= int(user_input) <= 100:
            user_input = int(user_input)
            if user_input < number_to_guess:
                print("Guessed number is greater.")
            elif user_input > number_to_guess:
                print("Guessed number is lower.")
            else:
                print("You win!")
                print(f"You guess number {number_to_guess} in {i} attempts!")
                return
        else:
            print("Number must be between 1 and 100.")
            attempts += 1
            continue

    print(f"You lose. Number was {number_to_guess}")

if __name__ == "__main__":
    guess_number()