from turtle import *
import math



def circle(perimeter, given_color):

    color(given_color)
    # circumference = perimeter * pi
    for i in range(perimeter):
        forward(math.pi())
        left(360.00 / perimeter)


def fruitarm(perimeter, degrees, given_color):

    # out of the middle
    penup()
    right(degrees)
    forward(perimeter * 0.5)
    pendown()

    # first circle
    color('magenta')
    right(90)
    circle(perimeter, given_color)


    # second circle

    penup()
    left(90)
    forward(perimeter)
    right(90)
    pendown()
    circle(perimeter, given_color)

    # back
    penup()
    right(90)
    forward(perimeter * 1.5)
    pendown()

    # align
    penup()
    right(180 - degrees)
    pendown()

def hexagonConnection(perimeter, size, given_color):

    # move to outer circle
    penup()
    forward(perimeter * size)
    right(120)
    pendown()

    # connect
    color('red')
    for i in range(6):
        forward(perimeter * size)
        right(60)

    # realign
    penup()
    right(60)
    forward(perimeter * size)
    right(180)
    pendown()



def sixstar(perimeter, size, sun_color, moon_color):

    # suntriangle
    penup()
    right(180)
    forward(perimeter * size)
    right(150)
    pendown()
    color(sun_color)

    for i in range(3):
        # strecke = wurzel{[(2 * perimeter) ** 2] - [perimeter ** 2]}
        forward(math.sqrt(((size * perimeter) ** 2) - (((size * 0.5) * perimeter) ** 2)) * 2)
        right(120)

    # align
    penup()
    right(30)
    forward(perimeter * size)
    pendown()

    # moontriangle
    penup()
    forward(perimeter * size)
    right(150)
    pendown()
    color(moon_color)
    for i in range(3):
        # strecke = wurzel{[(2 * perimeter) ** 2] - [perimeter ** 2]}
        forward(math.sqrt(((size * perimeter) ** 2) - (((size * 0.5) * perimeter) ** 2)) * 2)
        right(120)

    # align
    penup()
    right(30)
    forward(perimeter * size)
    right(180)
    pendown()

def witdhConnection(perimeter, size_factor, witdh_color):

    color(witdh_color)

    # to the rim
    penup()
    right(180)
    forward(perimeter * size_factor)
    right(180)

# first
    # align
    left(19)
    pendown()

    # six directions
    for i in range(3):
        forward(sqrt(((perimeter * 2.5) ** 2) + (sqrt((perimeter ** 2) - ((0.5 * perimeter) ** 2)) ** 2)))
        right(180 - 82)
        forward(sqrt(((perimeter * 2.5) ** 2) + (sqrt((perimeter ** 2) - ((0.5 * perimeter) ** 2)) ** 2)))
        right(180 - 38)

    #align
    penup()
    right(19)
    forward(perimeter * size_factor * 2)
    right(180)
    pendown()

# second
    # align
    left(19)
    pendown()

    # six directions
    for i in range(3):
        forward(sqrt(((perimeter * 2.5) ** 2) + (sqrt((perimeter ** 2) - ((0.5 * perimeter) ** 2)) ** 2)))
        right(180 - 82)
        forward(sqrt(((perimeter * 2.5) ** 2) + (sqrt((perimeter ** 2) - ((0.5 * perimeter) ** 2)) ** 2)))
        right(180 - 38)

    #align
    penup()
    right(19)
    forward(perimeter * size_factor)
    right(180)
    pendown()


def sixstarLines(perimeter, size_faktor, sun_color, moon_color):

    # sunlines
    right(180)

    for i in range(3):

        penup()
        forward(perimeter *  size_faktor)
        right(180)
        pendown()
        color(sun_color)
        forward(perimeter *  size_faktor)
        left(60)

    right(180)

    # moonlines
    for i in range(3):

        penup()
        forward(perimeter *  size_faktor)
        right(180)
        pendown()
        color(moon_color)
        forward(perimeter *  size_faktor)
        left(60)




def drawfruit(perimeter, given_color):

    # align to the middle
    penup()
    right(90)
    forward(perimeter * 0.5)
    left(90)
    pendown()

    # middlecircle
    circle(perimeter, given_color)

    # align
    penup()
    left(90)
    forward(perimeter / 2)
    right(180)
    pendown()

    color(given_color)
    fruitarm(perimeter, 60, given_color)
    fruitarm(perimeter, 120, given_color)
    fruitarm(perimeter, 180, given_color)
    fruitarm(perimeter, 240, given_color)
    fruitarm(perimeter, 300, given_color)
    fruitarm(perimeter, 360, given_color)



def MetatronsCube(perimeter, fruitFaktor, shifted):

    # und los gehts
    perimeter = perimeter * fruitFaktor
    given_color = 'black'
    hexagon_color = 'orange'
    sun_color = 'green'
    moon_color = 'green'
    witdh_color = 'turquoise'

    drawfruit(perimeter, given_color)

    hexagonConnection(perimeter, 2, hexagon_color)
    hexagonConnection(perimeter, 1, hexagon_color)

    sixstar(perimeter, 2, sun_color, moon_color)
    sixstar(perimeter, 1, moon_color, sun_color)

    witdhConnection(perimeter, 2, witdh_color)

    sixstarLines(perimeter, 2, hexagon_color, hexagon_color)

    if not shifted:
        left(90)


def stackedCube(perimeter, repetition, shifted):

    #repetition = repetition
    for i in range(repetition):
        MetatronsCube(perimeter, i + 1, shifted)


def finishCircles(perimeter, repetition):
    given_color = 'magenta'
    finishPeri = int(perimeter * (repetition) * 2.5)
    penup()
    forward(finishPeri)
    left(90)
    pendown()
    for i in range(repetition):


        circle(finishPeri * 2, given_color)
        penup()
        left(90)
        forward(finishPeri)
        finishPeri = int(perimeter * (repetition - i) * 2.5)
        left(180)
        forward(finishPeri)
        left(90)
        pendown()

'''__main__'''
repetition = 12
perimeter = 12

speed(10000)
width(2)
shifted = True


stackedCube(perimeter, repetition, shifted)

finishCircles(perimeter, repetition)




"""__main__

circle(perimeter)
left(90)
color('white')
forward(perimeter / 2)
right(180)
color('magenta')
fruitarm(60)
fruitarm(120)
fruitarm(180)
fruitarm(240)
fruitarm(300)
fruitarm(360)
outerCirclesConnection(perimeter)
innerCirclesConnection(perimeter)
sixstar(perimeter)
"""

bye()
