from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create()
        self.head = self.body[0]

    def create(self):
        for position in STARTING_POSITIONS:
            self.add(position)
    
    def add(self,position):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(position)
        self.body.append(new)

    def extend(self):
        self.add(self.body[-1].position())

    def move(self):
        for pos_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[pos_num - 1].xcor()
            new_y = self.body[pos_num - 1].ycor()
            self.body[pos_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.body:
            segment.goto(1000,1000)
        self.body.clear()
        self.create()
        self.head = self.body[0]