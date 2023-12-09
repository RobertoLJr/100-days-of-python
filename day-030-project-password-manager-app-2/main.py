from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip


# ---------------------------- FIND PASSWORD ------------------------------------#
def find_password():
    """Produce a tkinter messagebox with username and password data for a certain website."""
    website = entry_website.get()

    try:
        with open("data/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File found.")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Produce a randomly generated password containing 8-10 letters, 2-4 symbols and 2-4 numbers."""
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Append the website, username and password in a local .txt file."""

    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please, do not leave any fields empty before saving.")
    else:
        try:
            # Open existing JSON file
            with open("data/data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # Create new JSON file if non-existing
            with open("data/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update previously existing JSON file
            data.update(new_data)
            with open("data/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img_logo = PhotoImage(file="img/logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1, sticky="e")
label_username = Label(text="Email/Username:")
label_username.grid(column=0, row=2, sticky="e")
label_password = Label(text="Password:")
label_password.grid(column=0, row=3, sticky="e")

# Entries
entry_website = Entry()
entry_website.grid(column=1, row=1, sticky="ew")
entry_website.focus()
entry_username = Entry()
entry_username.grid(column=1, row=2, columnspan=2, sticky="ew")
entry_username.insert(0, "email@gmail.com")
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="ew")

# Buttons
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3, sticky="ew")
button_add = Button(text="Add", command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="ew")
button_search = Button(text="Search", command=find_password)
button_search.grid(column=2, row=1, sticky="ew")

window.mainloop()
