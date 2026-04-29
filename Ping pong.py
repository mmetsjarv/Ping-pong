import pygame
import sys

# 1. Mängu seadistamine
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
TAUST = (153, 232, 158)
TEXT_COLOR = (0, 102, 51)

# Skoori värv
SCORE_COLOR = (0, 102, 51)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping pong - Metsjärv")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 24, bold=True)

# Piltide lisamine
ball_img = pygame.image.load("ball.png")
ball_img = pygame.transform.scale(ball_img, (20, 20))

paddle_img = pygame.image.load("pad.png")
paddle_img = pygame.transform.scale(paddle_img, (120, 20))

# Objektid
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 4
ball_speed_x = 4
ball_speed_y = 4

paddle_width = 120
paddle_height = 20
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = int(SCREEN_HEIGHT / 1.5)
paddle_speed = 5

score = 0

# Mängu põhitsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Liikumine
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    paddle_x += paddle_speed
    if paddle_x <= 0 or paddle_x + paddle_width >= SCREEN_WIDTH:
        paddle_speed *= -1

    # Põrked seintega
    if ball_x <= 0 or ball_x + 20 >= SCREEN_WIDTH:
        ball_speed_x *= -1

    if ball_y <= 0:
        ball_speed_y *= -1

    if ball_y + 20 >= SCREEN_HEIGHT:
        score -= 1
        ball_y = SCREEN_HEIGHT // 4
        ball_speed_y *= -1

    # Kokkupõrkete tuvastamine
    ball_rect = pygame.Rect(ball_x, ball_y, 20, 20)
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    if ball_rect.colliderect(paddle_rect):
        if ball_speed_y > 0:
            ball_speed_y *= -1
            score += 1

    # Joonistamine
    screen.fill(TAUST)

    screen.blit(ball_img, (ball_x, ball_y))
    screen.blit(paddle_img, (paddle_x, paddle_y))

    # Skoori kuvamine valitud värviga
    score_text = font.render(f"Skoor: {score}", True, (0, 102, 51))
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
