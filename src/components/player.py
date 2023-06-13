import math
from enum import Enum

from src.configurations import *
from src.utility.player_state import PlayerState


class Player:
    width = player_width
    height = player_height

    def __init__(self, game, image_file_name, pos_x, pos_y):
        self.state = PlayerState.IDLE
        self.game = game

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = 0

        self.biy = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.image = pygame.transform.scale(pygame.image.load(image_file_name), (self.width, self.height))

        self.speed_x = 0
        self.speed_y = 0

        self.gures = set()

        self.move = [self.pos_x, self.pos_y]

    def center(self):
        return [self.pos_x + self.width // 2, self.pos_y + self.height // 2]

    def handle_event(self, event):
        # Allow for long press key presses
        if event.type != pygame.KEYDOWN:
            return 0

        key = event.key
        if key == pygame.K_SPACE:
            self.state = PlayerState.SHOOTING
            self.speed_x = 0.01 * self.game.power_size * math.cos(math.radians(self.direction))
            self.speed_y = 0.01 * self.game.power_size * math.sin(math.radians(self.direction))

            return 1

        elif key in (pygame.K_LEFT, pygame.K_RIGHT):
            self.state = PlayerState.AIMING

            pygame.key.set_repeat(500, 100)
            pygame.time.set_timer(pygame.USEREVENT, 100)

            if key == pygame.K_RIGHT:
                self.direction += 5

            elif key == pygame.K_LEFT:
                self.direction -= 5

        elif key in (pygame.K_UP, pygame.K_DOWN):
            self.state = PlayerState.POWER
            if key == pygame.K_UP and self.game.power_size < max_power_size:
                self.game.set_power_size(self.game.power_size + 100)
            elif key == pygame.K_DOWN and self.game.power_size > 0:
                self.game.set_power_size(self.game.power_size - 100)

        return 0

    def update(self):
        # Check if the custom event for long press has been triggered
        if pygame.event.peek(pygame.USEREVENT):
            # Handle long press here for aiming
            for event in pygame.event.get(pygame.USEREVENT):
                if event.type == pygame.USEREVENT:
                    if pygame.key.get_pressed()[pygame.K_LEFT]:
                        self.direction -= 5
                    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                        self.direction += 5

        self.pos_x, self.pos_y = self.pos_x + self.speed_x, self.pos_y + self.speed_y
        self.biy.x, self.biy.y = self.pos_x, self.pos_y

        if self.speed_x == 0 and self.speed_y == 0:
            self.game.shooting = False

        if not (
                0 < self.pos_x + self.speed_x < screen_width - self.width and
                0 < self.pos_y + self.speed_y < screen_height - self.height):
            self.stop()

        self.speed_x = self.update_speed(self.speed_x)
        self.speed_y = self.update_speed(self.speed_y)
        # self.start = [(self.pos_x + self.width) // 2, (self.pos_y + self.height) // 2]

        if self.state == PlayerState.SHOOTING and self.speed_x == self.speed_y == 0:
            self.state = PlayerState.IDLE

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
        if self.state in [PlayerState.AIMING, PlayerState.POWER]:
            start = self.center()
            end = [start[0] + 100 * math.cos(math.radians(self.direction)),
                   start[1] + 100 * math.sin(math.radians(self.direction))]
            pygame.draw.line(screen, white, start, end, 2)

        if self.state == PlayerState.POWER:
            self.game.power_bar.draw()

        screen.blit(self.image, (self.pos_x, self.pos_y))
