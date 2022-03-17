from turtle import Turtle
ALIGNMENT = "center"
FRONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FRONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FRONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FRONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FRONT)
