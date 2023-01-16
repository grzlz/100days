from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.print_score()

    def print_score(self):
        self.goto(0, 300)
        self.clear()
        self.write(f"{self.left_score} - {self.right_score}", align="center", font=("Courier", 24, "normal"))

    def move_score(self, favor):
        if favor == "right":
            self.right_score += 1
        elif favor == "left": 
            self.left_score += 1

    def announce_point(self, favor):
        self.goto(0, 0)
        self.write(f"Point for {favor} player.", align="center", font=("Courier", 24, "normal"))
        