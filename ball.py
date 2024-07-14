from turtle import Turtle
import random
INITIAL_DEGREES = [45, 135]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("whitesmoke")
        self.xmove = 1.8
        self.ymove = 1.8
        self.sec = 0.01

    def ball_move1(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.ymove *= -1

    def paddle_bounce(self):
        self.xmove *= -1
        self.sec *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.xmove *= -1
        self.sec = 0.01













