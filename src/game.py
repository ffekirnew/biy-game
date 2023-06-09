import pygame

from src.components.gure import Gure
from src.components.player import Player
from src.components.player_indicator import PlayerIndicator
from src.components.power_bar import PowerBar
from src.configurations import *


class Game:
    def __init__(self, screen):
        self.turn = 0
        self.players = []
        self.gures = []
        self.screen = screen
        self.power_size = 100
        self.power_bar = PowerBar(self.screen)

        self.player_indicator = PlayerIndicator(100, screen_height - 10)

    def add_player(self, player: Player):
        self.players.append(player)

    def add_gure(self, gure: Gure):
        self.gures.append(gure)

    def set_power_size(self, power_size):
        self.power_size = power_size
        self.power_bar.update(self.power_size)

    def handle_event(self, event):
        current_player_status = self.players[self.turn].handle_event(event)

        self.turn = (self.turn + current_player_status) % len(self.players)

    def force_turn(self, turn: int):
        self.turn = turn

    def draw(self):
        for gure in self.gures:
            for i, player in enumerate(self.players):
                if player.biy.colliderect(gure.gure) and gure not in player.gures:
                    player.gures.append(gure)
                    player.stop()
                    player.pos_x = gure.posx
                    player.pos_y = gure.posy
                    self.force_turn(i)

            gure.draw(self.screen)

        for player_index, player in enumerate(self.players[:]):
            opponent_taken = False

            if not opponent_taken:
                for opponent in self.players[:]:
                    if player != opponent and len(player.gures) == len(self.gures):
                        if player.biy.colliderect(opponent.biy):
                            player.pos_x, player.pos_y = opponent.pos_x, opponent.pos_y
                            self.players.remove(opponent)
                            player.stop()
                            self.force_turn(player_index)
                            opponent_taken = True
                            break

            player.update()
            player.draw(self.screen)

        if self.players[self.turn].state == "POWER" or "AIMING":
            self.power_bar.draw()

        self.player_indicator.draw(self.screen, self.turn + 1)
