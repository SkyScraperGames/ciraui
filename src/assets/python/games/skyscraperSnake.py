from cira.ciragame import *
from random import randint

class MyGame(CiraGame):
    # It's a snaaake!
    gameTitle = "Snake"

    # called once when the program first initializes
    def awake(self):
        print("Snake!  Use WASD to collect treats and avoid the walls!")

    # called at the beginning of each new play session
    def start(self):
        self.player = Player()
        self.lastMove = 'UP'

        self.borderColor = (0, 255, 0)
        self.headColor = (255, 255, 255)
        self.happyColor = (100, 200, 255)
        self.deathColor = (255, 0, 0)
        self.bodyColor = self.happyColor

        self.speedCounter = 4
        self.speedCountdown = self.speedCounter

        self.treatCounter = 30
        self.treatCountdown = self.treatCounter
        self.treats = []
        self.treatColor = (255, 255, 0)

        self.deathCountdown = 12
        self.deathTimer = 0

        print("New Game!")
        self.printScore("Score:")

    # called each frame before the scene draws
    def update(self):
        # handle death
        if self.deathTimer > 0:
            self.deathTimer -= 1
            if self.deathTimer <= 0:
                self.reset()
            return

        # handle input
        if cira.keys.getKey('1-Up'):
            if self.lastMove is not 'DOWN':
                self.player.setFace('UP')
        if cira.keys.getKey('1-Right'):
            if self.lastMove is not 'LEFT':
                self.player.setFace('RIGHT')
        if cira.keys.getKey('1-Down'):
            if self.lastMove is not 'UP':
                self.player.setFace('DOWN')
        if cira.keys.getKey('1-Left'):
            if self.lastMove is not 'RIGHT':
                self.player.setFace('LEFT')

        # detect collisions
        head = self.player.head
        if head[0] <= 0 or head[0] >= cira.display.getWidth() - 1:
            self.die()
            return
        if head[1] <= 0 or head[1] >= cira.display.getHeight() - 1:
            self.die()
            return
        if self.player.isBody(head):
            self.die()
            return

        # player move
        self.speedCountdown -= 1
        if self.speedCountdown <= 0:
            shouldGrow = False
            if cira.keys.getKey('space'):
                shouldGrow = True
            self.lastMove = self.player.moveForward(self.treats)
            self.speedCountdown = self.speedCounter

        # treats!
        self.treatCountdown -= 1
        if self.treatCountdown <= 0:
            newTreatX = randint(1, cira.display.getWidth() - 2)
            newTreatY = randint(1, cira.display.getHeight() - 2)
            self.treats.append((newTreatX, newTreatY))
            self.treatCountdown = self.treatCounter

    # called when each new frame needs to be drawn
    def draw(self):
        cira.display.clearScreen(0, 0, 0)
        # draw arena border
        for col in range(cira.display.getWidth()):
            cira.display.putPixel(col, 0, self.borderColor[0], self.borderColor[1], self.borderColor[2])
            cira.display.putPixel(col, cira.display.getHeight() - 1, self.borderColor[0], self.borderColor[1], self.borderColor[2])
        for row in range(cira.display.getHeight()):
            cira.display.putPixel(0, row, self.borderColor[0], self.borderColor[1], self.borderColor[2])
            cira.display.putPixel(cira.display.getWidth() - 1, row, self.borderColor[0], self.borderColor[1], self.borderColor[2])
        # draw treats
        for treat in self.treats:
            cira.display.putPixel(treat[0], treat[1], self.treatColor[0], self.treatColor[1], self.treatColor[2])
        # draw player
        self.player.draw(self.headColor, self.bodyColor)

    # end the game
    def die(self):
        self.deathTimer = self.deathCountdown
        self.bodyColor = self.deathColor
        print("")
        self.printScore("Final Score:")
        print("")

    # prints the score
    def printScore(self, msg):
        print(msg + " " + str(self.player.treatsEaten))


class Player():
    def __init__(self):
        self.head = (10, 10)
        self.face = 'UP'
        self.body = []
        self.treatsEaten = 0

  # moves the player forward one space, possibly eating a treat
    def moveForward(self, treats):
        self.body.append(self.head)

        if self.face is 'UP':
            if self.head[1] > 0:
                self.head = (self.head[0], self.head[1] - 1)
        elif self.face is 'RIGHT':
            if self.head[0] < cira.display.getWidth() - 1:
                self.head = (self.head[0] + 1, self.head[1])
        elif self.face is 'DOWN':
            if self.head[1] < cira.display.getHeight() - 1:
                self.head = (self.head[0], self.head[1] + 1)
        elif self.face is 'LEFT':
            if self.head[0] > 0:
                self.head = (self.head[0] - 1, self.head[1])
        else:
            raise Exception("Invalid face")

        ateTreat = False
        for treat in treats:
            if self.head[0] is treat[0] and self.head[1] is treat[1]:
                ateTreat = True
                self.treatsEaten += 1
                treats.remove(treat)
        if not ateTreat:
            self.body.pop(0)

        return self.face

  # returns true if the point is a member of the snake's body
    def isBody(self, point):
        for bodyX, bodyY in self.body:
            if point[0] is bodyX and point[1] is bodyY:
                return True
        return False

  # set the direction of the player
    def setFace(self, face):
        self.face = face

  # draw the player snake
    def draw(self, headColor, bodyColor):
        for bx, by in self.body:
            cira.display.putPixel(bx, by,  bodyColor[0],  bodyColor[1],  bodyColor[2])
        cira.display.putPixel(self.head[0], self.head[1], headColor[0],  headColor[1],  headColor[2])
