import pygame

from src.utility.background_preference import BackgroundPreference
from src.utility.game_mode import GameMode

# Game Configurations
screen_width = 1280
screen_height = 600

game_mode = [GameMode.RANDOM]
number_of_gures = [5]
number_of_players = [2]
background_preference = [BackgroundPreference.GRASSY]

menu_background_image_file = "assets/images/backgrounds/green-pattern.jpg"
background_image_file = [
    "assets/images/backgrounds/colourful-brick-wall-seamless-pattern-with-copy-space-background.jpg"]
loading_wheel_image_file = "assets/images/loading_wheels/loading.png"

display = (screen_width, screen_height)

white = pygame.Color("WHITE")
green = pygame.Color("GREEN")
red = pygame.Color("RED")
blue = pygame.Color("BLUE")
black = pygame.Color("BLACK")

# Gure Configurations
gure_width = 30
gure_height = 30
gure_image_file = "assets/images/gure/gure11.png"

# Font Configurations
geez_pixels_font_file = "assets/fonts/geez-pixels.ttf"
crackman_font_file = "assets/fonts/crackman/Crackman.otf"
menelik_font_file = "assets/fonts/Menelik.ttf"
anbassa_font_file = "assets/fonts/Anbassa.ttf"
zibrikrik_font_file = "assets/fonts/Zibriqriq.ttf"
habesha_pixels_font_file = "assets/fonts/HABESHAPIXELS.ttf"

# Player Configurations
player_width = 20
player_height = 20

# Power Configurations
max_power_size = 2000
