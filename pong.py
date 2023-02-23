import pygame
import sys
from random import randint
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
spriteColors = [
    (102, 84, 94),
    (163, 145, 147),
    (170, 111, 115),
    (238, 169, 144)
]
screenColor = (246, 224, 181)
playerColor = spriteColors[randint(0, 3)]
enemyColor = spriteColors[randint(0, 3)]
ballColor = spriteColors[randint(0, 3)]

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
pygame.display.set_caption("Cozy Pong")
surface = pygame.display.set_mode(SCREEN_SIZE)


rectWidth, rectHeight = 10, 100
ballWidth, ballHeight = 15, 15
rectX, rectY = 0, ((SCREEN_HEIGHT/2) - (rectHeight/2))

# Player Paddle
playerPaddle = Paddle(playerColor, rectWidth, rectHeight)
playerPaddle.rect.x = rectX
playerPaddle.rect.y = rectY

# Enemy Paddle
enemyPaddle = Paddle(enemyColor, rectWidth, rectHeight)
enemyPaddle.rect.x = SCREEN_WIDTH - rectWidth
enemyPaddle.rect.y = rectY

# Ball


ball = Ball(ballColor, ballWidth, ballHeight)
ball.rect.x = SCREEN_WIDTH/2
ball.rect.y = SCREEN_HEIGHT/2


spriteList = pygame.sprite.Group()
spriteList.add(playerPaddle)
spriteList.add(enemyPaddle)
spriteList.add(ball)

playing = True

clock = pygame.time.Clock()

# Scoring
playerScore = 0
enemyScore = 0

# GAME LOOP
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    if (enemyScore >= 5) or (playerScore >= 5):
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
        playerScore += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        enemyScore += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= (SCREEN_HEIGHT - ballHeight):
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    # enemy ai
    if ball.velocity[0] > 0:
        if ball.velocity[1] > 0:
            if (enemyPaddle.rect.y + rectHeight) < SCREEN_HEIGHT:
                enemyPaddle.move_down(enemyPaddle.velocity)
        else:
            if (enemyPaddle.rect.y > 0):
                enemyPaddle.move_up(enemyPaddle.velocity)

    # Collisions
    if pygame.sprite.collide_mask(ball, playerPaddle) or pygame.sprite.collide_mask(ball, enemyPaddle):
        ball.bounce()

    surface.fill(screenColor)

    spriteList.draw(surface)

    # Displaying scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(playerScore), 1, playerColor)
    surface.blit(text, (SCREEN_WIDTH/4, 10))
    text = font.render(str(enemyScore), 1, enemyColor)
    surface.blit(text, ((SCREEN_WIDTH/4) * 3, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
