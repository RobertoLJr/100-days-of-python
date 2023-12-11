# Day 31 Project: Flash Card App

## Concept

This program simulates a Flash Card Application originally for words in French and their respective translation
to English. However, with little tinkering, it should work for other languages or for questions/answers. When
first executed, the program will try to load a CSV file derived from previous executions. If none is found, it
will open an original file. Then, it works as following:

1. The user will be prompted with a card containing a randomly picked word in French.
2. The user will have 3 seconds to guess the correct translation (no input is needed) before the card is flipped.
3. The user can click the `X` button or the `checkmark` button depending on their performance.
4. Whenever the user clicks the `checkmark` button, that word will be removed from the list.
5. When the user closes the application, it will generate a new CSV file containing only the words not guessed or answered correctly.
6. The next time the user opens the application, it will load the last saved CSV file instead of the original file.

There is room for improvement, which could be implemented soon (we'll see!). In a non-exhaustive list, those are:

- Prompt to load a specific file.
- Timer configuration and visualization.
- Scoreboard.
- Interactive sounds.

## Resources

### Modules and libraries

- [pandas](https://pandas.pydata.org/docs/)
- [random](https://docs.python.org/3/library/random.html)
- [tkinter](https://docs.python.org/3/library/tkinter.html)