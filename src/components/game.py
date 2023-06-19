import math
import random
from typing import Tuple

import pygame

from src.components.gure import Gure
from src.components.player import Player
from src.components.player_status_indicator import PlayerStatusIndicator
from src.components.power_bar import PowerBar
from src.configurations import *
from src.utility.game_mode import GameMode
from src.utility.player_state import PlayerState


class Game:
    """Implement a game class that will be used in the pygame window.
    Parameters:
        screen (pygame.Surface): The pygame window.
    Attributes:
        turn (int): The turn of the game.
        players (list): A list of players.
        gures (list): A list of gures.
        screen (pygame.Surface): The pygame window.
        power_size (int): The power size of the game.
        power_bar (PowerBar): An object of the power bar type.
        player_indicator (PlayerStatusIndicator): An object of the player indicator type.
    Methods:
        add_player(player): Add a new player to the game.
        add_gure(gure): Add a new gure to the game.
        set_power(power): Set the power of the game.
        handle_event(event): Handle events for the game.
        update(): Update the game.
        draw(screen): Draw the game.
    Returns:
        None.
    """

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

        self.screen_size = (self.screen.get_width(), self.screen.get_height())
        self.scale_factor = 1.0

        self.turn = 0
        self.players = []
        self.gures = []

        self.power_size = 100

        self.power_bar = PowerBar(self.screen)
        self.player_indicator = PlayerStatusIndicator(self.screen)

        self.load()

    def resize(self):
        """Resize the game.
        Parameters:
            None.
        Return:
            None.
        """
        # resize the screen and calculate new positions for the players and gures and change their pos_x and pos_y
        prev_screen_size = self.screen_size
        self.screen_size = (self.screen.get_width(), self.screen.get_height())
        self.scale_factor = self.screen_size[0] / prev_screen_size[0]

        for player in self.players:
            player.pos_x = player.pos_x * self.scale_factor
            player.pos_y = player.pos_y * self.scale_factor
            player.player = pygame.Rect(player.pos_x, player.pos_y, player.width, player.height)

        for gure in self.gures:
            gure.pos_x = gure.pos_x * self.scale_factor
            gure.pos_y = gure.pos_y * self.scale_factor
            gure.gure = pygame.Rect(gure.pos_x, gure.pos_y, gure.width, gure.height)

        self.power_bar = PowerBar(self.screen)
        self.player_indicator = PlayerStatusIndicator(self.screen)

    def load(self) -> None:
        """Load the game.
        Parameters:
            None.
        Return:
            None.
        """
        if background_image == BackgroundPreference.GRASSY:
            background_image_file[
                0] = "assets/images/backgrounds/colourful-brick-wall-seamless-pattern-with-copy-space-background.jpg"
        else:
            background_image_file[0] = "assets/images/backgrounds/retro.jpg"
        for i in range(number_of_players[0]):
            self.players.append(
                Player(self, f"assets/images/biy/biy-{i + 1}{i + 1}.png", random.randint(0, self.screen.get_width()),
                       random.randint(0, self.screen.get_height())))
        if game_mode[0] == GameMode.RANDOM:
            for i in range(number_of_gures[0]):
                self.gures.append(
                    Gure(random.randint(0, self.screen.get_width()), random.randint(0, self.screen.get_height())))
        else:
            # add 5 gures drawing a cross in the game
            padding = 150
            gures = [
                Gure(self.screen.get_width() // 2, self.screen.get_height() // 2),
                Gure(self.screen.get_width() // 2 - padding, self.screen.get_height() // 2),
                Gure(self.screen.get_width() // 2 + padding, self.screen.get_height() // 2),
                Gure(self.screen.get_width() // 2, self.screen.get_height() // 2 - padding),
                Gure(self.screen.get_width() // 2, self.screen.get_height() // 2 + padding)
            ]

            for gure in gures:
                self.gures.append(gure)

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
        """Set the power size of the game.
        Parameters:
            power_size (int): The power size of the game.
        Return:
            None.
        """
        self.power_size = power_size
        self.power_bar.update(self.power_size)

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle events for the game.
        Parameter:
            event (pygame.event.Event): An event object.
        Return:
            None.
        """
        current_player_status = self.players[self.turn].handle_event(
            event)  # if the player shoots, will return 1. Else 0

        self.turn = (self.turn + current_player_status) % len(
            self.players)  # then use that to change the turn to the next player, or not

    def force_turn(self, turn: int) -> None:
        """Force the turn to a specific player.
        Parameter:
            turn (int): The index of the player to force the turn to.
        Return:
            None.
        """
        self.turn = turn

    def handle_gure_interactions(self) -> None:
        """Handle interactions between gures and players.
        If a player is within the radius of a gure, the player will stop moving.
        Parameter:
            None.
        Return:
            None.
        """
        biy_radius = Player.height // 2
        for player_index, player in enumerate(self.players[:]):
            for gure in self.gures:
                distance = math.sqrt((player.pos_x - gure.pos_x) ** 2 + (player.pos_y - gure.pos_y) ** 2)
                next_x, next_y = player.pos_x + player.speed_x, player.pos_y + player.speed_y
                next_distance = math.sqrt((next_x - gure.pos_x) ** 2 + (next_y - gure.pos_y) ** 2)

                if (player.pos_x < gure.pos_x < next_x or next_y < gure.pos_y < player.pos_y) and (
                        distance < biy_radius * 2) and (player.shooting_start_position != gure.center()):
                    if gure.center() == player.center():
                        continue
                    player.gures.add(gure)
                    player.stop()
                    player.pos_x = gure.pos_x + gure.width // 2 - player.width // 2
                    player.pos_y = gure.pos_y + gure.height // 2 - player.height // 2
                    self.force_turn(player_index)

    def handle_player_interactions(self) -> None:
        """Handle interactions between players.
        If a player is shooting, check if they hit another player.
        If they do, stop the player and add the gure to the player.
        Parameter:
            None.
        Return:
            None.
        """
        biy_radius = Player.height // 2
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

    def draw_players(self, scaling_factor: float, translation_vector: Tuple[float]) -> None:
        """Draw all players on the screen.
        Parameter:
            scaling_factor (float): The scaling factor of the game.
            translation_vector (Tuple[float]): The translation vector of the game.
        Return:
            None.
        """
        for player in self.players:
            player.update()
            player.draw(self.screen, scaling_factor, translation_vector)

    def draw_gures(self, scaling_factor: float, translation_vector: Tuple[float]) -> None:
        """Draw all gures on the screen.
        Parameter:
            scaling_factor (float): The scaling factor of the game.
        Return:
            None.
        """
        for gure in self.gures:
            gure.draw(self.screen, scaling_factor, translation_vector)

    def draw(self) -> None:
        """Draw the game on the screen.
        Parameter:
            None.
        Return:
            None.
        """
        self.handle_player_interactions()
        self.handle_gure_interactions()

        scaling_factor, translation_vector = self.determine_scaling_and_translation_vector()

        self.draw_gures(scaling_factor, translation_vector)
        self.draw_players(scaling_factor, translation_vector)

        if all(player.state != PlayerState.SHOOTING for player in self.players):
            self.player_indicator.draw(self.players[self.turn], len(self.gures))

        # flash on the gures still left to complete with red for the player that is aiming or powering
        if self.players[self.turn].state == PlayerState.AIMING or self.players[self.turn].state == PlayerState.POWER:
            for gure in self.gures:
                if gure not in self.players[self.turn].gures:
                    # draw a red dot on the gure
                    pygame.draw.circle(self.screen, (255, 0, 0),
                                       (int(gure.pos_x + gure.width // 2),
                                        int(gure.pos_y + gure.height // 2)), 5)

    def determine_scaling_and_translation_vector(self) -> Tuple[float, Tuple[float]]:
        """Determine the scaling factor and translation vector to draw the game.
        Parameter:
            None.
        Return:
            scaling_factor (float): The scaling factor of the game.
            translation_vector (Tuple[float]): The translation vector of the game.
        """
        # determine the most extreme x and y values and calculate the scaling factor and translation vector for all gures and playrs
        min_x = min([gure.pos_x for gure in self.gures] + [player.pos_x for player in self.players])
        max_x = max([gure.pos_x for gure in self.gures] + [player.pos_x for player in self.players])
        min_y = min([gure.pos_y for gure in self.gures] + [player.pos_y for player in self.players])
        max_y = max([gure.pos_y for gure in self.gures] + [player.pos_y for player in self.players])

        scaling_factor = min(self.screen.get_width() / (max_x - min_x), self.screen.get_height() / (max_y - min_y))

        translation_vector = (self.screen.get_width() / 2 - (max_x + min_x) / 2 * scaling_factor,
                              self.screen.get_height() / 2 - (max_y + min_y) / 2 * scaling_factor)

        return 1, (0, 0)
