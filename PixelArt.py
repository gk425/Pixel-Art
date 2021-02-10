# Giwon Kim. Class of 2019
# Mini Project 3.

# This is a very basic initial setup for the pixel-art project, using
# the turtle module.
# Full documentation of the module can be found at
# https://docs.python.org/3.6/library/turtle.html

import turtle           # Allows us to use all function in turtle module

# Basic initialization of the screen and the drawing turtle object
wn = turtle.Screen()    # Creates a screen object called 'wn'
wn.setworldcoordinates(-155, 0, 400, 400) # Sets the lowerleft corner(-155, 0) and upper-right corner (400, 400)
t = turtle.Turtle()     # Creates the turtle called 't'
t.hideturtle()          # Hides the appearance of the Turtle
t.speed(0)              # Turtle has no extra delay in carrying out its performance
turtle.tracer(0,0)      # The screen has no extra delay in rendering the graphics

# --------------------------------------------------------------------------#
# Your global variables and constants go below.
# --------------------------------------------------------------------------#
# the reason why I use a list of colors as a global value(outside of fuction) is that
# python can keep remembering the previous color
# after click a pallet to change another color. Otherwise the previous color will disappear.
colors = [ "darkorchid4", "blue", "darkgreen", "yellow", "orange", "red", "white", "black" ]
# --------------------------------------------------------------------------#
# Your functions go below.
# --------------------------------------------------------------------------#

# A function, gridsquare(), provides a grid of 20-by-20 squares that are 20 pixels long.
def gridsquares():
    # Draw the vertical lines with 20 pixels long line spacing.
    x = 0
    # Since we need a grid of 20-by-20 squares that are 20 pixels long.
    # the total length is 400
    while x <= 400:
        t.penup()
        # Set the orientation of the turtle to the north.
        t.setheading(90)
        t.goto(x, 0)
        t.pencolor("grey")
        t.pendown()
        t.forward(400)
        # Move rightwards by 20 pixels to draw next vertical line.
        x = x + 20
    # Draw the horizontal lines with 20 pixels long line spacing.
    y = 0
    # Since we need a grid of 20-by-20 squares that are 20 pixels long.
    # the total length is 400
    while y <= 400:
        t.penup()
        # Set the orientation of the turtle to the east.
        t.setheading(0)
        t.goto(0, y)
        t.pencolor("grey")
        t.pendown()
        t.forward(400)
        # Move upwards by 20 pixels to draw next vertical line.
        y = y + 20


# Takes a coorninate (x, y) and a color, which is the clicked coordinate and
# the selected color from the user.
# fills a selected grid square with a selected color.
def colorfilling(x, y, chosencolor) :
    t.penup()
    # Set the orientation of the turtle to the east.
    t.setheading(0)
    # Since it's a set of 20-by-20 grid squares
    # By using x // 20 and y // 20, we can find the place of a selected square
    # so that it can fill the square with a selected color.
    gridx = x // 20
    gridy = y // 20
    # Going to the lower left corner of the selected square to fill up the color.
    t.goto(gridx * 20, gridy * 20)
    t.pendown()
    t.pencolor("grey")
    t.fillcolor(chosencolor)
    t.begin_fill()
    for k in range(0, 4) :
        t.forward(20)
        t.left(90)
    t.end_fill()


# Provides a pallet of colors to the left of the grid, and the user can switch
# the color of the left-click by clicking on the pallet.
# A pallet is a set of 50-by-50 grid squares.
def pallet():
    k = 0 # k is index of colors which is a global variable
    y = 0 # y is the value of y in a coordinate (-50, y)
    while y < 400 :
        t.penup()
        t.setheading(0)
        # To build up a pallet box of colors from lowerleft corner (-50, 0)
        t.goto(-50, y)
        t.pendown()
        t.pencolor('black')
        t.fillcolor(colors[k])
        t.begin_fill()
        for i in range(0, 4) :
            t.forward(50)
            t.left(90)
        t.end_fill()
        # Since a pallet is a set of 50-by-50 squares, y = y + 50
        y = y + 50
        k = k + 1

# Draws a "Show Art button"
class drawShowArtButton :
    """Represents the draw show art button"""
    def __init__(self, xl, yl, xu, yu):
        self.coord = (xl, yl, xu, yu)

    def drawbutton(self):
        t.penup()
        t.goto(self.coord[0], self.coord[1])  # go to lower left corner
        t.setheading(90) # to the north
        t.pendown()
        t.pencolor('black')
        t.fillcolor('lightblue')
        t.begin_fill()
        for k in range(4) :
            t.forward(80)
            t.right(90)
        t.end_fill()

    # In order to write a letter "Show" in the box
    def write_show(self) :
        t.penup()
        t.goto(-120, 205)
        t.pendown()
        t.write('Show', font=("Arial", 18, "bold"))

    # In order to write a letter "Art" in the box
    def write_art(self) :
        t.penup()
        t.goto(-110, 185)
        t.pendown()
        t.write('Art', font=("Arial", 18, "bold"))

# Draws an arrow below the "Show Art" button.
def drawarrow() :
    t.penup()
    t.goto(-100, 150)
    t.setheading(270)
    t.pendown()
    t.pensize(8)
    t.forward(30)
    t.left(230)
    t.forward(10)
    t.back(10)
    t.right(100)
    t.forward(10)

# Create list of lists for the color information.
mycolorlist = []
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])
mycolorlist.append(['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'])

# What to do if the user left-clicks on the coordinates (x,y)
# Parameters: x and y coordinates of a left click on the screen
chosencolor = 'white' # To avoid errors when the user left click on the grid squares before selecting the color from a pallet.
def leftclickfn(x, y) :
    global chosencolor
    # If a user already chose the collor (x > 0), then fill up a selected square with the collor
    if x > 0 :
        gridx = int(x // 20)
        gridy = int(y // 20)
        colorfilling(x, y, chosencolor)
        mycolorlist[gridx][gridy] = chosencolor # Stores color info every time I call the colorfilling function.
    # If the user haven't choose any collor from the pallet, then we can define
    # choosencolor after the user choose a color from the pallet.
    elif x <= 0 and -50 <= x :
        gridy = int(y // 50)
        chosencolor = colors[gridy] # chooses the color by where the user clicks on the color pallet


    # If the user left click the "Show Art" button, then display a tiny 2-by-2 pixels square.
    if x < -60 and y < 240 and x > -140 and y > 160 :
        coord_x = 0
        coord_y = 0
        for coord_x in range(0, 20) :
            for coord_y in range(0, 20) :
                color = mycolorlist[coord_x][coord_y] # smallx index = 0~19, smally index = 0~19
                t.penup()
                t.setheading(0)
                t.goto(-120 + (coord_x * 2), 60 + (coord_y * 2)) # Because "Show Art" is a 2-by-2 pixels square
                t.dot(4, color)
                t.forward(2)
            t.back(40)
            t.left(90)
            t.forward(2)
            t.right(90)

# What to do if the user right-clicks on the coordinates (x,y)
# Parameters: x and y coordinates of a right click on the screen
def rightclickfn(x,y):
    if x > 0 :
        t.penup()
        # Set the orientation of the turtle to the east.
        t.setheading(0)
        # Since it's a set of 20-by-20 grid squares
        # By using x // 20 and y // 20, we can find the place of a selected square
        # so that it can fill the square with white color by right clicks.
        gridx = int(x // 20)
        gridy = int(y // 20)
        # Going to the lower left corner of the selected square to fill up the color.
        t.goto(gridx * 20, gridy * 20)
        t.pendown()
        t.pencolor("grey")
        mycolorlist[gridx][gridy] = 'white'
        t.fillcolor('white')
        t.begin_fill()
        for k in range(0, 4) :
            t.forward(20)
            t.left(90)
        t.end_fill()

# --------------------------------------------------------------------------#
# Your main code goes below.
# --------------------------------------------------------------------------#

# Provides a 20-by-20 grid squares
gridsquares()

# Provides a pallet of colors to the left of the grid
pallet()

# Provides a "Show Art" button.
drawshowartbtn = drawShowArtButton(-140, 160, -60, 240)
drawshowartbtn.drawbutton()
drawshowartbtn.write_show()
drawshowartbtn.write_art()
drawarrow() # Provides an arrow below the button.
t.pensize(1) # To reset the pen size to whatever it was before after drawing the arrow.

# Right-click on a canvas square fills that square white.
wn.onclick(rightclickfn, 2)

# A user can fill up a square with a colors from the pallet by leftclicking.
# And a user can see what the art looks like when reduced down to pixels
# by leftclicking the "Show Art" button.
wn.onclick(leftclickfn, 1)

# Wait for user to click somewhere on the screen object
wn.mainloop()
