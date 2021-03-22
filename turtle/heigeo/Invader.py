from turtle import Turtle, Screen

class Invader(Turtle):
    def __init__(self, speed, position):
        super().__init__(shape='circle', visible=False)
        self.color('red')
        self.penup()
        self.setposition(position)
        self.speed(speed)
        self.showturtle()

    def change_speed(self, newSpeed):
        self.speed(newSpeed)

    def change_position(self, x, y):
        self.setposition(x, y)

