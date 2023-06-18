
import pygame

from src.configurations import game_mode, number_of_players, number_of_gures
from src.screens.menu_screens import options_menu, draw_menu
from src.screens.menu_screens.player_number_menu import player_number_menu
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item_index = (selected_item_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item_index = (selected_item_index + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    selected_item = menu_items[selected_item_index]

                    if menu_items_actions[selected_item] == "random":
                        game_mode[0] = GameMode.RANDOM
                        player_number_menu(screen)
                        return
                    elif menu_items_actions[selected_item] == "five_gure":
                        game_mode[0] = GameMode.FIVEGURE
                        player_number_menu(screen)
                        return
                    elif menu_items_actions[selected_item] == "quit":
                        pygame.quit()
                        exit()

        draw_menu(screen, title, menu_items, selected_item_index)
        pygame.display.flip()


def mode_menu(screen):
    title_text = "ጨዋታ ይግዙ"
    random_game_text = ("Random", "random")
    five_gure_text = ("Five Gure", "five_gure")
    quit_text = ("ውጣ", "quit")

    menu_builder(screen, title_text, {
        random_game_text[0]: random_game_text[1],
        five_gure_text[0]: five_gure_text[1],
        quit_text[0]: quit_text[1]
    })
