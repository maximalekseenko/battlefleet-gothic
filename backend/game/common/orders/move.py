from math import atan2, cos, degrees, sin

from backend.game import Order

class Move(Order):
    NAME = "MOVE"
    TYPE = "MOVEMENT"

    def Fix_Target(self, target:tuple[int, int]=None) -> any:
        if target == None: return

        delta_X = self.vessel.position[0] - target[0]
        delta_Y = self.vessel.position[1] - target[1]

        # direction fix
        # print(degrees(atan2(delta_X, delta_Y)))

        # position fix
        sinner = sin(self.vessel.rad_rotation)
        cosinner = cos(self.vessel.rad_rotation)
        a = (sinner * -delta_X + cosinner * -delta_Y)

        # round fix
        target = (
            self.game.Round(self.vessel.position[0] + a * sinner),
            self.game.Round(self.vessel.position[1] + a * cosinner)
        )

        return target


    def Do(self, target:tuple[int, int]=None) -> None:
        target = self.Fix_Target(target)

        # check if target valid
        if target == None: return

        self._Step(target)


    def _Step(self, target:tuple[int, int]=None):

        # get new position
        new_x = self.vessel.position[0] - sin(self.vessel.rad_rotation)
        new_y = self.vessel.position[1] + cos(self.vessel.rad_rotation)

        # if finished movement
        if abs(new_x - target[0]) < 1 or abs(new_y - target[1]) < 1:
            self.vessel.position = target
        else: 
            self.vessel.position = (new_x, new_y)

        self._Step(target)

