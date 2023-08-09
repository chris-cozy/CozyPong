"""
This module contains the Screen class, representing the screen object in the Pong game.
"""
import pygame

pygame.init()


class Screen():
    """
    Represents the screen object.
    """

    def __init__(self, caption, screen_size, screen_width, screen_height, screen_color):
        """
        Initialize the screen with size, width, height, color, and a caption.
        """
        super().__init__()

        pygame.display.set_caption(caption)

        self.surface = pygame.display.set_mode(screen_size)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_color = screen_color

    def fill(self):
        """
        Fill the screen with the color.
        """
        self.surface.fill(self.screen_color)

    def draw(self, sprite_list):
        """
        Draw the list of sprites on the screen.
        """
        sprite_list.draw(self.surface)

    def display_text(self, player_score, enemy_score, player_color, enemy_color):
        """
        Display text on the screen. Player's score, Enemy's score, Player color, Enemy color.
        """
        font = pygame.font.Font(None, 74)
        text = font.render(str(player_score), 1, player_color)
        self.surface.blit(text, (self.screen_width/4, 10))
        text = font.render(str(enemy_score), 1, enemy_color)
        self.surface.blit(text, ((self.screen_width/4) * 3, 10))

    def flip(self):
        """
        Flip the screen.
        """
        pygame.display.flip()