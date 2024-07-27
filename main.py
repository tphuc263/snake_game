from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from score_board import Score_board

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(100)

snake = Snake()
food = Food()
score_board = Score_board()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_tail()
        score_board.increase_score()

    #detect collision with wall.
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 280 or x_cor < -280 or y_cor > 280 or y_cor < -280:
        game_is_on = False
        score_board.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
