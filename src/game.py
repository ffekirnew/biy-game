import pygame
from src.configurations import *


class Game:
    def __init__(self, player1, player2):
        self.turn = 0
        self.player1 = player1
        self.player2 = player2
        self.turns = [player1, player2]
        self.targeting = False
        self.shooting = False
        self.powerSize = 100

    def updateScreen(self, screen):
        if self.targeting:
            pygame.draw.line(screen, white, self.turns[self.turn].start, self.turns[self.turn].end)
            pygame.draw.rect(screen, green, (400, 900, self.powerSize, 20))
            pygame.draw.rect(screen, white, (400 + self.powerSize, 900, 500 - self.powerSize, 20))
