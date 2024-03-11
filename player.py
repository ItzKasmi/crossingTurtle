from turtle import Turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.teleport(0, -275)

    def up(self):
        self.forward(25)
