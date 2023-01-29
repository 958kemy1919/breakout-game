from turtle import Turtle


class Wall(Turtle):

    def __init__(self,position,color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(0.7,2.6)
        self.goto(position)
        self.hitted_walls = []

    def destroy_wall(self,wall):
        self.hitted_walls.append(wall)
        self.hideturtle()

    def reset(self):
        self.hitted_walls = []
        self.showturtle()