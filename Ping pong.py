import pygame
import sys

# Käivitab pygame mooduli
pygame.init()

# Mänguakna mõõtmed
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Taustavärv (hele roheline)
TAUST = (153, 232, 158)

# Skoori värv
SCORE_COLOR = (0, 102, 51)

# Loob mänguakna
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Akna pealkiri
pygame.display.set_caption("Ping pong 1 - Metsjärv")

# Kell mängu kaadrisageduse kontrollimiseks
clock = pygame.time.Clock()

# Fondi loomine skoori kuvamiseks
font = pygame.font.SysFont("comicsansms", 24, bold=True)

# Palli pilt ja suuruse muutmine
ball_img = pygame.image.load("ball.png")
ball_img = pygame.transform.scale(ball_img, (20, 20))

# Aluse pilt ja suuruse muutmine
paddle_img = pygame.image.load("pad.png")
paddle_img = pygame.transform.scale(paddle_img, (120, 20))

# Palli algasukoht
ball_x = SCREEN_WIDTH - 30
ball_y = 10

# Palli kiirus
ball_speed_x = 4
ball_speed_y = 4

# Aluse algväärtused
paddle_width = 120
paddle_height = 20

# Aluse algasukoht ekraani keskel
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = int(SCREEN_HEIGHT / 1.5)

# Aluse automaatse liikumise kiirus
paddle_speed = 5

# Mängija algpunktid
score = 0

# Mängu põhitsükkel
running = True
while running:

    # Sündmuste kontrollimine
    for event in pygame.event.get():
        # Akna sulgemise kontroll
        if event.type == pygame.QUIT:
            running = False

    # Palli liigutamine
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Aluse automaatne liikumine
    paddle_x += paddle_speed

    # Kui alus jõuab servani, muudab suunda
    if paddle_x <= 0 or paddle_x + paddle_width >= SCREEN_WIDTH:
        paddle_speed *= -1

    # Vasak ja parem sein
    if ball_x <= 0 or ball_x + 20 >= SCREEN_WIDTH:
        ball_speed_x *= -1

    # Ülemine sein
    if ball_y <= 0:
        ball_speed_y *= -1

    # Alumine sein
    if ball_y + 20 >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # Loob ristkülikud kokkupõrke kontrollimiseks
    ball_rect = pygame.Rect(ball_x, ball_y, 20, 20)
    paddle_rect = pygame.Rect(
        paddle_x,
        paddle_y,
        paddle_width,
        paddle_height
    )

    # Kui pall puudutab alust
    if ball_rect.colliderect(paddle_rect):

        # Kontrollib, et pall liiguks alla
        if ball_speed_y > 0:

            # Muudab palli suunda ülespoole
            ball_speed_y *= -1

            # Lisab ühe punkti
            score += 1

    # Täidab tausta värviga
    screen.fill(TAUST)

    # Joonistab palli
    screen.blit(ball_img, (ball_x, ball_y))

    # Joonistab aluse
    screen.blit(paddle_img, (paddle_x, paddle_y))

    # Kuvab skoori
    score_text = font.render(
        f"Skoor: {score}",
        True,
        SCORE_COLOR
    )

    screen.blit(score_text, (20, 20))

    # Uuendab ekraani
    pygame.display.flip()

    # Piirab mängu kiiruse 60 FPS-ile
    clock.tick(60)

# Mängu lõpetamine
pygame.quit()
sys.exit()
