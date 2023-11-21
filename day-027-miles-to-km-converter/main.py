from tkinter import *


def calculate():
    """Change the label_result text to the user_input value times 1.60934"""

    label_result.config(text=float(user_input.get()) * 1.60934)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=120)
window.config(padx=100, pady=10)

# Create label for user input
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

label_miles = Label(text="Miles", font=("Arial", 12, "normal"))
label_miles.grid(column=2, row=0)

label_equals = Label(text="is equal to", font=("Arial", 12, "normal"))
label_equals.grid(column=0, row=1)

label_result = Label(text=0, font=("Arial", 12, "normal"))
label_result.grid(column=1, row=1)

label_km = Label(text="Km", font=("Arial", 12, "normal"))
label_km.grid(column=2, row=1)

# Create Calculate Button
button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=2)

window.mainloop()
