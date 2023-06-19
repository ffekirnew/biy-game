from src.configurations import *


def loading(screen):
    loading_font = pygame.font.Font(habesha_pixels_font_file, 40)
    loading_text = loading_font.render("በመክፈት ላይ...", True, (255, 255, 255))
    loading_rect = loading_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    screen.fill((0, 0, 0))
    screen.blit(loading_text, loading_rect)
    pygame.display.flip()
