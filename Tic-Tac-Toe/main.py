from turtle import Screen
from grid import Grid
from pencil import Pencil
from dot import Dot


screen = Screen()
screen.setup(width=700, height=700)
screen.title("Tic-Tac-Toe")
screen.bgcolor("black")
screen.tracer(0)

grid = Grid()
pencil = Pencil()

row1col1 = Dot(x=-205, y=205)
row1col2 = Dot(x=0, y=205)
row1col3 = Dot(x=204, y=205)

row2col1 = Dot(x=-205, y=0)
row2col2 = Dot(x=0, y=0)
row2col3 = Dot(x=204, y=0)

row3col1 = Dot(x=-205, y=-204)
row3col2 = Dot(x=0, y=-204)
row3col3 = Dot(x=204, y=-204)

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

x_wins = False
o_wins = False


def put_x(row, col):
    board[row-1][col-1] = "X"


def put_o(row, col):
    board[row-1][col-1] = "O"


def is_empty(row, col):
    return board[row-1][col-1] == " "


def win_check():
    x = -296
    y = 210
    global x_wins
    global o_wins
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            screen.onscreenclick(None)
            screen.tracer(1)
            pencil.final_line_horizontal(x, y)
            if board[row][0] == "X":
                x_wins = True
            else:
                o_wins = True
            return True
        y -= 205

    x += 95
    y = 300

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            screen.onscreenclick(None)
            screen.tracer(1)
            pencil.final_line_vertical(x, y)
            if board[0][col] == "X":
                x_wins = True
            else:
                o_wins = True
            return True
        x += 199

    x = -290
    y = 290

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        screen.onscreenclick(None)
        screen.tracer(1)
        pencil.final_line_diagonal(x, y, heading=315)
        if board[0][0] == "X":
            x_wins = True
        else:
            o_wins = True
        return True

    x += 580
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        screen.onscreenclick(None)
        screen.tracer(1)
        pencil.final_line_diagonal(x, y, heading=225)
        if board[0][2] == "X":
            x_wins = True
        else:
            o_wins = True
        return True

    return False


def draw_check():
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True


game_is_on = True

while game_is_on:
    screen.update()

    screen.onscreenclick(pencil.goto)

    if pencil.x_turn():
        if pencil.distance(row1col1) < 141 and is_empty(1, 1):
            pencil.draw_x(xcor=-270, ycor=90)
            put_x(1, 1)
            pencil.switch_turns()
        elif pencil.distance(row1col2) < 141 and is_empty(1, 2):
            pencil.draw_x(xcor=-70, ycor=90)
            put_x(1, 2)
            pencil.switch_turns()
        elif pencil.distance(row1col3) < 141 and is_empty(1, 3):
            pencil.draw_x(xcor=130, ycor=90)
            put_x(1, 3)
            pencil.switch_turns()
        elif pencil.distance(row2col1) < 141 and is_empty(2, 1):
            pencil.draw_x(xcor=-270, ycor=-115)
            put_x(2, 1)
            pencil.switch_turns()
        elif pencil.distance(row2col2) < 141 and is_empty(2, 2):
            pencil.draw_x(xcor=-70, ycor=-115)
            put_x(2, 2)
            pencil.switch_turns()
        elif pencil.distance(row2col3) < 141 and is_empty(2, 3):
            pencil.draw_x(xcor=130, ycor=-115)
            put_x(2, 3)
            pencil.switch_turns()
        elif pencil.distance(row3col1) < 141 and is_empty(3, 1):
            pencil.draw_x(xcor=-270, ycor=-320)
            put_x(3, 1)
            pencil.switch_turns()
        elif pencil.distance(row3col2) < 141 and is_empty(3, 2):
            pencil.draw_x(xcor=-70, ycor=-320)
            put_x(3, 2)
            pencil.switch_turns()
        elif pencil.distance(row3col3) < 141 and is_empty(3, 3):
            pencil.draw_x(xcor=130, ycor=-320)
            put_x(3, 3)
            pencil.switch_turns()

    else:
        if pencil.distance(row1col1) < 141 and is_empty(1, 1):
            pencil.draw_o(xcor=-270, ycor=90)
            put_o(1, 1)
            pencil.switch_turns()
        elif pencil.distance(row1col2) < 141 and is_empty(1, 2):
            pencil.draw_o(xcor=-70, ycor=90)
            put_o(1, 2)
            pencil.switch_turns()
        elif pencil.distance(row1col3) < 141 and is_empty(1, 3):
            pencil.draw_o(xcor=130, ycor=90)
            put_o(1, 3)
            pencil.switch_turns()
        elif pencil.distance(row2col1) < 141 and is_empty(2, 1):
            pencil.draw_o(xcor=-270, ycor=-115)
            put_o(2, 1)
            pencil.switch_turns()
        elif pencil.distance(row2col2) < 141 and is_empty(2, 2):
            pencil.draw_o(xcor=-70, ycor=-115)
            put_o(2, 2)
            pencil.switch_turns()
        elif pencil.distance(row2col3) < 141 and is_empty(2, 3):
            pencil.draw_o(xcor=130, ycor=-115)
            put_o(2, 3)
            pencil.switch_turns()
        elif pencil.distance(row3col1) < 141 and is_empty(3, 1):
            pencil.draw_o(xcor=-270, ycor=-320)
            put_o(3, 1)
            pencil.switch_turns()
        elif pencil.distance(row3col2) < 141 and is_empty(3, 2):
            pencil.draw_o(xcor=-70, ycor=-320)
            put_o(3, 2)
            pencil.switch_turns()
        elif pencil.distance(row3col3) < 141 and is_empty(3, 3):
            pencil.draw_o(xcor=130, ycor=-320)
            put_o(3, 3)
            pencil.switch_turns()

    if win_check():
        game_is_on = False
        if x_wins:
            pencil.x_wins()
        else:
            pencil.o_wins()
    elif draw_check():
        game_is_on = False
        pencil.tie()

screen.exitonclick()
