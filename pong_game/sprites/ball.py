"""
This module contains the Ball class, representing the ball object in the Pong game.
"""
import pygame
from random import randint
import math
from utils.constants import BLACK, VELOCITY_BOOST


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

    def paddle_bounce(self, paddle):
        """
        Change the ball's velocity upon colliding with a paddle.
        Calculate the angle of reflection based on where the ball hits the paddle, and apply to the velocity.
        Increase the ball speed after each hit
        """
        ball_center = self.rect.centery
        paddle_center = paddle.rect.centery
        relative_intersection = (
            paddle_center - ball_center) / (paddle.rect.height / 2)

        reflection_angle = relative_intersection * \
            (math.pi / 4)  # Maximum reflection angle

        # Apply reflection to ball's velocity
        if(paddle.player):
            ball_speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        else:
            ball_speed = -math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

        self.velocity[0] = ball_speed * math.cos(reflection_angle)
        self.velocity[1] = ball_speed * -math.sin(reflection_angle)

        # Increase ball speed slightly for added challenge
        self.velocity[0] *= VELOCITY_BOOST
        self.velocity[1] *= VELOCITY_BOOST
        paddle.increase_velocity()

    def wall_bounce(self, screen_width, screen_height, cooldown_time):
        """
        Handle bouncing off the walls and scoring.

        Args:
            screen_width (int): Width of the game screen.
            screen_height (int): Height of the game screen.
            cooldown_time (int): Cooldown time in milliseconds.
        Returns:
            int: Value indicating scoring (1, -1, or 0).
        """
        val = 0
        if self.rect.x >= (screen_width - self.rect.width):
            if self.velocity[0] > 0:  # Check for positive X velocity to avoid rapid bounces
                self.velocity[0] = -self.velocity[0]
                val = 1
            # Introduce a cooldown after bouncing
            pygame.time.wait(cooldown_time)
        if self.rect.x <= 0:
            if self.velocity[0] < 0:  # Check for negative X velocity to avoid rapid bounces
                self.velocity[0] = -self.velocity[0]
                val = -1
            # Introduce a cooldown after bouncing
            pygame.time.wait(cooldown_time)
        if self.rect.y >= (screen_height - self.rect.height):
            self.velocity[1] = -self.velocity[1]
            # Introduce a cooldown after bouncing
            pygame.time.wait(cooldown_time)
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]
            # Introduce a cooldown after bouncing
            pygame.time.wait(cooldown_time)

        return val
