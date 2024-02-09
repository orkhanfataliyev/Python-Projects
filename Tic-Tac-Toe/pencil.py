from turtle import Turtle

FONT = ("Comic Sans", 200, "bold")


class Pencil(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-350, y=350)
        self.turn = 2
        self.hideturtle()

    def draw_x(self, xcor, ycor):
        self.color("cyan")
        self.goto(xcor, ycor)
        self.write(arg="X", font=FONT)

    def draw_o(self, xcor, ycor):
        self.color("magenta")
        self.goto(xcor, ycor)
        self.write(arg="O", font=FONT)

    def x_turn(self):
        return self.turn % 2 == 0

    def switch_turns(self):
        self.turn += 1
        self.goto(x=-350, y=350)

    def x_wins(self):
        self.speed("fastest")
        self.goto(-40, 310)
        self.color("white")
        self.write(arg="X WINS", font=("Impact", 30, "normal"))

    def o_wins(self):
        self.speed("fastest")
        self.goto(-40, 310)
        self.color("white")
        self.write(arg="O WINS", font=("Impact", 30, "normal"))

    def tie(self):
        self.speed("fastest")
        self.goto(-30, 310)
        self.color("white")
        self.write(arg="Draw", font=("Impact", 30, "normal"))

    def final_line_vertical(self, x, y):
        self.pensize(width=20)
        self.color("yellow")
        self.penup()
        self.goto(x, y)
        self.setheading(270)
        self.pendown()
        self.forward(600)
        self.penup()

    def final_line_horizontal(self, x, y):
        self.pensize(width=20)
        self.color("yellow")
        self.penup()
        self.goto(x, y)
        self.setheading(0)
        self.pendown()
        self.forward(600)
        self.penup()

    def final_line_diagonal(self, x, y, heading):
        self.pensize(width=20)
        self.color("yellow")
        self.penup()
        self.goto(x, y)
        self.setheading(heading)
        self.pendown()
        self.forward(820)
        self.penup()
