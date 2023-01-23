from turtle import Screen, Turtle 
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.bgcolor("black")
writer = Turtle()
writer.penup()
writer.hideturtle()
us_map = Turtle()
us_map.shape(image)

# Import data
data = pd.read_csv("50_states.csv")

number_states = len(data.index)


while number_states > 0:

    answer =  screen.textinput(title="Guess the State", prompt=f"{number_states} states remaining. What's another state's name?")
    answer = answer.capitalize()

    if answer in data["state"].values:
        
        cords = data[data["state"] == answer]
        writer.goto(int(cords.x), int(cords.y))
        writer.write(answer)
        number_states -= 1


screen.exitonclick()