

import pygame
import word


class Genie:
	def __init__(self, window, game, player, x, y, wishChoices):
		self.window = window
		self.player = player
		self.wishChoices = wishChoices
		self.game = game
		self.width=15*8
		self.height=20*8
		self.rect=pygame.Rect(x, y, self.width, self.height)
		self.interactionDistanceSquared = 16384
		self.growingAnimationFrame = -1
		self.idleAnimation = 0
		self.wishText = self.makeWishChoices()

	def makeWishChoices(self):
		for i in range(len(self.wishChoices)):
			pass
		#self.text = [Word(self.window, wish, )]

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
			self.window.blit(self.game.genieIdle[self.game.animation], (self.rect.x-cameraX, self.rect.y-16-cameraY))
		elif self.growingAnimationFrame > -1:
			# then do the expansion frame
			self.window.blit(self.game.genieAppear[self.growingAnimationFrame], (self.rect.x-cameraX, self.rect.y-16-cameraY))
			
		else:
			# do the sitting in the lamp animation/image
			self.window.blit(self.game.genieLamp, (self.rect.x-cameraX, self.rect.y-16-cameraY))

