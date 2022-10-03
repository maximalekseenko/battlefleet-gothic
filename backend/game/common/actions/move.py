from cmath import pi, sqrt
from math import atan2, degrees, hypot
import backend.game as game


class Move(game.Action):
    NAME = "MOVE"


    def Check(self, position, **kargs) -> bool:

        # delta movement
        delta_x = self.vessel.position[0] - position[0]
        delta_y = self.vessel.position[1] - position[1]

        # calculations
        distance = hypot(delta_x, delta_y)
        angle = degrees(atan2(delta_x, delta_y))
        
        print(self.vessel.rotation, '\t', angle, '\t', self.vessel.rotation != angle)
        print(self.vessel.speed_current, '\t', distance, '\t', self.vessel.speed_current - distance)

        # checks
        if self.vessel.speed_current - distance < 0: return False
        if self.vessel.rotation != angle: return False

        # return
        return True


    def Do(self, position, **kargs) -> None:
        if not self.Check(position): return
        
        self.vessel.position = position

        


    def Get_Done(self, position, **kargs) -> dict:
        if not self.Check(position): return None

        return {
            'type': "MOVEMENT",
            'name': self.NAME,
            'actor': self.vessel,
            'position': position,
        }