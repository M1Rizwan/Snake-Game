import turtle as t
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_snake_bit(position)

    def extend_snake(self):
        self.add_snake_bit(self.snake[-1].position())

    def add_snake_bit(self, position):
        new_snakebit = t.Turtle(shape="square")
        new_snakebit.penup()
        new_snakebit.color("red")
        new_snakebit.goto(position)
        self.snake.append(new_snakebit)

    def move(self):
        for no in range(len(self.snake)-1, 0, -1):
            pre_x = self.snake[no - 1].xcor()
            pre_y = self.snake[no - 1].ycor()
            self.snake[no].goto(pre_x, pre_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
