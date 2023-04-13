from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Century Gothic', 14, 'normal')


# Purpose:
# Keep track of score
# Display it during game play

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.display_score()

    def add_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def end_game(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
