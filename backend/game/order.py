class Order:
    '''
    \n constants:
    *   `NAME`
    *   `TYPE`
    \n functions:
    *   `Validate`
    '''
    NAME:str
    TYPE:str


    def __init__(self, vessel, id:int) -> None:

        from .vessel import Vessel
        self.vessel:Vessel = vessel

        from .game import Game
        self.game:Game = vessel.game

        self.id:int = id


    def Validate(self, **kargs) -> bool: pass


    def Initiate(self, **kargs) -> dict:
        return {
            'vesselid': self.vessel.id,
            'ordername': self.NAME,
            **kargs
        }
