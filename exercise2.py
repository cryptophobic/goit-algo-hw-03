import math
import turtle


line = 810
level = 8
linie = line / 3**level
height = math.sqrt(3) * line / 2

screen = turtle.Screen()
#screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

def draw(boardie, current_level):
    if current_level > 1:
        for angle in [-60, 120, -60]:
            draw(boardie, current_level - 1)
            boardie.left(angle)
            boardie.forward(linie)
        draw(boardie, current_level - 1)

turtle.hideturtle()
turtle.ht()
turtle.speed(0)
board = turtle.Turtle()
board.left(120)
board.forward(linie)  # draw base
draw(board, level)
board.left(120)
board.forward(linie)  # draw base
draw(board, level)
board.left(120)
board.forward(linie)  # draw base
draw(board, level)

turtle.done()
screen.exitonclick()
