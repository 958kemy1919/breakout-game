from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.move = 40
        self.shapesize(0.8,2.5)
        self.goto(position)

    def go_left(self):
        new_x_coord = self.xcor()-self.move
        self.goto((new_x_coord,self.ycor()))

    def go_right(self):
        new_x_coord = self.xcor() + self.move
        self.goto((new_x_coord, self.ycor()))

    def resize_paddle(self):
        self.shapesize(0.4,1.25)

    def reset(self):
        self.goto(0,-230)
        self.shapesize(0.8,2.5)