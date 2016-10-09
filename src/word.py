import pygame

class Word:
	def __init__(self, window, content, x, y, size, color):
		pygame.font.init()
		self.window = window
		self.content = content
		self.rect = pygame.Rect(x, y, 0, 0)
		self.font = pygame.font.Font("../fonts/joystixMonospace.ttf", size)
		self.text = self.font.render(self.content, 1, color)

	def update(self):
		self.window.blit(self.text, (self.rect.x, self.rect.y))
		
	def drawAt(self, cameraX, cameraY):
		self.window.blit(self.text, (self.rect.x-cameraX, self.rect.y-cameraY))