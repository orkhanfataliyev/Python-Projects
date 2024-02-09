from turtle import Turtle


class Grid(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_lines()

    def draw_lines(self):
        self.pensize(width=8)
        self.hideturtle()
        self.pencolor("white")

        self.penup()
        self.goto(x=-300, y=-300)
        self.forward(200)
        self.setheading(90)
        self.pendown()
        self.forward(600)
        self.setheading(0)
        self.penup()
        self.forward(200)
        self.setheading(270)
        self.pendown()
        self.forward(600)
        self.setheading(0)
        self.penup()
        self.forward(200)
        self.setheading(90)
        self.forward(200)
        self.setheading(180)
        self.pendown()
        self.forward(600)
        self.setheading(90)
        self.penup()
        self.forward(200)
        self.setheading(0)
        self.pendown()
        self.forward(600)
        self.penup()
