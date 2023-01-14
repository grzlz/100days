# Recreate a Damian Hirst point painting
# Import colorgram and extract color palette
# Import turtle package
import turtle
from turtle import Turtle, Screen 
from random import choice

turtle.colormode(255)

screen = Screen()
timmy = Turtle()
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]

timmy.pu()
timmy.hideturtle()

timmy.setpos(-384, -300)

def turn_left():
    timmy.setheading(90)
    timmy.fd(70)
    timmy.setheading(180)
    timmy.forward(80)

def turn_right():
    timmy.setheading(90)
    timmy.forward(70)
    timmy.setheading(0)
    timmy.fd(80)


def paint():
    for i in range(10):
        timmy.dot(35, choice(color_list))
        timmy.fd(80)


for i in range(5):
    paint()
    turn_left()
    paint()
    turn_right()


screen.exitonclick()