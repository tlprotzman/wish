

import pygame, sys, timeit
from game import Game 
from actor import Actor 
from level import Level
from genie import Genie
from mainmenu import Mainmenu


screenWidth = 22 * 64
screenHeight = 11 * 64
backgroundColor = (49, 27, 146)


wishTable = {"doublejump":[False, "for a double jump", ["You now have", "a double jump"]],
			 "tophat":[False, "for a snazzy hat", ["You now have", "the snazziest hat"]],
			 "fireman":[False, "I could stop fires", ["You can't stop fires", "but here's a nice hat!"]],
			 "turban":[False, "to wear a turban", ["That is one", "cool turban!"]],
			 "knife":[False, "to kill.", ["Congrats, press j", "to murder!"]],
			 "goldknife":[False, "I had a super weapon", ["Congrats, press j", "to destroy!"]],
			 "fryingpan":[False, "I were a chef", ["Now, press j", "to fry enemies!"]],
			 "amostrich":[False, "for friends", ["Be free, handsome one"]],
			 "healthpack":[False, "to be healthy", ["Stay safe out", "there!"]],
			 "spikeimmune":[False, "to be spikeproof", ["A late night", "roundevous with", "a cactus?"]],
			 "fasterrunning":[False, "to join the olympics", ["Hope you like", "running!"]],
			 "lowgravity":[False, "be an astronaut!", ["Hope you make", "it to the moon!"]],
			 "backwards":[False, "it was last theme", ["more", "words"]],
			 "amsimon":[False, "to include", ["He couldn't be here", "in person, but", "he's here in spirit"]],
			 "regen":[True, "words about regen", ["I hope you like", "regenerating health"]]
			}


#Remember to pass window into all the functions that need it!
window = pygame.display.set_mode((screenWidth, screenHeight))
game = Game(window, screenHeight, screenWidth)
game.wishTable = wishTable
player = Actor(window, game, 95, 200, "Player")

'''
pygame.mixer.init()
pygame.mixer.music.load("../audio/sondtrack.wav")
'''



def main():
	game.setTileset("Grass")

	# game.enemyList.append([Actor(window, game, 200, 300, 'Ostrich')])
	game.levelList.append(Level(game, player, window,"../levels/testlevel.txt"))
	game.levelList.append(Level(game, player, window,"../levels/testlevel2.txt"))
 
	game.setCurrentLevel(game.levelList[0])

	running = True
	while running:
		startTime = timeit.default_timer()
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_ESCAPE]:
			running = False


		game.clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		if game.gameState == 'PLAYING':
			window.fill(backgroundColor)
			game.getCurrentLevel().drawParallax(game.camera_x, game.camera_y)
			player.update(game.camera_x, game.camera_y)
			for enemy in game.enemyList[game.levelCounter]:
				damage = 1
				if game.wishTable["goldknife"][0]:
					damage = 3
				enemy.updateEnemy(game.camera_x, game.camera_y, player.rect.x+player.rect.width/2, player.rect.y+player.rect.height/2, player.isAttacking, damage, player)
			game.getCurrentLevel().update(game.camera_x, game.camera_y)
			for genie in game.genieList[game.levelCounter]:
			 	genie.update(game.camera_x, game.camera_y)
			game.getCurrentLevel().drawLights(game.camera_x, game.camera_y)

			game.camera_x += ((player.rect.x+player.rect.width/2-game.screenWidth/2) - game.camera_x)/5

			if game.camera_x < 0:
				game.camera_x = 0

			if game.camera_x > game.getCurrentLevel().getLevelWidth()-game.screenWidth:
				game.camera_x = game.getCurrentLevel().getLevelWidth()-game.screenWidth

			if game.wishTable["lowgravity"][0]:
				game.camera_y += ((player.rect.y+player.rect.height/2-game.screenHeight/2) - game.camera_y-64)/6
			else:
				game.camera_y += ((player.rect.y+player.rect.height/2-game.screenHeight/2) - game.camera_y-64)/50
				

			# if game.camera_y < 0:
			# 	game.camera_y = 0

			# if game.camera_y > game.getCurrentLevel().getLevelHeight()-game.screenHeight:
			# 	game.camera_Y = game.getCurrentLevel().getLevelHeight()-game.screenHeight
			# print(player.rect.x+player.rect.width/2)

			# game.levelTitle.update()
			# game.drawLives()
			game.update()
		elif game.gameState == 'MAINMENU':
			Mainmenu.update()
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

		#FPS Counter
		print(round(1 / (timeit.default_timer() - startTime), 0))



if __name__ == '__main__':
	main()
pygame.quit()
