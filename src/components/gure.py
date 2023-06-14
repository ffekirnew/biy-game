import pygame

from src.configurations import *


class Gure:
    """A class to represent a gure.
    Attributes:
        width (int): The width of the gure.
        height (int): The height of the gure.
        color (pygame.Color): The color of the gure.
        image (pygame.Surface): The image of the gure.
        pos_x (int): The x position of the gure.
        pos_y (int): The y position of the gure.
        gure (pygame.Rect): The rectangle of the gure.
    """
    width = gure_width
    height = gure_height
    color = gure_color

    def __init__(self, posx=0, posy=0) -> None:
        """Initialize a gure object.
        Parameters:
            posx (int): The x position of the gure.
            posy (int): The y position of the gure.
        Return:
            None.
        """
        self.image = pygame.transform.scale(pygame.image.load(gure_image_file), (self.width, self.height))
        self.pos_x = posx
        self.pos_y = posy
        self.gure = pygame.Rect(posx, posy, self.width, self.height)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the gure on the screen.
        Parameters:
            screen (pygame.Surface): The screen to be drawn on.
        Return:
            None.
        """
        screen.blit(self.image, (self.pos_x, self.pos_y))
