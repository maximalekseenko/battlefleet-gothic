
from math import atan2, degrees, hypot, radians, sin, cos
import backend.game as game


class SelectVessel(game.Action):
    NAME = "SELECTVESSEL"
    TYPE = ""


    def __init__(self, scene) -> None:
        # super().__init__(None)
        from frontend.scenes import ActionsMenu
        self.scene:ActionsMenu = scene

        self.game:game.Game = self.scene.act.game


    def Is_Valid_Args(self, **kargs) -> bool:pass 


    def Do(self, position, **kargs) -> None:
        print(position, self.game.Get_Vessel_In_Position(position, False, False, False, True))
        self.scene.selected_vessel = self.game.Get_Vessel_In_Position(position, False, False, False, True)
        self.scene.Update()
        


    def Get_Done(self, game:game.Game, position, **kargs) -> dict:
        if not self.Check(game, position): return None

        return {
            'type': self.TYPE,
            'name': self.NAME,
            'actor': self.vessel,
            'position': position,
        }

