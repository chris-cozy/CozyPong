import pygame

pygame.init()


class Screen():

    def __init__(self, caption, screenSize, screenWidth, screenHeight, screenColor):
        super().__init__()

        pygame.display.set_caption(caption)

        self.surface = pygame.display.set_mode(screenSize)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screenColor = screenColor

    def fill(self):
        self.surface.fill(self.screenColor)

    def draw(self, spriteList):
        spriteList.draw(self.surface)

    def display_text(self, playerScore, enemyScore, playerColor, enemyColor):
        font = pygame.font.Font(None, 74)
        text = font.render(str(playerScore), 1, playerColor)
        self.surface.blit(text, (self.screenWidth/4, 10))
        text = font.render(str(enemyScore), 1, enemyColor)
        self.surface.blit(text, ((self.screenWidth/4) * 3, 10))

    def flip(self):
        pygame.display.flip()
