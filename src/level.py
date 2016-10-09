
import pygame
import math
from tile import Tile
from actor import Actor
from genie import Genie

class Level:
	def __init__(self, game, player, window, arrayOrFilename):
		self.window = window
		self.game = game
		self.player = player
		self.parallaxHeight = 0
		self.parallaxImageHeight = 480 # this should be the height of the image martin made
		if type(arrayOrFilename) == type("Jordan"):
			self.loadLevelFile(arrayOrFilename)
		else:
			self.levelArray = arrayOrFilename
		x = 0
		y = 0
		self.walls = []
		self.backgrounds = []
		self.levelWidth = 0
		self.levelHeight = 0
		self.lightSources = []


		enemyList = []
		genieList = []
		for row in self.levelArray:
			self.levelHeight += 1
			for item in row:
				if item == "O":
					enemyList += [Actor(self.window, self.game, x, y-64, "Ostrich")]
				elif item == "_":
					# place the spawn point for the level
					self.spawnX = x-64
					self.spawnY = y-64
				elif item == "W":
					enemyList += [Actor(self.window, self.game, x, y, "BatSleep")]
				elif item == "w":
					enemyList += [Actor(self.window, self.game, x, y, "Bat")]
				elif item == "G":
					genieList += [Genie(self.window, self.game, self.player, x-64, y-87, self.genieMessage, self.genieWishes, False)] # THERE'S ONLY ONE GENIE PER LEVEL, IF THERE ISN'T YOU'RE FUCKED!
				elif item == "g":
					genieList += [Genie(self.window, self.game, self.player, x-64, y-87, self.genieMessage, self.genieWishes)]
				elif item == "P":
					if y==0 or self.levelArray[round((y/64)-1)][round(x/64)]!="P":
						if (round(x/64) < (len(row)) - 1 and self.levelArray[round(y/64)][round(x/64)+1]!="P"):
							tile = Tile(self.window, x, y, "Ground", self.game.groundRImage)
						elif (round(x/64) > 0 and self.levelArray[round(y/64)][round(x/64)-1]!="P"):
							tile = Tile(self.window, x, y, "Ground", self.game.groundLImage)
						else:
							tile = Tile(self.window, x, y, "Ground", self.game.groundImage)
					else:
						tile = Tile(self.window, x, y, "Ground", self.game.dirtImage)
					self.walls.append(tile)
				elif item == "S":
					if (round(x/64) < (len(row)) - 1 and self.levelArray[round(y/64)][round(x/64)+1]!="S" and round(x/64) > 0 and self.levelArray[round(y/64)][round(x/64)-1]!="S"):
						tile = Tile(self.window, x, y, "Ground", self.game.stoneCImage)
					elif (round(x/64) < (len(row)) - 1 and self.levelArray[round(y/64)][round(x/64)+1]!="S"):
						tile = Tile(self.window, x, y, "Ground", self.game.stoneRImage)
					elif (round(x/64) > 0 and self.levelArray[round(y/64)][round(x/64)-1]!="S"):
						tile = Tile(self.window, x, y, "Ground", self.game.stoneLImage)
					else:
						tile = Tile(self.window, x, y, "Ground", self.game.stoneImage)
					self.walls.append(tile)
				elif item == "|":
					if y==0 or self.levelArray[round((y/64)-1)][round(x/64)]!="|":
						tile = Tile(self.window, x, y, "Pilar", self.game.pillarTImage)
					else:
						tile = Tile(self.window, x, y, "Pillar", self.game.pillarImage)
					self.backgrounds.append(tile)
				elif item == "^":
					tile = Tile(self.window, x, y, "Spike", self.game.spikeImage)
					self.backgrounds.append(tile)
				elif item == "H":
					tile = Tile(self.window, x, y, "Hidden", self.game.waterImage)
					self.walls.append(tile)
				elif item == "T":
					tile = Tile(self.window, x, y-64, "Torch", self.game.torchImage[self.game.animation])
					self.backgrounds.append(tile)
					self.lightSources += [(x+32, y-64)]

				elif item == "C":
					tile = Tile(self.window, x, y, "Coin", self.game.coinImage)
					self.backgrounds.append(tile)
					self.game.countMaxCoins+=1
				elif item == "M":
					tile = Tile(self.window, x, y, "Health", self.game.healthImage)
					self.backgrounds.append(tile)					

				elif item == ".":
					if y==0 or self.levelArray[round((y/64)-1)][round(x/64)]==" ":
						tile = Tile(self.window, x, y, "Wave", self.game.waveImage[self.game.animation])
					else:
						tile = Tile(self.window, x, y, "Water", self.game.waterImage)
					self.backgrounds.append(tile)
				x += 64
			y += 64
			x = 0
		self.levelWidth = len(self.levelArray[0])*64
		self.levelHeight = len(self.levelArray)*64
		self.staticTiles = pygame.Surface((self.levelWidth, self.levelHeight)) #(64*self.levelWidth, 64*self.levelHeight)
		self.belowGroundBackground = pygame.Surface((self.game.screenWidth, self.game.screenHeight))
		self.belowGroundBackground.fill((109, 99, 52))
		self.staticTiles.fill((255,255,255,0))
		self.staticTiles.set_colorkey((255,255,255,0))
		self.makeBackgroundImage()
		self.game.enemyList.append(enemyList)
		self.game.genieList.append(genieList)
		# lighting here:
		# this first one is darkness the size of the screen
		self.darknessMap = pygame.Surface((self.game.screenWidth, self.game.screenHeight))
		self.darknessMap.fill((0, 0, 0))
		self.torchR = 128
		self.torchMap = pygame.Surface((self.torchR*2, self.torchR*2))
		pygame.draw.circle(self.torchMap, (255, 255, 255), (128, 128), 128)
		self.torchMap.set_alpha(25)
		self.darknessMap.set_alpha(100)
		self.torchMap.set_colorkey((0,0,0))
		self.torchImage = pygame.image.load("../images/torchmap.png")
		self.makeFullLightMap()
		self.setupParallax()
		#self.torchImage.set_colorkey(255, 255, 255)

	def loadLevelFile(self, filename):
		f = open(filename, "r")
		lines = f.readlines()
		firstLine = lines[0].split()
		self.parallaxHeight = float(firstLine[0])*64
		lengthOfMessage = int(lines[1])
		self.genieMessage = [line[:-1] for line in lines[2:2+lengthOfMessage]]
		self.genieWishes = [line[:-1] for line in lines[2+lengthOfMessage : 5+lengthOfMessage]]
		
		self.levelArray = [line[:-1] for line in lines[5+lengthOfMessage:]]
		f.close()

	def getLevelWidth(self):
		return self.levelWidth

	def getLevelHeight(self):
		return self.levelHeight

	def makeBackgroundImage(self):
		for tile in self.walls:
			tile.drawTo(0, 0, self.staticTiles)

	def getWalls(self):
		return self.walls

	def getBackgrounds(self):
		return self.backgrounds

	def makeFullLightMap(self):
		self.tallDarkness = pygame.Surface((self.getLevelWidth(), self.getLevelHeight()/2))
		self.tallDarkness.fill((50, 50, 50))
		self.torchImage = pygame.transform.scale(self.torchImage, (4*self.torchR, 4*self.torchR))
		print("CREATED LIGHTING MAP")
		self.fullLightingMap = pygame.Surface((self.getLevelWidth(), self.getLevelHeight()))
		self.fullLightingMap.fill((50, 50, 50))
		for torch in self.lightSources:
			self.fullLightingMap.blit(self.torchImage, (torch[0]-2*self.torchR, torch[1]-1.5*self.torchR))
			# self.fullLightingMap.blit(self.torchImage, (torch[0]-self.torchR+6, torch[1]-self.torchR+48))

	def drawFullLightMap(self, cameraX, cameraY):
		self.window.blit(self.fullLightingMap, (0-cameraX, 0-cameraY) , special_flags=pygame.BLEND_RGBA_SUB)
		self.window.blit(self.tallDarkness, (0-cameraX, -self.getLevelHeight()/2-cameraY-1) , special_flags=pygame.BLEND_RGBA_SUB)

	def drawLights(self, cameraX, cameraY):
		self.drawFullLightMap(cameraX, cameraY)
		# for torch in self.lightSources:
		# 	self.darknessMap.blit(self.torchImage, (torch[0]-cameraX-self.torchR+6, torch[1]-cameraY-self.torchR+48))
		# self.window.blit(self.darknessMap, (0, 0))#, special_flags=pygame.BLEND_RGBA_SUB)


	def setupParallax(self):
		self.parallaxWidth = self.game.screenWidth-32
		self.parallaxDrawHeight = self.parallaxHeight - self.game.screenHeight/2

		# then set up the close parallax
		self.completeCloseParallax = pygame.Surface((3*self.parallaxWidth, self.parallaxImageHeight))
		self.completeCloseParallax.set_colorkey((0,0,0))
		self.completeCloseParallax.blit(self.game.closeParallax, (0, 0))
		self.completeCloseParallax.blit(self.game.closeParallax, (self.parallaxWidth, 0))
		self.completeCloseParallax.blit(self.game.closeParallax, (self.parallaxWidth*2, 0))

		# then set up the far parallax
		self.completeFarParallax = pygame.Surface((3*self.parallaxWidth, self.parallaxHeight))
		self.completeFarParallax.set_colorkey((0,0,0))
		self.completeFarParallax.blit(self.game.farParallax, (0, 0))
		self.completeFarParallax.blit(self.game.farParallax, (self.parallaxWidth, 0))
		self.completeFarParallax.blit(self.game.farParallax, (self.parallaxWidth*2, 0))

	def drawParallax(self, cameraX, cameraY):
		closeX = -((cameraX*self.game.close_parallax_scale)%(self.parallaxWidth))
		farX = -((cameraX*self.game.far_parallax_scale)%(self.parallaxWidth))
		self.window.blit(self.completeFarParallax, (farX, self.parallaxDrawHeight-cameraY))
		self.window.blit(self.completeCloseParallax, (closeX, self.parallaxDrawHeight-cameraY))
		self.window.blit(self.belowGroundBackground, (0, (self.parallaxHeight-self.game.screenHeight/2)-cameraY+self.parallaxImageHeight))

	def drawParallaxOLD(self, cameraX, cameraY):
		parallaxWidth = self.game.screenWidth-32
		x = -((cameraX*self.game.far_parallax_scale)%(parallaxWidth))
		# do the background one
		self.window.blit(self.game.farParallax, (x, (self.parallaxHeight-self.game.screenHeight/2)-cameraY)) # -cameraY*self.game.close_parallax_scale
		self.window.blit(self.game.farParallax, (x+parallaxWidth, (self.parallaxHeight-self.game.screenHeight/2)-cameraY))
		self.window.blit(self.game.farParallax, (x+2*parallaxWidth, (self.parallaxHeight-self.game.screenHeight/2)-cameraY))
		x = -((cameraX*self.game.close_parallax_scale)%(parallaxWidth))
		# then do the foreground one
		self.window.blit(self.game.closeParallax, (x, (self.parallaxHeight-self.game.screenHeight/2)-cameraY)) # -cameraY*self.game.close_parallax_scale
		self.window.blit(self.game.closeParallax, (x+parallaxWidth, (self.parallaxHeight-self.game.screenHeight/2)-cameraY))
		self.window.blit(self.game.closeParallax, (x+2*parallaxWidth, (self.parallaxHeight-self.game.screenHeight/2)-cameraY))
		self.window.blit(self.belowGroundBackground, (0, (self.parallaxHeight-self.game.screenHeight/2)-cameraY+self.parallaxImageHeight))
		# backgroundColor = (109, 99, 52)
		# pygame.draw.rect(self.window, backgroundColor, (0, (self.parallaxHeight-self.game.screenHeight/2)-cameraY+self.parallaxImageHeight, self.getLevelWidth(), self.getLevelHeight()))

	def update(self, cameraX, cameraY):
		if self.player.rect.right<0:
			print("THIS SHOULDNT'T HAPPEN! THIS IS LEVEL UPDATING!")
			if self.game.levelCounter < len(self.game.levelList)-1:
				self.game.levelCounter+=1
				self.game.setCurrentLevel(self.game.levelList[self.game.levelCounter])

				self.player.rect.x=SCREENWIDTH-self.player.rect.width
				self.player.rect.y -= 15
				self.game.levelTitle = Word("LEVEL " + str(len(self.game.levelList)-self.game.levelCounter) + ": " + self.game.nameList[self.game.levelCounter], 20, 20, 30, [255, 255, 255])
			else:
				self.game.gameState = "ENDSCREEN"

		# for tile in self.walls:
		# 	tile.update(cameraX, cameraY)
		self.window.blit(self.staticTiles, (-cameraX, -cameraY))
		for tile in self.backgrounds:
			if tile.name=="Wave":
				tile.image = self.game.waveImage[self.game.animation]
			elif tile.name=="Torch":
				tile.image = self.game.torchImage[self.game.animation]
			elif tile.name=="Coin":
				tile.image = self.game.coinImage[self.game.animation]
			elif tile.name=="Health":
				tile.image = self.game.lifeImage[math.floor(self.game.animation/2)]
				
			tile.update(cameraX, cameraY)







