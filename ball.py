from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speedx = -5
        self.speedy = 3
        
    

