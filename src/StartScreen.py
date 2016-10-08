class StartScreen:
    def __init__(self):
        self.words=["OH NO!!",
                    "YOU HAVE BEATEN YOUR FAVORITE",
                    "GAME BUT THERE IS NO REPLAY",
                    "BUTTON!! YOU MUST PLAY BACKWARDS",
                    "THROUGH THE GAME IN ORDER TO",
                    "REACH THE TITLE SCREEN!!",
                    "MOVE: A/D, JUMP: SPACE",
                    "PRESS ENTER TO UN-WIN THE GAME!!"]
        y = 0
        self.wordList=[]
        for item in self.words:
            self.wordList.append(Word(item, 80, 100+y*60, 50, [0, 0, 0]))
            y += 1
        self.wordList.append(Word("(for extra challenge: reach the title screen with only 3 lives!!)", 80, 10*64, 20, [0, 0, 0]))

    def update(self):
        pressed = pygame.key.get_pressed()

        window.fill((255, 255, 255))
        for word in self.wordList:
            word.update()
        if pressed[pygame.K_RETURN]:
            game.setGameState("CREDITSSCREEN")