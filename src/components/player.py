import math
import random
import pygame

from src.configurations import *


class Player:
    width = player_width
    height = player_height
    states = ["IDLE", "SHOOTING", "AIMING"]

    def __init__(self, game, image_file_name, pos_x, pos_y):
        self.state = self.states[0]
        self.game = game

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = 0

        self.biy = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.image = pygame.transform.scale(pygame.image.load(image_file_name), (self.width, self.height))

        self.speed_x = 0
        self.speed_y = 0

        self.gures = []

        self.move = [self.pos_x, self.pos_y]

    def center(self):
        return [self.pos_x + self.width // 2, self.pos_y + self.height // 2]

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return 0

        key = event.key
        if key == pygame.K_SPACE:
            self.state = "SHOOTING"
            self.speed_x = 0.01 * self.game.power_size * math.cos(math.radians(self.direction))
            self.speed_y = 0.01 * self.game.power_size * math.sin(math.radians(self.direction))

            return 1

        elif key in (pygame.K_LEFT, pygame.K_RIGHT):
            self.state = "AIMING"
            self.direction += 10 if key == pygame.K_RIGHT else -10

        elif key in (pygame.K_UP, pygame.K_DOWN):
            self.state = "POWER"
            if key == pygame.K_UP and self.game.power_size < max_power_size:
                self.game.set_power_size(self.game.power_size + 100)
            elif key == pygame.K_DOWN and self.game.power_size > 0:
                self.game.set_power_size(self.game.power_size - 100)

        return 0

    def update(self):
        self.pos_x, self.pos_y = self.pos_x + self.speed_x, self.pos_y + self.speed_y
        self.biy.x, self.biy.y = self.pos_x, self.pos_y

        if self.speed_x == 0 and self.speed_y == 0:
            self.game.shooting = False

        if not (
                - self.width // 2 <= self.pos_x <= screen_width - self.width // 2
                and
                - self.height // 2 <= self.pos_y <= screen_height - self.height // 2
        ):
            self.stop()

        self.speed_x = self.update_speed(self.speed_x)
        self.speed_y = self.update_speed(self.speed_y)
        # self.start = [(self.pos_x + self.width) // 2, (self.pos_y + self.height) // 2]

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    @staticmethod
    def update_speed(speed):
        speedDx = {True: -0.005, False: 0.005}
        x = speed > 0
        speed += speedDx[speed > 0]
        y = speed > 0
        if x != y:
            return 0
        return speed

    def draw(self, screen):
        if self.state == "AIMING" or self.state == "POWER":
            start = self.center()
            end = [start[0] + 100 * math.cos(math.radians(self.direction)),
                   start[1] + 100 * math.sin(math.radians(self.direction))]
            pygame.draw.line(screen, white, start, end, 2)

        if self.state == "POWER":
            # TODO: draw power bar
            pass

        screen.blit(self.image, (self.pos_x, self.pos_y))
