

import pygame

class Tile:
	def __init__(self, window, x, y, name, image):
		self.window = window
		self.width=64
		self.height=64
		self.rect=pygame.Rect(x, y, self.width, self.height)
		self.name= name
		self.image=image

	def update(self, cameraX, cameraY):
		self.window.blit(self.image, (self.rect.x-cameraX, self.rect.y-cameraY))

	def drawTo(self, cameraX, cameraY, surface):
		surface.blit(self.image, (self.rect.x-cameraX, self.rect.y-cameraY))