class CreditsScreen:
    def __init__(self):
        self.words=["PLAYING!!",
                    "THANK YOU FOR",
                    "",
                    "BACKWARDS GAME JAM",
                    "MADE IN 24 HRS FOR:",
                    "",
                    "AND SEAN",
                    "SIMON HOPKINS",
                    "TOBI HAHN",
                    "MARTIN DUFFY",
                    "GAME DEVELOPMENT BY:",]
        self.wordList=[]
        self.newY=0
        for item in self.words:
            word=Word(item, ((11*64)-round(len(item)/2)*50), self.newY, 60, [255, 255, 255])
            self.wordList.append(word)
            self.newY-=70
            print(round(len(item)/2))

    def update(self):
        pressed = pygame.key.get_pressed()
        window.fill((0, 0, 0))
        for word in self.wordList:
            word.update()
            word.rect.y+=3
            if self.wordList[len(self.wordList)-1].rect.y>SCREENHEIGHT or pressed[pygame.K_a]:
                game.setGameState("PLAYING")
                player.rect.y = 0
                player.rect.x = SCREENWIDTH-64
                pygame.mixer.music.play(-1, 0.0)