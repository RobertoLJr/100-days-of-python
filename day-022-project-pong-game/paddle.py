from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        """Move the paddle up while the key is pressed"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Move the paddle down while the key is pressed"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
