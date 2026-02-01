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

    # Restart the drawing
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

    # Draw the whole thing
    def draw(self):
        # Draw the rest of the points
        R, k, l = self.R, self.k, self.l
        for i in range (0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        # Drawing is now done so hidfe the turtle cursor
        self.t.hideturtle()

    # Update by one step
    def update(self):
        # Skip the rest of the steps if done
        if self.drawingCopmlete:
            return
        # Increment the angle
        self.a += self.step
        # Draw a step
        R, k, l = self.R, self.k, self.l
        # Set the angle
        a = math.radians(self.a)
        x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        # If drawing complete, set the flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # Drawing is now done so hide the turtle cursor
            self.t.hideturtle()

    