from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        if player == 1:
            self.goto(-430,0)
        elif player == 2:
            self.goto(430,0)
    
    def up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 20)
    
    def down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 20)
        