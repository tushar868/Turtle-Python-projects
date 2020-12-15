from turtle import*
import turtle 
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("black")
color('red','yellow')


begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()