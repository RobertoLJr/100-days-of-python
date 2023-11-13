from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, screen_w, screen_h):
        super().__init__()
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(int(-self.screen_w * .40), int(self.screen_w * .40))
        random_y = random.randint(int(-self.screen_h * .40), int(self.screen_h * .40))
        self.goto(random_x, random_y)
