import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator.")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

# Randomly choose n characters from letter, password and number lists (n = user input) and concatenate into password
for letter in range(nr_letters):
    password += random.choice(letters)
for symbol in range(nr_symbols):
    password += random.choice(symbols)
for number in range(nr_numbers):
    password += random.choice(numbers)

print(f"Order not randomized: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = ""

# Randomly choose n characters from letter, password and number lists (n = user input) and concatenate into
# hard_password
for letter in range(nr_letters):
    hard_password += random.choice(letters)
for symbol in range(nr_symbols):
    hard_password += random.choice(symbols)
for number in range(nr_numbers):
    hard_password += random.choice(numbers)

# Change hard_password data type to List, shuffle its elements and converts it to a String once more
hard_password_list = list(hard_password)
random.shuffle(hard_password_list)
hard_password = "".join(hard_password_list)

print(f"Order randomized: {hard_password}")
