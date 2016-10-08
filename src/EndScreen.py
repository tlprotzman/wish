class EndScreen:
    def __init__(self):
        self.title = ""
        self.pressEnter=Word("press enter", 7.8*64, 3*64, 40, [255, 255, 255])

    def update(self):
        if (game.life>3):
            self.title=Word("REVERSE", 7*64, 64, 80, [255, 255, 255])
        else:
            self.title=Word("YOU ARE AMAZING!", 2.5*64, 64, 80, [255, 255, 255])
        self.title.update()
        if math.floor(game.animation/2):
            self.pressEnter.update()
        window.blit(game.playerBreath[math.floor(game.animation/2)], (3*64 , SCREENHEIGHT-96-64))