from random import randint

def guess_number_game():
    number = randint(1, 100)
    tries = 10

    print('Welcome to the game!')
    print('I generated a number from 1 to 100.')
    print(f'You have {tries} tries to guess it. Good luck!')

    for i in range(1, tries + 1):
        user_input = int(input('Please enter your number: '))
        remaining_tries = tries - i
            
        if user_input == number and i == 1:
            print('Wow! You guessed the number on your first try! Incredible!🏆')
            return
        
        if user_input > number:
            if remaining_tries > 0:
                print(f'Nope, the number is smaller. Try again! You have {remaining_tries} tries left.')
                continue

        if user_input < number:
            if remaining_tries > 0:
                print(f'Nope, the number is bigger. Try again! You have {remaining_tries} tries left.')
                continue
               
        print(f'Congratulations! You guessed the number on try number {i}!')
        return
    
    print(f'Sorry, you didn’t guess the number. The correct number was {number}.')

if __name__ == "__main__":
    guess_number_game()