from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")

# Choose random answer
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

# Determine game difficulty and remaining guess attempts
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
        break
    elif difficulty == "hard":
        attempts = 5
        break

# Play game until last attempt or correct answer
while True:
    print(f"You have {attempts} attempt(s) remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        break
    elif guess > answer:
        print(f"Too high.")
        attempts -= 1
    else:
        print(f"Too low.")
        attempts -= 1

    if attempts >= 1:
        print("Guess again.")
    else:
        print("You've run out of guesses, you lose.")
        break
