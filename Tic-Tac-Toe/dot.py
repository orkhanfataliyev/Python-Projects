from turtle import Turtle


class Dot(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_len=0.225, stretch_wid=0.225)
        self.goto(x, y)
