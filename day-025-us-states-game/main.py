from turtle_printer import TurtlePrinter
import pandas
import turtle

# Configure initial screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get U.S. States data
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
states_count = len(states_list)

already_guessed = []
correct_answers = 0

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{correct_answers}/{states_count} States Correct",
                                    prompt="What's another state's name?").title()

    # Check for exiting code, save missing states into CSV
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in already_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list and answer_state not in already_guessed:
        correct_answers += 1
        already_guessed.append(answer_state)

        data_row = data[data.state == answer_state]
        turtle_printer = TurtlePrinter(data_row.state.item(), int(data_row.x), int(data_row.y))

    # Check if all states were answered
    if correct_answers == 50:
        is_game_on = False

screen.exitonclick()
