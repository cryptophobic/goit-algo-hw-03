import argparse
import time
import turtle
import random

class Koch:

    def __init__(self, level):
        level = int(level)
        if level <= 0 or level > 10:
            raise Exception("Level must be between 1 and 10")

        self.max_level = level
        self.screen = None
        self.board = None
        self.position = 0
        self.base_line_length = 300

    def __initialize_turtle(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=1.0, height=1.0)  # Note that it needs to be 1.0, and not 1
        screensize = self.screen.screensize()
        turtle.colormode(255)
        turtle.tracer(0)
        turtle.hideturtle()
        self.board = turtle.Turtle()
        self.position = -screensize[0]
        self.board.up()
        self.board.setpos(self.position, 0)
        self.board.down()

    def draw(self):
        self.__initialize_turtle()
        time.sleep(1)
        for current_level in range(1, self.max_level + 1):

            time.sleep(0.5)
            self.board.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.board.begin_fill()
            current_line_length = self.base_line_length / 3 ** current_level

            for _ in range(3):
                self.board.left(120)
                self.board.forward(current_line_length)  # draw base
                self.koch_line(current_level, current_line_length)

            self.board.end_fill()

            self.board.up()
            self.position += (self.base_line_length // 2.5)

            self.board.setpos(self.position, 0)
            self.board.down()
            turtle.update()

        turtle.done()
        self.screen.exitonclick()

    def koch_line(self, level, current_line_length):
        if level > 1:
            for angle in [-60, 120, -60]:
                self.koch_line(level - 1, current_line_length)
                self.board.left(angle)
                self.board.forward(current_line_length)
            self.koch_line(level - 1, current_line_length)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--level", help="Level of fractal. Max=10", required=True)
    args = parser.parse_args()
    koch = Koch(level=args.level)
    koch.draw()

