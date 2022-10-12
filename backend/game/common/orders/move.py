from math import atan2

from backend.game import Order

class Move(Order):
    NAME = "MOVE"
    TYPE = "MOVEMENT"


    def Validate(self, position) -> bool:
        dX = self.vessel.position[0] - position[0]
        dY = self.vessel.position[1] - position[1]
        if atan2(dX, dY) != self.vessel.rad_rotation: return False