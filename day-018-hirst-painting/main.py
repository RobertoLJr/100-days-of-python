import turtle
from turtle import Turtle, Screen
import random
# import colorgram

# rgb_colors = []
# # colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


turtle.colormode(255)
brush = Turtle()
brush.hideturtle()
brush.speed(0)
brush.penup()
brush.goto(-300, -300)

color_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
    (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]


def paint_dot():
    """Place a random-colored dot 20px wide at the turtle's position. Put the pen up afterward."""
    rgb = random.choice(color_list)
    brush.pendown()
    brush.dot(20, rgb)
    brush.penup()


def paint_line(num_dots):
    """Paint num_dots random-colored dots in a row, separated by 50px each."""
    for i in range(num_dots):
        paint_dot()
        brush.forward(50)


# For each row in 10, paint a line with 10 dots
for _ in range(10):
    paint_line(10)
    brush.goto(-300, brush.ycor() + 50)

screen = Screen()
screen.exitonclick()
