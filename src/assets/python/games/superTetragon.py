from cira.ciragame import *
from random import randint

class MyGame(CiraGame):
    # engine variables
    gameTitle = "Super Tetragon"

    # called once when the program first initializes
    def awake(self):
        print("Super Tetragon!  Use left & right to avoid the walls!")
        pass

    # called at the beginning of each new play session
    def start(self):
        self.player = Player()

        self.wallSpawnInterval = 35
        self.minSpawnInterval = 12
        self.wallShiftInterval = 4
        self.minShiftInterval = 2
        self.wallSpeedupInterval = 25
        self.wallFrequencyInterval = 1

        self.wallSpawnTimer = self.wallSpawnInterval
        self.wallShiftTimer = self.wallShiftInterval
        self.wallSpeedupTimer = self.wallSpeedupInterval
        self.wallFrequencyTimer = self.wallFrequencyInterval

        self.walls = []
        self.wallColor = (255, 0, 0)

        self.healthColor = (255, 255, 0)
        self.happyColor = (100, 200, 255)
        self.playerColor = self.happyColor

        self.deathTimer = 0
        self.deathColor = (255, 255, 0)
        self.deathCountdown = 12

        self.score = 0
        print("New Game: Health = " + str(self.player.health))
        self.printScore("Score:")

    # called each update frame
    def update(self):
        # handle death
        if self.deathTimer > 0:
            self.deathTimer -= 1
            if self.deathTimer <= 0:
                if self.player.health <= 0:
                    print("")
                    self.printScore("Final Score:")
                    print("")
                    self.reset()
                # shift the walls in, but don't count it as a score
                self.shiftWalls(False)
                self.playerColor = self.happyColor
            return

        # player input
        if cira.keys.getKey("1-Left"):
            self.player.moveLeft()
        if cira.keys.getKey("1-Right"):
            self.player.moveRight()

        # detect collisions
        for wall in self.walls:
            if wall.doesCollide(self.player.x, self.player.y):
                self.takeDamage()
                return

        # move walls
        self.wallShiftTimer -= 1
        if self.wallShiftTimer <= 0:
            # shift the walls in and count any resulting score
            self.shiftWalls(True)
            self.wallShiftTimer = self.wallShiftInterval

        # generate walls
        self.wallSpawnTimer -= 1
        if self.wallSpawnTimer <= 0:
            randWalls = self.randomWall()
            newWall = Wall(randWalls[0], randWalls[1], randWalls[2], randWalls[3])
            self.walls.append(newWall)
            self.wallSpawnTimer = self.wallSpawnInterval
            self.wallSpeedupTimer -= 1
            self.wallFrequencyTimer -= 1

        # speed things up
        if self.wallSpeedupTimer <= 0:
            self.wallShiftInterval = max(self.minShiftInterval, self.wallShiftInterval - 1)
            self.wallSpeedupTimer = self.wallSpeedupInterval
        if self.wallFrequencyTimer <= 0:
            self.wallSpawnInterval = max(self.minSpawnInterval, self.wallSpawnInterval - 1)
            self.wallFrequencyTimer = self.wallFrequencyInterval

    # called when each new frame needs to be drawn
    def draw(self):
        cira.display.clearScreen(0, 0, 0)
        # draw walls and center column
        for wall in self.walls:
            wall.draw(self.wallColor)
        cira.display.putPixel(9, 10, self.wallColor[0], self.wallColor[1], self.wallColor[2])
        cira.display.putPixel(9, 11, self.wallColor[0], self.wallColor[1], self.wallColor[2])
        cira.display.putPixel(10, 10, self.wallColor[0], self.wallColor[1], self.wallColor[2])
        cira.display.putPixel(10, 11, self.wallColor[0], self.wallColor[1], self.wallColor[2])
        # draw player
        self.player.draw(self.playerColor, self.healthColor)

    # handle player death
    def takeDamage(self):
        self.playerColor = self.deathColor
        self.deathTimer = self.deathCountdown
        self.player.takeDamage()

    # shift all the walls one space in
    def shiftWalls(self, shouldScore):
        for wall in self.walls:
            if wall.shift() and shouldScore:
                self.score += 1
                self.printScore("Score:")

    # return a n length list of unique elements chosen from the population sequence
    def sample(self, population, n):
        ret = []
        if n > len(population):
            raise Exception("Cannot select more items than are contained in the population")
        for i in range(n):
            nextIndex = randint(0, len(population) - 1)
            nextItem = population[nextIndex]
            ret.append(nextItem)
            population.remove(nextItem)
        return ret

    # generate a random 1-to-3 section wall
    def randomWall(self):
        ret = [False] * 4
        numWalls = randint(1, 3)
        samples = self.sample(range(4), numWalls)
        for s in samples:
            ret[s] = True
        return ret

    # prints the score
    def printScore(self, msg):
        print(msg + " " + str(self.score))


class Player:
    TOP = 9
    LEFT = 8
    BOTTOM = TOP + 3
    RIGHT = LEFT + 3

    def __init__(self):
        self.health = 3
        self.x = 9
        self.y = 9
        self.r = 100
        self.g = 200
        self.b = 255
        self.face = 'UP'

    def moveLeft(self):
        if self.face == 'UP':
            if self.x > self.LEFT:
                self.x -= 1
            else:
                self.y += 1
                self.face = 'LEFT'
            pass
        elif self.face == 'RIGHT':
            if self.y > self.TOP:
                self.y -= 1
            else:
                self.x -= 1
                self.face = 'UP'
            pass
        elif self.face == 'DOWN':
            if self.x < self.RIGHT:
                self.x += 1
            else:
                self.y -= 1
                self.face = 'RIGHT'
            pass
        elif self.face == 'LEFT':
            if self.y < self.BOTTOM:
                self.y += 1
            else:
                self.x += 1
                self.face = 'DOWN'
            pass
        else:
            raise Exception("illegal direction")

    def moveRight(self):
        if self.face == 'UP':
            if self.x < self.RIGHT:
                self.x += 1
            else:
                self.y += 1
                self.face = 'RIGHT'
            pass
        elif self.face == 'RIGHT':
            if self.y < self.BOTTOM:
                self.y += 1
            else:
                self.x -= 1
                self.face = 'DOWN'
            pass
        elif self.face == 'DOWN':
            if self.x > self.LEFT:
                self.x -= 1
            else:
                self.y -= 1
                self.face = 'LEFT'
            pass
        elif self.face == 'LEFT':
            if self.y > self.TOP:
                self.y -= 1
            else:
                self.x += 1
                self.face = 'UP'
            pass
        else:
            raise Exception("illegal direction")

    def takeDamage(self):
        self.health -= 1
        print("Ouch! Health = " + str(self.health))

    def draw(self, color, healthColor):
        # draw player dot
        cira.display.putPixel(self.x, self.y, color[0], color[1], color[2])
        # draw player health
        for col in range(cira.display.getWidth() - self.health, cira.display.getWidth()):
            cira.display.putPixel(col, cira.display.getHeight() - 1, healthColor[0], healthColor[1], healthColor[2])


class Wall():
    def __init__(self, up, right, down, left):
        self.distance = 10
        self.faces = {'UP':up, 'RIGHT':right, 'DOWN':down, 'LEFT':left}

    def doesCollide(self, x, y):
        if self.distance is not 1:
            return False
        if self.faces['UP'] and y is 9:
            return True
        if self.faces['RIGHT'] and x is 11:
            return True
        if self.faces['DOWN'] and y is 12:
            return True
        if self.faces['LEFT'] and x is 8:
            return True
        return False

    def shift(self):
        if self.distance > 0:
            self.distance -= 1
            if self.distance is 0:
                return True
        return False

    def draw(self, color):
        if self.distance > 0:
            top = 10 - self.distance
            right = 10 + self.distance
            bottom = 11 + self.distance
            left = 9 - self.distance
            # draw top wall
            if self.faces['UP']:
                self.drawHorizontal(top, left, right, color)
            # draw right wall
            if self.faces['RIGHT']:
                self.drawVertical(right, top, bottom, color)
            # draw bottom wall
            if self.faces['DOWN']:
                self.drawHorizontal(bottom, left, right, color)
            # draw left wall
            if self.faces['LEFT']:
                self.drawVertical(left, top, bottom, color)

    def drawHorizontal(self, y, startX, endX, color):
        if y < 0 or y >= cira.display.getHeight():
            return
        if startX < 0:
            startX = 0
        if endX >= cira.display.getWidth():
            endX = cira.display.getWidth() - 1
        for col in range(startX, endX + 1):
            cira.display.putPixel(col, y, color[0], color[1], color[2])

    def drawVertical(self, x, startY, endY, color):
        if x < 0 or x >= cira.display.getWidth():
            return
        if startY < 0:
            startY = 0
        if endY >= cira.display.getHeight():
            endY = cira.display.getHeight() - 1
        for row in range(startY, endY + 1):
            cira.display.putPixel(x, row, color[0], color[1], color[2])
