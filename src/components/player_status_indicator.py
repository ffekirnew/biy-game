# Implement a player indicator component that will be used in the pygame window
import pygame


class PlayerStatusIndicator:
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

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

        self.padding = 10
        self.pos_x = self.screen.get_width() - 260 - self.padding
        self.pos_y = self.screen.get_height() - 50 - self.padding
        self.height = self.screen.get_height() - self.pos_y - self.padding
        self.width = self.screen.get_width() - self.pos_x - self.padding

        self.font = pygame.font.SysFont("JetBrains Mono", 20)
        self.color = pygame.Color("WHITE")

    def draw(self, player, total_gures):
        """Draw the player indicator.
        Parameters:
            screen (pygame.Surface): The pygame window.
            player (Player): An object of the player type.
        Return:
            None.
        """
        # draw two rectangles to show the number of gures left and the players turn
        percentage = (40, 60)
        rect_1_width = self.width * percentage[0] // 100
        rect_2_width = self.width * percentage[1] // 100
        rectangle_1 = pygame.Rect(self.pos_x, self.pos_y, rect_1_width, self.height)
        rectangle_2 = pygame.Rect(self.pos_x + rect_1_width + self.padding, self.pos_y, rect_2_width, self.height)

        pygame.draw.rect(self.screen, self.color, rectangle_1, 1, 10)
        text = self.font.render("Turn: ", True, self.color)
        self.screen.blit(text, (self.pos_x + 10, self.pos_y + 10))
        self.screen.blit(player.image, (self.pos_x + rect_1_width - player.width - 10, self.pos_y + 10))

        pygame.draw.rect(self.screen, self.color, rectangle_2, 1, 10)
        text = self.font.render(f"Gures: {len(player.gures)}/{total_gures}", True, self.color)
        self.screen.blit(text, (self.pos_x + rect_1_width + self.padding + 10, self.pos_y + 10))
