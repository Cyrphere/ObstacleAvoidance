import sys
import pygame

pygame.init()


white = (255, 255, 255)


class Obj(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, is_goal=False):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        pygame.draw.rect(self.image, color, [
                         40, 40, width, height])  # why 40,40
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.is_goal = is_goal

    def collides_with(self, other):
        if other.rect.colliderect(self.rect):
            return True
        return False
