# Python program to draw 
# Rainbow Benzene
# using Turtle Programming
import turtle
#colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
colors = ['blue', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%2])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)