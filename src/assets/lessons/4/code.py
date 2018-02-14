from cira.ciragame import *

class MyGame(CiraGame):
  # called when each new frame needs to be drawn
  def draw(self):
        cira.display.clearScreen(0, 0, 0)
        # change the location of the pixel by changing the X and Y coordinates
            # X must be a number between 0 and 19, Y must be between 0 and 22
        # change the color of the pixel by changing the R, G, and B values
                # R, G, and B must be numbers between 0 and 255
        # the putPixel function takes 5 arguments
        # example: cira.display.putPixel(x, y, r, g, b)
        cira.display.putPixel(10, 11, 150, 0, 150)
