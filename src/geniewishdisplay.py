import pygame


class GenieWishDisplay:
	def __init__(self, window, genie, message, wishes):
		self.window = window
		self.genie = genie
		self.leftFacing = genie.leftFacing
		self.message = message + ["", "I wish..."]
		self.wishes = wishes
		self.renderText()

	def renderText(self):
		color1 = (0, 0, 0)
		self.unselected = [self.genie.game.genieFont.render(line, 1, color1) for line in self.message]
		self.unselected += [self.genie.game.genieFont.render(wish, 1, color1) for wish in self.wishes]
		
		color2 = (255, 255, 255)
		self.selected = ["" for line in self.message]
		self.selected += [self.genie.game.genieFont.render(wish, 1, color2) for wish in self.wishes]

	def displayWishes(self, cameraX, cameraY, selectedWish = -2):
		y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
		x = self.genie.rect.x - cameraX + 136
		if (not self.leftFacing):
			self.window.blit(self.genie.game.speechImage, (x-16, y-16))
		else:
			x -= 416
			y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
			self.window.blit(self.genie.game.speechLImage, (x-16, y-16))
		for i in range(len(self.wishes)+len(self.message)):
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