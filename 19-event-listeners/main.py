from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def reset():
    tim.reset()

screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=reset)

screen.exitonclick()