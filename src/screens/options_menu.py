import pygame

from src.configurations import *


def options_menu(screen):
    menu_font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 60)

    title_text = title_font.render("Options", True, white)
    back_text = menu_font.render("Back", True, white)

    title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 4))
    back_rect = back_text.get_rect(center=(screen_width / 2, screen_height / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        screen.fill((0, 0, 0))
        screen.blit(title_text, title_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()
