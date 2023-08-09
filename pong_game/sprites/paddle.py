import pygame

"""
This module contains the Paddle class, representing the paddle objects in the Pong game.
"""
BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    """
    Represents the paddles in the Pong game.

    Attributes:
        color (tuple): RGB color tuple for the paddle.
        width (int): Width of the paddle.
        height (int): Height of the paddle.
    """

    def __init__(self, color, width, height):
        """
        Initialize the paddle with given color, width, and height.
        """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = 5

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        """
        Set the position of the paddle based on coords.
        """
        self.rect.x = x
        self.rect.y = y

    def move_up(self, pixels):
        """
        Move the paddle up by given number of pixels.
        """
        self.rect.y -= pixels

    def move_down(self, pixels):
        """
        Move the paddle down by given number of pixels.
        """
        self.rect.y += pixels

    def check_keys(self, paddle_height, screen_height):
        """
        Check and handle keyboard input for paddle movement.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if (self.rect.y > 0):
                self.move_up(self.velocity)

        if keys[pygame.K_DOWN]:
            if (self.rect.y + paddle_height) < screen_height:
                self.move_down(self.velocity)
