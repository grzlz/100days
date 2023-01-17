import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_list = [CarManager() for car in range(4)]

screen.onkeypress(key="w", fun=player.move)
screen.onkeypress(key="s", fun=player.move_bd)

game_is_on = True
while game_is_on:
    for car in car_list:
        car.move()
    time.sleep(0.1)
    screen.update()
