import random

from pygame.locals import *

from src.configurations import *
from src.components.game import Game
from src.screens.menu_screens.main_menu import main_menu

pygame.font.init()


def win_screen(screen, winner):
    clock = pygame.time.Clock()

    display = (screen[0].get_width(), screen[0].get_height())
    background = pygame.transform.scale(pygame.image.load(background_image_file[0]), display)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                if event.type == VIDEORESIZE:
                    # Handle window resizing event
                    display = event.size
                    screen[0] = pygame.display.set_mode(display, RESIZABLE)
                    background = pygame.transform.scale(pygame.image.load(background_image_file[0]), display)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    main_menu(screen)

        screen[0].blit(background, (0, 0))
        # draw a big rectangle in the middle of the screen
        pygame.draw.rect(screen[0], black, (screen[0].get_width() // 4, screen[0].get_height() // 4,
                                            screen[0].get_width() // 2, screen[0].get_height() // 2))
        # draw the winner
        winner.width *= 4
        winner.height *= 4

        screen[0].blit(winner.image,
                       (screen[0].get_width() // 2 - winner.width, screen[0].get_height() // 2 - winner.height))

        # draw the winner text
        # winner_text = pygame.font.SysFont("JetBrains Mono", 60).render("Wins!", True, white)
        # winner_rect = winner_text.get_rect(
        #     center=(screen[0].get_width() // 2, screen[0].get_height() // 2 + winner.height * 2))
        # screen[0].blit(winner_text, winner_rect)

        pygame.display.flip()
        clock.tick(60)
