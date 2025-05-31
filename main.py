# This is the main file where main logic for the game will be executed.Other supporting files imported here.

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

# Create a screen object from turtle Screen Class to dislay the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink")
screen.title("My Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

# Listen() will recieve input from keyboard & calls respective method.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
    for item in snake.snake[1:]:
        if snake.head.distance(item) < 10:
            game_on = False
            score.game_over()

# Closes the screen on click if the game is over.
screen.exitonclick()
