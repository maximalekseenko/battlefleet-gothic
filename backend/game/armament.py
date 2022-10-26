from backend import game


class Armament(game.Order):
    """
    \n constants:
    *   `NAME`
    *   `RANGE`
    *   `FIREPOWER`
    *   `FIREARC`

    *   `ARMAMENT_ORDER`
    """

    COLOR:str

    NAME:str
    RANGE:int
    FIREPOWER:int
    FIREARC:game.FIREARC


    def __init__(self, vessel, firearc=None) -> None:

        from .vessel import Vessel
        self.vessel:Vessel = vessel

        from .game import Game
        self.game:Game = vessel.game

        if firearc != None:
            self.FIREARC = firearc