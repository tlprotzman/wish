

import pygame


class GenieWishDisplay:
	def __init__(self, window, genie, message, wishes):
		self.window = window
		self.genie = genie
		self.leftFacing = genie.leftFacing
		self.message = message
		self.wishes = wishes
		self.renderText()

	def renderText(self):
		color1 = (0, 0, 0)
		self.unselected = [self.genie.game.genieFont.render(wish, 1, color1) for wish in self.wishes]
		self.unselected = [self.genie.game.genieFont.render(self.message, 1, color1)] + self.unselected
		color2 = (255, 255, 255)
		self.selected = [self.genie.game.genieFont.render(wish, 1, color2) for wish in self.wishes]
		self.selected = [""] + self.selected

	def displayWishes(self, cameraX, cameraY, selectedWish = -2):
		x = self.genie.rect.x - cameraX
		y = self.genie.rect.y - cameraY - 120
		for i in range(len(self.wishes)+1):
			if i == selectedWish+1 and i != 0:
				self.window.blit(self.selected[i], (x, y))
			else:
				self.window.blit(self.unselected[i], (x, y))
			y += 24
"""
6.5


P               S                                             PPP                                                       
P               |                                    PPPPP                                                              
P               |                                                                                  PPPPP                
P       ^^^^^^^SSSSSSS                                                      PPPPPPPPPPPPP                              
P       SSSSSSSSSSSSSS                                          PPPPPPPPPPPPPPPPPPPPPPPPPPP                              
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP             PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        PPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP           PPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP               PPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                             PPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                              PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                           PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                 PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
"""