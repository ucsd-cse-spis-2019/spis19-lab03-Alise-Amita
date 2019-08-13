import turtle

# draws the letter a with the turtle
def drawA(theTurtle, size):
    """ this function takes a turtle and draws the letter A"""
    theTurtle.left(75)
    theTurtle.forward(size*100)
    theTurtle.right(150)
    theTurtle.forward(size*100)
    theTurtle.right(180)
    theTurtle.forward(size*50)
    theTurtle.left(75)
    theTurtle.forward(size*30)

# makes a turtle object and calls the drawA function
aTurtle = turtle.Turtle()
aTurtle.speed(1)
drawA(aTurtle, 2)
# testing different versions
#drawA(aTurtle, 5)
