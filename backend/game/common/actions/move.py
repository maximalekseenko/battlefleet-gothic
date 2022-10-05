from cmath import pi, rect, sqrt
from math import atan2, degrees, hypot, radians, sin, cos
import backend.game as game


class Move(game.Action):
    NAME = "MOVE"
    TYPE = "MOVEMENT"

    def Fix_Args(self, game:game.Game, position, **kargs) -> dict:

        delta_x, delta_y = sin(radians(self.vessel.rotation)), cos(radians(self.vessel.rotation))

        # math a
        a = (delta_x * (position[0] - self.vessel.position[0]) + delta_y * (position[1] - self.vessel.position[1])) / (delta_x ** 2 + delta_y ** 2)

        kargs['position'] = (self.vessel.position[0] + a * delta_x, self.vessel.position[1] + a * delta_y)


        return kargs


    def Check(self, game:game.Game, position, **kargs) -> bool:

        # delta movement
        delta_x = self.vessel.position[0] - position[0]
        delta_y = self.vessel.position[1] - position[1]

        # calculations
        distance = hypot(delta_x, delta_y)
        angle = degrees(atan2(delta_x, delta_y))

        # checks
        if self.vessel.speed_current - distance < 0: return False
        if self.vessel.rotation != angle: return False

        # return
        return True


    def Do(self, game:game.Game, position, **kargs) -> None:
        if not self.Check(game, position): return
        
        self.vessel.position = position


    def Get_Done(self, game:game.Game, position, **kargs) -> dict:
        if not self.Check(game, position): return None

        return {
            'type': self.TYPE,
            'name': self.NAME,
            'actor': self.vessel,
            'position': position,
        }