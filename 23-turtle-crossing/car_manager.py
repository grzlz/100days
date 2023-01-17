from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_XCOR = range(300, 400, 30)
STARTING_YCOR = range(-250, 251, 30)
# Create cars that are 20px high and 40px wide
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.color(choice(COLORS))
        self.reset_position()

    def move(self):
        if self.xcor() > -340:
            self.forward(-MOVE_INCREMENT)

        else:
            self.reset_position()

    def reset_position(self):
        self.goto(choice(STARTING_XCOR), choice(STARTING_YCOR))

      

