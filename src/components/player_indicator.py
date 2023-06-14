# Implement a player indicator component that will be used in the pygame window
import pygame

from src.configurations import player_width


class PlayerIndicator:
    """Implement a player indicator component that will be used in the pygame window.
    Parameters:
        x (int): The x coordinate of the player indicator.
        y (int): The y coordinate of the player indicator.
    Attributes:
        x (int): The x coordinate of the player indicator.
        y (int): The y coordinate of the player indicator.
        font (pygame.font.Font): The font of the player indicator.
        color (pygame.Color): The color of the player indicator.
    Methods:
        draw(screen, player): Draw the player indicator.
    Returns:
        None.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("JetBrains Mono", 20)
        self.color = pygame.Color("WHITE")

    def draw(self, screen, player):
        """Draw the player indicator.
        Parameters:
            screen (pygame.Surface): The pygame window.
            player (Player): An object of the player type.
        Return:
            None.
        """
        text = self.font.render("Turn", True, self.color)
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(player.image, (self.x + player_width, self.y))
        screen.blit(text, text_rect)
