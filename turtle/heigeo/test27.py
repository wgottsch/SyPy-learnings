from Invader import Invader

myFigure = Invader('slowest', (80, 80))
invader = Invader('slowest', (100, 100))

invader.change_position(-100, -100)
myFigure.change_position(-10, -10)

invader.change_speed('fastest')

invader.pendown()  # try an original turtle method

invader.change_position(100, -100)

screen = Screen()

screen.exitonclick()