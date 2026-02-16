import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player)< 20:
            game_is_on = False
            scoreboard.game_over()

    if player.goto_next_level():
        player.goto((0, -280))
        car_manager.level_up()
        scoreboard.increase_score()

    loop += 1

screen.exitonclick()