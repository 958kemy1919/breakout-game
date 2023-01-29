

from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard

screen = Screen()
screen.title("Breakout Video Game")
screen.bgcolor("black")
screen.setup(800,750)
screen.tracer(0)

paddle = Paddle((0,-230))
ball = Ball()
scoreboard = Scoreboard()
walls = []
colors = ["yellow","yellow","green","green","orange","orange","red","red"]

x_position = -370
y_position = 100

for i in range(0,8):
    for j in range(0,14):
        position = (x_position,y_position)
        walls.append(Wall(position,colors[i]))
        x_position += 57
    x_position = - 370
    y_position += 20


screen.listen()
screen.onkey(fun=paddle.go_left,key="Left")
screen.onkey(fun=paddle.go_right,key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    sleep(ball.speed)
    ball.move()

    for wall in walls:
        if ball.distance(wall.position()) < 25:
            if wall not in wall.hitted_walls:
                wall.destroy_wall(wall)
                ball.bounce_x()
                if wall.color() == "orange" or wall.color() == "red":
                    ball.speed_up()
                scoreboard.add_poens(wall.color())
                scoreboard.write_score()
                break

    if ball.ycor() < -210 and ball.distance(paddle) < 50 or ball.ycor() > 360:
        if ball.ycor() > 360:
            paddle.resize_paddle()
        if ball.ycor() < -210 and ball.distance(paddle) < 50:
            ball.hit_paddle()
        ball.bounce_x()

    if ball.xcor() < -370 or ball.xcor() > 370:
        ball.bounce_y()

    if ball.ycor() < -370:
        scoreboard.add_lost_life()
        if scoreboard.is_end_game():
            scoreboard.reset()
            for wall in walls:
                wall.reset()
        scoreboard.write_score()
        ball.reset()
        paddle.reset()

screen.exitonclick()
