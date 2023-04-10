import random
from turtle import Turtle, Screen
from random import randint, seed, getstate, setstate, choice


def draw_dashed_lines(turtle_obj):
    for i in range(10):
        turtle_obj.fd(10)
        turtle_obj.up()
        turtle_obj.fd(10)


def draw_shape(turtle_obj, num_sides):
    turn_angle = round((360 / num_sides), 4)
    for steps in range(num_sides):
        turtle_obj.right(turn_angle)
        turtle_obj.fd(100)


def draw_all_shapes(turtle_obj, screen_obj, n_sides_low, n_sides_high):
    screen_obj.colormode(255)
    for n_sides in range(n_sides_low, n_sides_high):
        turtle_obj.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        draw_shape(turtle_obj, n_sides)
    screen_obj.exitonclick()


def random_change_color(turtle_obj, screen_obj):
    screen_obj.colormode(255)
    line_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    turtle_obj.color(line_color)


def take_random_steps(turtle_obj, direction, step_length):
    turtle_obj.setheading(direction)
    turtle_obj.fd(step_length)


def move_turtle_change_color(turtle_obj, direction, step_length, screen_obj):
    random_change_color(turtle_obj, screen_obj)
    take_random_steps(turtle_obj, direction, step_length)


def random_walk(turtle_obj, screen_obj, num_steps):
    for i in range(num_steps):
        direction = choice([90, 180, 270, 360])
        step_length = 30
        move_turtle_change_color(turtle_obj, direction, step_length, screen_obj)


def draw_spirograph(turtle_obj, screen_obj):
    for i in range(0, 360, 10):
        random_change_color(turtle_obj, screen_obj)
        turtle_obj.setheading(i)
        turtle_obj.circle(100)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph_m1(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


if __name__ == "__main__":
    # create a turtle object named tim
    tim = Turtle()
    tim.shape("classic")
    tim.speed("fastest")

    # Create screen object
    screen = Screen()
    screen.colormode(255)

    draw_spirograph_m1(5)
    screen.exitonclick()
