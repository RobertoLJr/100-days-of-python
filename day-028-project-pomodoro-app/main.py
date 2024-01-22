from tkinter import *
from winsound import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
DARKEST = "#092635"
DARKER = "#1B4242"
DARK = "#5C8374"
LIGHT = "#9EC8B9"
FONT_NAME = "Times New Roman"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    label_title.config(text="Timer")
    label_checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Call the countdown function as a button command."""

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_title.config(text="Break", fg=DARKER)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=DARKEST)
        countdown(short_break_sec)
    else:
        label_title.config(text="Work", fg=DARK)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """Updates the text from the timer every second."""

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        PlaySound("sound/reception-bell-14620.wav", SND_ASYNC)
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔️"

        label_checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Configure initial window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=LIGHT)

# Add Timer title element
label_title = Label(text="Timer", fg=DARK, bg=LIGHT, font=(FONT_NAME, 50, "normal"))
label_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=LIGHT, highlightthickness=0)
tomato_img = PhotoImage(file="img/tomato_198447.png").subsample(3, 3)
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Add other window elements
button_start = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 16, "normal"), command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 16, "normal"), command=reset_timer)
button_reset.grid(column=2, row=2)

label_checkmarks = Label(fg=DARK, bg=LIGHT, font=(FONT_NAME, 16, "normal"))
label_checkmarks.grid(column=1, row=3)

window.mainloop()
