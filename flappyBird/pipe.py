import pygame
import random
from parameters import *


class Pipe:
    def __init__(self, x_offset):
        self.image = pygame.image.load("resources/pipe.png")
        self.rotated = pygame.transform.rotate(self.image, 180)
        self.height = 560
        self.space = 200
        self.border = 100
        self.lower = self.border - self.height # lower boundary
        self.upper = game_height - self.border - self.space - self.height # upper boundary
        self.x = screen_wight + x_offset
        self.y = self.get_random_y()
        self.rect_image = self.image.get_rect(topleft=(self.x, self.height + self.y + self.space))
        self.rect_rotated = self.rotated.get_rect(topleft=(self.x, self.y))

    def get_random_y(self):
        return random.randint(self.lower, self.upper)

    def move(self):
        self.x -= 4
        self.rect_image.x = self.x
        self.rect_rotated.x = self.x

    def draw(self, screen):
        screen.blit(self.rotated, self.rect_rotated)
        screen.blit(self.image, self.rect_image)
