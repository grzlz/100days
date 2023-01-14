from turtle import Screen, Turtle
from snake import Snake
import time 

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)


# Create snake body
snake = Snake()
screen.listen()

screen.onkey(key="w", fun=snake.go_up)
screen.onkey(key="a", fun=snake.go_left)
screen.onkey(key="s", fun=snake.go_down)
screen.onkey(key="d", fun=snake.go_right)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()



screen.exitonclick()