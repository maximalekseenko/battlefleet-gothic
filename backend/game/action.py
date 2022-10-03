import backend.game as game


class Action:
    NAME:str


    def __init__(self, vessel) -> None:
        self.vessel:game.Vessel = vessel


    def Check(self, **kargs) -> bool: pass
    def Do(self, **kargs) -> None: pass
    def Get_Done(self, **kargs) -> dict: pass