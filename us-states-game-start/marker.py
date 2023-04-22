from turtle import Turtle

FONT = ("Arial", 8, "normal")


class Marker(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("Black")
        self.penup()

    def mark_state(self, name_of_state, position):
        self.goto(position)
        self.write(f"{name_of_state}", font=FONT)


