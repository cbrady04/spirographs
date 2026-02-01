import turtle
import math

# A class that draws a Spirograph
class Spiro:
    # Constructor
    def __init__(self, xc, yc, col, R, r, l):

        # Create the turtle object
        self.t = turtle.Turtle()
        # Set cursor shape
        self.t.shape('turtle')
        # Set the step in degrees
        self.step = 5
        # Set the drawing complete flag
        self.drawingComplete = False

        # Set the parameters
        self.setparams(xc, yc, col, R, r, l)

        # Initialise the drawing
        self.restart()
    
    def setparams(self, xc, yc, col, R, r, l):
        # The Spirograph parameters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # Reduce r/R to its smallest form by dividing with the GCD
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
        # Get ratio of radii
        self.k = r.float(R)
        # Set the colour
        self.t.colour(*col)
        # Store the current angle
        self.a = 0

    def restart(self):
        # Set the flag
        self.drawingComplete = False
        # Show the turtle
        self.t.showturtle()
        # Go to the first point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    