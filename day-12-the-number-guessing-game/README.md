# Day 12 Project: The Number Guessing Game

## Concept

**Note**: this project has two codes that should produce the same result on the console. The `main.py`,
however, is a lot simpler than the `alternative_main.py`. The latter has upgraded modularization via
some functions to provide easier maintenance and support to smoother changes in gameplay, such as number of
user attempts.

This simple game asks for the user to type 'easy' or 'hard' in order to pick a game difficulty.
Then, the program "thinks" of a random number between 1 and 100 and asks for the user to input
a guess, providing feedback whether the guess is too high or too low. Depending on the chosen
difficulty, the user will have 10 or 5 remaining attempts to guess the correct number.

Upon either depleting their attempts or providing the correct answer, the program outputs
a final message before closing.

## Resources

- [Text to ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)