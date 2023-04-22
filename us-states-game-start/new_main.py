import turtle
import pandas as pd
FONT = ("Arial", 8, "normal")
if __name__ == "__main__":
    screen = turtle.Screen()
    # Create the whole image of state as turtle
    screen.title("Gues the names of all states in U.S.A")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pd.read_csv("50_states.csv")
    all_states = data["state"].to_list()

    guessed_states = []
    missing_states = []
    while len(guessed_states) <= len(all_states):
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            missing_states = pd.DataFrame([state for state in all_states if state not in guessed_states],
                                          columns=["missing_states"])
            missing_states.to_csv("missing_states.csv")
            break

        if answer_state in all_states and answer_state not in guessed_states:
            state_data = data[data["state"] == answer_state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(float(state_data["x"]), float(state_data["y"]))
            t.write(answer_state, font=FONT)
            guessed_states.append(answer_state)

    turtle.mainloop()
    print(missing_states)


