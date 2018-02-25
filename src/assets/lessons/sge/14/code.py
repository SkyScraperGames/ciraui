from cira.ciragame import *
# this is a comment
class MyGame(CiraGame):
    # engine variables
    title = "Quick Start"

    xLower=0
    xUpper=19

    yLower=0
    yUpper=22

    # These are the variables for my "player" pixel
    x = 9
    y = 11
    red = 0
    green = 0
    blue = 255

    # These are the variables for my "chaser" pixel
    cpuX=0
    cpuY=0
    cpuRed=255
    cpuGreen=0
    cpuBlue=0

    speed = 10
    turn = 0
    speedUp = 0

    #Game over?
    gameOver = False
    messagePrinted = False

    # called once when the program starts up
    def awake(self):
        pass

    # called at the beginning of each play session
    def start(self):
        if self.gameOver:
            # These are the variables for my "player" pixel
            self.x = 9
            self.y = 11
            self.red = 0
            self.green = 0
            self.blue = 255

            # These are the variables for my "chaser" pixel
            self.cpuX=0
            self.cpuY=0
            self.cpuRed=255
            self.cpuGreen=0
            self.cpuBlue=0

            self.speed = 10
            self.turn = 0
            self.speedUp = 0

            #Game over?
            self.gameOver = False
            self.messagePrinted = False

        pass

    # called each time the frame updates
    def update(self):
        if self.gameOver:
            return

        if cira.keys.getKey('1-Left') and cira.keys.getKey('1-Up'):
            self.movePlayer(5)
        elif cira.keys.getKey('1-Left') and cira.keys.getKey('1-Down'):
            self.movePlayer(7)
        elif cira.keys.getKey('1-Right') and cira.keys.getKey('1-Up'):
            self.movePlayer(6)
        elif cira.keys.getKey('1-Right') and cira.keys.getKey('1-Down'):
            self.movePlayer(8)
        elif cira.keys.getKey('1-Left'):
            self.movePlayer(3)
        elif cira.keys.getKey('1-Right'):
            self.movePlayer(4)
        elif cira.keys.getKey('1-Up'):
            self.movePlayer(1)
        elif cira.keys.getKey('1-Down'):
            self.movePlayer(2)

        #Add 1 to turn
        self.turn += 1

        #Divide the turn by the speed
        # if there's no remainder, then move the computer pixel
        if self.turn % self.speed == 0:

            #Speed up the computer every 5 times it moves
            self.speedUp += 1
            if self.speedUp == 5 and self.speed > 1:
                self.speedUp = 0
                self.speed -= 1

            # If the computer is to the left of the player, move right
            # or if the computer is to the right of the player, move left
            self.cpuX=self.chasePlayer(self.x,self.cpuX)

            #If the computer is above the player, move down. If the computer
            # is below the player, move up.
            self.cpuY=self.chasePlayer(self.y,self.cpuY)

        #Check to see if the player has been caught
        if self.x == self.cpuX and self.y == self.cpuY:
            self.gameOver = True
        pass

    # called when each frame needs to be drawn
    def draw(self):

        if self.gameOver:
            if self.messagePrinted == False:
                cira.display.clearScreen(255,255,255)
                print "Final speed: " + str(self.speed)
                print "Score: " + str(self.turn)
                self.messagePrinted = True
            else:
                self.start()
        else:
            cira.display.clearScreen(0,0,0)
            cira.display.putPixel(self.x,self.y,self.red,self.green,self.blue)
            cira.display.putPixel(self.cpuX,self.cpuY,self.cpuRed,self.cpuGreen,
                self.cpuBlue)
        return

    def movePlayer(self,direction):
        if direction==1 or direction==5 or direction==6:
            if self.y>self.yLower:
                self.y-=1

        if direction==2 or direction==7 or direction==8:
            if self.y<self.yUpper:
                self.y+=1

        if direction==3 or direction==5 or direction==7:
            if self.x>self.xLower:
                self.x-=1

        if direction==4 or direction==6 or direction==8:
            if self.x<self.xUpper:
                self.x+=1

        return

    def chasePlayer(self,playerCoordinate,cpuCoordinate):
            if cpuCoordinate<playerCoordinate:
                return cpuCoordinate+1
            elif cpuCoordinate>playerCoordinate:
                return cpuCoordinate-1

            return cpuCoordinate
