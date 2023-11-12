from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from turtle import Screen, Turtle
import time

# Setup screen config
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Define bodies
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
message_board = Turtle()
message_board.hideturtle()
message_board.penup()

is_game_on = False
user_difficulty = screen.textinput("Set Difficulty", "Choose difficulty (easy/hard): ")

# Write player controls instructions
screen.update()
for i in range(5, 0, -1):
    message_board.goto(0, 0)
    if user_difficulty == "hard":
        message_board.write("The turtle can only move up!", align="center", font=("Courier", 12, "normal"))
    else:
        message_board.write("The turtle can move up, down, right and left!", align="center",
                            font=("Courier", 12, "normal"))

    message_board.goto(0, -50)
    message_board.write(i, align="center", font=("Courier", 12, "normal"))
    screen.update()
    time.sleep(1)
    message_board.clear()

# Set key listener and Player controls
screen.listen()
screen.onkeypress(player.move_up, "Up")
if user_difficulty == "easy":
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_down, "Down")
    screen.onkeypress(player.move_right, "Right")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    # Generate and move all the cars perpetually to the left
    car_manager.generate_car()
    car_manager.move_car()

    # Detect Player collision with any car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.end_game()
            is_game_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        scoreboard.level_up()
        player.go_to_start()
        car_manager.accelerate()

screen.exitonclick()
