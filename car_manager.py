from turtle import Turtle
import random
import time

COLORS = ["blue", "gold", "red", "purple", "green", "orange"]

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(280, random.randint(-280, 280))
        self.left(180)

    def move_car(self):
        self.forward(10)


