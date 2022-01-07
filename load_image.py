import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print('No File!')
        sys.exit()
    image = pygame.image.load(fullname)
    return image