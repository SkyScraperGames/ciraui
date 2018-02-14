from cira.ciragame import *
# this is a comment
class MyGame(CiraGame):
    # engine variables
    title = "Quick Start"

    # These are the variables for my "player" pixel
    x = 9
    y = 11
    red = 0
    green = 0
    blue = 255

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
        cira.display.putPixel(self.x,self.y,self.red,self.green,self.blue)
        return
