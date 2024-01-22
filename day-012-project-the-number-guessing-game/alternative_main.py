# This alternative code is mode complex and involves more abstraction, but it is also more modularized

from art import logo
from random import randint

# Determine attempts based on game difficulty
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5


# Check the user's guess against actual answer
def check_answer(guess, answer, attempts):
    """Checks guess against correct answer. Returns the number of attempts remaining."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < attempts:
        print("Too low")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Set game difficulty according to input
def set_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if mode == "easy":
        return EASY_MODE_ATTEMPTS
    else:
        return HARD_MODE_ATTEMPTS


# Play the game until 0 attempts or correct answer
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)

    # To play the game knowing the answer beforehand for tests, uncomment the line below
    # print(f"Psst, the correct answer is {answer}.")

    attempts = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print(f"You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


play_game()
