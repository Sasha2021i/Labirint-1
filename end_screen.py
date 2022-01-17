import sys

import pygame
from settings import WIDTH, HEIGHT
from start_screen import screen


def end_screen():
    intro_text = ["                                                    ПОБЕДА!!!", "",
                  "                                  Поздравляем, вы прошли игру."]
    surf = pygame.Surface((WIDTH, HEIGHT))
    screen.blit(surf, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 150
    screen.fill((0, 0, 100))
    pygame.mixer.music.load("sounds/super-mario-saundtrek.mp3")
    pygame.mixer.music.play(0)
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()