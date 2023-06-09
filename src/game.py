# define a class that will control the game. This class will be responsible for
# starting the game, updating all elements in the game, and resetting the game
# it should have two methods: init and run
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


class Game:
    def __init__(self):
        self.display = (800, 600)
        self.components = []
        pygame.init()
        pygame.display.set_caption("Biy Game")
        self.window = pygame.display.set_mode(self.display)

    def add_component(self, component) -> None:
        self.components.append(component)
        return

    def draw(self) -> None:
        for component in self.components:
            component.draw(self.window)
        return

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # Clear the screen
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            # Draw the components
            self.draw()
            # Update the display
            pygame.display.flip()
            # Set the fps to 60
            pygame.time.wait(16)

        return 0
