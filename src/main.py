import pygame, sys, math, random
import Word, Game, Actor, Title, Level, StartScreen, CreditsScreen, EndScreen

SCREENWIDTH = 22*64
SCREENHEIGHT = 11*64

window = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.mixer.init()
pygame.mixer.music.load("soundtrack.wav")

def sign(v):
    return abs(v)/v

game=Game()

startScreen = StartScreen()

creditsScreen = CreditsScreen()

endScreen = EndScreen()

game.levelList=[]
game.enemyList=[]
game.nameList=[]

game.setTileset("Snow")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([])
game.nameList.append("Congrats, this is the last level!")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "       PPPP           ",
                              "      PPPPPP   PPPP   ",
                              "PPP   PPPPPPP  PPPPPPP",
                              "PPPP PPPPPPPP  PPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([])
game.nameList.append("This is it, just one more level!")

game.levelList.append(Level(["                      ",
                            "                      ",
                            "       PP             ",
                            "       PP             ",
                            "      PPP             ",
                            "     PPPP      PP     ",
                            "   PPPPPP             ",
                            "PPPPPPPPP          PPP",
                            "PPPPPPPPPPP     PPPPPP",
                            "PPPPPPPPPPP     PPPPPP",
                            "PPPPPPPPPPP     PPPPPP", ]))

game.enemyList.append([])
game.nameList.append("Don't fall in now!")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "PPPP                  ",
                              "PPPP                  ",
                              "        PPPPPPP       ",
                              "                      ",
                              "                      ",
                              "PPPPPPPP           PPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([Actor(10*64, 3*64, "Enemy"),
                       Actor(14*64, 3*63, "Enemy"),
                       Actor(12*64, 7*64, "Enemy")])
game.nameList.append("Watch out!")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "                PPPPPP",
                              "             PPPPPPPPP",
                              "        PPPPPPPPPP    ",
                              "        PPPPPPP       ",
                              "                      ",
                              "PPPPP             PPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([Actor(10*64, 3*64, "Enemy")])
game.nameList.append("Welcome to the land of snow!")

game.setTileset("Mountain")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "          PPP         ",
                              "          PPP         ",
                              "          PPP         ",
                              "PPPP......PPP......PPP",
                              "PPPP...............PPP",
                              "PPPP...............PPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([])
game.nameList.append("Swim?")

game.levelList.append(Level( ["PPPPP                ",
                              "PPPPP                 ",
                              "                      ",
                              "                      ",
                              "PPP                   ",
                              "PPPPP                 ",
                              "PPPPP                 ",
                              "PPPPP.............PPPP",
                              "PPPPP..H..........PPPP",
                              "PPPPP..HH........HPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([])
game.nameList.append("What lies beneath the waves?")

game.levelList.append(Level( ["PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "                      ",
                              "                      ",
                              "PP........PP        PP",
                              "PP...HH...PP   PP   PP",
                              "PP........PP        PP",
                              "PPH.......PPP       PP",
                              "PP....H...PP    P   PP",
                              "PP....H..HPP    P  PPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([])
game.nameList.append("Like left, like right")

game.levelList.append(Level( ["                  PPPP",
                              "                    PP",
                              "                      ",
                              "                      ",
                              "PP                  PP",
                              "PP                  PP",
                              "PP..................PP",
                              "PP.........PPPHHHH..PP",
                              "PP.....PP..PPP......PP",
                              "PPHHHHHPPHHPPP......PP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([Actor(19*64, 9*64, "Enemy")])
game.nameList.append("3 Pools of Water")

game.levelList.append(Level( ["PPPPPPPPPP     PP     ",
                              "PPPPPPPPPP     PP     ",
                              "         PP    PP     ",
                              "          PP   PP     ",
                              "PP             PP   PP",
                              "PP             P    PP",
                              "PP        PP       PPP",
                              "PP                 PPP",
                              "PP                PPPP",
                              "PP.......PPPP.....PPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))


game.enemyList.append([])
game.nameList.append("The only way is up?")

game.setTileset("Grass")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([])
game.nameList.append("Good luck!")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "           PPP        ",
                              "                      ",
                              "                      ",
                              "       PPPP       PPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([Actor(5 * 64, 0, "Enemy")])

for i in range (0, 100):
    game.enemyList[len(game.enemyList)-1].append(Actor(random.randint(3, 17)*64, -(i^3)*64, "Enemy"))

game.nameList.append("Its raining & pouring & this game is boring!!")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "           PP         ",
                              "         PPPPP...P    ",
                              "PPPPPPPPPPPPPPPPPPPPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([])
game.nameList.append("There's a long road ahead")

game.levelList.append(Level( ["                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "                      ",
                              "        PP            ",
                              "      PPPP........PP  ",
                              "      PPPPH.......PPPP",
                              "PPPPPPPPPPPPPPPPPPPPPP", ]))

game.enemyList.append([])
game.nameList.append("This is level 1!")

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