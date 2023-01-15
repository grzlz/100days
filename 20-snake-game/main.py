from turtle import Screen
from snake import Snake
from food import Food
from scoreborad import Scoreboard
import time 

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

# Create snake body
snake = Snake()
food = Food()
score = Scoreboard()

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

# Detect collission with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.move_score()
        snake.extend()

# Detect collission with wall
    if snake.segments[0].xcor() > 425 or snake.segments[0].xcor() < -425 or snake.segments[0].ycor() > 425 or snake.segments[0].ycor() < -425:
        is_game_on = False
        score.game_over()

# Detect collission with tail
    if snake.segments[0].position() in [segment.position() for segment in snake.segments][1:]:
        is_game_on = False
        score.game_over()


screen.exitonclick()