# Implement a player indicator component that will be used in the pygame window
import pygame

from src.configurations import player_width


class PlayerIndicator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("JetBrains Mono", 20)
        self.color = pygame.Color("WHITE")

    def draw(self, screen, player):
        text = self.font.render("Turn", True, self.color)
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(player.image, (self.x + player_width, self.y))
        screen.blit(text, text_rect)
