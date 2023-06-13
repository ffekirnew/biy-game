from enum import Enum


class PlayerState(Enum):
    IDLE = "IDLE"
    AIMING = "AIMING"
    SHOOTING = "SHOOTING"
    POWER = "POWER"
