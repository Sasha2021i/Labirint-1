import sys

import pygame
from settings import WIDTH, HEIGHT
from load_image import load_image

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def start_screen():
    intro_text = ["ЛАБИРИНТ",
                  "Правила",
                  "просто доберись до конца лабиринта", "", "", "", "жми любую клавишу чтобы продолжть", "удачи!"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
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
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
