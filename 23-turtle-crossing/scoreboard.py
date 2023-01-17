from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 0
        self.display_score()

    def increase_level(self):
        self.level += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0 ,0)
        self.write("GAME OVER.", align="center", font=FONT)