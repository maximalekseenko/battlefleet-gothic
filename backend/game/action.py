class Action:
    NAME:str


    def __init__(self, vessel) -> None:
        from .vessel import Vessel
        self.vessel:Vessel = vessel


    def Is_Valid_Args(self, **kargs) -> bool: pass
    def Fix_Args(self, **kargs) -> dict: pass

    def Do(self, **kargs) -> None: pass
    def Get_Done(self, **kargs) -> dict: pass