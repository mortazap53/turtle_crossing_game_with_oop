import time
from turtle import Screen
from player import Player
from cars import CarManager
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Score()

screen.listen()
screen.onkey(player.move, "space")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    if player.ycor() > 275:
        car.speed_up()
        player.new_level()
        score.update_level()

    for c in car.cars:
        if player.distance(c) < 20:
            score.game_over()
            game_on = False

screen.exitonclick()