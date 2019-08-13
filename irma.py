import turtle
import csv

#Alise Bruevich and Amita Stowitts
#This code will track the hurricane based on Irma data

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    
    t = turtle.Turtle()
    t.speed(1)
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

        

def irma():
    """Animates the path of hurricane Irma
    """
    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()

    hurricaneFile = "data/irma.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)
        next(pointreader)        

        for row in pointreader:

            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            # This code just prints out the date and time elements of each
            # row in the file.
            # Make sure you understand what is happening here.
            # Then, you'll need to change this code
            print("Lat:", row[2], "Lon:", row[3], "Wind:", row[4])

            t.setpos(float(row[3]), float(row[2]))
            
            #based on wind speeds changes color and width of line
            
            if (int(row[4]) >= 157):
                t.color("red")
                t.pensize(10)
            elif (int(row[4]) >= 130):
                t.color("orange")
                t.pensize(8)
            elif (int(row[4]) >= 111):
                t.color("yellow")
                t.pensize(6)                          
            elif (int(row[4]) >= 96):
                t.color("green")
                t.pensize(4)
            elif (int(row[4]) >= 74):
                t.color("blue")
                t.pensize(2)
            else:
                t.color("white")


    # Hack to make sure a reference to the background image stays around
    # Do not remove or change this line
    return map_bg_img


# Feel free to add "helper" functions here


if __name__ == "__main__":
    bg=irma()

