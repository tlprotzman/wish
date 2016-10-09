

import pygame, sys
from game import Game 
from actor import Actor 
from level import Level
from genie import Genie


screenWidth = 22 * 64
screenHeight = 11 * 64
backgroundColor = (49, 27, 146)

#Remember to pass window into all the functions that need it!
window = pygame.display.set_mode((screenWidth, screenHeight))
game = Game(window, screenHeight, screenWidth)
player = Actor(window, game, 95, 200, "Player")

'''
pygame.mixer.init()
pygame.mixer.music.load("../audio/sondtrack.wav")
'''

def main():
	game.setTileset("Grass")

	# game.enemyList.append([Actor(window, game, 200, 300, 'Ostrich')])
	game.levelList.append(Level(game, player, window,"../levels/testlevel.txt"))
	wishes = ["Nope", "Just kidding", "Yada Yada"]
	game.genieList.append([Genie(window, game, player, 320, 361, ["Hello, what do","you wish for?"], wishes, True)])
 
	game.setCurrentLevel(game.levelList[0])

	running = True
	while running:
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_ESCAPE]:
			running = False


		game.clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if game.gameState == 'PLAYING':
			window.fill(backgroundColor)
			#game.getCurrentLevel().drawParallax(game.camera_x, game.camera_y)
			player.update(game.camera_x, game.camera_y)
			for enemy in game.enemyList[game.levelCounter]:
			 	enemy.updateEnemy(game.camera_x, game.camera_y, player.rect.x+player.rect.width/2, player.rect.y+player.rect.height/2)
			game.getCurrentLevel().update(game.camera_x, game.camera_y)
			for genie in game.genieList[game.levelCounter]:
			 	genie.update(game.camera_x, game.camera_y)
			

			game.camera_x += ((player.rect.x+player.rect.width/2-game.screenWidth/2) - game.camera_x)/5

			if game.camera_x < 0:
				game.camera_x = 0

			if game.camera_x > game.getCurrentLevel().getLevelWidth()-game.screenWidth:
				game.camera_x = game.getCurrentLevel().getLevelWidth()-game.screenWidth

			game.camera_y += ((player.rect.y+player.rect.height/2-game.screenHeight/2) - game.camera_y)/50

			# if game.camera_y < 0:
			# 	game.camera_y = 0

			if game.camera_y > game.getCurrentLevel().getLevelHeight()-game.screenHeight:
				game.camera_Y = game.getCurrentLevel().getLevelHeight()-game.screenHeight
			# print(player.rect.x+player.rect.width/2)

			# game.levelTitle.update()
			# game.drawLives()
		elif game.gameState == 'STARTSCREEN':
			startScreen.update()
		elif game.gameState == 'CREDITSSCREEN':
			creditsScreen.update()
		elif game.gameState == 'ENDSCREEN':
			window.fill(backgroundColor)
			game.getCurrentLevel().update()
			endScreen.update()
			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_RETURN]:
				running = False

		game.animate()
		pygame.display.update()


if __name__ == '__main__':
	main()
pygame.quit()
