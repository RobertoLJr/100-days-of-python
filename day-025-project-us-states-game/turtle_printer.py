from turtle import Turtle


class TurtlePrinter(Turtle):
    def __init__(self, state, x_cor, y_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(state, align="center", font=("Arial", 10, "bold"))
