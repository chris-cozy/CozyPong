import pygame
import sys
from random import randint
from sprites.paddle import Paddle
from sprites.ball import Ball
from screen import Screen
from utils.constants import SCREEN_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_COLOR, CAPTION, P_WIDTH, P_HEIGHT, B_HEIGHT, B_WIDTH, SCORE_LIMIT, BOUNCE_COOLDOWN, SPRITE_COLORS

pygame.init()
clock = pygame.time.Clock()

player_color = SPRITE_COLORS[randint(0, 3)]
enemy_color = SPRITE_COLORS[randint(0, 3)]
ball_color = SPRITE_COLORS[randint(0, 3)]

player_x, player_y = 0, ((SCREEN_HEIGHT/2) - (P_HEIGHT/2))
enemy_x, enemy_y = (SCREEN_WIDTH - P_WIDTH), ((SCREEN_HEIGHT/2) - (P_HEIGHT/2))
ball_x, ball_y = (SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)

# Screen Initialization #
screen = Screen(CAPTION, SCREEN_SIZE, SCREEN_WIDTH,
                SCREEN_HEIGHT, SCREEN_COLOR)

# Paddles and Ball Initialization #
player_paddle = Paddle(player_color, P_WIDTH, P_HEIGHT, True)
enemy_paddle = Paddle(enemy_color, P_WIDTH, P_HEIGHT, False)
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

screen.title_screen()
waiting_for_input = True
while waiting_for_input:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                waiting_for_input = False

playing = True
paused = False

### GAME LOOP ###
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = True

    if (paused):
        screen.paused()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Press 'P' to resume
                    paused = False
                if event.key == pygame.K_q:  # Press 'P' to resume
                    pygame.quit()
                    sys.exit()
    # Scoring #
    if (enemy_score >= SCORE_LIMIT) or (player_score >= SCORE_LIMIT):
        # Display winner and options
        screen.display_winner(player_score)
        screen.display_restart_or_quit()
        pygame.display.flip()

        # Wait for player input
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    waiting_for_input = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player_score = 0
                        enemy_score = 0
                        waiting_for_input = False
                    elif event.key == pygame.K_q:
                        playing = False
                        waiting_for_input = False

    player_paddle.check_keys()

    sprite_list.update()

    val = ball.wall_bounce(SCREEN_WIDTH, SCREEN_HEIGHT, BOUNCE_COOLDOWN)

    if (val == 1):
        player_score += 1
    elif (val == -1):
        enemy_score += 1

    # Enemy AI #
    if ball.velocity[0] > 0:
        predicted_impact_point = ball.rect.centery
        reaction_time = 0.2  # AI reaction speed
        if ball.velocity[1] > 0:
            predicted_impact_point += reaction_time * ball.velocity[1]
        else:
            predicted_impact_point -= reaction_time * abs(ball.velocity[1])

        if enemy_paddle.rect.centery < predicted_impact_point:
            enemy_paddle.move_down(enemy_paddle.velocity)
        elif enemy_paddle.rect.centery > predicted_impact_point:
            enemy_paddle.move_up(enemy_paddle.velocity)

    # Collisions #
    if pygame.sprite.collide_mask(ball, player_paddle):
        ball.paddle_bounce(player_paddle)
    elif pygame.sprite.collide_mask(ball, enemy_paddle):
        ball.paddle_bounce(enemy_paddle)

    # Screen Logic #
    screen.fill()
    screen.draw(sprite_list)
    screen.display_text(player_score, enemy_score, player_color, enemy_color)
    screen.flip()

    clock.tick(60)

pygame.quit()
