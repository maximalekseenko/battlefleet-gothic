class Order:
    '''
    \n constants:
    *   `NAME`
    *   `TYPE`
    \n functions:
    *   `Validate`
    *   `On_Give`
    *   `Is_Visible`
    *   `Is_Enabled`
    *   `Is_Warn`
    '''
    NAME:str
    TYPE:str


    def __init__(self, vessel, id:int) -> None:

        from .vessel import Vessel
        self.vessel:Vessel = vessel

        from .game import Game
        self.game:Game = vessel.game

        self.id:int = id


    def Is_Invisible(self) -> bool: return False
    def Is_Disabled(self) -> bool: return False
    def Is_Warn(self) -> bool: return False
    def Fix_Target(self, target=None) -> any: pass
    def Do(self, **kargs) -> None: pass


    def Get(self, target) -> dict:
        return {
            'vesselid': self.vessel.id,
            'orderid': self.id,
            'target': target
        }
