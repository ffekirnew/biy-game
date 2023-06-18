from src.configurations import *
from src.screens.loading import loading
from src.screens.options_menu import options_menu

pygame.font.init()


def main_menu(screen):
    menu_font = pygame.font.SysFont("JetBrains Mono", 36)
    title_font = pygame.font.SysFont("JetBrains Mono", 60)

    title_text = title_font.render("Biy Game", True, white)
    start_text = menu_font.render("Start", True, white)
    options_text = menu_font.render("Options", True, white)
    quit_text = menu_font.render("Quit", True, white)

    title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 4))
    start_rect = start_text.get_rect(center=(screen_width / 2, screen_height / 2))
    options_rect = options_text.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
    quit_rect = quit_text.get_rect(center=(screen_width / 2, screen_height * 3 / 4))

    menu_items = [
        {"text": start_text, "rect": start_rect, "action": "start"},
        {"text": options_text, "rect": options_rect, "action": "options"},
        {"text": quit_text, "rect": quit_rect, "action": "quit"}
    ]

    selected_item_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item_index = (selected_item_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item_index = (selected_item_index + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    selected_item = menu_items[selected_item_index]
                    if selected_item["action"] == "start":
                        loading(screen)
                        pygame.time.wait(3000)
                        return
                    elif selected_item["action"] == "options":
                        options_menu(screen)
                    elif selected_item["action"] == "quit":
                        pygame.quit()
                        exit()

        screen.blit(menu_background, (0, 0))
        screen.blit(title_text, title_rect)

        for index, item in enumerate(menu_items):
            text = item["text"]
            rect = item["rect"]
            if index == selected_item_index:
                pygame.draw.rect(screen, green, rect.inflate(10, 10))
            screen.blit(text, rect)

        pygame.display.flip()
