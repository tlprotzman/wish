

import pygame
import word
from geniewishdisplay import GenieWishDisplay 


class Genie:
	def __init__(self, window, game, player, x, y, message, wishChoices, facingLeft = True):
		self.leftFacing = facingLeft
		self.window = window
		self.player = player
		self.message = message
		self.wishChoices = wishChoices
		self.game = game
		self.width=15*8
		self.height=20*8
		self.rect=pygame.Rect(x, y, self.width, self.height)
		self.interactionDistanceSquared = 16384
		self.growingAnimationFrame = -1
		self.idleAnimation = 0
		self.wishDisplay = GenieWishDisplay(self.window, self, message, wishChoices)

		self.wishesAlpha = 0
		self.chosenWish = -1

	def chooseWish(self, wish):
		self.chosenWish = wish
		self.wishDisplay.chooseWish(wish)
		self.wishDisplay.setWishFlagTrue()

	def isInMenu(self):
		return self.growingAnimationFrame == 4

	def distanceSquared(self, x, y):
		return (x - self.rect.x)**2 + (y-self.rect.y)**2

	def update(self, cameraX, cameraY):
		distance = self.distanceSquared(self.player.rect.x, self.player.rect.y)

		# this determines what frame it should show
		if distance < self.interactionDistanceSquared:
			# then start the appearing animation
			if self.growingAnimationFrame < 4:
				self.growingAnimationFrame += 1
			else:
				self.idleAnimation += 1
				self.idleAnimation %= 4
		else:
			if self.growingAnimationFrame > -1:
				self.growingAnimationFrame -= 1
		#self.window.blit(self.game.genieLamp, (self.rect.x-cameraX, self.rect.y-16-cameraY))
		if self.growingAnimationFrame == 4:
			# then do the idle expanded animation
			if self.leftFacing:
				self.window.blit(self.game.genieIdleL[self.game.animation], (self.rect.x-cameraX, self.rect.y-16-cameraY))
			else:
				self.window.blit(self.game.genieIdleR[self.game.animation], (self.rect.x-cameraX, self.rect.y-16-cameraY))
			if self.chosenWish == -1:
				self.wishDisplay.displayWishes(cameraX, cameraY)
			else:
				self.wishDisplay.displayPosttext(cameraX, cameraY)
		elif self.growingAnimationFrame > -1:
			# then do the expansion frame
			if self.leftFacing:
				self.window.blit(self.game.genieAppearL[self.growingAnimationFrame], (self.rect.x-cameraX, self.rect.y-16-cameraY))
			else:
				self.window.blit(self.game.genieAppearR[self.growingAnimationFrame], (self.rect.x-cameraX, self.rect.y-16-cameraY))
			
		else:
			# do the sitting in the lamp animation/image
			if self.leftFacing:
				self.window.blit(self.game.genieLampL, (self.rect.x-cameraX, self.rect.y-16-cameraY))
			else:
				self.window.blit(self.game.genieLampR, (self.rect.x-cameraX, self.rect.y-16-cameraY))

