import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x = WIDTH // 2
y = HEIGHT // 2
step = 20

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - radius - step >= 0:
        y -= step
    if keys[pygame.K_DOWN] and y + radius + step <= HEIGHT:
        y += step
    if keys[pygame.K_LEFT] and x - radius - step >= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + radius + step <= WIDTH:
        x += step

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.flip()

    clock.tick(30)