from turtle import Turtle

Starting_position = (0, -280)
Move_distance = 20
Finishing_line = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(Starting_position)

    def move(self):
        if self.ycor() < Finishing_line:
            self.forward(Move_distance)

    def new_level(self):
        self.goto(Starting_position)