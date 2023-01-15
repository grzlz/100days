# Create scoreboard to keep track of the score using turtle.write and display it
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 400)
        self.move_score()

    def move_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 18, "normal"))
        self.score += 1
