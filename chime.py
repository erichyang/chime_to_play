import os

import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT


class Chime(pygame.sprite.Sprite):

    def __init__(self):
        super(Chime, self).__init__()
        self.surf = pygame.Surface((25, 100))
        CHIME_IMG = pygame.image.load(os.path.join('assets', 'chime'))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
