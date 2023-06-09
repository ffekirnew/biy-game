from src.components.biy import Biy
from src.game import Game
from src.components.gure import Gure
from src.configurations import *

pygame.init()


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Biy Game")
    clock = pygame.time.Clock()

    player1 = Biy(None, WIDTH / 2 - 450, HEIGHT / 2)
    player2 = Biy(None, WIDTH / 2 + 450, HEIGHT / 2)

    game = Game(player1, player2)
    player1.game = game
    player2.game = game

    gures = [
        Gure(WIDTH / 2, HEIGHT / 2),
        Gure(WIDTH / 2 - 200, HEIGHT / 2 - 200),
        Gure(WIDTH / 2 + 200, HEIGHT / 2 - 200),
        Gure(WIDTH / 2 - 200, HEIGHT / 2 + 200),
        Gure(WIDTH / 2 + 200, HEIGHT / 2 + 200),
    ]

    playerActions = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE]

    while True:
        playing = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key in playerActions:
                playing = game.turns[game.turn].event(event)
        screen.fill(background)
        player1.update(gures, player2.biy)
        player2.update(gures, player1.biy)
        for gure in gures:
            gure.draw(screen)
        pygame.draw.ellipse(screen, green, player1.biy)
        pygame.draw.ellipse(screen, red, player2.biy)
        game.updateScreen(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
