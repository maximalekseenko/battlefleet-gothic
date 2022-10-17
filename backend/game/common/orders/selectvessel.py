
from math import atan2, degrees, hypot, radians, sin, cos
import backend.game as game


class SelectVessel(game.Order):
    NAME = "SELECTVESSEL"
    TYPE = ""


    def __init__(self, scene) -> None:
        # super().__init__(None)
        from frontend.scenes import OrdersMenu
        self.scene:OrdersMenu = scene

        self.game:game.Game = self.scene.act.game


    def Do(self, position=None) -> None:
        self.scene.selected_vessel = self.game.Get_Vessel_In_Position(position, False, False, False, True)
        self.scene.Update()
        

    def Get_Done(self, game:game.Game, position) -> dict:
        if not self.Check(game, position): return None

        return {
            'type': self.TYPE,
            'name': self.NAME,
            'actor': self.vessel,
            'position': position,
        }

