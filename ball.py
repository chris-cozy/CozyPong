import pygame
from random import randint
BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def paddle_bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def wall_bounce(self, screenWidth, bWidth, screenHeight, bHeight):
        val = 0
        if self.rect.x >= (screenWidth - bWidth):
            self.velocity[0] = -self.velocity[0]
            val = 1
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
            val = -1
        if self.rect.y >= (screenHeight - bHeight):
            self.velocity[1] = -self.velocity[1]
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

        return val
