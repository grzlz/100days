import turtle as t
from turtle import Turtle, Screen
from random import choice, sample, randint

t.colormode(255)

timmy = Turtle()
timmy.shape("classic")
timmy.color("green")
timmy.speed("fastest")

def random_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)

    return((r, g, b))



# Draw a circle
for i in range(72):
    timmy.color(random_color())
    timmy.circle(200)
    timmy.left(5)


screen = Screen()
screen.exitonclick()