from math import atan2, cos, degrees, sin

from backend.game import Order

class Move(Order):
    NAME = "MOVE"
    TYPE = "MOVEMENT"


    def Fix_Target(self, target:tuple[int, int]=None) -> any:
        if target == None: return

        delta_X = target[0] - self.vessel.position[0]
        delta_Y = target[1] - self.vessel.position[1]

        # direction check
        if (self.vessel.rotation - degrees(atan2(delta_Y, delta_X))) % 360 > 90: return None

        # get distance
        sinner = sin(self.vessel.rad_rotation)
        cosinner = -cos(self.vessel.rad_rotation)
        distance = (cosinner * delta_X + sinner * delta_Y)

        # fix distance
        # TODO
        # if distance > self.vessel.move

        target = (
            self.game.Round(self.vessel.position[0] + distance * cosinner),
            self.game.Round(self.vessel.position[1] + distance * sinner))


        return target


    def Do(self, target:tuple[int, int]=None) -> None:
        target = self.Fix_Target(target)

        # check if target valid
        if target == None: return

        self._Step(target)


    def _Step(self, target:tuple[int, int]=None):

        # get new position
        new_x = self.vessel.position[0] + cos(self.vessel.rad_rotation)
        new_y = self.vessel.position[1] - sin(self.vessel.rad_rotation)

        delta_X = target[0] - new_x
        delta_Y = target[1] - new_y

        # if finished movement
        # print(self.vessel.rotation, cos(self.vessel.rad_rotation), sin(self.vessel.rad_rotation))
        # print(delta_X, delta_Y, degrees(atan2(delta_Y, delta_X)))
        print("A",new_x, new_y)
        if (self.vessel.rotation - degrees(atan2(delta_Y, delta_X))) % 360 > 90:
            self.vessel.position = target
            return
        else: 
            self.vessel.position = (new_x, new_y)
            self._Test()

        self._Step(target)

    
    def _Test():
        pass

