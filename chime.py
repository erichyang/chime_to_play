import os
import time

import pygame
import random
import math
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT


class Chime(pygame.sprite.Sprite):

    def __init__(self, num):
        super(Chime, self).__init__()
        self.surf = pygame.Surface((50, 100))
        self.surf.fill((255, 0, 255))
        self.surf.set_colorkey((255, 0, 255))
        sound = ['A', 'C', 'D', 'E', 'G']
        self.id = num
        self.sound = f'./assets/audio/{sound[num]}6.mp3'
        num += 1
        self.img = pygame.image.load(os.path.join('assets', f'chime{num}.png'))
        self.width = self.img.get_size()[0]
        self.height = self.img.get_size()[1]
        self.cords = [900-(self.width+100)*(5-num), 300]
        self.mass = self.width * self.height / 100  # Change based on Chime size

        self.rect = pygame.Rect(self.cords[0], self.cords[1], self.width, self.height)

        self.moment_of_inertia = self.mass * (self.width * self.width + self.height * self.height) / 12
        self.position = [300, 300]
        self.linear_velocity = 0
        self.angle = 0
        self.angular_velocity = 0
        self.force = [0, 0]
        self.torque = 0

        self.rect = self.img.get_rect(center=(self.position[0], self.position[1]))
        self.mask = pygame.mask.from_surface(self.img)

    # Draws all chimes
    def draw_chimes(self, screen, topleft, angle):
        rotated_image = pygame.transform.rotate(self.img, angle)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=topleft).center)
        screen.blit(rotated_image, new_rect)
        self.rect = rotated_image.get_rect(center=self.img.get_rect(topleft=topleft).center)
        self.mask = pygame.mask.from_surface(rotated_image)
    # Initialize rigid bodies and give random parameters
    def init_chimes(self):
        self.position = [300, 300]
        self.angle = random.randint(0, 360) / 360 * math.pi * 2
        self.linear_velocity = [0, 0]
        self.angular_velocity = 0

        self.mass = 10
        self.width = 10
        self.height = 10
        self.moment_of_inertia = self.mass * (self.width * self.width + self.height * self.height) / 12

    def computeFAT(self):
        self.force = [0, 0]
        r = [self.width / 2, self.height / 2]
        self.torque = r[0] * self.force[1] - r[1] * self.force[0]

    def run_sim(self, screen):
        dt = 1
        self.computeFAT()
        self.draw_chimes(screen, (self.position[0], self.position[1]), self.angle)
        linear_acceleration = [self.force[0] / self.mass, self.force[1] / self.mass]
        self.linear_velocity[0] += linear_acceleration[0] * dt
        self.linear_velocity[1] += linear_acceleration[1] * dt
        self.position[0] += self.linear_velocity[0] * dt
        self.position[1] += self.linear_velocity[1] * dt
        angular_acceleration = self.torque / self.moment_of_inertia
        self.angular_velocity += angular_acceleration * dt
        self.angle += self.angular_velocity * dt
        self.angle += 1
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
