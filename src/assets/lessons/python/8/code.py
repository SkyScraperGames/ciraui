from cira.ciragame import *
import random

class MyGame(CiraGame):

    # Player start location
    # the 'playerX' and 'playerY' variables determine the starting X and Y coordinates
    playerX = 10
    playerY = 10

    # Movement
    # the 'speed' variable determines how many pixels your dot will travel when a key is pressed
    speed = 1

    # Box Color
    # squareRed, Green, and Blue are variables that determine the color of the box
    squareRed = 0
    squareGreen = 255
    squareBlue = 0

    # this section draws the box
    square = []

    def makeSquare(self):
        self.XMIN = 1
        self.XMAX = 18
        self.YMIN = 1
        self.YMAX = 21

        locationX = random.randrange(self.XMIN, self.XMAX)
        locationY = random.randrange(self.YMIN, self.YMAX)

        self.square.append([locationX, locationY])
        self.square.append([locationX+1, locationY])
        self.square.append([locationX+1, locationY+1])
        self.square.append([locationX, locationY+1])
        self.square.append([locationX-1,locationY+1])
        self.square.append([locationX-1,locationY])
        self.square.append([locationX-1,locationY-1])
        self.square.append([locationX,locationY-1])
        self.square.append([locationX+1,locationY-1])

    def drawSquare(self):
        for i in self.square:
            cira.display.putPixel(i[0], i[1], self.squareRed, self.squareGreen, self.squareBlue)

    def winGame(self):
        center = self.square[0]
        for square in self.square:
            if square[0] == self.playerX and square[1] == self.playerY:
                print "Congratulations! You won!"
                return True

    # called once when the program starts up
    def awake(self):
        print("Move with WASD to get to the square!")

    # called at the beginning of each play session
    def start(self):
        self.makeSquare()

        self.won = False

    # called each time the frame updates
    def update(self):
        # this conditional statement determines if a new button was pressed and sets
        # the lastKey value to whatever button was most recently pressed
        xLim = 19
        yLim = 22
        if cira.keys.getKey("1-Left"):
            if self.playerX > 0:
                self.playerX -= self.speed
        elif cira.keys.getKey("1-Right"):
            if self.playerX < xLim:
                self.playerX += self.speed
        elif cira.keys.getKey("1-Up"):
            if self.playerY > 0:
                self.playerY -= self.speed
        elif cira.keys.getKey("1-Down"):
            if self.playerY < yLim:
                self.playerY += self.speed

        if self.playerY <= 0:
            self.playerY = 0
        if self.playerY >= yLim:
            self.playerY = yLim
        if self.playerX <= 0:
            self.playerX = 0
        if self.playerX >= xLim:
            self.playerX = xLim

        if not self.won:
            self.won = self.winGame()

    # called when each frame needs to be drawn
    def draw(self):
        cira.display.clearScreen(0, 0, 0)

        self.drawSquare()
        # Here is where your playerX and playerY variables will be used by the game
        # Replace X and Y with self.playerX and playerY and R G B with color values
        cira.display.putPixel(self.playerX, self.playerY, 255, 255, 255)
