from math import atan2, cos, degrees, hypot, sin

from backend.game import Order

class Move(Order):
    NAME = "Move"
    TYPE = "MOVEMENT"


    def On_Do(self, target:tuple[int, int]=None) -> None:
        target = self.Fix_Target(target)

        # check if target valid
        if target == None: return

        # check if turn speed left
        if self.vessel.turn_speed <= 0: return

        # check if same
        if target == self.vessel.position: return

        # remove distance
        delta_X = self.vessel.position[0] - target[0]
        delta_Y = self.vessel.position[1] - target[1]
        sinner = sin(self.vessel.rad_rotation)
        cosinner = -cos(self.vessel.rad_rotation)
        self.vessel.turn_speed -= abs(cosinner * delta_X + sinner * delta_Y)

        self.vessel.position = target

        
    def Fix_Target(self, target:tuple[int, int]=None) -> any:
        if target == None: return

        delta_X = self.vessel.position[0] - target[0]
        delta_Y = self.vessel.position[1] - target[1]

        # direction check
        if 90 < (self.vessel.rotation - degrees(atan2(delta_Y, -delta_X)) % 360) % 360 < 270: 
            return self.vessel.position

        # get distance
        sinner = sin(self.vessel.rad_rotation)
        cosinner = -cos(self.vessel.rad_rotation)
        distance = abs(cosinner * delta_X + sinner * delta_Y)

        # cut distance
        if distance >= self.vessel.turn_speed: distance = self.vessel.turn_speed

        # fix distance
        target = self._Step(self.vessel.position, distance)

        return (self.game.Round(target[0]), self.game.Round(target[1]))


    def _Step(self, position:tuple[int, int], distance:int):
        step_acc = 0.5

        # get step
        step = (
            + cos(self.vessel.rad_rotation) * step_acc,
            - sin(self.vessel.rad_rotation) * step_acc)

        # close
        distance -= hypot(*step)
        # TODO: checks (blas markers ect.)

        # if finished movement
        if distance <= 0: return (position[0] + step[0], position[1] + step[1])
        
        # continue
        else: return self._Step((position[0] + step[0], position[1] + step[1]), distance)


    def Is_Disabled(self) -> bool:
        return self.vessel.turn_speed <= 0
