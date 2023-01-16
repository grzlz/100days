from turtle import Turtle

PADDLE_LENGTH = 5
PADDLE_POSITION = 450

class Paddle:
    def __init__(self, input_side):
        self.paddle_segments = []
        self.heading = 0
        side = 1
        if input_side == "left":
            side = -1

        for i in range(PADDLE_LENGTH):
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.penup()
            paddle.speed("fastest")
            paddle.goto(PADDLE_POSITION * side, i * -20)
            self.paddle_segments.append(paddle)

    def move_up(self):
        for paddle in self.paddle_segments:
            paddle.setheading(90)
            paddle.fd(20)

    def move_down(self):
        for paddle in self.paddle_segments:
            paddle.setheading(270)
            paddle.fd(20)

    


