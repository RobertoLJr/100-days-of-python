from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Keep the ball moving continuously"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Change the direction vertically whenever the ball bounces on either up or downside of the screen"""
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        """Change the direction horizontally whenever the ball bounces on either the left or right paddle"""
        self.x_move *= -1

    def reset_position(self):
        """Make the ball go to (0, 0) x and y coordinates, accordingly, and reset its move_speed to 0.1"""
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1
