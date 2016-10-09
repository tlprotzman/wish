import pygame
import random

class Particle:
	def __init__(self, game, window, x, y, color):
		self.window = window
		self.rect = pygame.Rect(x, y, 8, 8)
		self.game = game
		self.color = (random.randint(0, 255)*color[0], random.randint(0, 255)*color[1], random.randint(0, 255)*color[2])
		self.velocity_x = random.randint(-5, 5)
		self.velocity_y = random.randint(-5, 5)
		
	def update(self):
		if not self.isGone():
			self.rect.x += self.velocity_x
			self.rect.y += self.velocity_y
			self.velocity_y += 1

			pygame.draw.rect(self.window, self.color, pygame.Rect(self.rect.x-self.game.camera_x, self.rect.y-self.game.camera_y, 8, 8))
		
	def isGone(self):
		if self.rect.y > self.game.screenHeight:
			return True
		return False