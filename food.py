from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.respawn()

    # Repositions the food after the snake's head comes in contact with it
    def respawn(self):
        self.goto(randint(-290, 290), randint(-290, 260))
