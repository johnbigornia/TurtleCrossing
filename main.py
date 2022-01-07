import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car_spawn_counter = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.move_cars()

    if car_spawn_counter == 6:
        car_spawn_counter = 0
        car_manager.create_car()

    if player.is_at_finish_line():
        car_manager.level_up()
        player.go_to_start()
        scoreboard.increase_level()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False

    car_spawn_counter += 1
    screen.update()

screen.exitonclick()
