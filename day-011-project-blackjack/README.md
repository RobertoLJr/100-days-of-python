# Day 11 Project: Blackjack

## Concept

A [game of Blackjack](https://games.washingtonpost.com/games/blackjack) is a popular casino banking game
using decks of 52 cards, also known as 21 or _vingt-un_. The goal of the game is to add up cards to the
largest number without exceeding 21, otherwise the player reaches a **bust** and loses immediately.

The cards are counted as follows: all the cards from 2 to 10 count as their face value. However, the Jack,
the Queen and King each count as 10. The Ace is a wild card - it can count as 1 or 11, depending on
whether the player has reached 21 already.

This program simulates a simpler version of this game in which the player plays against
a single opponent, being the computer, and goes as follows:

1. The program first prompts the user for wanting to play a game, requiring an input of 'y' or 'n';
2. Upon playing, the player is dealt two random cards and its respective current score. The program also
shows the computer's first card, also determined randomly;
3. The program prompts the user for an input for drawing another card or passing;
4. The program calculates whether the computer is close to or exactly at 21 to decide if it draws another
random card or passes;
5. When both the player and the computer pass, the program shows all the cards and total scores and
declares the winner before asking again for another round.

Note: for simplicity, this game abstracts probability and does not remove cards from the deck once
they are picked for the player's or computer's hand.

## Resources

### Functions and Methods

- [os.system(_command_)](https://docs.python.org/3/library/os.html?highlight=module%20os#os.system)

### Modules

- [os - Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html?highlight=module%20os#module-os)