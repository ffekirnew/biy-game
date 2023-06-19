import pygame
from pygame.locals import *

from src.configurations import background_preference
from src.screens.menu_screens import draw_menu
from src.utility.background_preference import BackgroundPreference


def menu_builder(screen, title, menu_items_actions):
    selected_item_index = 0
    menu_items = list(menu_items_actions.keys())
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == VIDEORESIZE:
                # Handle window resizing event
                display = event.size
                screen[0] = pygame.display.set_mode(tuple(display), RESIZABLE)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item_index = (selected_item_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item_index = (selected_item_index + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    selected_item = menu_items[selected_item_index]

                    if menu_items_actions[selected_item] in [BackgroundPreference.MUDDY, BackgroundPreference.GRASSY]:
                        background_preference[0] = menu_items_actions[selected_item]
                        return

                    elif menu_items_actions[selected_item] == "back":
                        return

        draw_menu(screen[0], title, menu_items, selected_item_index)
        pygame.display.flip()


def background_image_menu(screen):
    title_text = "የብይ ጨዋታ"
    muddy = ("ጭቃማ", BackgroundPreference.MUDDY)
    grassy = ("ሳራማ", BackgroundPreference.GRASSY)
    back = ("ተመለስ", "back")

    menu_builder(screen, title_text, {
        muddy[0]: muddy[1],
        grassy[0]: grassy[1],
        back[0]: back[1]
    })
