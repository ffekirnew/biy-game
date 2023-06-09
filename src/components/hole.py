# create a hole class that will use pygame.Circle and will be used to simulate a hole for marbles
import pygame
from src.components import Component, Display
import numpy as np


class Hole(Component):
    width = 20
    height = 20
    color = (255, 255, 255)

    def __init__(self, display: Display):
        super().__init__()
        x, y = np.random.randint(0, display.w), np.random.randint(0, display.h)
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
