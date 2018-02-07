from cira.ciragame import *

class MyGame(CiraGame):
    # called when each frame needs to be drawn
    def draw(self):
        cira.display.clearScreen(0, 0, 0)
        # Draw your character by placing pixels
        # use the cira.display.putPixel(x, y, r, g, b) function from lesson 4
        # each pixel needs to be on its own line
        cira.display.putPixel()
