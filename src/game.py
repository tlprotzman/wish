import pygame, sys, timeit
from word import Word
from particles import Particle
pygame.font.init()
import random

class Game:
	def __init__(self, window, screenHeight, screenWidth, playSoundEffects = False):
		self.soundEffects = playSoundEffects
		self.clock = pygame.time.Clock()
		self.currentLevel = 0
		self.gameState = 'MAINMENU'
		self.levelList = []
		self.levelCounter = 0
		self.enemyList = []
		self.genieList = []
		self.nameList = []
		self.particles = []
		self.wishTable = {} # this should be overwritten
		self.life = 0
		self.coins = 0
		self.maxCoins = 0
		self.countMaxCoins = 0
		self.animation = 0
		self.animationCounter = 0
		self.window = window
		self.screenHeight = screenHeight
		self.screenWidth = screenWidth
		self.camera_x = 0
		self.camera_y = 0
		self.close_parallax_scale = .25
		self.far_parallax_scale = .1
		self.genieFont = pygame.font.Font("../fonts/joystixMonospace.ttf", 18)
		self.currentCharacter = 'player'
		self.updateCounter = 0 # this is for speed runs, it should restart counting after you press enter
		self.speedRunTimer = 0

		#SOUND
		if self.soundEffects:
			self.coinEffect = pygame.mixer.Sound("../sound/coin.wav")
			self.ostrichEffect = pygame.mixer.Sound('../sound/ostrich.wav')
			self.hoorayEffect = pygame.mixer.Sound('../sound/hooray.wav')
			self.wishEffect = pygame.mixer.Sound('../sound/wish.wav')

		self.UIImage = pygame.image.load("../images/ui.png")
		self.speechImage = pygame.image.load("../images/speech.png")
		self.speechLImage = pygame.transform.flip(self.speechImage, True, False)

		self.lifeImage = [pygame.image.load("../images/life.png"),
						  pygame.image.load("../images/life-2.png")]

		self.waterImage = pygame.image.load("../images/water.png")

		self.coinImage = [pygame.image.load("../images/coin-1.png"),
						  pygame.image.load("../images/coin-2.png"),
						  pygame.image.load("../images/coin-3.png"),
						  pygame.image.load("../images/coin-2.png")]
						  
		self.healthImage = pygame.image.load("../images/life.png")

		self.waveImage = [pygame.image.load("../images/wave1.png"),
						  pygame.image.load("../images/wave2.png"),
						  pygame.image.load("../images/wave3.png"),
						  pygame.image.load("../images/wave4.png")]

		self.playerBreath = [pygame.image.load("../images/player-idle-1.png"),
							 pygame.image.load("../images/player-idle-2.png"),
							 pygame.image.load("../images/player-idle-3.png"),
							 pygame.image.load("../images/player-idle-4.png")]

		self.playerWalk = [pygame.image.load("../images/player-run-1.png"),
						   pygame.image.load("../images/player-run-2.png"),
						   pygame.image.load("../images/player-run-3.png"),
						   pygame.image.load("../images/player-run-4.png")]
						   
		self.playerFight = [pygame.image.load("../images/player-fight-1.png"),
						    pygame.image.load("../images/player-fight-2.png"),
						    pygame.image.load("../images/player-fight-3.png"),
						    pygame.image.load("../images/player-fight-3.png"),
						    pygame.image.load("../images/player-fight-4.png")]
	
		self.playerJump = pygame.image.load("../images/player-run-1.png")


		self.knifeFight  = [pygame.image.load("../images/weapon-attack-1.png"),
						    pygame.image.load("../images/weapon-attack-2.png"),
						    pygame.image.load("../images/weapon-attack-3.png"),
						    pygame.image.load("../images/weapon-attack-4.png"),
						    pygame.image.load("../images/weapon-attack-5.png")]
						   
		self.torchImage = [pygame.image.load("../images/torch-1.png"),
						   pygame.image.load("../images/torch-2.png"),
						   pygame.image.load("../images/torch-3.png"),
						   pygame.image.load("../images/torch-4.png")]

		self.knife = [pygame.image.load("../images/weapon-1.png"),
					  pygame.image.load("../images/weapon-2.png")]
					  
		self.gold =   [pygame.image.load("../images/gold-1.png"),
					  pygame.image.load("../images/gold-2.png")]
					  
		self.goldFight = [pygame.image.load("../images/gold-attack-1.png"),
						    pygame.image.load("../images/gold-attack-2.png"),
						    pygame.image.load("../images/gold-attack-3.png"),
						    pygame.image.load("../images/gold-attack-4.png"),
						    pygame.image.load("../images/gold-attack-2.png")]
							
		self.frying =   [pygame.image.load("../images/frying-1.png"),
					  pygame.image.load("../images/frying-2.png")]
					  
		self.fryingFight = [pygame.image.load("../images/frying-attack-1.png"),
						    pygame.image.load("../images/frying-attack-2.png"),
						    pygame.image.load("../images/frying-attack-3.png"),
						    pygame.image.load("../images/frying-attack-4.png"),
						    pygame.image.load("../images/frying-attack-2.png")]
		
		self.weapon = self.knife
		self.weaponFight = self.knifeFight
		
		

		self.enemyBreath = [pygame.image.load("../images/ostrich-idle-1.png"),
							pygame.image.load("../images/ostrich-idle-2.png"),
							pygame.image.load("../images/ostrich-idle-3.png"),
							pygame.image.load("../images/ostrich-idle-4.png")]

		self.enemyJump = pygame.image.load("../images/ostrich-idle-1.png")

		self.enemyRun =    [pygame.image.load("../images/ostrich-run-1.png"),
							pygame.image.load("../images/ostrich-run-2.png"),
							pygame.image.load("../images/ostrich-run-3.png"),
							pygame.image.load("../images/ostrich-run-4.png")]
							
		self.batFly =      [pygame.image.load("../images/bat-fly-1.png"),
							pygame.image.load("../images/bat-fly-2.png"),
							pygame.image.load("../images/bat-fly-3.png"),
							pygame.image.load("../images/bat-fly-4.png")]
							
		self.batHang = pygame.image.load("../images/bat-hang-1.png")
		
		self.farParallax = pygame.image.load("../images/blue_parallax.png")
		self.closeParallax = pygame.image.load("../images/color_parallax.png")

		# Genie images:
		self.genieAppearR = [pygame.image.load("../images/genie-appear-1R.png"),
							pygame.image.load("../images/genie-appear-2R.png"),
							pygame.image.load("../images/genie-appear-3R.png"),
							pygame.image.load("../images/genie-appear-4R.png"),]
		self.genieIdleR = [pygame.image.load("../images/genie-idle-1R.png"),
							pygame.image.load("../images/genie-idle-2R.png"),
							pygame.image.load("../images/genie-idle-3R.png"),
							pygame.image.load("../images/genie-idle-4R.png"),]
		self.genieLampR = pygame.image.load("../images/lampR.png")
		self.genieAppearL = [pygame.image.load("../images/genie-appear-1L.png"),
							pygame.image.load("../images/genie-appear-2L.png"),
							pygame.image.load("../images/genie-appear-3L.png"),
							pygame.image.load("../images/genie-appear-4L.png"),]
		self.genieIdleL = [pygame.image.load("../images/genie-idle-1L.png"),
							pygame.image.load("../images/genie-idle-2L.png"),
							pygame.image.load("../images/genie-idle-3L.png"),
							pygame.image.load("../images/genie-idle-4L.png"),]
		self.genieLampL = pygame.image.load("../images/lampL.png")
		
		self.topHat = pygame.image.load("../images/topHat.png")
		self.fireman = pygame.image.load("../images/fireHat.png")
		self.turban = pygame.image.load("../images/beanie.png")
		
		self.hatImage = self.topHat

		self.particles = []
		
	def addParticle(self, x, y, color, lifespan):
		self.particles += [Particle(self, self.window, x, y, color, lifespan)]
		
	def setPlayerType(self, playerType):
		if playerType == 'simon':
			self.currentCharacter = 'simon'
			self.playerBreath = [pygame.image.load("../images/player-breath1.png"),
								 pygame.image.load("../images/player-breath2.png"),
								 pygame.image.load("../images/player-breath1.png"),
								 pygame.image.load("../images/player-breath2.png")]

			self.playerWalk = [pygame.image.load("../images/player-walk1.png"),
							   pygame.image.load("../images/player-walk2.png"),
							   pygame.image.load("../images/player-walk3.png"),
							   pygame.image.load("../images/player-walk4.png")]
							   
			self.playerFight = [pygame.image.load("../images/player-fight-1.png"),
							    pygame.image.load("../images/player-fight-2.png"),
							    pygame.image.load("../images/player-fight-3.png"),
							    pygame.image.load("../images/player-fight-3.png"),
							    pygame.image.load("../images/player-fight-4.png")]

			self.playerJump = pygame.image.load("../images/player-jump.png")


		elif playerType == 'ostrich':
			self.currentCharacter = 'ostrich'
			self.playerBreath = [pygame.image.load("../images/ostrich-idle-1.png"),
								 pygame.image.load("../images/ostrich-idle-2.png"),
								 pygame.image.load("../images/ostrich-idle-3.png"),
								 pygame.image.load("../images/ostrich-idle-4.png")]

			self.playerWalk = [pygame.image.load("../images/ostrich-run-1.png"),
							   pygame.image.load("../images/ostrich-run-2.png"),
							   pygame.image.load("../images/ostrich-run-3.png"),
							   pygame.image.load("../images/ostrich-run-4.png")]
							   
			self.playerFight = [pygame.image.load("../images/player-fight-1.png"),
							    pygame.image.load("../images/player-fight-2.png"),
							    pygame.image.load("../images/player-fight-3.png"),
							    pygame.image.load("../images/player-fight-3.png"),
							    pygame.image.load("../images/player-fight-4.png")]

			self.playerJump = pygame.image.load("../images/ostrich-run-1.png")

	def makeParticles(self, x, y, color, count, lifespan, velocity=20):
		for i in range (0, count):
			if len(self.particles) < 250:
				vel = velocity + random.randint(-5, 5)
				self.particles.append(Particle(self, self.window, x, y, color, lifespan, vel))
			
	def setCurrentLevel(self, newLevel):
		self.currentLevel = newLevel

	def getCurrentLevel(self):
		return self.currentLevel

	def getLevelIndex(self):
		return self.levelCounter

	def progressALevel(self):
		self.levelCounter += 1
		if self.levelCounter == 6:
			print("Updates in the game:", self.updateCounter)
			print("(an HEAVILY BIASED count of speedrunning time)")
			print("YOUR TIME IS:", timeit.default_timer() - self.speedRunTimer)
			print("YOU DIED:", self.levelList[0].player.deaths, "TIMES")
			sys.exit()
			pygame.quit()
			return
		self.currentLevel = self.levelList[self.levelCounter]

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
			self.groundImage = pygame.image.load("../images/sand.png")
			self.groundLImage = pygame.image.load("../images/sandl.png")
			self.groundRImage = pygame.image.load("../images/sandr.png")
			self.dirtImage = pygame.image.load("../images/sanddeep.png")
			self.stoneImage = pygame.image.load("../images/stone.png")
			self.stoneLImage = pygame.image.load("../images/stonel.png")
			self.stoneRImage = pygame.image.load("../images/stoner.png")
			self.stoneCImage = pygame.image.load("../images/stonec.png")
			self.pillarImage = pygame.image.load("../images/pillar.png")
			self.pillarTImage = pygame.image.load("../images/pillart.png")
			self.spikeImage = pygame.image.load("../images/spikes.png")
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
	
	def getMaxCoinCount(self):
		return self.countMaxCoins

	def setMaxCoins(self, coins):
		self.maxCoins = coins

	def update(self):
		self.window.blit(self.UIImage, (0, 0))	
		pygame.draw.rect(self.window, (176, 18, 10), (104, 40,  self.life * 3.92, 32))		#Make sure to set the life image!!!
		coinStat = Word(self.window, str(self.coins) + " / " + str(self.maxCoins), 670, 30, 40, (255, 160, 0))
		coinStat.update()
		self.updateCounter += 1
			
		

