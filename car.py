import turtle
from turtle import *
import random

turtle.colormode(255)


class Car:

    def __init__(self):
        self.level_x = 1000
        self.cars = []
        self.car_speed = 2

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=3)

            new_car.r = random.randint(0, 255)
            new_car.g = random.randint(0, 255)
            new_car.b = random.randint(0, 255)

            new_car.color(new_car.r, new_car.g, new_car.b)

            rand_x = random.randrange(300, self.level_x)
            rand_y = random.randrange(-280, 280)
            new_car.goto(rand_x, rand_y)

            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self, level):
        self.car_speed += level
