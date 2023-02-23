import pygame
import sys
from paddle import Paddle

pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screenColor = (255, 204, 203)
pygame.display.set_caption("Cozy Pong")
surface = pygame.display.set_mode(SCREEN_SIZE)


# Player Paddle
rectColor = (119, 198, 110)
rectWidth, rectHeight = 10, 100
rectX, rectY = 0, (SCREEN_HEIGHT/2)
rectSpeed = 1

playerPaddle = Paddle(rectColor, rectWidth, rectHeight)
playerPaddle.rect.x = rectX
playerPaddle.rect.y = rectY


spriteList = pygame.sprite.Group()
spriteList.add(playerPaddle)

playing = True

clock = pygame.time.Clock()

# GAME LOOP
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if (playerPaddle.rect.y > 0):
            playerPaddle.move_up(5)

    if keys[pygame.K_DOWN]:
        if (playerPaddle.rect.y + rectHeight) < SCREEN_HEIGHT:
            playerPaddle.move_down(5)

    spriteList.update()

    surface.fill(screenColor)

    spriteList.draw(surface)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
