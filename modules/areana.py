from random import randint

class Areana:

    def __init__(self, pygame, sys, size):
        self.pygame = pygame
        self.sys = sys
        self.size = size

        # colors
        self.bgColor = (235, 201, 52) # Background color of pygame window

        pygame.init()

        self.screen = self.pygame.display.set_mode(self.size)
        self.pygame.display.set_caption("Paratha Tha Koe") # delete old window and make new

        # create objects
        rawPlayerImg = self.pygame.image.load('./img/MainCharacter.png')
        self.player = self.pygame.transform.scale(rawPlayerImg, (200, 200))
        self.playerX = 0
        self.playerY = 100
        self.playerSpeed = 20

        RawBombImg = self.pygame.image.load('./img/bomb.png')
        self.bomb = self.pygame.transform.scale(RawBombImg, (20, 20))
        self.bombX = 500
        self.bombY = []
        self.bombSpeed = 0.3
        self.createBombs()


    def createBombs(self):
        self.number_of_bombs = randint(1, 5)
        for i in range(0, self.number_of_bombs):
            self.bombY.append(randint(0, 480))


    def areana(self):
        while True:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT: self.sys.exit()

                # move player
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_w or event.key == self.pygame.K_UP:
                        self.playerY -= self.playerSpeed # go up
                        # upper border = -20
                        if self.playerY <= -20:
                            self.playerY = 290


                    if event.key == self.pygame.K_s or event.key == self.pygame.K_DOWN:
                        self.playerY += self.playerSpeed # go down
                        # down border = 290
                        if self.playerY >= 290:
                            self.playerY = -20

            self.screen.fill(self.bgColor)
            self.screen.blit(self.player, (0, self.playerY))

            # swapn multiple bombs
            if self.bombX <= 0: # empty bombY and create new
                self.bombY = []
                self.bombX = 500
                self.createBombs()

            for i in range(0, self.number_of_bombs):
                self.screen.blit(self.bomb, (self.bombX, self.bombY[i]))
                self.bombX -= self.bombSpeed

            # check if bomb hit the player
            for i in range(0, self.number_of_bombs):
                # in self.playerY + 20 - 20 is the height of bomb
                # in self.playerY + 200 - 200 is the height of plyer
                if self.bombY[i] >= self.playerY + 20 and self.bombY[i] <= self.playerY + 200: # is bombY match
                    if self.bombX == 103.99999999998614:
                        # Lose
                        return 'showMsg'


            self.pygame.display.flip()
