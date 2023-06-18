import pygame

from src.configurations import display
from src.screens.main_screen import main

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode(display)

pygame.mixer.music.load("assets/music/background_music/home-head_first.mp3")
pygame.display.set_caption("Biy Game")

# define a loading function to show a loading screen given a loading wheel image


if __name__ == "__main__":
    main(screen)
