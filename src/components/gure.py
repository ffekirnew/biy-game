import pygame

from src.configurations import *


class Gure:
    width = gure_width
    height = gure_height
    color = gure_color

    def __init__(self, posx=0, posy=0) -> None:
        self.image = pygame.transform.scale(pygame.image.load("assets/gure.png"), (self.width, self.height))
        self.posx = posx
        self.posy = posy
        self.gure = pygame.Rect(posx, posy, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.image, (self.posx, self.posy))
