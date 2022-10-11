class Action:
    NAME:str
    TYPE:str
    DISPLAY_NAME:str
    TOOLTIP:str


    def __init__(self, vessel) -> None:
        from .vessel import Vessel
        self.vessel:Vessel = vessel
        self.game = vessel.game

        self.use_minimum = 0
        self.use_maximum = 1
        self.use_current = 0


    def Is_Valid_Args(self, position=None) -> bool: return True
    def Fix_Position(self, position=None) -> dict: return position

    def Step(self, **kargs): pass

    def On_Selected(self) -> None: pass
    def On_Positioned(self, position) -> None: pass

    def Do(self, position=None) -> None: pass

    def Get_Done(self, **kargs) -> dict: pass


    def Get_Order_Size(self) -> bool:
        if self.TYPE == "SPECAL": return 0
        if self.TYPE == "MOVEMENT": return 1


    def Get_Visual(self, scene):
        from .orderbutton import OrderButton
        return OrderButton(scene, self)

