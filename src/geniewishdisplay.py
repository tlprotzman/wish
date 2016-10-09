import pygame


class GenieWishDisplay:
	def __init__(self, window, genie, message, wishes):
		self.window = window
		self.genie = genie
		self.leftFacing = genie.leftFacing
		self.message = message + ["", "I wish..."]
		self.wishes = wishes
		self.color1 = (0,0,0)
		self.color2 = (255, 255, 255)
		self.getWishes()
		self.chosenWish = -1



	def getWishes(self):
		[print(x) for x in self.wishes]
		wishes = [self.genie.game.wishTable[wish] for wish in self.wishes]
		self.pretext = [x[1] for x in wishes]
		self.posttext = [x[2] for x in wishes] # this is a table of lines! not a straight up string!
		self.renderPretext()
		self.renderPostText()
		self.renderMessage()

	def chooseWish(self, wishNum):
		self.chosenWish = wishNum

	def renderPretext(self):
		pretext = []
		for i in range(len(self.pretext)):
			line = str(i+1) + ") " + self.pretext[i]
			pretext += [[self.genie.game.genieFont.render(line, 1, self.color1), self.genie.game.genieFont.render(line, 1, self.color2)]]
		self.pretext = pretext
		# self.pretext = [(self.genie.game.genieFont.render(line, 1, self.color1), self.genie.game.genieFont.render(line, 1, self.color2)) for line in self.pretext]
		# index zero of that is the unselected option

	def renderPostText(self):
		# this should make a table of tables of pre rendered text lines
		self.posttext = [[self.genie.game.genieFont.render(x, 1, self.color1) for x in subtable] for subtable in self.posttext]

	def renderMessage(self):
		self.message = [self.genie.game.genieFont.render(line, 1, self.color1) for line in self.message]


	def displayWishes(self, cameraX, cameraY):
		if (not self.leftFacing):
			y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
			x = self.genie.rect.x - cameraX + 136
			self.window.blit(self.genie.game.speechImage, (x-16, y-16))
		else:
			x = self.genie.rect.x - cameraX + 136 - 500 # because it's to the left
			y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
			self.window.blit(self.genie.game.speechLImage, (x-16, y-16))

		for i in range(len(self.message)):
			self.window.blit(self.message[i], (x, y))
			y += 24
		for i in range(len(self.pretext)):
			self.window.blit(self.pretext[i][i == self.chosenWish], (x, y))
			y += 24

	def displayPosttext(self, cameraX, cameraY):
		if (not self.leftFacing):
			y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
			x = self.genie.rect.x - cameraX + 136
			self.window.blit(self.genie.game.speechImage, (x-16, y-16))
		else:
			x = self.genie.rect.x - cameraX + 136 - 500 # because it's to the left
			y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
			self.window.blit(self.genie.game.speechLImage, (x-16, y-16))

		y += 24*4
		for i in range(len(self.posttext[self.chosenWish])):
			self.window.blit(self.posttext[self.chosenWish][i], (x, y))
			y += 24

	def setWishFlagTrue(self):
		self.genie.game.wishTable[self.wishes[self.chosenWish]][0] = True

	# def renderText(self):
	# 	color1 = (0, 0, 0)
	# 	self.unselected = [self.genie.game.genieFont.render(line, 1, color1) for line in self.message]
	# 	self.unselected += [self.genie.game.genieFont.render(wish, 1, color1) for wish in self.wishes]
		
	# 	color2 = (255, 255, 255)
	# 	self.selected = ["" for line in self.message]
	# 	self.selected += [self.genie.game.genieFont.render(wish, 1, color2) for wish in self.wishes]

	# def displayWishes(self, cameraX, cameraY, selectedWish = -2):
	# 	y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
	# 	x = self.genie.rect.x - cameraX + 136
	# 	if (not self.leftFacing):
	# 		self.window.blit(self.genie.game.speechImage, (x-16, y-16))
	# 	else:
	# 		x -= 500
	# 		y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
	# 		self.window.blit(self.genie.game.speechLImage, (x-16, y-16))
	# 	for i in range(len(self.wishes)+len(self.message)):
	# 		if i == selectedWish+1 and i != 0:
	# 			self.window.blit(self.selected[i], (x, y))
	# 		else:
	# 			self.window.blit(self.unselected[i], (x, y))
	# 		y += 24

	# def displayAfterText(self, cameraX, cameraY, selectedWish):
	# 	y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
	# 	x = self.genie.rect.x - cameraX + 136
	# 	if (not self.leftFacing):
	# 		self.window.blit(self.genie.game.speechImage, (x-16, y-16))
	# 	else:
	# 		x -= 500
	# 		y = self.genie.rect.y - cameraY - 120 - 20*len(self.message) - 48
	# 		self.window.blit(self.genie.game.speechLImage, (x-16, y-16))
	# 	for i in range(len(self.wishes)+len(self.message)):
	# 		if i == selectedWish+1 and i != 0:
	# 			self.window.blit(self.selected[i], (x, y))
	# 		else:
	# 			self.window.blit(self.unselected[i], (x, y))
	# 		y += 24
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