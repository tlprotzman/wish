# this is to display a level select? and a play/credits thing
# if we want it
import pygame
import math
from word import Word

class Mainmenu:
	def __init__(self, window, game):
		self.game = game
		self.window = window
		self.timer = 0		
		self.main = pygame.image.load("../images/main.png")
		self.pressEnter = Word(self.window, "PRESS ENTER", 500, 500, 40, (255, 255, 255))
		
	def update(self):
		pressed = pygame.key.get_pressed()
		self.timer += 0.1
		if self.timer >= 24:
			self.timer = 24
		self.window.blit(self.main, (0, 0))
		if math.floor(self.timer)%2==0:
			self.pressEnter.update()
		self.surf = pygame.Surface((self.game.screenWidth, self.game.screenHeight))  # the size of your rect
		self.surf.fill((0, 0, 0))           # this fills the entire surface
		self.surf.set_alpha(255-self.timer*10)                # alpha level
		self.window.blit(self.surf, (0,0))    # (0,0) are the top-left coordinates
		if pressed[pygame.K_RETURN]:
			self.game.gameState = "PLAYING"
			pygame.mixer.music.load("../music/gameTheme.wav")
			pygame.mixer.music.play(-1, 0.0)