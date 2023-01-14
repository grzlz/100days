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

# Step de 42
timmy.speed("fastest")
timmy.setpos(-384, -364.5)

for i in range(10):
    timmy.begin_fill()
    timmy.circle(24)
    timmy.end_fill()
    timmy.fillcolor(choice(color_list))
    timmy.fd(85.4)


# Rotate 90 degrees, go 145.8 pixels up, rotate left, go forward 85.4 and finally draw a circle of a 24 radius
def right_margin():
    timmy.left(90)
    timmy.fd(145.8)
    timmy.left(90)
    timmy.fd(85.4)

    for i in range(10):
        timmy.begin_fill()
        timmy.circle(24)
        timmy.end_fill()
        timmy.fillcolor(choice(color_list))
        timmy.fd(85.4)

def left_margin():
    timmy.right(90)
    timmy.forward(72.9)
    timmy.right(90)
    timmy.fd(85.4)

    for i in range(10):
        timmy.begin_fill()
        timmy.circle(24)
        timmy.end_fill()
        timmy.fillcolor(choice(color_list))
        timmy.fd(85.4)

for i in range(4):
    right_margin()
    left_margin()


screen.exitonclick()