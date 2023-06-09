from game import Game

from src.components import Display
from src.components.hole import Hole
from src.components.terrain import Terrain
from src.components.player import Player

if __name__ == "__main__":
    game = Game()
    display = Display(800, 600)
    game.add_component(Terrain(display))
    game.add_component(Hole(display))
    game.add_component(Player(display))
    game.run()
