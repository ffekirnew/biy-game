import math
import random
import pygame

from src.configurations import *


class Player:
    width = player_width
    height = player_height

    def __init__(self, game, color, posx, posy):
        self.game = game
        self.posx = posx
        self.posy = posy
        self.theta = 0
        self.color = color
        self.biy = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.start = [self.posx + 10, self.posy + 10]
        self.end = [int(self.start[0] + 40 * math.cos(math.radians(self.theta))),
                    int(self.start[1] + 40 * math.sin(math.radians(self.theta)))]

        self.speed_x = 0
        self.speed_y = 0

        self.gures = []

        self.move = [self.posx, self.posy]

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return 0

        key = event.key
        if key == pygame.K_SPACE:
            self.speed_x = 0.01 * self.game.powerSize * math.cos(math.radians(self.theta))
            self.speed_y = 0.01 * self.game.powerSize * math.sin(math.radians(self.theta))

            return 1

        elif key in (pygame.K_LEFT, pygame.K_RIGHT):
            self.theta += 10 if key == pygame.K_RIGHT else -10
            self.end = [
                int(self.posx + 40 * math.cos(math.radians(self.theta))),
                int(self.posy + 40 * math.sin(math.radians(self.theta)))
            ]

        elif key in (pygame.K_UP, pygame.K_DOWN):
            if key == pygame.K_UP:
                while self.game.powerSize < 500:
                    self.game.powerSize += 100
            else:
                while self.game.powerSize > 0:
                    self.game.powerSize -= 100

        return 0

    def update(self, gure=[], opponent=None):
        self.posx, self.posy = self.posx + self.speed_x, self.posy + self.speed_y
        self.start = [self.posx + 10, self.posy + 10]
        self.biy.x, self.biy.y = self.posx, self.posy

        if self.speed_x == 0 and self.speed_y == 0:
            self.game.shooting = False

        if self.posx <= 20 or self.posx >= screen_width - 20:
            self.speed_x = -1 * self.speed_x
        if self.posy <= 20 or self.posy >= screen_height - 20:
            self.speed_y = -1 * self.speed_y

        self.speed_x = self.updateSpeed(self.speed_x)
        self.speed_y = self.updateSpeed(self.speed_y)

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def updateSpeed(self, speed):
        speedDx = {True: -0.005, False: 0.005}
        x = speed > 0
        speed += speedDx[speed > 0]
        y = speed > 0
        if x != y:
            return 0
        return speed

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.biy)
