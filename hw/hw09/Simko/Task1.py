from random  import randint
choice = randint(1, 100)
left_attempts = 10
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 attempts to guess the number.")
while left_attempts > 0:
     guess = int(input("Enter your guess: "))
     if guess == choice:
         print("Congratulations! You guessed the number!")
         break
     elif guess < choice:
         print("Your guess is too low.")
     else:
         print("Your guess is too high.")
     left_attempts -= 1
     print("You have", left_attempts, "attempts left.")
     if left_attempts == 0:
          print("Sorry, you ran out of attempts. The number was", choice)
          print("Game over!")
          break