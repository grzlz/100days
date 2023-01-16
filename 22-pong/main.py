from turtle import Screen
from paddle import Paddle
WIDTH = 1000
HEIGHT = 700

right_paddle = Paddle("right")
left_paddle = Paddle("left")

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
 

screen.listen()
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)


screen.exitonclick()



