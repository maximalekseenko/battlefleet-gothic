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
    def On_Do(self, target=None) -> None: pass
    def Get_Display_Text(self, target=None): return ''

    def Do(self, target=None):
        # if self.Is_Disabled: return
        # if self.Is_Invisible: return
        self.On_Do(target)

    def Get(self, target) -> dict:
        return {
            'vesselid': self.vessel.id,
            'orderid': self.id,
            'target': target
        }
