from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("grey")
        self.shapesize(0.4,0.7)
        self.penup()
        self.hits = 0
        self.speed = 0.01
        self.x_move = -10
        self.y_move = -10
        self.goto((0,0))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x,new_y))

    def bounce_x(self):
        self.y_move *= -1


    def bounce_y(self):
        self.x_move *= -1

    def hit_paddle(self):
        self.hits += 1
        self.speed_up()

    def speed_up(self):
        if self.hits % 4 == 0 or self.hits % 12 == 0:
            self.speed *= 0.9

    def reset(self):
        self.speed = 0.04
        self.goto((0,0))