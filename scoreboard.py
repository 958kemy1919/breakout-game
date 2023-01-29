from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("silver")
        self.hideturtle()
        self.penup()
        self.poens = 0
        self.lifes = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto((-350,320))
        self.write("|",True,"left",font=("Arial",40,"bold"))
        self.goto((-270,260))
        if self.poens < 10:
            self.write(f"00{self.poens}",True,"center",font=("Arial",40,"normal"))
        elif self.poens < 100:
            self.write(f"0{self.poens}",True,"center",font=("Arial",40,"normal"))
        else:
            self.write(f"{self.poens}",True,"center",font=("Arial",40,"normal"))
        self.goto((170,320))
        if self.lifes == 1:
            self.write("|",True,"center",font=("Arial",40,"bold"))
        elif self.lifes > 1:
            self.write(f"{self.lifes}",True,"center",font=("Arial",40,"normal"))
        self.goto((280,260))
        self.write("000",True,"right",font=("Arial",40,"normal"))

    def add_poens(self,color):
        if color == ("yellow","yellow"):
            self.poens += 1
        elif color == ("green","green"):
            self.poens += 3
        elif color == ("orange","orange"):
            self.poens += 5
        elif color == ("red","red"):
            self.poens += 7

    def add_lost_life(self):
        self.lifes += 1

    def is_end_game(self):
        if self.lifes == 4:
            return True
        else:
            return False

    def reset(self):
        self.poens = 0
        self.lifes = 1