from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed(0)
        self.refresh()

    def refresh(self):
        xx_cor = random.randint(-280, 280)
        yy_cor = random.randint(-280, 280)
        self.goto(xx_cor, yy_cor)
