from turtle import Turtle

# Fixed constants for the game
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    # Creates the head and 2 body parts of the snake and places them in the center of the screen
    def create_snake(self):
        for pos in STARTING_POS:
            part = Turtle("square")
            part.color("white"), part.pu(), part.goto(pos)
            self.snake_body.append(part)
        self.head = self.snake_body[0]

    # Adds a tail part every time the snake eats food
    def add_part(self):
        new_part = Turtle("square")
        new_part.color("white"), new_part.pu()
        new_part.goto(self.snake_body[-1].pos())
        self.snake_body.append(new_part)

    # Keeps the snake moving one step every time
    def move(self):
        for snake_part in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[snake_part].goto(self.snake_body[snake_part - 1].pos())
        self.head.fd(MOVE_DISTANCE)

    # Resizes the snake back to a head and 2 body parts
    def reset(self):
        for part in self.snake_body:
            part.ht()
        self.snake_body.clear()
        self.create_snake()

    # Changes the snake's head to face North
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    # Changes the snake's head to face South
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    # Changes the snake's head to face West
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    # Changes the snake's head to face East
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
