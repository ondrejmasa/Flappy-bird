import pygame.mixer

from parameters import *
from bird import Bird
from pipe import Pipe
from button import Button


class Game:
    def __init__(self):
        self.bird = Bird(100, screen_height//2)
        self.pipes = [Pipe(0), Pipe(screen_wight//2 + 39)]
        self.game_over = False
        self.score = 0
        self.can_score = True
        self.restart_button = Button(screen_wight//2, game_height //2, pygame.image.load("resources/restart.png"))
        self.can_play = False
        self.time = 0
        self.point_sound = pygame.mixer.Sound("sounds/point.wav")
        self.hit_sound = pygame.mixer.Sound("sounds/hit.wav")
        self.swooshing_sound = pygame.mixer.Sound("sounds/swooshing.wav")
        self.lower_volume()

    def lower_volume(self):
        self.point_sound.set_volume(0.1)
        self.hit_sound.set_volume(0.1)
        self.swooshing_sound.set_volume(0.1)

    def generate_pipes(self):
        if self.pipes[0].x <= -78:
            self.pipes.pop(0)
            self.pipes.append(Pipe(0))
            self.can_score = True

    def game_over_check(self):
        if self.bird.rect.top <= 0:
            self.game_over = True
            self.time = pygame.time.get_ticks()
        if self.bird.rect.bottom >= game_height:
            self.game_over = True
            self.time = pygame.time.get_ticks()
        for pipe in self.pipes:
            if self.bird.rect.colliderect(pipe.rect_image) or self.bird.rect.colliderect(pipe.rect_rotated):
                self.game_over = True
                self.hit_sound.play()
                self.time = pygame.time.get_ticks()

    def update_score(self):
        if self.pipes[0].rect_image.centerx < self.bird.rect.centerx and self.can_score:
            self.score += 1
            self.point_sound.play()
            self.can_score = False

    def update(self):
        if self.can_play:
            self.generate_pipes()
            if not self.game_over:
                self.game_over_check()
            self.update_score()
            if not self.game_over:
                for pipe in self.pipes:
                    pipe.move()
            self.bird.update()
        else:
            self.bird.animate()

    def restart(self):
        self.swooshing_sound.play()
        self.bird = Bird(100, screen_height // 2)
        self.pipes = [Pipe(0), Pipe(screen_wight // 2 + 39)]
        self.game_over = False
        self.score = 0
        self.can_score = True
        self.can_play = False

    def draw(self, screen):
        for pipe in self.pipes:
            pipe.draw(screen)
        self.bird.draw(screen)
        if self.game_over:
            if self.restart_button.draw(screen):
                self.restart()
