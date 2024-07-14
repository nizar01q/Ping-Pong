from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import pygame
pygame.init()
sound1 = pygame.mixer.Sound("paddle.wav")
sound2 = pygame.mixer.Sound("wall.wav")
sound3 = pygame.mixer.Sound("miss.wav")

screen = Screen()
screen.bgpic('pongimg.png')
screen.setup(825, 550)
screen.title("Ping-Pong")
screen.tracer(0)


paddle1 = Paddle(x=-390, y=0)
paddle2 = Paddle(x=380, y=0)

ball = Ball()

scoreboard1 = Scoreboard(-150, 205)
scoreboard2 = Scoreboard(118, 205)


screen.listen()
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

game_on = True


while game_on:
    screen.update()
    time.sleep(ball.sec)
    ball.ball_move1()

    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.wall_bounce()
        sound2.play()

    if ball.distance(paddle2) < 80 and ball.xcor() > 360:
        ball.paddle_bounce()
        sound1.play()

    if ball.distance(paddle1) < 80 and ball.xcor() < -365:
        ball.paddle_bounce()
        sound1.play()

    if ball.xcor() > 410:      # if paddle 2 miss
        ball.reset_position()
        scoreboard1.increase_score()
        sound3.play()

    if ball.xcor() < -410:
        ball.reset_position()  # if paddle 1 miss
        scoreboard2.increase_score()
        sound3.play()






























screen.exitonclick()