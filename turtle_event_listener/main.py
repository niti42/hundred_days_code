from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_counterclockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_drawing():
    tim.reset()


if __name__ == "__main__":
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=turn_clockwise)
    screen.onkey(key="d", fun=turn_counterclockwise)
    screen.onkey(key="c", fun=clear_drawing)

    screen.exitonclick()
