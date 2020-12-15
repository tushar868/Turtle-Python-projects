from turtle import*
import turtle
speed(speed ='fastest')

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("black")


colors = [ "red","purple","blue","green","orange","yellow"]

draw = turtle.Turtle()


for x in range(360):

    draw.pencolor(colors[x % 6])

    draw.width(x/500 + 1)

    draw.forward(x)

    draw.left(59)

turtle.done()

#just take care of indentation of for loop