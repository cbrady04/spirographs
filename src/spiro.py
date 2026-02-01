import turtle

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

    