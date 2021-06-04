from turtle import *
import time

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.update_score()
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FONT)

    def level_up(self, level_no):
        self.score += 1
        self.goto(0, 0)
        self.write(f"Level {level_no }", align=ALIGNMENT, font=FONT)
        time.sleep(1)
        self.update_score()
