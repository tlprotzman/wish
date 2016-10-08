import pygame

class Game:
	def __init__(self):
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

		self.lifeImage = pygame.image.load()
		self.waterImage = pygame.image.load()
		self.waveImage = pygame.image.load()
		self.playerBreath = pygame.image.load()
		self.playerWalk = pygame.image.load()
		self.playerJump = pygame.image.load()
		self.enemyBreath = pygame.image.load()
		self.enemyJump = pygame.image.load()


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

	def setTileSet(self):
	#Fill in with the images that are done

	def drawLives(self):
		for i in range(game.life):
			window.blit(game.lifeImage, (20 + i * 60, 64))		#Make sure to set the life image!!!

