from turtle import Turtle

PADDLE_LENGTH = 5

class Paddle:
    def __init__(self):
        self.paddle_segments = []
        for i in range(PADDLE_LENGTH):
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.goto(0, i * -20)
            self.paddle_segments.append(paddle)