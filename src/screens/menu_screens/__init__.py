from src.configurations import *


def draw_menu(screen, title, menu_items, selected_item_index):
    font = pygame.font.Font(habesha_pixels_font_file, 36)

    title_text = font.render(title, True, white)
    title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 4))
    screen.blit(menu_background, (0, 0))
    screen.blit(title_text, title_rect)

    for index in range(len(menu_items)):
        item = menu_items[index]
        if index == selected_item_index:
            text = font.render(item, True, red)
        else:
            text = font.render(item, True, white)
        rect = text.get_rect(center=(screen_width / 2, screen_height / 4 + (index + 1) * 100))
        screen.blit(text, rect)
