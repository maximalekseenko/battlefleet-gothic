from enum import Enum



class ARC(Enum):
    LEFT = 0
    FRONT = 1
    RIGHT = 2
    LEFTFRONTRIGHT = 3



class Armament:

    COLOR:str

    NAME:str
    RANGE:int
    FIREPOWER:int
    FIREARC:ARC

    def __init__(self) -> None:
        pass

        # turn stuff
        self.turn_is_used:bool


    def Turn_Reset(self):
        self.turn_is_used = False