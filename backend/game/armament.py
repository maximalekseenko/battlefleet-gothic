from enum import Enum



class FIREARC(Enum):
    LEFT = 0
    FRONT = 1
    RIGHT = 2
    LEFTFRONTRIGHT = 3



class Armament:

    def __init__(self, firearc) -> None:
        self.range = 30
        self.firepower = 6
        self.firearc = firearc

        # turn stuff
        self.turn_is_used:bool


    def Turn_Reset(self):
        self.turn_is_used = False