from enum import Enum


class PlayerState(Enum):
    """Enumerate the possible states of a player."""
    IDLE = "IDLE"
    AIMING = "AIMING"
    SHOOTING = "SHOOTING"
    POWER = "POWER"
