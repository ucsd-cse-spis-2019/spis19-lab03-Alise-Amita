import turtle

def drawA(theTurtle):
    theTurtle.left(75)
    theTurtle.forward(300)
    theTurtle.right(150)
    theTurtle.forward(300)
    theTurtle.right(180)
    theTurtle.forward(150)
    theTurtle.left(75)
    theTurtle.forward(80)

aTurtle = turtle.Turtle()
aTurtle.speed(1)
drawA(aTurtle)

