from turtle import Turtle
import random
import time

Colors = ["red", "orange", "gray", "green", "blue", "purple"]
Starting_moving_distance = 5
Move_increment = 10

class CarManager:
    def __init__(self):
        self.cars = []

    def making_cars(self):
        turtle = Turtle()
        turtle.penup()
        turtle.color(random.choice(Colors))
        turtle.shape("square")
        turtle.shapesize(stretch_len=3, stretch_wid=1)
        turtle.goto(280, random.randrange(-200, 200, 20))
        self.cars.append(turtle)

