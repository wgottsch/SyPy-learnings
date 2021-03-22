# Klassenbibliothek zu "heiligen Geometrie"
#
#
from turtle import Turtle, Screen
import math

class Figure(Turtle):

# x = Raumkoordinaten
# y =
# Z =

# Radius
# Linienfarbe
# Liniendicke
# Füllfarbe

# def Init
# def paint(x, y, radius, **kwargs)

    # self ist ein Objekt vom typ "Turtle", 
    def __init__(self, x, y, z, radius, line_col, fill_col, num_side, site_length, length, breadth):
       super().__init__(shape='dot', visible=True)
       self.x = x
       self.y = y
       self.z = z
       self.radius = radius
       self.line_col = line_col
       self.fill_col = fill_col
       self.num_side = num_side
       self.site_length = site_length
       self.length = length
       self.breadth = breadth

    def drawCircle(self, x, y, radius):
        self.penup()
        self.goto (x,y)
        self.circle(radius)

    def drawLine (self, x1, y1, x2, y2):
        self.penup()
        self.goto (x1, y1)
        self.pendown()
        self.goto (x2, y2)
        self.penup()

    def drawPolygon (self, x, y, num_side, radius):
        sideLen = 2 * radius * math.sin (math.pi / num_side)
        angle = 360 / num_side
        self.penup()
        self.goto (x, y)
        self.pendown()
        for iter in range (num_side):
            self.forward (sideLen)
            self.left (angle)

    def get_perimeter(self):
       return 2 * (self.length + self.breadth)
   
    def get_area(self):
       return self.length * self.breadth

def main():
   
    a = Figure(100,100,100,50,"blue","black",4,10,10,5)
    a.drawCircle(100, 100, 10)
    a.drawLine(100,100,50,50)
    a.pendown()

    screen =  Screen()
    #screen.register_shape("dot", (1,1)
    
    screen.exitonclick()

main()    