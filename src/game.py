class Game:
    def __init__(self):
        self.clock=pygame.time.Clock()
        self.currentLevel=0
        self.gameState="STARTSCREEN"

        self.lifeImage = pygame.image.load("images/life.png")

        self.waterImage = pygame.image.load("images/water.png")

        self.waveImage = [pygame.image.load("images/wave1.png"),
                          pygame.image.load("images/wave2.png"),
                          pygame.image.load("images/wave3.png"),
                          pygame.image.load("images/wave4.png")]

        self.playerBreath = [pygame.image.load("images/player-breath1.png"),
                             pygame.image.load("images/player-breath2.png")]

        self.playerWalk = [pygame.image.load("images/player-walk1.png"),
                           pygame.image.load("images/player-walk2.png"),
                           pygame.image.load("images/player-walk3.png"),
                           pygame.image.load("images/player-walk4.png")]

        self.playerJump = pygame.image.load("images/player-jump.png")

        self.enemyBreath = [pygame.image.load("images/enemy1.png"),
                            pygame.image.load("images/enemy2.png")]
        self.enemyJump = pygame.image.load("images/enemy3.png")

        self.animation = 0
        self.animationCounter = 0
        self.levelList=[]
        self.levelCounter=0
        self.enemyList=[]
        self.nameList=[]
        self.levelTitle = Word("This is the last level!", 20, 20, 30, [255, 255, 255])
        self.bonusLife = True
        self.life = 1

    def setCurrentLevel(self, newLevel):
        self.currentLevel=newLevel

    def getCurrentLevel(self):
        return self.currentLevel

    def animate(self):
        self.animationCounter += 1
        if self.animationCounter == 7:
            self.animation += 1
            if self.animation == 4:
                self.animation = 0
            self.animationCounter = 0

    def getGameState(self):
        return self.gameState

    def setTileset(self, tileSet):
        if tileSet=="Grass":
            self.groundImage = pygame.image.load("images/ground.png")
            self.groundLImage = pygame.image.load("images/groundl.png")
            self.groundRImage = pygame.image.load("images/groundr.png")
            self.dirtImage = pygame.image.load("images/dirt.png")
        elif tileSet=="Snow":
            self.groundImage = pygame.image.load("images/snow.png")
            self.groundLImage = pygame.image.load("images/snowl.png")
            self.groundRImage = pygame.image.load("images/snowr.png")
            self.dirtImage = pygame.image.load("images/dirt.png")
        elif tileSet=="Mountain":
            self.groundImage = pygame.image.load("images/mountain.png")
            self.groundLImage = pygame.image.load("images/mountainL.png")
            self.groundRImage = pygame.image.load("images/mountainR.png")
            self.dirtImage = pygame.image.load("images/mountain.png")


    def setGameState(self, newGameState):
        self.gameState=newGameState

    def drawLives(self):
        for i in range (0, game.life):
            window.blit(game.lifeImage, (20+ i*64, 64))