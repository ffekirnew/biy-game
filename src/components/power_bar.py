# design a singleton class to manage the power bar in the pygame given a screen to be displayed on
import pygame

from src.configurations import white, max_power_size, screen_height, screen_width


class PowerBar:
    """A class to manage the power bar in the pygame given a screen to be displayed on.
    Attributes:
        screen (pygame.Surface): The pygame screen to be displayed on.
        power_size (int): The power size of the game.
        power_bar (pygame.Rect): The pygame rectangle representing the power bar.
    """

    def __init__(self, screen):
        """Initialize the power bar.
        Parameters:
            screen (pygame.Surface): The pygame screen to be displayed on.
        Return:
            None.
        """
        self.screen = screen
        self.power_size = 100
        self.power_bar = pygame.Rect(10, 10, (self.power_size // max_power_size) * (screen_width - 10), 10)

    def update(self, power_size):
        """Update the power bar.
        Parameters:
            power_size (int): The power size of the game.
        Return:
            None.
        """
        self.power_size = power_size
        screen_power_bar_size = min(round((self.power_size / max_power_size) * (screen_width - 10)), screen_width - 20)
        self.power_bar = pygame.Rect(10, 10, screen_power_bar_size, 10)

    def draw(self, scale_factor: float = 1.0) -> None:
        """Draw the power bar.
        Parameters:
            scale_factor (float): The scale factor of the game.
        Return:
            None.
        """
        pygame.draw.rect(self.screen, white, self.power_bar)
