from turtle import*
import turtle
import random
 
loadWindow = turtle.Screen()
turtle.colormode(255)
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("black")



turtle.speed(100)

sides=5


def shape(size, sides):
     for i in range(sides):
         turtle.forward(size)
         turtle.left(360/sides)


for i in range(100):
    shape(5*i, sides)
    turtle.left(i)
                #turtle.color(9*i,i,i)
    colormode(255)
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    pencolor(a, b, c)
    fillcolor(a, b, c)
    

turtle.exitonclick()