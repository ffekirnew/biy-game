# design a singleton class to manage the power bar in the pygame given a screen to be displayed on
import pygame

from src.configurations import white, max_power_size, screen_height, screen_width


class PowerBar:
    def __init__(self, screen):
        self.screen = screen
        self.power_size = 100
        self.power_bar = pygame.Rect(10, 10, (self.power_size // max_power_size) * (screen_width - 10), 10)

    def update(self, power_size):
        self.power_size = power_size
        screen_power_bar_size = min(round((self.power_size / max_power_size) * (screen_width - 10)), screen_width - 20)
        self.power_bar = pygame.Rect(10, 10, screen_power_bar_size, 10)

    def draw(self):
        pygame.draw.rect(self.screen, white, self.power_bar)
