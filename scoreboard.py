from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x, y):
        self.score = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.color("medium slate blue")
        self.write(self.score, align="left", font=('agency fb', 50, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="left", font=('agency fb', 50, 'bold'))




