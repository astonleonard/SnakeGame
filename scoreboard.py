from turtle import Turtle
ALIGNMENT = "center"
FRONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FRONT)

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as data:
                self.high_score = self.score
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
