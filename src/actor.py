
import pygame, math, random

def sign(num):
	if (num==0):
		return 0
	else:
		return num/abs(num)

class Actor:
	def __init__(self, window, game, x, y, name, speed = 1, max_speed = 12, max_fall = 20, gravity = 1.3, friction = 0.5):
		if name == "Player":
			self.height = 16*8
			self.jump_force = 45
		else:
			self.height = 128
			self.jump_force = 15

		self.window = window
		self.game = game

		self.width = 64
		self.rect = pygame.Rect(x, y, self.width, self.height)
		self.surface = pygame.Surface((self.rect.w, self.rect.h))
		self.speed = speed
		self.velocity_y = 0
		self.velocity_x = 0
		self.max_fall = max_fall
		self.max_speed = max_speed
		self.friction = friction
		self.gravity = gravity
		self.onGround = True
		self.name = name
		self.deathTimer = 0
		self.shouldFlip = False
		self.facing = 'right'
		self.changeDirection = 0
		self.direction = 1
		self.fightTimer = 0
		self.isAttacking = False


	def movement(self):
		f = self.friction
		# if self.onGround:
		# 	f = self.friction / 4

		self.onGround = False
		self.rect.x += self.velocity_x
		self.collideX()
		self.rect.y += self.velocity_y
		self.collideY()

		self.velocity_y += self.gravity
		
		#Uncomment if it's time to dance!
		if (abs(self.velocity_x) < f / 2):
			self.velocity = 0


		if (abs(self.velocity_x) > 0):
			self.velocity_x -= f * sign(self.velocity_x)



		if (abs(self.velocity_x) > self.max_speed):
			self.velocity_x = self.max_speed * sign(self.velocity_x)

		if abs(self.velocity_y) > self.max_fall:
			self.velocity_y = self.max_fall * sign(self.velocity_y)

		#print(abs(self.velocity_x))
	def getInput(self):
		pressed = pygame.key.get_pressed()

		if pressed[pygame.K_a]:
			self.velocity_x -= self.speed

		if pressed[pygame.K_d]:
			self.velocity_x += self.speed
			
		if pressed[pygame.K_j]:
			self.fight()
			
		if pressed[pygame.K_SPACE]:
			self.jump()

	
	# I excluded a section about screenwidth and the extra life
	def fight(self):
		if (not self.isAttacking):
			self.fightTimer = 1		
	
	def jump(self):
		if self.onGround:
			self.jump_force_adjusted = self.jump_force + abs(self.velocity_x) * 2
			print(self.jump_force_adjusted)
			self.velocity_y = -self.jump_force_adjusted

	def collideX(self):
		for wall in self.game.getCurrentLevel().getWalls():
			if self.rect.right+self.velocity_x > wall.rect.left and self.rect.left + self.velocity_x < wall.rect.right:
				if self.rect.bottom <= wall.rect.top and self.rect.bottom + self.velocity_y > wall.rect.top:
					self.velocity_y = 0
					self.rect.bottom = wall.rect.top
					self.onGround = True
				if self.rect.top >= wall.rect.bottom and self.rect.top + self.velocity_y < wall.rect.bottom:
					self.velocity_y = 0
					self.rect.top = wall.rect.bottom
	def collideY(self):
		for wall in self.game.getCurrentLevel().getWalls():
			if self.rect.top < wall.rect.bottom and self.rect.bottom  > wall.rect.top:
				if self.rect.right <= wall.rect.left and self.rect.right + self.velocity_x + 2 > wall.rect.left:
					self.velocity_x = 0
					self.rect.right = wall.rect.left - 2
				if self.rect.left >= wall.rect.right and self.rect.left + self.velocity_x - 1 <= wall.rect.right:
					self.velocity_x = 0
					self.rect.left = wall.rect.right+2
	
	def drawPlayer(self, cameraX, cameraY):
		# if (self.deathTimer > 0 and self.deathTimer %2 == 0):
		# 	self.deathTimer = self.deathTimer
		# if self.onGround and self.velocity_x == 0:
		# 	self.window.blit(self.game.playerBreath)
		if (self.deathTimer>0 and self.deathTimer%2 == 0):
			self.deathTimer = self.deathTimer
			# don't do anything, wait a frame before drawing


		else:
			
			if self.velocity_x < 0:
				self.shouldFlip = True
				self.direction = -1
			elif self.velocity_x > 0:
				self.shouldFlip = False
				self.direction = 1

			if (self.onGround and self.velocity_x == 0):
				# this is breath
				self.window.blit(pygame.transform.flip((self.game.playerBreath[self.game.animation]), self.shouldFlip, False), (self.rect.x-cameraX, self.rect.y-16-cameraY))
			elif (not self.onGround):
				self.window.blit(pygame.transform.flip((self.game.playerJump), self.shouldFlip, False), (self.rect.x-cameraX, self.rect.y-16-cameraY))
			elif (self.velocity_x > 0):
				self.window.blit(pygame.transform.flip((self.game.playerWalk[self.game.animation]), self.shouldFlip, False), (self.rect.x-cameraX, self.rect.y-16-cameraY))
			elif (self.velocity_x < 0):
				self.window.blit(pygame.transform.flip((self.game.playerWalk[3-self.game.animation]), self.shouldFlip, False), (self.rect.x-cameraX, self.rect.y-16-cameraY))
			else:
				self.window.blit(self.game.playerBreath[1], (self.rect.x-cameraX, self.rect.y-16-cameraY))
		
			if self.direction==1:
				self.window.blit(pygame.transform.flip((self.game.knife[math.floor(self.game.animation/2)]), self.shouldFlip, False), (self.rect.x-16-cameraX, self.rect.y-8-cameraY))
			else:
				if self.velocity_x < 0:
					self.window.blit(pygame.transform.flip((self.game.knife[1-math.floor(self.game.animation/2)]), self.shouldFlip, False), (self.rect.x-cameraX, self.rect.y-8-cameraY))
				else:
					self.window.blit(pygame.transform.flip((self.game.knife[math.floor(self.game.animation/2)]), self.shouldFlip, False), (self.rect.x-cameraX, self.rect.y-8-cameraY))

				
			
		

		# come back to this


	def drawEnemy(self, cameraX, cameraY, facing):
		if facing == 'right':
			enemyFlip = True
		else:
			enemyFlip = False

		if (self.velocity_x == 0):
			self.rect.height = 128
			self.window.blit(pygame.transform.flip(self.game.enemyBreath[self.game.animation], enemyFlip, False), (self.rect.x - cameraX, self.rect.y - cameraY))
		else:
			self.rect.height = 96
			self.window.blit(pygame.transform.flip(self.game.enemyRun[self.game.animation], enemyFlip, False), (self.rect.x - cameraX, self.rect.y - cameraY))


	def AI(self, facing, playerX, playerY):
		# depends on what the type of creature is
		if self.name == "Ostrich":
			blockedRight = False
			blockedLeft = False
			for wall in self.game.getCurrentLevel().getWalls():
				if self.rect.top < wall.rect.bottom and self.rect.bottom > wall.rect.top:
					if self.rect.right + 10 <= wall.rect.left and self.rect.right + 80 >= wall.rect.left:
						blockedRight = True
					if self.rect.left + -10 > wall.rect.right and self.rect.left - 80 < wall.rect.right:
						blockedLeft = True
			if facing == 'right':
				if ((not blockedRight) and (abs(playerY - (self.rect.y + self.rect.height) / 2) < 300) and (0 < (playerX - (self.rect.x + self.rect.width / 2)) < 800)):
					print('wrk?')
					self.velocity_x = 13
				print((0 < (playerX - (self.rect.x + self.rect.width / 2)) < 200))
			if facing == 'left':
				if ((not blockedLeft) and (abs(playerY - (self.rect.y + self.rect.height) / 2) < 300) and (0 > (playerX - (self.rect.x + self.rect.width / 2)) > -800)):
					print('wrk?')
					self.velocity_x = -13
				print((0 < (playerX - (self.rect.x + self.rect.width / 2)) < 200))


	def die(self):
		self.deathTimer = 0
		if (self.deathTimer > 0):
			self.deathTimer -= 1
		if self.rect.y > self.game.getCurrentLevel().getLevelHeight() and self.deathTimer==0:
			self.deathTimer = 50
			self.rect.x = 32
			self.rect.y = 0
			self.game.life += 1
		else:
			pass
			for enemy in self.game.enemyList[self.game.levelCounter]:
				if self.rect.colliderect(enemy) and self.deathTimer == 0:
					self.deathTimer = 50
					print("We need to have the user move back to the respawn point!")
					self.rect.x = 32
					self.rect.y = 0
					self.game.life += 1


	def update(self, cameraX, cameraY):
		self.getInput()
		self.die()
		self.movement()
		self.drawPlayer(cameraX, cameraY)
		# print("Location: ", self.rect.x, self.rect.y)
		# print("Velocities: ", self.velocity_x, self.velocity_y)

	def updateEnemy(self, cameraX, cameraY, playerX, playerY):
		if self.changeDirection == 50:	
			if random.randint(1, 2) == 1:
				self.facing = 'right'
			else:
				self.facing = 'left'
			self.changeDirection = 0
		else:
			self.changeDirection += 1
		self.movement()
		self.AI(self.facing, playerX, playerY)
		self.drawEnemy(cameraX, cameraY, self.facing)























