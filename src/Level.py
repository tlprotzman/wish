class Level:
    def __init__(self, array):
        self.levelArray = array
        x = 0
        y = 0
        self.walls = []
        self.backgrounds = []
        for row in self.levelArray:
            for item in row:
                if item == "P":
                    if y==0 or self.levelArray[round((y/64)-1)][round(x/64)]==" ":
                        if (round(x/64) < 21 and self.levelArray[round(y/64)][round(x/64)+1]!="P"):
                            tile = Tile(x, y, "Ground", game.groundRImage)
                        elif (round(x/64) > 0 and self.levelArray[round(y/64)][round(x/64)-1]!="P"):
                            tile = Tile(x, y, "Ground", game.groundLImage)
                        else:
                            tile = Tile(x, y, "Ground", game.groundImage)
                    else:
                        tile = Tile(x, y, "Ground", game.dirtImage)
                    self.walls.append(tile)
                elif item == "H":
                    tile = Tile(x, y, "Hidden", game.waterImage)
                    self.walls.append(tile)
                elif item == ".":
                    if y==0 or self.levelArray[round((y/64)-1)][round(x/64)]==" ":
                        tile = Tile(x, y, "Wave", game.waveImage[game.animation])
                    else:
                        tile = Tile(x, y, "Water", game.waterImage)
                    self.backgrounds.append(tile)
                x += 64
            y += 64
            x = 0

    def getWalls(self):
        return self.walls

    def getBackgrounds(self):
        return self.backgrounds

    def update(self):

        if player.rect.right<0:
            if game.levelCounter < len(game.levelList)-1:
                game.levelCounter+=1
                game.setCurrentLevel(game.levelList[game.levelCounter])

                player.rect.x=SCREENWIDTH-player.rect.width
                player.rect.y -= 15
                game.levelTitle = Word("LEVEL " + str(len(game.levelList)-game.levelCounter) + ": " + game.nameList[game.levelCounter], 20, 20, 30, [255, 255, 255])
            else:
                game.gameState = "ENDSCREEN"

        for tile in self.walls:
            tile.update()
        for tile in self.backgrounds:
            if tile.name=="Wave":
                tile.image = game.waveImage[game.animation]
            tile.update()