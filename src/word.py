import pygame

class Word:
	def __init__(self, window, word, x, y, size, color):
		pygame.font.init()
		self.window = window
		self.word = word
		self.rect = pygame.Rect(x, y, 0, 0)
		self.font = pygame.font.Font("../fonts/joystixMonospace.ttf", size)
		self.text = self.font.render(self.word, 1, color)

	def update(self):
		self.window.blit(self.text, (self.rect.x, self.rect.y))
		