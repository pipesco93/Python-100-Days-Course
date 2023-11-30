from ctypes import alignment
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,  0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()