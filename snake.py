from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """here we create the first three segments"""
        for place in STARTING_POSITION:
            self.add_segment(place)

    def add_segment(self, place):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("orange")
        new_snake.goto(place)
        self.segments.append(new_snake)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # here we hold our last(3rd) segment to place of second and hold the second to place of first.
        # if we have three segments (3 -> 2, 2 ->1, 1 ---->)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # we specify the position of second last segment
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # we get the position of second last to the
        self.head.forward(MOVE_DISTANCE)                     # last(3 -> 2, 2 ->1, 1 -_>)

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

    def stop(self):
        self.stop()
