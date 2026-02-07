from turtle import Turtle
import random
import time

Colors = ["red", "orange", "gray", "green", "blue", "purple"]
Move_steps_or_speed = 5

class CarManager:
    def __init__(self):
        self.cars = []

    def making_cars(self):
        number = random.randint(1,6)
        if number == 6:
            turtle = Turtle()
            turtle.penup()
            turtle.color(random.choice(Colors))
            turtle.shape("square")
            turtle.shapesize(stretch_len=2, stretch_wid=1)
            turtle.goto(280, random.randrange(-200, 200, 20))
            self.cars.append(turtle)

    def move_cars(self):
        for car in self.cars:
            car.setx(car.xcor() - Move_steps_or_speed)

