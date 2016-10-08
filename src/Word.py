class Word:
    def __init__(self, word, x,y, size, color):
        pygame.font.init()
        self.word=word
        self.surface=window
        self.rect=pygame.Rect(x,y,0, 0)
        self.font = pygame.font.Font("joystixMonospace.ttf", size)
        self.text = self.font.render(self.word, 1, (color[0], color[1], color[2]))
    def update(self):
        self.surface.blit(self.text, (self.rect.x, self.rect.y))