import pygame

class Game:
	def __init__(self, window, screenHeight, screenWidth):
		self.clock = pygame.time.Clock()
		self.currentLevel = 0
		self.gameState = 'PLAYING'
		self.levelList = []
		self.levelCounter = 0
		self.enemyList = []
		self.nameList = []
		self.life = 3
		self.animation = 0
		self.animationCounter = 0
		self.window = window
		self.screenHeight
		self.screenWidth


		self.lifeImage = pygame.image.load("../images/life.png")

		self.waterImage = pygame.image.load("../images/water.png")

		self.waveImage = [pygame.image.load("../images/wave1.png"),
						  pygame.image.load("../images/wave2.png"),
						  pygame.image.load("../images/wave3.png"),
						  pygame.image.load("../images/wave4.png")]

		self.playerBreath = [pygame.image.load("../images/player-breath1.png"),
							 pygame.image.load("../images/player-breath2.png")]

		self.playerWalk = [pygame.image.load("../images/player-walk1.png"),
						   pygame.image.load("../images/player-walk2.png"),
						   pygame.image.load("../images/player-walk3.png"),
						   pygame.image.load("../images/player-walk4.png")]

		self.playerJump = pygame.image.load("../images/player-jump.png")

		self.enemyBreath = [pygame.image.load("../images/enemy1.png"),
							pygame.image.load("../images/enemy2.png")]
		self.enemyJump = pygame.image.load("../images/enemy3.png")



	def setCurrentLevel(self, newLevel):
		self.currentLevel = newLevel

	def getCurrentLevel(self):
		return self.currentLevel

	def animate(self):
		self.animationCounter += 1
		if self.animationCounter == 7:
			self.animation += 1
			if self.animation == 4:
				self.animation = 0
			self.animationCounter = 0

	def setGameState(self, newGameState):
		self.gameState = newGameState

	def getGameState(self):
		return self.gameState

	def setTileset(self, tileSet):
		if tileSet=="Grass":
			self.groundImage = pygame.image.load("../images/ground.png")
			self.groundLImage = pygame.image.load("../images/groundl.png")
			self.groundRImage = pygame.image.load("../images/groundr.png")
			self.dirtImage = pygame.image.load("../images/dirt.png")
		elif tileSet=="Snow":
			self.groundImage = pygame.image.load("../images/snow.png")
			self.groundLImage = pygame.image.load("../images/snowl.png")
			self.groundRImage = pygame.image.load("../images/snowr.png")
			self.dirtImage = pygame.image.load("../images/dirt.png")
		elif tileSet=="Mountain":
			self.groundImage = pygame.image.load("../images/mountain.png")
			self.groundLImage = pygame.image.load("../images/mountainL.png")
			self.groundRImage = pygame.image.load("../images/mountainR.png")
			self.dirtImage = pygame.image.load("../images/mountain.png")

	def drawLives(self):
		for i in range(self.life):
			self.window.blit(self.lifeImage, (20 + i * 60, 64))		#Make sure to set the life image!!!

