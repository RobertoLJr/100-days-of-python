# Day 7: Hangman

## Concept

The [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) is a guessing game for two or more players.
One player thinks of a word, phrase, or sentence and the other(s) tries to guess it by suggesting
letters or numbers within a certain number of guesses. Originally a paper-and-pencil game, there are
now electronic versions.

This program takes characters as inputs from the user for as long as the game is running. It informs
the player whether his/her guess is right, wrong or have already been given in previous moves. Depending
on the scenario, the ASCII art might be updated, representing the player's remaining guesses.

The player wins when all the _ spaces have been filled with letters and loses when all the
guesses have been used while there is still any _ space.

## Resources

### Classes

- [range(stop)](https://docs.python.org/3/library/functions.html#func-range) -> Interestingly enough, rather than being a function, **range** is actually an immutable sequence type.

### Functions

- [len(s)](https://docs.python.org/3/library/functions.html#len)
- [str.lower()](https://docs.python.org/3/library/stdtypes.html?highlight=lower#str.lower)
