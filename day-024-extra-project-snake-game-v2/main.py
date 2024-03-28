from board import Board
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
import time

# First screen setup
screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Get window width and height
screen_w = screen.window_width()
screen_h = screen.window_height()

snake = Snake()
food = Food(screen_w, screen_h)
scoreboard = Scoreboard(screen_h)
board = Board(screen_w, screen_h)

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

# Populate segments according to initial positions
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() > int(screen_w * .45) or snake.head.xcor() < int(-(screen_w * .45))
            or snake.head.ycor() > int(screen_h * .45) or snake.head.ycor() < int(-(screen_h * .45))):
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
