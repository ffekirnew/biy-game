import pygame

from src.components.player import Player
from src.configurations import *


class Game:
    def __init__(self):
        self.turn = 0
        self.players = []
        self.powerSize = 100

    def add_player(self, player: Player):
        self.players.append(player)

    def handle_event(self, event):
        self.turn = (self.turn + self.players[self.turn].handle_event(event)) % len(self.players)

    def updateScreen(self, screen):
        pygame.draw.line(screen, white, self.players[self.turn].start, self.players[self.turn].end)
        pygame.draw.rect(screen, green, (400, 900, self.powerSize, 20))
        pygame.draw.rect(screen, white, (400 + self.powerSize, 900, 500 - self.powerSize, 20))
