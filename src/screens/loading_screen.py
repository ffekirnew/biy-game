from src.configurations import *


def loading(screen):
    loading_text = pygame.font.SysFont("JetBrains Mono", 36).render("Loading...", True, (255, 255, 255))
    loading_rect = loading_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    screen.fill((0, 0, 0))
    screen.blit(loading_text, loading_rect)
    pygame.display.flip()
