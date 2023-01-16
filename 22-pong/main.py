from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
WIDTH = 1000
HEIGHT = 700

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
score = Scoreboard()

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
    print(score.left_score)
    screen.update()
    sleep(0.1)
    ball.move()

    if abs(ball.ycor()) > 330:
        ball.bounce()
    # Detect collision with paddle
    if ball.distance(right_paddle) < 30 or ball.distance(left_paddle) < 30 and abs(ball.xcor()) > 430:
        ball.hit()
    # Keep score
    if ball.xcor() < -470:
        score.move_score("right")
        score.announce_point("right")
        sleep(2)
        ball.goto(0,0)

    elif ball.xcor() > 470:
        score.move_score("left")
        score.announce_point("left")
        sleep(2)
        ball.goto(0,0)

    score.print_score()

screen.exitonclick()



