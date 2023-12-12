# Day 34 Project: GUI Trivia Quiz

## Concept

This program works with the tkinter module to provide the user with an interactive quiz game. For every execution,
it calls the Open Trivia API (see resources) to fetch 10 True/False questions of any category and any difficulty.
Then, it works as follows:

1. The user will be given a question to which they can answer True or False via the buttons on the interface.
2. For each correct answer, the screen will turn green for 1 second and the visible score will be updated.
3. For each wrong answer, the screen will turn red for 1 second.
4. After 10 questions, the program no longer fetch questions and buttons are disabled.

Some improvement opportunities were identified and should be addressed soon, such as better colors and UI, as
well as fixes for unintended user behavior.

## Resources

### APIs

- [Open Trivia Database](https://opentdb.com/)

### Modules and libraries

- [html](https://docs.python.org/3/library/html.html)
- [requests](https://docs.python-requests.org/en/latest/)
- [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter)