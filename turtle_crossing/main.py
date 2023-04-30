import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()

    screen.listen()
    screen.onkeypress(player.go_up, "Up")

    car_manager = CarManager()
    level = Scoreboard()
    game_is_on = True
    while game_is_on:
        timer.sleep(0.1)

        screen.update()
        car_manager.create_car()
        car_manager.move_cars()
        # If the turtle collides with any of the cars then game over
        for car in car_manager.all_cars:
            if car.distance(player) <= 20:
                level.game_over()
                game_is_on = False


        if player.is_at_finish_line():
            player.go_to_start()
            level.increase_level()
            car_manager.level_up()



    screen.exitonclick()
