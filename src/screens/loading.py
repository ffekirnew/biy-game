import pygame

from src.configurations import *


def loading(screen):
    """Show a loading screen given a loading wheel image.
    Parameters:
        None.
    Returns:
        None.
    """
    loading_image = pygame.transform.scale(pygame.image.load(loading_image_file), (100, 100))
    loading_image_rect = loading_image.get_rect(center=(screen_width / 2, screen_height / 2))

    loading_angle = 0
    loading_speed = 5

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.blit(menu_background, (0, 0))
        screen.blit(loading_image, loading_image_rect)

        loading_image = pygame.transform.rotate(loading_image, loading_angle)
        loading_angle += loading_speed

        pygame.display.update()
