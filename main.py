import turtle
import pandas
from state import State

WIDTH = 725
HEIGHT = 491

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgpic("blank_states_img.gif")

df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()

correct_states = 0
guessed_states = []

game_is_on = True
while correct_states < 50:
    user_answer = turtle.textinput(title=f"{correct_states}/50 States Correct",
                                   prompt="What's another state name? (You can type \'exit\' anytime.)") \
        .title()

    if user_answer == "Exit":
        missing_states = []
        for state in df.state:
            if state not in guessed_states:
                missing_states.append(state)
                row = df[df.state == state]
                state = State(row, state, "red")
        break

    # Check if user's answer is correct
    if user_answer in all_states and not (user_answer in guessed_states):
        row = df[df.state == user_answer]
        state = State(row, user_answer, "black")
        guessed_states.append(user_answer)
        correct_states += 1

print(f"Your final score is {correct_states}/50")

new_df = pandas.DataFrame(missing_states)
new_df.to_csv("states_to_learn.csv")
screen.exitonclick()
