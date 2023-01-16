from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from random import randint

WIDTH = 1000
HEIGHT = 700

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()

screen = Screen() 
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
 

screen.listen()
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)




is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.1)
    ball.move()
    print(ball.ycor())

    # Detect collision with wall and bounce
    if abs(ball.ycor()) > 330:
        ball.bounce()

        

screen.exitonclick()



