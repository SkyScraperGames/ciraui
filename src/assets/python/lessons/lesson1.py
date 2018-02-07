from cira.ciragame import *
# this is a comment
class MyGame(CiraGame):
    # engine variables
    title = "DrawingTutorial"

    # called once when the program starts up
    def awake(self):
        pass

    # called at the beginning of each play session
    def start(self):
        pass

    # called each time the frame updates
    def update(self):
        pass

    # called when each frame needs to be drawn
    def draw(self):
        cira.display.clearScreen(0, 0, 0)
        # change the color of the pixel by changing the R, G, and B values
            # R, G, and B must be numbers between 0 and 255
        # change the location of the pixel by changing the X and Y coordinates
            # X must be a number between 0 and 19, Y must be between 0 and 22
        # ex: cira.display.putPixel(x, y, r, g, b)
        cira.display.putPixel(10, 11, 150, 0, 150)
