import pygame
import sys
from random import randint
from paddle import Paddle
from ball import Ball
from screen import Screen

### CONSTANTS ###
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500
SCREEN_COLOR = (246, 224, 181)
CAPTION = "Cozy Pong"
P_WIDTH, P_HEIGHT = 10, 100
B_WIDTH, B_HEIGHT = 15, 15
SCORE_LIMIT = 5

pygame.init()
clock = pygame.time.Clock()

spriteColors = [
    (102, 84, 94),
    (163, 145, 147),
    (170, 111, 115),
    (238, 169, 144)
]
playerColor = spriteColors[randint(0, 3)]
enemyColor = spriteColors[randint(0, 3)]
ballColor = spriteColors[randint(0, 3)]

playerX, playerY = 0, ((SCREEN_HEIGHT/2) - (P_HEIGHT/2))
enemyX, enemyY = (SCREEN_WIDTH - P_WIDTH), ((SCREEN_HEIGHT/2) - (P_HEIGHT/2))
ballX, ballY = (SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)

# Screen Initialization #
screen = Screen(CAPTION, SCREEN_SIZE, SCREEN_WIDTH,
                SCREEN_HEIGHT, SCREEN_COLOR)

# Paddles and Ball Initialization #
playerPaddle = Paddle(playerColor, P_WIDTH, P_HEIGHT)
enemyPaddle = Paddle(enemyColor, P_WIDTH, P_HEIGHT)
ball = Ball(ballColor, B_WIDTH, B_HEIGHT)

playerPaddle.set_pos(playerX, playerY)
enemyPaddle.set_pos(enemyX, enemyY)
ball.set_pos(ballX, ballY)

# Sprite group setup #
spriteList = pygame.sprite.Group()
spriteList.add(playerPaddle)
spriteList.add(enemyPaddle)
spriteList.add(ball)

playerScore, enemyScore = 0, 0

playing = True

### GAME LOOP ###
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    if (enemyScore >= SCORE_LIMIT) or (playerScore >= SCORE_LIMIT):
        playing = False

    playerPaddle.check_keys(P_HEIGHT, SCREEN_HEIGHT)

    spriteList.update()

    val = ball.wall_bounce(SCREEN_WIDTH, B_WIDTH, SCREEN_HEIGHT, B_HEIGHT)

    if (val == 1):
        playerScore += 1
    elif (val == -1):
        enemyScore += 1

    # Enemy AI #
    if ball.velocity[0] > 0:
        if ball.velocity[1] > 0:
            if (enemyPaddle.rect.y + P_HEIGHT) < SCREEN_HEIGHT:
                enemyPaddle.move_down(enemyPaddle.velocity)
        else:
            if (enemyPaddle.rect.y > 0):
                enemyPaddle.move_up(enemyPaddle.velocity)

    # Collisions #
    if pygame.sprite.collide_mask(ball, playerPaddle) or pygame.sprite.collide_mask(ball, enemyPaddle):
        ball.paddle_bounce()

    # Screen Logic #
    screen.fill()
    screen.draw(spriteList)
    screen.display_text(playerScore, enemyScore, playerColor, enemyColor)
    screen.flip()

    clock.tick(60)

pygame.quit()
