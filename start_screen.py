import sys

import pygame
from settings import WIDTH, HEIGHT
from load_image import load_image

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def start_screen():
    intro_text = ["ЛАБИРИНТ",
                  "Правила",
                  "Просто доберись до конца лабиринта", "", "", "", "Жми любую клавишу чтобы продолжть", "Удачи!"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
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
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.load("sounds/super-mario-saundtrek.mp3")
                pygame.mixer.music.play(-1)
                return
        pygame.display.flip()
