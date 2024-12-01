import pygame


screen_wight = 500
screen_height = 850

game_height = 768

bg = pygame.image.load("resources/bg.png")
ground = pygame.image.load("resources/ground.png")

ground_scroll = 0


def draw_with_shade(screen, font, text, x, y):
    score_surface_shade = font.render(text, True, "black")
    screen.blit(score_surface_shade, score_surface_shade.get_rect(center=(x + 2, y + 2)))
    screen.blit(score_surface_shade, score_surface_shade.get_rect(center=(x - 2, y - 2)))
    screen.blit(score_surface_shade, score_surface_shade.get_rect(center=(x - 2, y + 2)))
    screen.blit(score_surface_shade, score_surface_shade.get_rect(center=(x + 2, y - 2)))
    score_surface = font.render(text, True, "white")
    screen.blit(score_surface, score_surface.get_rect(center=(x, y)))
