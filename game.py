import pygame
import sys
from load_level import load_level
from load_level import all_sprites
from go import go_dawn, go_up, go_left, go_right
from start_screen import start_screen, screen
from end_screen import end_screen
from generation_map import generation_map

s = pygame.mixer.Sound("sounds/the-end-sound-effect.mp3")
FPS = 50
x, y = -5, -5
generation_map()
load_level('map.txt', x, y, 'none')
pause = False
vol = 1.0
start_screen()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_F8:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_F9:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_DOWN:
                sost, x, y = go_dawn()
                if sost == 'do':
                    load_level('map.txt', x, y, 'dawn')
            elif event.key == pygame.K_UP:
                sost, x, y = go_up()
                if sost == 'win':
                    vol = 0.0
                    pygame.mixer.music.set_volume(vol)
                    s.play()
                    end_screen()
                if sost == 'do':
                    load_level('map.txt', x, y, 'up')
            elif event.key == pygame.K_LEFT:
                sost, x, y = go_left()
                if sost == 'do':
                    load_level('map.txt', x, y, 'left')
            elif event.key == pygame.K_RIGHT:
                sost, x, y = go_right()
                if sost == 'do':
                    load_level('map.txt', x, y, 'right')
    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
