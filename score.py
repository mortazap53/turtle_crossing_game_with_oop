from turtle import Turtle

Font = ("courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-250, 230)
        self.write(f"Mission : {self.level}", font=Font)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Mission : {self.level}", font=Font)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!",align="center",font=Font)