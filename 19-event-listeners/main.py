# Build a turtle racing game

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(len(colors)):
    color_turtle = Turtle(shape="turtle")
    color_turtle.color(colors[i])
    color_turtle.penup()
    color_turtle.goto(x=-230, y=-100 + i*30)
    all_turtles.append(color_turtle)

is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"{winning_color.capitalize()} turtle won! You win!")
            else:
                print(f"{winning_color.capitalize()} turtle won! You lose!")
                
        else:
            random_distance = randint(0, 10)    
            turtle.forward(random_distance)
    



screen.exitonclick()