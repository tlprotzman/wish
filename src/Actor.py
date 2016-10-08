class Actor(object):
    def __init__(self, x , y , name, speed = 0.5, max_speed = 7, max_fall = 20, gravity = 1, friction = 0.25):

        if name=="Player":
            self.height = 96
            self.jump_force = 22
        else:
            self.height = 56
            self.jump_force = 15

        self.width = 64
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.surface = pygame.Surface((self.rect.w, self.rect.h))
        self.speed = speed
        self.velocity_y = 0
        self.velocity_x = 0
        self.max_fall = max_fall
        self.max_speed = max_speed
        self.speed = speed
        self.friction = friction
        self.gravity = gravity
        self.onGround = True
        self.name = name
        self.deathTimer = 0

    def movement(self):
        f = self.friction
        if self.onGround and game.levelCounter<5:
            f = self.friction/4

        self.onGround = False

        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        self.velocity_y += self.gravity

        if (abs(self.velocity_x) > 0):
            self.velocity_x -= f * sign(self.velocity_x)

        if (abs(self.velocity_x) < f):
            self.velocity = 0

        if (abs(self.velocity_x) > self.max_speed):
            self.velocity_x = self.max_speed * sign(self.velocity_x)

        if abs(self.velocity_y) > self.max_fall:
            self.velocity_y = self.max_fall * sign(self.velocity_y)

    def getInput(self):
        pressed = pygame.key.get_pressed()

        if(pressed[pygame.K_a]):
            self.velocity_x -= self.speed

        if(pressed[pygame.K_d]):
            self.velocity_x += self.speed

        if (pressed[pygame.K_SPACE]):
            self.jump()

        if (pressed[pygame.K_u]):
            self.rect.x = 0

    def jump(self):
        if self.onGround:
            self.velocity_y = -self.jump_force

    def collide(self):
        for wall in game.getCurrentLevel().getWalls():
            if self.rect.right+self.velocity_x > wall.rect.left and self.rect.left + self.velocity_x < wall.rect.right:
                if self.rect.bottom <= wall.rect.top and self.rect.bottom + self.velocity_y > wall.rect.top:
                    self.velocity_y = 0
                    self.rect.bottom = wall.rect.top
                    self.onGround = True
                if self.rect.top >= wall.rect.bottom and self.rect.top + self.velocity_y < wall.rect.bottom:
                    self.velocity_y = 0
                    self.rect.top = wall.rect.bottom
            if self.rect.top < wall.rect.bottom and self.rect.bottom  > wall.rect.top:
                if self.rect.right <= wall.rect.left and self.rect.right + self.velocity_x + 1 > wall.rect.left:
                    self.velocity_x = 0
                    self.rect.right = wall.rect.left - 1
                if self.rect.left >= wall.rect.right and self.rect.left + self.velocity_x - 1 <= wall.rect.right:
                    self.velocity_x = 0
                    self.rect.left = wall.rect.right+2
        if self.rect.right > SCREENWIDTH:
            self.rect.right = SCREENWIDTH
        if self.name=="Player" and game.levelCounter == len(game.levelList)-1 and game.bonusLife:
            if self.rect.colliderect(game.getCurrentLevel().getBackgrounds()[14]):
                game.life -= 1
                game.bonusLife = False


    def drawPlayer(self):
        if (self.deathTimer>0 and self.deathTimer%2 == 0):
            self.deathTimer = self.deathTimer
        elif (self.onGround and self.velocity_x == 0):
            window.blit(game.playerBreath[math.floor(game.animation/2)], (self.rect.x, self.rect.y+1))
        elif (not self.onGround):
            window.blit(game.playerJump, (self.rect.x, self.rect.y+1))
        elif (self.velocity_x > 0):
            window.blit(game.playerWalk[game.animation], (self.rect.x, self.rect.y+1))
        elif (self.velocity_x < 0):
            window.blit(game.playerWalk[3-game.animation], (self.rect.x, self.rect.y+1))
        else:
            window.blit(game.playerBreath[1], (self.rect.x, self.rect.y+1))

    def drawEnemy(self):
        if (self.onGround and self.velocity_x == 0):
            window.blit(game.enemyBreath[math.floor(game.animation/2)], (self.rect.x, self.rect.y))
        else:
            window.blit(game.enemyJump, (self.rect.x, self.rect.y))

    def AI(self):
        if random.randint(1, 40)==1 and self.onGround:
            self.jump()
            blockedRight = False
            blockedLeft = False
            for wall in game.getCurrentLevel().getWalls():
                if self.rect.top < wall.rect.bottom and self.rect.bottom > wall.rect.top:
                    if self.rect.right + 10 <= wall.rect.left and self.rect.right + 80 >= wall.rect.left:
                        blockedRight = True
                    if self.rect.left + -10 > wall.rect.right and self.rect.left - 80 < wall.rect.right:
                        blockedLeft = True
            if random.randint(1,2)==1:
                if not blockedLeft:
                    self.velocity_x = -5
                elif not blockedRight:
                    self.velocity_x = 5
            else:
                if not blockedRight:
                    self.velocity_x = 5
                elif not blockedLeft:
                    self.velocity_x = -5


    def die(self):
        if (self.deathTimer > 0):
            self.deathTimer -= 1
        if self.rect.y > SCREENHEIGHT and self.deathTimer==0:
                self.deathTimer = 50
                self.rect.x = 32
                self.rect.y = 0
                game.life += 1
        else:
            for enemy in game.enemyList[game.levelCounter]:
                if self.rect.colliderect(enemy) and self.deathTimer==0:
                    self.deathTimer = 50
                    self.rect.x = 32
                    self.rect.y = 0
                    game.life += 1


    def update(self):
        if self.name=="Player":
            self.getInput()
            self.die()
        else:
            self.AI()

        self.movement()
        self.collide()

        if self.name=="Player":
            self.drawPlayer()
        else:
            self.drawEnemy()
