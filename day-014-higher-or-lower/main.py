from art import logo, vs
from game_data import data
import os
import random


def clear_screen():
    """Clear the console for Windows or Unix/Linux systems."""
    os.system('cls' if os.name == 'nt' else 'clear')


def find_answer(celeb1, celeb2):
    """Return 'A' if dictionary celeb1 has higher value for key ['follower_count'], else return 'B'"""
    if celeb1['follower_count'] > celeb2['follower_count']:
        return 'A'
    else:
        return 'B'


# Generate data for the first gameplay
score = 0
is_over = False
option_a = random.choice(data)
option_b = random.choice(data)

# Make sure option_a and option_b are never the same data
while option_b == option_a:
    option_a = random.choice(data)


def play_game():
    """Loop through the game until game over."""
    global option_a, option_b, is_over, score

    while not is_over:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
        print(vs)
        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Check if user guess is the correct answer
        if guess == find_answer(option_a, option_b):
            score += 1
            option_a = option_b
            option_b = random.choice(data)
            while option_b == option_a:
                option_a = random.choice(data)
            clear_screen()
            play_game()
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            is_over = True


play_game()
