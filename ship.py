import pygame
WHITE = (255, 255, 255)


class Ship(pygame.sprite.Sprite):

    def __init__(self, color, width, height, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = [0, 0]
        self.magnitude = 6
        self.dead = False

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move_left()
        if key[pygame.K_RIGHT]:
            self.move_right()
        if key[pygame.K_UP]:
            self.move_up()
        if key[pygame.K_DOWN]:
            self.move_down()

    def move_left(self):
        self.vel[0] -= self.magnitude

    def move_right(self):
        self.vel[0] += self.magnitude

    def move_down(self):
        self.vel[1] += self.magnitude

    def move_up(self):
        self.vel[1] -= self.magnitude

    def move(self, width, height):
        if not self.dead:
            B = 0.08
            if self.rect.x > width - self.width/2:
                self.rect.x = width-self.width/2
                self.vel = [0, 0]
            if self.rect.x < self.width/2:
                self.rect.x = self.width/2
                self.vel = [0, 0]
            if self.rect.y > height - self.height:
                self.rect.y = height-self.height
                self.vel = [0, 0]
            if self.rect.y < 0:
                self.rect.y = 0
                self.vel = [0, 0]
            self.vel[0] -= self.vel[0] * B
            self.vel[1] -= self.vel[1] * B
            self.rect.move_ip(self.vel[0], self.vel[1])

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.vel = [0, 0]

    def collides_with(self, r):
        if (r.rect.colliderect(self.rect)):
            return True
        return False

    def stop(self):
        self.vel = [0, 0]
        self.dead = True

    def reset(self):
        self.dead = False
        self.rect.x = 300
        self.rect.y = 440
        self.vel = [0, 0]
