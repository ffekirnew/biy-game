import random

from src.components.gure import Gure
from src.components.player import Player
from src.configurations import *
from src.components.game import Game
from src.screens.menu_screens.main_menu import main_menu

pygame.font.init()


def main(screen):
    # play music
    # pygame.mixer.music.play(10, 54.8, 2000)
    clock = pygame.time.Clock()

    main_menu(screen)

    game = Game(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    main_menu(screen)

                if len(game.players) > 1:
                    game.handle_event(event)

        screen.blit(background, (0, 0))

        if len(game.players) == 1:
            winner = game.players[0]
            screen.blit(winner.image, (screen_width // 2 - player_width, screen_height // 4))
            winner_text = pygame.font.SysFont("JetBrains Mono", 60).render("Wins!", True, white)

            winner_rect = winner_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(winner_text, winner_rect)
        else:
            game.draw()
        pygame.display.flip()
        clock.tick(60)
