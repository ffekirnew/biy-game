# create a hole class that will use pygame.Circle and will be used to simulate a hole for marbles
import pygame
from src.components import Component, Display
import numpy as np


class Player(Component):
    width = 40
    height = 60
    color = (255, 132, 0)

    def __init__(self, display: Display):
        super().__init__()
        x, y = 0, display.h - self.height
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
