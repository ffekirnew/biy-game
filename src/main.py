import pygame

from src.components.player import Player
from src.game import Game
from src.components.gure import Gure
from src.configurations import screen_width, screen_height, green, red, white, blue

pygame.init()


def main():
    display = (screen_width, screen_height)
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.transform.scale(pygame.image.load("assets/background.jpg"), display)

    pygame.display.set_caption("Biy Game")
    clock = pygame.time.Clock()

    game = Game()

    players = [
        Player(game, green, screen_width / 2 - 450, screen_height / 2),
        Player(game, red, screen_width / 2 + 450, screen_height / 2),
        Player(game, blue, screen_width / 4 + 450, screen_height / 4),
    ]

    gures = [
        Gure(screen_width / 2, screen_height / 2),
        Gure(screen_width / 2 - 200, screen_height / 2 - 200),
        # Gure(screen_width / 2 + 200, screen_height / 2 - 200),
        # Gure(screen_width / 2 - 200, screen_height / 2 + 200),
        # Gure(screen_width / 2 + 200, screen_height / 2 + 200),
    ]

    for player in players:
        game.add_player(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                game.handle_event(event)

        screen.blit(background, (0, 0))
        for gure in gures:
            for player in players:
                if player.biy.colliderect(gure.gure) and gure not in player.gures:
                    player.gures.append(gure)
                    player.posx = gure.posx
                    player.posy = gure.posy
                    player.stop()

            gure.draw(screen)

        for player in players[:]:
            for opponent in players[:]:
                if player != opponent and len(player.gures) == len(gures):
                    if player.biy.colliderect(opponent.biy):
                        players.remove(opponent)

            player.update(gures, player.biy)
            player.draw(screen)

        game.updateScreen(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
