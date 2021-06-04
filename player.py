from turtle import *

START = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.tilt(90)
        self.color("black")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.goto(START)
        self.dist = 10

    def move(self):
        new_y = self.ycor() + self.dist
        self.goto(0, new_y)

    def level_up(self):
        self.goto(START)
