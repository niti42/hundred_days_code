from turtle import Screen
import time

from hundred_days_code.snake_game.food import Food
from hundred_days_code.snake_game.scoreboard import Scoreboard, read_text_file, PLAYER_DATA_FILE
from hundred_days_code.snake_game.snake import Snake

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    scoreboard.high_score = read_text_file(PLAYER_DATA_FILE)

    is_game_on = True
    while is_game_on:
        screen.update()
        timer.sleep(0.1)
        # move snake
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with the walls
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            scoreboard.reset()

            snake.reset_snake()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()

                snake.reset_snake()
        # If head collides with any segment in the tail
        # trigger game over

    screen.exitonclick()
