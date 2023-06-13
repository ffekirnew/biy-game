import math

import pygame

from src.components.gure import Gure
from src.components.player import Player
from src.components.player_indicator import PlayerIndicator
from src.components.power_bar import PowerBar
from src.configurations import *
from src.utility.player_state import PlayerState


class Game:
    def __init__(self, screen):
        self.turn = 0
        self.players = []
        self.gures = []

        self.screen = screen
        self.power_size = 100

        self.power_bar = PowerBar(self.screen)
        self.player_indicator = PlayerIndicator(screen_width - 100, 100)

    def add_player(self, player: Player) -> None:
        """Add a new player to the game.
        Parameters:
            player (Player): An object of the player type.
        Return:
            None.
        """
        self.players.append(player)

    def add_gure(self, gure: Gure) -> None:
        """Add a new gure to the game.
        Parameters:
            gure (Gure): An object of the gure type.
        Return:
            None.
        """

        self.gures.append(gure)

    def set_power_size(self, power_size: int) -> None:
        """Set the power size for shooting players.
        Parameter:
            power_size (int): Any integer greater than 0 and less
            than the max_power_size in the configuration.
        Return:
            None.
        """
        self.power_size = power_size
        self.power_bar.update(self.power_size)

    def handle_event(self, event) -> None:
        """Handle events from the game.
        Actually pass on the event to the current turn player to handle it themselves.
        Parameter:
            event (pygame.event): A pygame event
        Return:
            None
        """
        current_player_status = self.players[self.turn].handle_event(event) # if the player shoots, will return 1. Else 0

        self.turn = (self.turn + current_player_status) % len(self.players) # then use that to change the turn to the next player, or not

    def force_turn(self, turn: int):
        self.turn = turn

    def handle_gure_interactions(self):
        for player_index, player in enumerate(self.players[:]):
            for gure in self.gures:
                distance = math.sqrt((player.pos_x - gure.pos_x) ** 2 + (player.pos_y - gure.pos_y) ** 2)
                next_x, next_y = player.pos_x + player.speed_x, player.pos_y + player.speed_y
                next_distance = math.sqrt((next_x - gure.pos_x) ** 2 + (next_y - gure.pos_y) ** 2)

                if (player.pos_x < gure.pos_x < next_x or next_y < gure.pos_y < player.pos_y) and (
                        distance < biy_radius * 2):
                    player.gures.add(gure)
                    player.stop()
                    player.pos_x = gure.pos_x
                    player.pos_y = gure.pos_y
                    self.force_turn(player_index)

    def handle_player_interactions(self):
        for player_index, player in enumerate(self.players[:]):
            if player.state == PlayerState.SHOOTING:
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

                                self.force_turn(player_index - 1)
                            else:
                                self.force_turn(player_index)

    def draw_players(self):
        for player in self.players:
            player.update()
            player.draw(self.screen)

    def draw_gures(self):
        for gure in self.gures:
            gure.draw(self.screen)

    def draw(self):
        self.handle_player_interactions()
        self.handle_gure_interactions()

        self.draw_gures()
        self.draw_players()

        if all(player.state != PlayerState.SHOOTING for player in self.players):
            self.player_indicator.draw(self.screen, self.players[self.turn])
