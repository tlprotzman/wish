import pygame
import random

class Particle:
	def __init__(self, game, window, x, y, color, lifespan = 10, speed = 10):
		self.window = window
		self.rect = pygame.Rect(x, y, 8, 8)
		self.game = game
		self.color = (random.randint(0, 255)*color[0], random.randint(0, 255)*color[1], random.randint(0, 255)*color[2])
		self.speed = speed
		self.velocity_x = random.randint(-self.speed, self.speed)
		self.velocity_y = random.randint(-self.speed*2, 0)
		self.timeAlive = lifespan
		
	def update(self, cameraX, cameraY):
		if not self.isGone(cameraX, cameraY):
			self.rect.x += self.velocity_x
			self.rect.y += self.velocity_y
			self.velocity_y += 1 # gravity applies
			pygame.draw.rect(self.window, self.color, pygame.Rect(self.rect.x-cameraX, self.rect.y-cameraY, 8, 8))
			self.timeAlive -= .1
		else:
			self.timeAlive = 0
		
	def isGone(self, cameraX, cameraY):
		if self.rect.y -cameraY> self.game.screenHeight:
			return True
		return False