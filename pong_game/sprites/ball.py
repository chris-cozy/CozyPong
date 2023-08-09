"""
This module contains the Ball class, representing the ball object in the Pong game.
"""
import pygame
from random import randint
from utils.constants import BLACK


class Ball(pygame.sprite.Sprite):
    """
    Represents the ball in the Pong game.

    Attributes:
        color (tuple): RGB color tuple for the ball.
        width (int): Width of the ball.
        height (int): Height of the ball.
    """

    def __init__(self, color, width, height):
        """
        Initialize the ball with given color, width, and height.
        """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        """
        Set the position of the ball based on coords.
        """
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """
        Update the ball's position based on its velocity.
        """
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def paddle_bounce(self):
        """
        Change the ball's velocity upon colliding with a paddle.
        """
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def wall_bounce(self, screen_width, ball_width, screen_height, ball_height):
        """
        Handle bouncing off the walls and scoring.
        """
        val = 0
        if self.rect.x >= (screen_width - ball_width):
            self.velocity[0] = -self.velocity[0]
            val = 1
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
            val = -1
        if self.rect.y >= (screen_height - ball_height):
            self.velocity[1] = -self.velocity[1]
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

        return val
