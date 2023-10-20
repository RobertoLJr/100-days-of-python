# Day 14 Project: Higher or Lower

## Concept

This is a game that should work similarly to [The Higher Lower Game](https://www.higherlowergame.com/). In this
game, the player's goal is to guess which one of two options presented at a time has a higher or a lower amount
of something. For each correct answer, the player is confronted with another option in regard to their last
guess. If any answer is incorrect, the game is over and the score is showed.

In this program's implementation, the player's options will include some celebrities and their Instagram's
followers amount. The user should input 'A' or 'B' to guess which one of the two options has the
higher amount of followers. If the answer is correct, option A becomes option B, and a new option B is showed.
The screen clears everytime (this does not work in certain IDEs, but should run fine on terminals) a guess
is provided, and then the program's art is printed again with the new data on the screen.

## Resources

### Data Structures

- [Python 3 Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

- [Text to ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)

### Functions and Methods

- [os.system(_command_)](https://docs.python.org/3/library/os.html?highlight=module%20os#os.system)
- [random.choice(seq)](https://docs.python.org/3/library/random.html?highlight=choice#random.choice)
- [Python 3 Documentation - More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

### Modules

- [os - Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html?highlight=module%20os#module-os)
- [random](https://docs.python.org/3/library/random.html?highlight=random#module-random)