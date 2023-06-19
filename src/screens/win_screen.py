import random

from pygame.locals import *

from src.configurations import *
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

                if event.type == pygame.KEYDOWN and event.key in [pygame.K_ESCAPE, pygame.K_RETURN]:
                    main_menu(screen)

        screen[0].blit(background, (0, 0))
        screen_width, screen_height  = screen[0].get_width(), screen[0].get_height()
        # draw a big rectangle in the middle of the screen
        pygame.draw.rect(screen[0], black, (screen_width // 4, screen_height // 4,
                                            screen_width // 2, screen_height // 2))

        screen[0].blit(winner.image,
                       (screen_width // 2 - winner.width, screen_height // 2 - winner.height))

        # get a font from file
        winner_font = pygame.font.Font(habesha_pixels_font_file, 60)
        winner_text = winner_font.render("አሸናፊ!", True, white)
        winner_rect = winner_text.get_rect(
            center=(screen_width // 2, screen_height // 2 + winner.height * 2))
        screen[0].blit(winner_text, winner_rect)

        pygame.display.flip()
        clock.tick(60)
