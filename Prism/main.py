import turtle
from Prism import Prism
from TwoD_shapes import twoD_shapes

screen = turtle.Screen()
screen.bgcolor(0.0,0.4,0.4)
screen.screensize(1000,1000)
ana = turtle.Turtle()
ana.speed(3)
ana.pensize(2.5)

triangulo = twoD_shapes(ana,6,100)
prisma = Prism(triangulo,50)
prisma.draw3Dshape()
