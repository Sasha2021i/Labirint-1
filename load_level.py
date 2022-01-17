import pygame
from load_image import load_image

all_sprites = pygame.sprite.Group()
image = load_image("mario.png")
image = pygame.transform.scale(image, (40, 50))
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png'),
    'mario': image
}


def load_level(filename, x, y, napr):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        data = mapFile.readlines()
        for j in range(len(data)):
            if j != len(data) - 1:
                data[j] = data[j][:-1]
        if x == -5 and y == -5:
            for j in range(len(data)):
                for i in range(len(data)):
                    sprite = pygame.sprite.Sprite()
                    if data[j][i] == '.':
                        sprite.image = tile_images['empty']
                    elif data[j][i] == '#':
                        sprite.image = tile_images['wall']
                    else:
                        sprite.image = tile_images['mario']
                    sprite.rect = sprite.image.get_rect()
                    sprite.rect.x = 50 * i
                    sprite.rect.y = 50 * j
                    all_sprites.add(sprite)
        else:
            for j in range(len(data)):
                if napr == 'dawn':
                    if j == y or j == y + 1:
                        for i in range(len(data)):
                            if i == x:
                                sprite = pygame.sprite.Sprite()
                                if data[j][i] == '.':
                                    sprite.image = tile_images['empty']
                                elif data[j][i] == '#':
                                    sprite.image = tile_images['wall']
                                else:
                                    sprite.image = tile_images['mario']
                                sprite.rect = sprite.image.get_rect()
                                sprite.rect.x = 50 * i
                                sprite.rect.y = 50 * j
                                all_sprites.add(sprite)

                elif napr == 'up':
                    if j == y or j == y - 1:
                        for i in range(len(data)):
                            if i == x:
                                sprite = pygame.sprite.Sprite()
                                if data[j][i] == '.':
                                    sprite.image = tile_images['empty']
                                elif data[j][i] == '#':
                                    sprite.image = tile_images['wall']
                                else:
                                    sprite.image = tile_images['mario']
                                sprite.rect = sprite.image.get_rect()
                                sprite.rect.x = 50 * i
                                sprite.rect.y = 50 * j
                                all_sprites.add(sprite)

                elif napr == 'right':
                    if j == y:
                        for i in range(len(data)):
                            if i == x or i == x + 1:
                                sprite = pygame.sprite.Sprite()
                                if data[j][i] == '.':
                                    sprite.image = tile_images['empty']
                                elif data[j][i] == '#':
                                    sprite.image = tile_images['wall']
                                else:
                                    sprite.image = tile_images['mario']
                                sprite.rect = sprite.image.get_rect()
                                sprite.rect.x = 50 * i
                                sprite.rect.y = 50 * j
                                all_sprites.add(sprite)

                else:
                    if j == y:
                        for i in range(len(data)):
                            if i == x or i == x - 1:
                                sprite = pygame.sprite.Sprite()
                                if data[j][i] == '.':
                                    sprite.image = tile_images['empty']
                                elif data[j][i] == '#':
                                    sprite.image = tile_images['wall']
                                else:
                                    sprite.image = tile_images['mario']
                                sprite.rect = sprite.image.get_rect()
                                sprite.rect.x = 50 * i
                                sprite.rect.y = 50 * j
                                all_sprites.add(sprite)


