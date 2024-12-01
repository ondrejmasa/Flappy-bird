import pygame
from parameters import *
from game import Game


pygame.init()


font = pygame.font.Font("FlappyBirdRegular.ttf", 80)


screen = pygame.display.set_mode((screen_wight, screen_height))
pygame.display.set_caption("Flappy bird")

FPS = 60
clock = pygame.time.Clock()

game = Game()


run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game.game_over:
                    if not game.can_play:
                        game.can_play = True
                    game.bird.jump()
                else:
                    time = pygame.time.get_ticks()
                    if time > game.time + 1000:
                        game.restart()

    # draw background
    screen.blit(bg, (0, 0))

    # draw game
    game.draw(screen)
    game.update()

    # draw + scroll ground
    screen.blit(ground, (ground_scroll, 768))
    if not game.game_over:
        ground_scroll -= 4
        if ground_scroll <= -36:
            ground_scroll = 0

    # draw score
    if not game.game_over:
        draw_with_shade(screen, font, str(game.score), screen_wight//2, 100)
    else:
        draw_with_shade(screen, font, str(game.score), screen_wight // 2, game_height// 2 - 55)

    pygame.display.update()

pygame.quit()
