def main():
    game.setCurrentLevel(game.levelList[0])

    running = True
    while running:
        game.clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        if game.gameState == "PLAYING":
            window.fill((25, 134, 242))
            for enemy in game.enemyList[game.levelCounter]:
                enemy.update()
            player.update()
            game.getCurrentLevel().update()
            game.levelTitle.update()
            game.drawLives()
        elif game.gameState=="STARTSCREEN":
            startScreen.update()
        elif game.gameState=="CREDITSSCREEN":
            creditsScreen.update()
        elif game.gameState=="ENDSCREEN":
            window.fill((25, 134, 242))
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