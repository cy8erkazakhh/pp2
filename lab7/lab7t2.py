import pygame
import os
import sys

pygame.init()
pygame.mixer.init()

MUSIC_DIR = "music_player"

playlist = [os.path.join(MUSIC_DIR, f) for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
playlist.sort()

if not playlist:
    print("Нет музыкальных файлов в папке music_player!")
    sys.exit()

current_index = 0
is_playing = False

screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Keyboard Music Player")
font = pygame.font.Font(None, 36)

def play_music(index):
    global is_playing
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    is_playing = True
    print(f"▶️ Playing: {os.path.basename(playlist[index])}")

def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    print("⏹️ Stopped")

def next_music():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    play_music(current_index)

def prev_music():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    play_music(current_index)

play_music(current_index)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    stop_music()
                else:
                    play_music(current_index)
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()
            elif event.key == pygame.K_ESCAPE:
                running = False

    # --- Отображение состояния ---
    screen.fill((30, 30, 30))
    text = font.render(f"Now: {os.path.basename(playlist[current_index])}", True, (255, 255, 255))
    screen.blit(text, (50, 80))
    pygame.display.flip()

pygame.quit()
sys.exit()