from turtle import Turtle, Screen
import time

from hundred_days_code.pong.Ball import Ball
from hundred_days_code.pong.Paddle import Paddle

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    ball = Ball()

    game_is_on = True
    while game_is_on:
        screen.update()
        # Change the refresh rate to change the speed of the ball.
        time.sleep(0.3)

        ball.move()

        if ball.ycor() > 295:
            ball.reflect_down()

    screen.exitonclick()
