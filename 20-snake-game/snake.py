# Create Snake class
from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.setposition(-i*20, 0)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)       
        self.segments[0].fd(MOVE_DISTANCE)

    def go_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def go_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def go_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)



