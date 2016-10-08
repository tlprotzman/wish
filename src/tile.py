

import pygame

class Tile:
	def __init__(self, window, x, y, name, image):
		self.window = window
		self.width=64
		self.height=64
		self.rect=pygame.Rect(x, y, self.width, self.height)
		self.name= name
		self.image=image

	def update(self):
		self.window.blit(self.image, (self.rect.x, self.rect.y))