import pygame.mixer

from parameters import *


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.images = [pygame.image.load(f"resources/bird{i}.png").convert_alpha() for i in range(1, 4)]
        self.index = 0
        self.image = self.images[self.index % 3]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.counter = 0
        self.speed = 2
        self.wing_sound = pygame.mixer.Sound("sounds/wing.wav")
        self.lower_volume()

    def lower_volume(self):
        self.wing_sound.set_volume(0.1)

    def jump(self):
        self.speed = -8
        self.wing_sound.play()

    def animate(self):
        self.counter += 1
        if self.counter > 5:
            self.index += 1
            self.speed += 2
            self.counter = 0
        self.image = self.images[self.index % 3]

    def update(self):
        self.animate()
        if not self.y+36 > game_height:
            self.y += self.speed

        if self.speed < 6:
            self.image = pygame.transform.rotate(self.image, 15)
            self.rect = self.image.get_bounding_rect()
            self.rect.center = (self.x+8, self.y+10)

        elif self.speed > 6:
            self.image = pygame.transform.rotate(self.image, -45)
            self.rect = self.image.get_bounding_rect()
            self.rect.center = (self.x+8, self.y+10)

        else:
            self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, (self.x-25, self.y-18))
