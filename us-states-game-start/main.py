import turtle
from turtle import Screen

import pandas as pd
from marker import Marker

FONT = ("Courier", 12, "normal")


# Use this block of code to get the coordinates of any point that is clicked on the
# turtle screen.
# def get_mouse_click_coor(x, y):
#     print(x,y)
# # turtle.onscreenclick(get_mouse_click_coor)

def repeat_answer_check(name, answers_list):
    return True if name in answers_list else False


if __name__ == "__main__":
    screen = Screen()
    screen.title("How many states of the U.S.A can you name?")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    marker = Marker()

    score = 0
    previous_answers = []
    # Get the data of states
    us_states_loc = "50_states.csv"
    states = pd.read_csv(us_states_loc)

    # game loop len(states)
    while score <= len(states):
        answer = screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name?").title()
        if answer == "Exit":
            break
        if not repeat_answer_check(answer, previous_answers):
            for i in range(len(states)):
                state_name = states.loc[i]["state"]
                if answer == state_name:
                    state_xcor = states.loc[i]["x"]
                    state_ycor = states.loc[i]["y"]
                    marker.mark_state(state_name, (state_xcor, state_ycor))
                    previous_answers.append(answer)
                    score += 1
        else:
            previous_answers.append(answer)

    all_states = states["state"].to_list()
    missing_states = {"missing_states": [s for s in all_states if s not in previous_answers]}
    missing_states = pd.DataFrame(missing_states)
    missing_states.to_csv("missing_states.csv")
