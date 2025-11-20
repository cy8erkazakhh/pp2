import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SNAKE")

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_apple(apple, color):
    pygame.draw.rect(screen, color, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def generate_apple():
    return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

game_over_image = pygame.image.load('./assets/game_over.jpg')
game_over_rect = game_over_image.get_rect()
game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
dx, dy = 0, 0

food_types = [RED, BLUE]
food_timers = [5, 7]
foods = [(generate_apple(), random.choice(food_types), time.time()) for _ in range(len(food_types))]

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 1, 0

    current_time = time.time()
    for i in range(len(foods)):
        if current_time - foods[i][2] >= food_timers[i]:
            foods[i] = (generate_apple(), random.choice(food_types), current_time)

    new_head = (snake[0][0] + dx, snake[0][1] + dy)

    if (
        new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT
    ):
        screen.blit(game_over_image, game_over_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
        continue

    if dx != 0 or dy != 0:
        if new_head in snake:
            screen.blit(game_over_image, game_over_rect)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
            continue

    snake.insert(0, new_head)

    for food in foods:
        if snake[0] == food[0]:
            snake.append(snake[-1])
            foods.remove(food)
            foods.append((generate_apple(), random.choice(food_types), current_time))
            break
    else:
        snake.pop()

    if (
        snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or
        snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT
    ):
        screen.blit(game_over_image, game_over_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    draw_snake(snake)
    for food in foods:
        draw_apple(food[0], food[1])

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
