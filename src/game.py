import pygame

class Game:
	def __init__(self, window):
		self.clock = pygame.time.Clock()
		self.currentLevel = 0
		self.gameState = 'STARTSCREEN'
		self.levelList = []
		self.levelCounter = 0
		self.enemyList = []
		self.nameList = []
		self.life = 3
		self.animation = 0
		self.animationCounter = 0
		self.window = window


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

	def getCurrentlevel(self):
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

	#def setTileSet(self):
	#Fill in with the images that are done

	def drawLives(self):
		for i in range(game.life):
			self.window.blit(game.lifeImage, (20 + i * 60, 64))		#Make sure to set the life image!!!

