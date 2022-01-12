from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
score = Scoreboard()

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Ultimate Snake Charmer!")
screen.tracer(0)

# Setup Event Listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_in_progress = True


def quit_game():
    global game_in_progress
    game_in_progress = False


screen.onkey(quit_game, "q")

# Keep the snake moving forward
while game_in_progress:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food.pos()) < 15:
        snake.add_part()
        score.update_score()
        score.display_score()
        food.respawn()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        score.reset()
        food.respawn()
        snake.reset()

    # Detect collision with tail
    for snake_part in snake.snake_body[1:]:
        if snake.head.distance(snake_part) < 10:
            score.reset()
            food.respawn()
            snake.reset()

screen.exitonclick()
