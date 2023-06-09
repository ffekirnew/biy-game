# create a screen type that is a named tuple to contain the width and height
from collections import namedtuple
from abc import ABC, abstractmethod

Display = namedtuple("Display", ["w", "h"])


class Component(ABC):
    def __init__(self, display: Display = None):
        pass

    @abstractmethod
    def draw(self, screen) -> None:
        pass
