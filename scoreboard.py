from turtle import Turtle
ALGNEMENT="center"
FONT=("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False,
    #               ALGNEMENT, FONT)
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}",False,
                   ALGNEMENT,FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score+=1
        self.update_score()


