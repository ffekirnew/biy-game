import math

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

            for opponent in self.players[:]:
                if player != opponent:
                    dx = player.pos_x - opponent.pos_x
                    dy = player.pos_y - opponent.pos_y
                    distance = math.sqrt(dx ** 2 + dy ** 2)

                    if distance < biy_radius * 2:
                        angle = math.atan2(dy, dx)
                        sin_angle = math.sin(angle)
                        cos_angle = math.cos(angle)

                        # Rotate the velocities
                        vx1 = player.speed_x * cos_angle + player.speed_y * sin_angle
                        vy1 = player.speed_y * cos_angle - player.speed_x * sin_angle
                        vx2 = opponent.speed_x * cos_angle + opponent.speed_y * sin_angle
                        vy2 = opponent.speed_y * cos_angle - opponent.speed_x * sin_angle

                        # Calculate new velocities after collision
                        v1x = ((biy_radius - biy_radius) * vx1 + (2 * biy_radius) * vx2) / (
                                    biy_radius + biy_radius)
                        v2x = ((2 * biy_radius) * vx1 + (biy_radius - biy_radius) * vx2) / (
                                    biy_radius + biy_radius)
                        v1y = vy1
                        v2y = vy2

                        # Rotate the velocities back
                        player.speed_x = v1x * cos_angle - v1y * sin_angle
                        player.speed_y = v1y * cos_angle + v1x * sin_angle
                        opponent.speed_x = v2x * cos_angle - v2y * sin_angle
                        opponent.speed_y = v2y * cos_angle + v2x * sin_angle

                        if len(player.gures) == len(self.gures):
                            self.players.remove(opponent)
                            opponent_taken = True

                        self.force_turn(player_index)

                else:
                    break

            player.update()
            player.draw(self.screen)

        if self.players[self.turn].state == "POWER" or "AIMING":
            self.power_bar.draw()

        self.player_indicator.draw(self.screen, self.turn + 1)
