import random
import os
from art import logo


def deal_card(deck):
    """Return one random card from the deck"""
    return random.choice(deck)


def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare_scores(your_score, opponent_score):
    if your_score == opponent_score:
        return "Draw 😐"
    elif opponent_score == 0:
        return "You lost, the opponent has a Blackjack 😱"
    elif your_score == 0:
        return "You won with a Blackjack 😎"
    elif your_score > 21:
        return "You lost. You went over 21 😓"
    elif opponent_score > 21:
        return "You won. The opponent went over 21 😁"
    elif your_score > opponent_score:
        return "You won 🙂"
    else:
        return "You lost ☹️"


def play_game():
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    user_score = 0
    computer_cards = []
    computer_score = 0
    is_over = False

    # Deal the first hand with 2 cards for each player
    for i in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    # Loop through user's plays
    while not is_over:
        # Store calculated scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} | Your current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check scores
        if user_score == 0 or computer_cards == 0 or user_score > 21:
            is_over = True
        else:
            another_draw = input("Would you like to draw another card (y/n)? ")
            if another_draw == 'y':
                user_cards.append(deal_card(cards))
                user_score = calculate_score(user_cards)
            else:
                is_over = True

    # Loop through computer's plays
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

    # Print final hands and scores and declare winner
    print(f"\nYour final hand is {user_cards} and your final score is {user_score}")
    print(f"The computer's hand is {computer_cards} and its final score is {computer_score}")
    print(compare_scores(user_score, computer_score))


while input("Do you want to play a game of Blackjack (y/n)? ") == 'y':
    # Clear screen after input (does not work in some IDEs)
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')
        cls()


    play_game()
