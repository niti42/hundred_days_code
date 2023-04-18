from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Century Gothic', 14, 'normal')


PLAYER_DATA_FILE = "data.txt"


def read_text_file(filename):
    # Open file, read the contents and close the file.
    with open(filename) as file:
        contents = file.read()
        return int(contents)


def write_score_to_file(filename, score):
    # write the player score to file
    with open(filename, mode='w') as file:
        file.write(score)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_text_file(PLAYER_DATA_FILE)
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        # If current score is greater than previous all-time high score, update the high score with current score
        if self.score > self.high_score:
            self.high_score = self.score
            write_score_to_file(PLAYER_DATA_FILE, f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
