from turtle import Screen, Turtle
import time 

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

segments = []

# Create snake body
for i in range(3):
    snake = Turtle(shape="square")
    snake.pu()
    snake.color("white")
    snake.setposition(-i*20, 0)
    segments.append(snake)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    segments[0].fd(20)







screen.exitonclick()