from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0,240)
        self.writescore(0)

    def writescore(self, winner):
        self.clear()
        if winner == 1:
            self.score1 += 1
        elif winner == 2:
            self.score2 += 1
        self.write(f"Score\n {self.score1} - {self.score2}", font= ("Comic Sans", 20, "normal"), align="center")
