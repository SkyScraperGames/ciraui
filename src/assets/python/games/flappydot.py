from random import randint

from cira.ciragame import *


class MyGame(CiraGame):
    # engine variables
    gameTitle = "Flappy Dot"
    gameAuthor = "Gray"
    gameTime = 40

    # game variables
    GRAVITY = -0.08
    JUMP = .80
    verticalVelocity = 0
    TERMINALVELOCITY = -.24

    player = None
    playerColor = (0, 128, 255)
    deathColor = (255, 0, 0)
    pipeGap = 8
    pipeShiftInterval = 4
    pipeSpawnInterval = 60
    pipeSpeedupInterval = 13
    pipeFrequencyInterval = 8
    pipeShiftTimer = pipeShiftInterval
    pipeSpawnTimer = pipeSpawnInterval
    pipeSpeedupTimer = pipeSpeedupInterval
    pipeFrequencyTimer = pipeFrequencyInterval

    minShiftInterval = 2
    minSpawnInterval = 20

    pipes = []
    deathTimer = 0
    deathCountdown = 60

    # called once when the program first initializes
    def awake(self):
        pass

    # called at the beginning of each new play session
    def start(self):
        self.player = [3.0, 10.0]
        self.verticalVelocity = self.JUMP;
        self.playerColor = (0, 128, 255)

        self.pipeShiftInterval = 4
        self.pipeSpawnInterval = 60
        self.pipeSpeedupInterval = 13
        self.pipeFrequencyInterval = 8
        self.pipeSpawnTimer = self.pipeSpawnInterval
        self.pipeShiftTimer = self.pipeShiftInterval
        self.pipeSpeedupTimer = self.pipeShiftInterval
        self.pipeFrequencyTimer = self.pipeFrequencyInterval
        self.pipes = []

        self.deathTimer = 0

    # called each update frame
    def update(self):

        # handle flappy movement
        self.verticalVelocity += self.GRAVITY
        self.player[1] = max(0, min(self.player[1] - self.verticalVelocity, cira.display.getHeight() - 1))

        # check for collisions
        for pipe in self.pipes:
            if pipe.doesCollide(self.player):
                self.player[0] -= 1
                self.die()
        if self.player[1] >= cira.display.getHeight() - 1 and self.deathTimer <= 0:
            self.verticalVelocity = self.JUMP
            self.die()

        # handle death
        if self.deathTimer > 0:
            self.deathTimer -= 1
            if self.deathTimer <= 0:
                cira.display.clearScreen(255, 0, 0)
                self.reset()
            return

        # player input
        if cira.keys.getKey('1-Up'):
            self.verticalVelocity = self.JUMP

        # move and remove pipes
        self.pipeShiftTimer -= 1
        if self.pipeShiftTimer <= 0:
            for pipe in self.pipes:
                pipe.shift()
            self.pipeShiftTimer = self.pipeShiftInterval

        # generate pipes
        self.pipeSpawnTimer -= 1
        if self.pipeSpawnTimer <= 0:
            newPipe = Pipe(self.pipeGap)
            self.pipes.append(newPipe)
            self.pipeSpawnTimer = self.pipeSpawnInterval
            self.pipeSpeedupTimer -= 1
            self.pipeFrequencyTimer -= 1

        # speed things up
        if self.pipeSpeedupTimer <= 0:
            self.pipeShiftInterval = max(self.minShiftInterval, self.pipeShiftInterval - 1)
            self.pipeSpeedupTimer = self.pipeSpeedupInterval
        if self.pipeFrequencyTimer <= 0:
            self.pipeSpawnInterval = max(self.minSpawnInterval, self.pipeSpawnInterval - 8)
            self.pipeFrequencyTimer = self.pipeFrequencyInterval

    def draw(self):
        cira.display.clearScreen(0, 0, 0)
        for pipe in self.pipes:
            pipe.draw()
        for col in xrange(cira.display.getWidth()):
            cira.display.putPixel(col, cira.display.getHeight() - 1, 0, 255, 0)
        cira.display.putPixel(int(self.player[0]), int(self.player[1]), self.playerColor[0], self.playerColor[1],
                              self.playerColor[2])

    def die(self):
        self.playerColor = self.deathColor
        self.deathTimer = self.deathCountdown


class Pipe:
    def __init__(self, gap):
        self.gap = gap
        self.column = cira.display.getWidth() - 1
        self.row = randint(1, cira.display.getHeight() - 2 - gap)

    def doesCollide(self, point):
        if self.column >= -1:
            if self.column <= int(point[0]) <= self.column + 1:
                if not self.row < int(point[1]) < self.row + self.gap:
                    return True
        return False

    def shift(self):
        if self.column >= -1:
            self.column -= 1

    def draw(self):
        if self.column >= -1:
            for row in xrange(cira.display.getHeight()):
                if self.column > -1:
                    if not self.row < row < self.row + self.gap:
                        cira.display.putPixel(self.column, row, 0, 255, 0)
                if self.column < cira.display.getWidth() - 1:
                    if not self.row < row < self.row + self.gap:
                        cira.display.putPixel(self.column + 1, row, 0, 200, 60)
