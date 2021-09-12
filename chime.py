import os
import time

import pygame
import random
import math
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT


class Chime(pygame.sprite.Sprite):

    def __init__(self):
        super(Chime, self).__init__()
        self.surf = pygame.Surface((25, 100))
        self.surf.fill((0, 0, 0))
        self.cords = [100, 100]
        self.img = pygame.image.load(os.path.join('assets', 'chime1.png'))

        self.width = 10  # Need width of picture
        self.height = 10  # Need height of picture
        self.mass = 10  # Change based on Chime size
        self.moment_of_inertia = self.mass * (self.width * self.width + self.height * self.height) / 12
        self.position = [300, 300]
        self.linear_velocity = 0
        self.angle = 0
        self.angular_velocity = 0
        self.force = [0, 0]
        self.torque = 0

    # Draws all chimes
    def draw_chimes(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.position[0], self.position[1], self.width, self.height))

    #Initialize rigid bodies and give random parameters
    def init_chimes(self):
        self.position = [random.randint(50, 750), random.randint(50, 750)]
        self.angle = random.randint(0, 360)/360 * math.pi * 2
        self.linear_velocity = [0, 0]
        self.angular_velocity = 0

        self.mass = 10
        self.width = 10
        self.height = 10
        self.moment_of_inertia = self.mass * (self.width * self.width + self.height * self.height) / 12

    def computeFAT(self):
        self.force = [0, 1]
        r = [self.width / 2, self.height / 2]
        self.torque = r[0] * self.force[1] - r[1] * self.force[0]

    def run_sim(self, screen):
        dt = 1
        self.computeFAT()
        self.draw_chimes(screen)
        linear_acceleration = [self.force[0] / self.mass, self.force[1] / self.mass]
        self.linear_velocity[0] += linear_acceleration[0] * dt
        self.linear_velocity[1] += linear_acceleration[1] * dt
        self.position[0] += self.linear_velocity[0] * dt
        self.position[1] += self.linear_velocity[1] * dt
        angular_acceleration = self.torque / self.moment_of_inertia
        self.angular_velocity += angular_acceleration * dt
        self.angle += self.angular_velocity * dt

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
