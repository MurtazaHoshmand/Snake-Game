from turtle import Screen
from snake import Snake
from food import Food
from scorboard import Scoreboard
import time

screen = Screen()
#  ------------------------------------- Creating Screen ------------------------------------
screen.setup(width=600, height=600 )
screen.bgcolor("gray")

screen.title("Snake Game")
screen.tracer(0)  # for control the moving of our snakes(to not have distance between them)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on = True
while is_on:
    screen.update()  # to update all of changes and turn the tracer on.
    time.sleep(0.1)  # it defines the speed of snake
    snake.move()
    # detect with food
    if snake.head.distance(food) < 16:
        food.refresh()
        score.increase_score()
        snake.extend()
    # detect with wall
    if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
        score.reset()
        snake.reset()

    # detect with the tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()
