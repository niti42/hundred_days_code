from turtle import Turtle, Screen
import time

from hundred_days_code.pong.ball import Ball
from hundred_days_code.pong.paddle import Paddle
from hundred_days_code.pong.scoreboard import Scoreboard

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((380, 0))
    l_paddle = Paddle((-380, 0))
    screen.listen()
    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")
    ball = Ball()
    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        screen.update()
        # Change the refresh rate to change the speed of the ball.
        time.sleep(ball.move_speed)
        ball.move()
        # Detect collision with walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        # Detect collision with the paddle
        if (ball.distance(r_paddle) < 50) and (ball.xcor() > 350) or (ball.distance(l_paddle) < 50) and (
                ball.xcor() < -350):

            ball.bounce_x()
        # Detect when right paddle misses
        if ball.xcor() > 400:
            scoreboard.l_point()
            ball.reset_position()
        # Detect when left paddle misses
        if ball.xcor() < - 400:
            scoreboard.r_point()
            ball.reset_position()
    screen.exitonclick()
