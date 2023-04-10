from turtle import Turtle, Screen
import random
import colorgram

# extract colors from the hirst painting downloaded: https://www.enca.com/sites/default/files/hirst.jpg
# colors = colorgram.extract('hirst_spot_painting.jpg', 25)
# rgb_colors = [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors]

color_list = [
    (232, 217, 220),
    (244, 159, 35),
    (14, 95, 184),
    (209, 75, 99),
    (46, 128, 56),
    (158, 6, 57),
    (253, 223, 0),
    (232, 169, 8),
    (224, 116, 165),
    (244, 218, 48),
    (14, 59, 143),
    (96, 203, 187),
    (10, 15, 81),
    (242, 155, 174),
    (75, 37, 8),
    (2, 115, 46),
    (164, 172, 189),
    (15, 180, 9),
    (89, 74, 197),
    (119, 1, 91),
    (182, 55, 83),
    (214, 91, 21)]


def paint_dots(turtle_obj, screen_obj, n_dots):
    screen_obj.colormode(255)
    for i in range(n_dots):
        turtle_obj.color(random.choice(color_list))
        turtle_obj.dot(20)
        turtle_obj.fd(50)


def make_spot_painting(n_dots, turtle_obj, screen_obj):
    turtle_obj.speed("fastest")
    turtle_obj.penup()
    turtle_obj.hideturtle()
    for _ in range(n_dots):
        paint_dots(turtle_obj, screen_obj, n_dots=n_dots)
        turtle_obj.left(90)
        turtle_obj.fd(50)
        turtle_obj.left(90)
        turtle_obj.fd(50 * n_dots)
        turtle_obj.right(90)
        turtle_obj.right(90)


if __name__ == "__main__":
    # create a turtle object named tim
    hirst = Turtle()
    hirst.shape("classic")

    # Create screen object
    screen = Screen()
    screen.setworldcoordinates(-1, -1, 660, 660)
    make_spot_painting(15, hirst, screen)
    screen.exitonclick()
