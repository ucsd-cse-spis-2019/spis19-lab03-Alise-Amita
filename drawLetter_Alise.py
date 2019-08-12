# Alise Bruevich
# In this file a program will draw the letter A
import turtle

def drawA(theTurtle):
    """ drawA takes in a Turtle object and draws an A """
    theTurtle.left(60)
    theTurtle.forward(100)
    theTurtle.right(120)
    theTurtle.forward(50)
    theTurtle.right(120)
    theTurtle.forward(50)
    theTurtle.backward(50)
    theTurtle.left(120)
    theTurtle.forward(50)
    

myTurtle = turtle.Turtle()  # Create a new Turtle object
myTurtle.speed(1) # Slow it down for simplicity
drawA(myTurtle)

