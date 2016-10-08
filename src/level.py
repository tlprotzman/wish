
import pygame
from tile import Tile

class Level:
	def __init__(self, game, player, array):
		self.levelArray = array
		x = 0
		y = 0
		self.walls = []
		self.backgrounds = []
		for row in self.levelArray:
			for item in row:
				if item == "P":
					if y==0 or self.levelArray[round((y/64)-1)][round(x/64)]==" ":
						if (round(x/64) < 21 and self.levelArray[round(y/64)][round(x/64)+1]!="P"):
							tile = Tile(x, y, "Ground", self.game.groundRImage)
						elif (round(x/64) > 0 and self.levelArray[round(y/64)][round(x/64)-1]!="P"):
							tile = Tile(x, y, "Ground", self.game.groundLImage)
						else:
							tile = Tile(x, y, "Ground", self.game.groundImage)
					else:
						tile = Tile(x, y, "Ground", self.game.dirtImage)
					self.walls.append(tile)
				elif item == "H":
					tile = Tile(x, y, "Hidden", self.game.waterImage)
					self.walls.append(tile)
				elif item == ".":
					if y==0 or self.levelArray[round((y/64)-1)][round(x/64)]==" ":
						tile = Tile(x, y, "Wave", self.game.waveImage[self.game.animation])
					else:
						tile = Tile(x, y, "Water", self.game.waterImage)
					self.backgrounds.append(tile)
				x += 64
			y += 64
			x = 0

	def getWalls(self):
		return self.walls

	def getBackgrounds(self):
		return self.backgrounds

	def update(self):

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

		for tile in self.walls:
			tile.update()
		for tile in self.backgrounds:
			if tile.name=="Wave":
				tile.image = self.game.waveImage[self.game.animation]
			tile.update()