import math
import random
import pygame


class Biy:
    def __init__(self, game, posx=random.randint(280, 1000), posy=random.randint(160, 800), width=20,
                 height=20) -> None:
        self.game = game
        self.posx = posx
        self.posy = posy
        self.theta = 0
        self.biy = pygame.Rect(self.posx, self.posy, width, height)
        self.start = [self.posx + 10, self.posy + 10]
        self.end = [int(self.start[0] + 40 * math.cos(math.radians(self.theta))),
                    int(self.start[1] + 40 * math.sin(math.radians(self.theta)))]

        self.speedx = 0
        self.speedy = 0

        self.move = [self.posx, self.posy]

    def event(self, pressed):
        direction = {pygame.K_LEFT: -10, pygame.K_RIGHT: 10}
        power = {pygame.K_UP: 100, pygame.K_DOWN: -100}
        if pressed.type == pygame.KEYDOWN:
            if pressed.key == pygame.K_SPACE:
                self.game.targeting = False
                self.game.shooting = True
                self.game.turn = 1 - self.game.turn
                self.speedx = 0.01 * self.game.powerSize * math.cos(math.radians(self.theta))
                self.speedy = 0.01 * self.game.powerSize * math.sin(math.radians(self.theta))
                self.game.powerSize = 100

            elif pressed.key in (pygame.K_LEFT, pygame.K_RIGHT):
                # if self.game.shooting:
                #     return
                self.game.targeting = True
                self.theta += direction.get(pressed.key, 0)
                self.theta = self.theta
                self.end = [
                    int(self.posx + 40 * math.cos(math.radians(self.theta))),
                    int(self.posy + 40 * math.sin(math.radians(self.theta)))
                ]

            elif pressed.key in (pygame.K_UP, pygame.K_DOWN):
                # if self.game.shooting:
                #     return
                self.game.targeting = True
                self.game.powerSize += power.get(pressed.key, 0)
                if self.game.powerSize < 0:
                    self.game.powerSize = 0
                elif self.game.powerSize > 500:
                    self.game.powerSize = 500

    def update(self, gure=[], opponent=None):

        self.posx, self.posy = self.posx + self.speedx, self.posy + self.speedy
        self.start = [self.posx + 10, self.posy + 10]
        self.biy.x, self.biy.y = self.posx, self.posy

        if self.speedx == 0 and self.speedy == 0:
            self.game.shooting = False

        if self.posx <= 20 or self.posx >= 1260:
            self.speedx = -1 * self.speedx
        if self.posy <= 20 or self.posy >= 940:
            self.speedy = -1 * self.speedy

        self.speedx = self.updateSpeed(self.speedx)
        self.speedy = self.updateSpeed(self.speedy)

        # if self.biy.colliderect(opponent):
        #     self.game.turn = 1 - self.game.turn
        #     self.game.targeting = False
        #     self.stop()

        # elif gure[0].contains(self.biy) or gure[1].contains(self.biy) or gure[2].contains(self.biy) or gure[3].contains(self.biy) or gure[4].contains(self.biy):
        #     self.game.turn = 1 - self.game.turn
        #     self.stop()

    def stop(self):
        self.speedx = 0
        self.speedy = 0

    def updateSpeed(self, speed):
        speedDx = {True: -0.005, False: 0.005}
        x = speed > 0
        speed += speedDx[speed > 0]
        y = speed > 0
        if x != y:
            return 0
        return speed
