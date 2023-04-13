from turtle import Turtle

STEP_LENGTH = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        # Change the number of steps to change the speed of the ball.
        new_x = self.xcor() + STEP_LENGTH
        new_y = self.ycor() + STEP_LENGTH
        self.got(new_x, new_y)





