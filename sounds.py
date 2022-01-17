import pygame

pygame.init()

pygame.mixer.music.load("sounds/super-mario-saundtrek.mp3")

W, H = 500, 300

clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)