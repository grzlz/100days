from turtle import Screen

class Court:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=1000, height=700)
        self.screen.exitonclick()
