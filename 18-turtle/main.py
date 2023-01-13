from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# Draw a pentagon 

figures = [3, 4, 5, 6, 7, 8, 9, 10]
colors = ["blue", "green", "red", "yellow", "purple", "green", "blue", "red"]


for figure in range(len(figures)):
    timmy.pencolor(colors[figure])
    for i in range(figures[figure]):
        timmy.fd(100)
        timmy.right(360/figures[figure])

    




screen = Screen()
screen.exitonclick()