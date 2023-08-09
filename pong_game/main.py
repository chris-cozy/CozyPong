import pygame
import sys
from random import randint
from sprites.paddle import Paddle
from sprites.ball import Ball
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

sprite_colors = [
    (102, 84, 94),
    (163, 145, 147),
    (170, 111, 115),
    (238, 169, 144)
]
player_color = sprite_colors[randint(0, 3)]
enemy_color = sprite_colors[randint(0, 3)]
ball_color = sprite_colors[randint(0, 3)]

player_x, player_y = 0, ((SCREEN_HEIGHT/2) - (P_HEIGHT/2))
enemy_x, enemy_y = (SCREEN_WIDTH - P_WIDTH), ((SCREEN_HEIGHT/2) - (P_HEIGHT/2))
ball_x, ball_y = (SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)

# Screen Initialization #
screen = Screen(CAPTION, SCREEN_SIZE, SCREEN_WIDTH,
                SCREEN_HEIGHT, SCREEN_COLOR)

# Paddles and Ball Initialization #
player_paddle = Paddle(player_color, P_WIDTH, P_HEIGHT)
enemy_paddle = Paddle(enemy_color, P_WIDTH, P_HEIGHT)
ball = Ball(ball_color, B_WIDTH, B_HEIGHT)

player_paddle.set_pos(player_x, player_y)
enemy_paddle.set_pos(enemy_x, enemy_y)
ball.set_pos(ball_x, ball_y)

# Sprite group setup #
sprite_list = pygame.sprite.Group()
sprite_list.add(player_paddle)
sprite_list.add(enemy_paddle)
sprite_list.add(ball)

player_score, enemy_score = 0, 0

playing = True

### GAME LOOP ###
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    if (enemy_score >= SCORE_LIMIT) or (player_score >= SCORE_LIMIT):
        playing = False

    player_paddle.check_keys(P_HEIGHT, SCREEN_HEIGHT)

    sprite_list.update()

    val = ball.wall_bounce(SCREEN_WIDTH, B_WIDTH, SCREEN_HEIGHT, B_HEIGHT)

    if (val == 1):
        player_score += 1
    elif (val == -1):
        enemy_score += 1

    # Enemy AI #
    if ball.velocity[0] > 0:
        if ball.velocity[1] > 0:
            if (enemy_paddle.rect.y + P_HEIGHT) < SCREEN_HEIGHT:
                enemy_paddle.move_down(enemy_paddle.velocity)
        else:
            if (enemy_paddle.rect.y > 0):
                enemy_paddle.move_up(enemy_paddle.velocity)

    # Collisions #
    if pygame.sprite.collide_mask(ball, player_paddle) or pygame.sprite.collide_mask(ball, enemy_paddle):
        ball.paddle_bounce()

    # Screen Logic #
    screen.fill()
    screen.draw(sprite_list)
    screen.display_text(player_score, enemy_score, player_color, enemy_color)
    screen.flip()

    clock.tick(60)

pygame.quit()