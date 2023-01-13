from turtle import Turtle, Screen
from random import choice, sample

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.pensize(5)

colors = ["blue", "green", "red", "yellow", "purple", "green", "blue", "red"]

degrees = sample(range(15, 181), 20)
print(degrees)

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