

import pygame


class GenieWishDisplay:
	def __init__(self, window, genie, wishes):
		self.window = window
		self.genie = genie
		self.leftFacing = genie.leftFacing
		self.wishes = wishes
		self.renderText()

	def renderText(self):
		color1 = (0, 0, 0)
		self.unselected = [self.genie.game.genieFont.render(wish, 1, color1) for wish in self.wishes]
		color2 = (255, 255, 255)
		self.selected = [self.genie.game.genieFont.render(wish, 1, color2) for wish in self.wishes]

	def displayWishes(self, cameraX, cameraY, selectedWish = -1):
		x = self.genie.rect.x - cameraX
		y = self.genie.rect.y - cameraY - 100
		for i in range(len(self.wishes)):
			if i == selectedWish:
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