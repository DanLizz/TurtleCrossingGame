from turtle import *
import time
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = Car()

skill_level = 1

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    # game_over
    for new_car in car.cars:
        if player.distance(new_car) < 20:
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 240:
        skill_level += 1
        scoreboard.level_up(level_no=skill_level)
        car.level_up(level=skill_level)
        player.level_up()


screen.exitonclick()
