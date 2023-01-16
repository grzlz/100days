from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 10

    def move(self):
        new_x, new_y = self.xcor() + self.x_move, self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.x_move *= -1