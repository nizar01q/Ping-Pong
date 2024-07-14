from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed("slow")
        self.shape("square")
        self.penup()
        self.color("goldenrod")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.left(90)
        self.goto(x, y)

    def move_up(self):
        self.speed("fastest")
        self.setheading(90)
        self.forward(50)

    def move_down(self):
        self.speed("fastest")
        self.setheading(270)
        self.forward(50)






