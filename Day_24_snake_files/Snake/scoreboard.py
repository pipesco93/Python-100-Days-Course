from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,  0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()