import random

import pygame
from src.components.player import Player
from src.components.power_bar import PowerBar
from src.game import Game
from src.components.gure import Gure
from src.configurations import screen_width, screen_height, white, green, red, blue

pygame.init()
pygame.font.init()

display = (screen_width, screen_height)
screen = pygame.display.set_mode(display)
background = pygame.transform.scale(pygame.image.load("assets/background.jpg"), display)

pygame.display.set_caption("Biy Game")

power_bar = PowerBar(screen)


def main_menu():
    menu_font = pygame.font.SysFont("JetBrains Mono", 36)
    title_font = pygame.font.SysFont("JetBrains Mono", 60)

    title_text = title_font.render("Biy Game", True, white)
    start_text = menu_font.render("Start", True, white)
    options_text = menu_font.render("Options", True, white)
    quit_text = menu_font.render("Quit", True, white)

    title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 4))
    start_rect = start_text.get_rect(center=(screen_width / 2, screen_height / 2))
    options_rect = options_text.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
    quit_rect = quit_text.get_rect(center=(screen_width / 2, screen_height * 3 / 4))

    menu_items = [
        {"text": start_text, "rect": start_rect, "action": "start"},
        {"text": options_text, "rect": options_rect, "action": "options"},
        {"text": quit_text, "rect": quit_rect, "action": "quit"}
    ]

    selected_item_index = 0

    while True:
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
                    if selected_item["action"] == "start":
                        return
                    elif selected_item["action"] == "options":
                        options_menu()
                    elif selected_item["action"] == "quit":
                        pygame.quit()
                        exit()

        screen.blit(background, (0, 0))
        screen.blit(title_text, title_rect)

        for index, item in enumerate(menu_items):
            text = item["text"]
            rect = item["rect"]
            if index == selected_item_index:
                pygame.draw.rect(screen, green, rect.inflate(10, 10))
            screen.blit(text, rect)

        pygame.display.flip()


def options_menu():
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


def main():
    clock = pygame.time.Clock()

    main_menu()

    game = Game(screen)

    players = [
        Player(game, "assets/biy/real-biy-4.png", screen_width / 2 - 450, screen_height / 2),
        Player(game, "assets/biy/real-biy-2.png", screen_width / 2 + 450, screen_height / 2),
        Player(game, "assets/biy/real-biy-3.png", screen_width / 2, screen_height / 4),
    ]

    gures = [
        Gure(random.randint(0, screen_width), random.randint(0, screen_height)),
        Gure(random.randint(0, screen_width), random.randint(0, screen_height)),
        Gure(random.randint(0, screen_width), random.randint(0, screen_height)),
        Gure(random.randint(0, screen_width), random.randint(0, screen_height)),
    ]

    for player in players:
        game.add_player(player)

    for gure in gures:
        game.add_gure(gure)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    main_menu()
                game.handle_event(event)

        screen.blit(background, (0, 0))

        game.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
