# this is to display a level select? and a play/credits thing
# if we want it
import pygame
from word import Word

class Mainmenu:
	def __init__(self, window, game):
		self.game = game
		self.window = window
		self.timer = 0
		#self.main = pygame.image.load("../images/main.png")
		self.pressEnter = Word(self.window, "PRESS ENTER", 500, 500, 40, (255, 255, 255))
		
	def update(self):
		pressed = pygame.key.get_pressed()
		self.pressEnter.update()
		#self.window.blit(self.main, (0, 0))
		if pressed[pygame.K_a]:
			self.game.gameState = "PLAYING"
			pygame.mixer.music.load("../music/gameTheme.wav")
			pygame.mixer.music.play(-1, 0.0)