import pygame
import sys
import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

base = pygame.image.load("clock/base_micky.jpg").convert_alpha()
minute_hand = pygame.image.load("clock/minute.png").convert_alpha()
second_hand = pygame.image.load("clock/second.png").convert_alpha()

base = pygame.transform.smoothscale(base, (WIDTH, HEIGHT))
minute_hand = pygame.transform.smoothscale(minute_hand, (1200,850))
second_hand = pygame.transform.smoothscale(second_hand, (65, 650))

clock = pygame.time.Clock()

def blit_rotate_center(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, new_rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(base, (0, 0))

    now = datetime.datetime.now()
    minute = now.minute
    second = now.second + now.microsecond / 1_000_000  # для плавности

    minute_angle = -((minute / 60) * 360)
    second_angle = -((second / 60) * 360)

    blit_rotate_center(screen, minute_hand, CENTER, minute_angle)
    blit_rotate_center(screen, second_hand, CENTER, second_angle)

    pygame.display.flip()
    clock.tick(60)
    