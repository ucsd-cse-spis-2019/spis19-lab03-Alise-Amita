import turtle

# draws the letter a with the turtle
def drawA(theTurtle):
    """ this function takes a turtle and draws the letter A"""
    theTurtle.left(75)
    theTurtle.forward(300)
    theTurtle.right(150)
    theTurtle.forward(300)
    theTurtle.right(180)
    theTurtle.forward(150)
    theTurtle.left(75)
    theTurtle.forward(80)

# makes a turtle object and calls the drawA function
aTurtle = turtle.Turtle()
aTurtle.speed(1)
drawA(aTurtle)

