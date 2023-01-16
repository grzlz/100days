from turtle import Turtle

PADDLE_LENGTH = 5
PADDLE_POSITION = 450

class Paddle(Turtle):
    def __init__(self, input_side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.speed("fastest")
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.direction = 1
        if input_side == "left":
            self.direction = -1
        self.goto(self.direction * 450, 0)


    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.forward(-20)

    


