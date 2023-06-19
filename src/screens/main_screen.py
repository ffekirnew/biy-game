import random

from pygame.locals import *

from src.configurations import *
from src.components.game import Game
from src.screens.menu_screens.main_menu import main_menu
from src.screens.win_screen import win_screen

pygame.font.init()


def main(screen):
    # play music
    pygame.mixer.music.play(10, 54.8, 2000)
    clock = pygame.time.Clock()

    main_menu(screen)

    game = Game(screen[0])
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
                    game.resize()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    main_menu(screen)

                if len(game.players) > 1:
                    game.handle_event(event)

        screen[0].blit(background, (0, 0))

        if len(game.players) == 1:
            win_screen(screen, game.players[0])
            return
        else:
            game.draw()
        pygame.display.flip()
        clock.tick(60)
