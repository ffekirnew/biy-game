
import pygame
from pygame.locals import *

from src.configurations import game_mode, number_of_players, number_of_gures
from src.screens.loading_screen import loading
from src.screens.menu_screens import options_menu, draw_menu
from src.screens.menu_screens.gure_number_menu import gure_number_menu
from src.utility.game_mode import GameMode


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

                    if menu_items_actions[selected_item] in ["2", "3", "4"]:
                        number_of_players[0] = int(menu_items_actions[selected_item])
                        if game_mode[0] == GameMode.FIVEGURE:
                            loading(screen[0])
                            pygame.time.wait(3000)
                        else:
                            gure_number_menu(screen)
                        return

                    elif menu_items_actions[selected_item] == "quit":
                        pygame.quit()
                        exit()

        draw_menu(screen[0], title, menu_items, selected_item_index)
        pygame.display.flip()


def player_number_menu(screen):
    title_text = "የብይ ጨዋታ"
    two_players = ("2 ተጫዋች", "2")
    three_players = ("3 ተጫዋች", "3")
    four_players = ("4 ተጫዋች", "4")
    quit = ("ውጣ", "quit")

    menu_builder(screen, title_text, {
        two_players[0]: two_players[1],
        three_players[0]: three_players[1],
        four_players[0]: four_players[1],
        quit[0]: quit[1]
    })
