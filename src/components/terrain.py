from src.components import Display, Component
import pygame
import noise


class Terrain(Component):
    def __init__(self, display: Display):
        super().__init__()
        self.width = display.w  # Adjust the width of the terrain
        self.height = display.h  # Adjust the height of the terrain

        self.scale = 50  # Adjust the scale of the terrain
        self.octaves = 6  # Adjust the number of octaves for Perlin noise
        self.persistence = 0.5  # Adjust the persistence for Perlin noise
        self.lacunarity = 2.0  # Adjust the lacunarity for Perlin noise

        self.terrain_surface = self.generate_terrain_surface()

    def generate_terrain_surface(self):
        terrain_surface = pygame.Surface((self.width, self.height))

        for y in range(self.height):
            for x in range(self.width):
                noise_value = noise.pnoise2(
                    x / self.scale,
                    y / self.scale,
                    octaves=self.octaves,
                    persistence=self.persistence,
                    lacunarity=self.lacunarity,
                    repeatx=self.width,
                    repeaty=self.height,
                    base=0,
                )

                # Adjust the color range to create a muddy appearance
                color_value = int((noise_value + 1) * 127.5)  # Convert noise value to a color value
                alpha_value = 255  # Set alpha value to 255 for full opacity

                terrain_surface.set_at((x, y), (139, 69, color_value, alpha_value))

        return terrain_surface

    def draw(self, screen) -> None:
        screen.blit(self.terrain_surface, (0, 0))
