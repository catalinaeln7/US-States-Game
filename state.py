from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class State(Turtle):

    def __init__(self, data, state, color):
        super().__init__()
        self.hideturtle()
        self.color(color)
        self.penup()
        self.goto(x=int(data.x), y=int(data.y))
        self.write(arg=state, move=False, align=ALIGNMENT, font=FONT)
