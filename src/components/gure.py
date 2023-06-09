import pygame

from src.configurations import *


class Gure:
    width = gure_width
    height = gure_height
    color = gure_color

    def __init__(self, posx=0, posy=0) -> None:
        self.gure = pygame.Rect(posx, posy, self.width, self.height)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.gure)
