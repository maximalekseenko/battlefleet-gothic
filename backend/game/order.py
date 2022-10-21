class Order:
    '''
    \n constants:
    *   `NAME`
    *   `TYPE`
    *   `SHOW_BASE`
    *   `SHOW_LINE`
    *   `SHOW_VALUE`
    *   `SHOW_TARGET`
    \n functions:
    *   `Validate`
    *   `On_Give`
    *   `Is_Visible`
    *   `Is_Enabled`
    *   `Is_Warn`
    '''
    NAME:str
    TYPE:str

    SHOW_BASE:bool
    SHOW_LINE:bool
    SHOW_VALUE:bool
    SHOW_TARGET:bool



    def __init__(self, vessel, id:int) -> None:

        from .vessel import Vessel
        self.vessel:Vessel = vessel

        from .game import Game
        self.game:Game = vessel.game

        self.id:int = id


    def Is_Invisible(self) -> bool: return False
    def Is_Disabled(self) -> bool: return False
    def Is_Warn(self) -> bool: return False
    def Get_Default_Data(self):
        '''
        'position':,
        'value':,
        'show_value':,
        '''
        return {
            'position':None,
            'value':None,
            'show_value':''
        }
    def Get_Data(self, target:tuple[int, int]|list[int]|None=None) -> dict[str,any]: 
        return self.Get_Default_Data()
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
