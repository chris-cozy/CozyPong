import pygame
import sys
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screenColor = (255, 204, 203)
pygame.display.set_caption("Cozy Pong")
surface = pygame.display.set_mode(SCREEN_SIZE)


# Player Paddle
rectColor = (119, 198, 110)
rectWidth, rectHeight = 10, 100
rectX, rectY = 0, ((SCREEN_HEIGHT/2) - (rectHeight/2))

playerPaddle = Paddle(rectColor, rectWidth, rectHeight)
playerPaddle.rect.x = rectX
playerPaddle.rect.y = rectY

# Enemy Paddle

enemyPaddle = Paddle(rectColor, rectWidth, rectHeight)
enemyPaddle.rect.x = SCREEN_WIDTH - rectWidth
enemyPaddle.rect.y = rectY

# Ball
ballWidth, ballHeight = 15, 15

ball = Ball(rectColor, ballWidth, ballHeight)
ball.rect.x = SCREEN_WIDTH/2
ball.rect.y = SCREEN_HEIGHT/2


spriteList = pygame.sprite.Group()
spriteList.add(playerPaddle)
spriteList.add(enemyPaddle)
spriteList.add(ball)

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
            playerPaddle.move_up(playerPaddle.velocity)

    if keys[pygame.K_DOWN]:
        if (playerPaddle.rect.y + rectHeight) < SCREEN_HEIGHT:
            playerPaddle.move_down(playerPaddle.velocity)

    spriteList.update()

    # bouncing logic
    if ball.rect.x >= (SCREEN_WIDTH - ballWidth):
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= (SCREEN_HEIGHT - ballHeight):
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    surface.fill(screenColor)

    spriteList.draw(surface)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
