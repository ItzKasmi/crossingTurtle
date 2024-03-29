import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

flappy = Player()
flappy.go_to_start()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(flappy.up, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(flappy) < 20:
            game_is_on = False

    # Detect turtle reaches top
    if flappy.is_at_finish_line():
        flappy.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()