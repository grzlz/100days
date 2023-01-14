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


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(1)
    snake.move()



screen.exitonclick()