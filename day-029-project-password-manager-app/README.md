# Day 29 Project: Password Manager App

## Concept

This program uses tkinter to run an application capable of recording data into an .txt file. It works as such:

1. The user provides a website name.
2. The user provides an email/username (filled with email@gmail.com by default).
3. The user provides a password or, alternatively, clicks the `Generate Password` button.

> The `Generate Password` button fills the password entry with a strong randomly generated password containing
8–10 letters, 2–4 symbols, and 2–4 numbers. At the same time, the password will be copied to the clipboard.

4. The user clicks the button `Add` to append the website name, the username, and the password into a local
data.txt file.

> If any of the three fields is empty, a pop-up warning shows up informing the user to fill the missing data
before saving.

## Resources

### Packages and modules

- [pyperclip](https://pypi.org/project/pyperclip/)
- [random](https://docs.python.org/3/library/random.html)
- [tkinter package](https://docs.python.org/3/library/tkinter.html)