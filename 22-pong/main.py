from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep

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

# Create the ball and make it move



is_game_on = True
iter = 0
while is_game_on:
    screen.update()
    sleep(0.1)

    if abs(ball.position() - right_paddle.position()) <= 15 or abs(ball.position() - left_paddle.position())<= 15:
        current_heading = ball.heading()
        new_heading = 160 - current_heading
        ball.setheading(new_heading)

    ball.forward(15)

    print(ball.position(), right_paddle.position(), abs(ball.position() - right_paddle.position()))

    iter += 1

screen.exitonclick()



