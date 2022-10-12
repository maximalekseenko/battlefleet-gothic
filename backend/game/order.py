class Order:
    '''
    \n constants:
    *   `NAME`
    *   `TYPE`
    \n functions:
    *   `Validate`
    *   `On_Give`
    '''
    NAME:str
    TYPE:str


    def __init__(self, vessel, id:int) -> None:

        from .vessel import Vessel
        self.vessel:Vessel = vessel

        from .game import Game
        self.game:Game = vessel.game

        self.id:int = id


    def Is_Valid_Args(self, **kargs) -> bool: pass
    def On_Give(self, **kargs) -> None: pass


    def Give(self, **kargs) -> None:
        if not self.Is_Valid_Args(**kargs): return
        self.On_Give(**kargs)


    def Get(self, **kargs) -> dict:
        return {
            'vesselid': self.vessel.id,
            'orderid': self.id,
            **kargs
        }
