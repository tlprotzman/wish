
import pygame
from tile import Tile

class Level:
	def __init__(self, game, player, window, array):
		self.window = window
		self.game = game
		self.player = player
		self.levelArray = array
		x = 0
		y = 0
		self.walls = []
		self.backgrounds = []
		self.levelWidth = 0
		self.levelHeight = 0
		for row in self.levelArray:
			self.levelHeight += 1
			for item in row:
				if item == "P":
					if y==0 or self.levelArray[round((y/64)-1)][round(x/64)]==" ":
						if (round(x/64) < 21 and self.levelArray[round(y/64)][round(x/64)+1]!="P"):
							tile = Tile(self.window, x, y, "Ground", self.game.groundRImage)
						elif (round(x/64) > 0 and self.levelArray[round(y/64)][round(x/64)-1]!="P"):
							tile = Tile(self.window, x, y, "Ground", self.game.groundLImage)
						else:
							tile = Tile(self.window, x, y, "Ground", self.game.groundImage)
					else:
						tile = Tile(self.window, x, y, "Ground", self.game.dirtImage)
					self.walls.append(tile)
				elif item == "H":
					tile = Tile(self.window, x, y, "Hidden", self.game.waterImage)
					self.walls.append(tile)
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
		self.staticTiles.fill((255,255,255,0))
		self.staticTiles.set_colorkey((255,255,255,0))
		self.makeBackgroundImage()

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
				tile.update(cameraX, cameraY)





