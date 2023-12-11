from tkinter import *
import pandas as pd
import random

# Load data
to_learn = {}
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn_csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

BACKGROUND_COLOR = "#B1DDC6"
CARD_TITLE_FRONT = data.columns.values[0]
CARD_TITLE_BACK = data.columns.values[1]


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(image_card, image=image_card_front)
    canvas.itemconfig(canvas_text_title, text=CARD_TITLE_FRONT)
    canvas.itemconfig(canvas_text_word, text=current_card[CARD_TITLE_FRONT])
    flip_timer = window.after(3000, flip_card)


def next_card_right():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(image_card, image=image_card_back)
    canvas.itemconfig(canvas_text_title, text=CARD_TITLE_BACK, fill="white")
    canvas.itemconfig(canvas_text_word, text=current_card[CARD_TITLE_BACK], fill="white")


# Setup UI
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

image_card_front = PhotoImage(file="img/card_front.png")
image_card_back = PhotoImage(file="img/card_back.png")
image_card = canvas.create_image(400, 263, image=image_card_front)
canvas_text_title = canvas.create_text(400, 150, text='', font=("Times New Roman", 40, "italic"))
canvas_text_word = canvas.create_text(400, 263, text='', font=("Times New Roman", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
image_button_wrong = PhotoImage(file="img/wrong.png")
button_wrong = Button(image=image_button_wrong, highlightthickness=0, border=0, command=next_card)
button_wrong.grid(column=0, row=1)

image_button_right = PhotoImage(file="img/right.png")
button_right = Button(image=image_button_right, highlightthickness=0, border=0, command=next_card_right)
button_right.grid(column=1, row=1)

next_card()

window.mainloop()
