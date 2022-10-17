from math import atan2, cos, degrees, hypot, sin

from backend.game import Order

class Rotate(Order):
    NAME = "Rotate"
    TYPE = "MOVEMENT"


    def Do(self, target:tuple[int, int]=None) -> None:
        target = self.Fix_Target(target)

        # check if target valid
        if target == None: return
        if target == self.vessel.position: return

        delta_X = self.vessel.position[0] - target[0]
        delta_Y = self.vessel.position[1] - target[1]
        self.vessel.rotation = degrees(atan2(delta_Y, -delta_X)) % 360

        
    def Fix_Target(self, target:tuple[int, int]=None) -> any:
        if target == None: return

        delta_X = self.vessel.position[0] - target[0]
        delta_Y = self.vessel.position[1] - target[1]

        # 
        rotation = (self.vessel.rotation - degrees(atan2(delta_Y, -delta_X)) % 360) % 360
        if self.vessel.turns > rotation or rotation > -self.vessel.turns % 360: 
            return target
        else: return self.vessel.position