import pygame

screen_width = 1280
screen_height = 600

gure_width = 40
gure_height = 40
gure_image_file = "assets/images/gure/gure.png"

player_width = 30
player_height = 30

max_power_size = 2000

menu_background_image_file = "assets/images/backgrounds/green-pattern.jpg"
background_image_file = "assets/images/backgrounds/mud-pattern.jpg"
loading_image_file = "assets/images/loading_wheels/loading.png"

display = (screen_width, screen_height)
menu_background = pygame.transform.scale(pygame.image.load(menu_background_image_file), display)
background = pygame.transform.scale(pygame.image.load(background_image_file), display)

white = pygame.Color("WHITE")
green = pygame.Color("GREEN")
red = pygame.Color("RED")
blue = pygame.Color("BLUE")
black = pygame.Color("BLACK")
