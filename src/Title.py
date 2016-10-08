class Tile:
    def __init__(self, x, y, name, image):
        self.width=64
        self.height=64
        self.rect=pygame.Rect(x, y, self.width, self.height)
        self.name= name
        self.image=image

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))