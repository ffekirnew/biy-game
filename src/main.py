import pygame
from pygame.locals import *

from src.configurations import display
from src.screens.main_screen import main

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = [pygame.display.set_mode(display, RESIZABLE)]

pygame.mixer.music.load("assets/music/background_music/home-head_first.mp3")
pygame.display.set_caption("Biy Game")

if __name__ == "__main__":
    main(screen)
