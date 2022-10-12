from math import atan2, degrees

from backend.game import Order

class Move(Order):
    NAME = "MOVE"
    TYPE = "MOVEMENT"


    def Is_Valid_Args(self, position, **kargs) -> bool:
        dX = self.vessel.position[0] - position[0]
        dY = self.vessel.position[1] - position[1]

        print(degrees(atan2(dX, dY)) % 360, self.vessel.rotation)

        if degrees(atan2(dX, dY)) % 360 != self.vessel.rotation: return False
        return True


    def On_Give(self, position, **kargs) -> None:
        self.vessel.position = position