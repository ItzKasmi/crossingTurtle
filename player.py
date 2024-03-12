from turtle import Turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)

    def up(self):
        self.forward(25)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True

    def go_to_start(self):
        self.teleport(0, -275)
