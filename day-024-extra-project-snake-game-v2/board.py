from turtle import Turtle


class Board(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.print_board()

    def print_board(self):
        """Print a board game 90% size of total screen size"""
        self.hideturtle()
        self.penup()
        self.color("lime")
        self.goto(int(self.width * -.45), int(self.height * -.45))
        self.pendown()
        self.setheading(90)
        self.forward(int(self.height * .9))
        self.setheading(0)
        self.forward(int(self.width * .9))
        self.setheading(270)
        self.forward(int(self.height * .9))
        self.setheading(180)
        self.forward(int(self.width * .9))
