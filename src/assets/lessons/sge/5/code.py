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
        if cira.keys.getKey('1-Left'):
            if self.x>0:
                self.x-=1
        elif cira.keys.getKey('1-Right'):
            if self.x<19:
                self.x+=1
        elif cira.keys.getKey('1-Up'):
            if self.y>0:
                self.y-=1
        elif cira.keys.getKey('1-Down'):
            if self.y<22:
                self.y+=1
        pass

    # called when each frame needs to be drawn
    def draw(self):
        cira.display.clearScreen(0,0,0)
        cira.display.putPixel(self.x,self.y,self.red,self.green,self.blue)
        return
