from turtle import Turtle, Screen
from random import choice, sample

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.pensize(5)    
timmy.speed("fastest")
colors = ["blue", "green", "red", "yellow", "purple", "green", "blue", "red"]

degrees = [0, 90, 180, 270]


# Generate a random walk function
def random_walk():
    left_right = choice(["left", "right"])
    timmy.pencolor(choice(colors))
    degree = choice(degrees)
    if left_right == "left":
        timmy.left(degree)
    else:
        timmy.right(degree)
    timmy.fd(40)

for i in range(120):
    random_walk()

screen = Screen()
screen.exitonclick()