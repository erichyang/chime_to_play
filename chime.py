import os
import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT


class Chime(pygame.sprite.Sprite):

    def __init__(self):
        super(Chime, self).__init__()
        self.surf = pygame.Surface((25, 100))
        self.surf.fill((0, 0, 0))
        self.cords = [100, 100]
        self.img = pygame.image.load(os.path.join('assets', 'chime1.png'))

        self.width = 10000  # Need width of picture
        self.height = 10000  # Need height of picture
        self.mass = 10  # Change based on Chime size
        self.moment_of_inertia = self.mass * (self.width * self.width + self.height * self.height) / 12
        self.position = (100, 100)
        self.linear_velocity = 'list'
        self.angle = 0
        self.angular_velocity = 0
        self.force = 'list'
        self.torque = 0

    # Draws all chimes
    def draw_chimes(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (300, 300), 20, 2)
        pygame.draw.circle(screen, (0, 0, 0), (self.position[0], self.position[1]), 20, 1)

    # Move the sprite based on user key presses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.cords[1] -= 5
        if pressed_keys[K_DOWN]:
            self.cords[1] += 5
        if pressed_keys[K_LEFT]:
            self.cords[0] -= 5
        if pressed_keys[K_RIGHT]:
            self.cords[0] += 5
