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
        time.sleep(0.1)
        ball.move()
        # Detect collision with walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        # Detect collision with the paddle
        if(ball.distance(r_paddle) < 50) and (ball.xcor() > 320) or  (ball.distance(l_paddle) < 50) and (ball.xcor() < -320):
            ball.bounce_x()

        # Detect when a player misses the ball
        # It has to go to the center of  the table and to be served in the opposite direction
        if ball.xcor() > 400 or ball.xcor() < -400:
            print("miss the ball")
            ball.reset()

    screen.exitonclick()
