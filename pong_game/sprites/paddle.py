import pygame

BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = 5

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move_up(self, pixels):
        self.rect.y -= pixels

    def move_down(self, pixels):
        self.rect.y += pixels

    def check_keys(self, pHeight, screenHeight):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if (self.rect.y > 0):
                self.move_up(self.velocity)

        if keys[pygame.K_DOWN]:
            if (self.rect.y + pHeight) < screenHeight:
                self.move_down(self.velocity)
