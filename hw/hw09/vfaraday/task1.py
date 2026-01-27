from random import randint

def guess_number_game():
    secret_number = randint(1, 100)
    attempts = 10

    print("Guess number from 1 to 100. You have 10 attempts!")

    for i in range(1, attempts + 1):
        try:
            user_guess = int(input(f"Attempt {i}: Enter your number: "))
        except ValueError:
            print("Enter only whole numbers.")
            continue

        if user_guess < secret_number:
            print("Guessed number is greater.")
        elif user_guess > secret_number:
            print("Guessed number is lower.")
        else:
            print(f"You guess number {secret_number} in {i} attempts! 🎉")
            return

    print(f"You out of attempts..Guessed number was {secret_number}")


if __name__ == "__main__":
    guess_number_game()