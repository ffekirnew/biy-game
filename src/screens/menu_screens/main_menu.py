import pygame
from pygame.locals import *

from src.configurations import menu_background_image_file, display
from src.screens.menu_screens.options_menu import options_menu
from src.screens.menu_screens import draw_menu
from src.screens.menu_screens.mode_menu import mode_menu


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

                    if menu_items_actions[selected_item] == "start":
                        mode_menu(screen)
                        return
                    elif menu_items_actions[selected_item] == "options":
                        options_menu(screen)
                    elif menu_items_actions[selected_item] == "quit":
                        pygame.quit()
                        exit()

        draw_menu(screen[0], title, menu_items, selected_item_index)
        pygame.display.flip()


def main_menu(screen):
    title_text = "ጨዋታ ይግዙ"
    start_text = ("እስከ", "start")
    options_text = ("አማራጭ", "options")
    quit_text = ("ውጣ", "quit")

    menu_builder(screen, title_text, {
        start_text[0]: start_text[1],
        options_text[0]: options_text[1],
        quit_text[0]: quit_text[1]
    })
