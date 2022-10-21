from math import atan2, cos, degrees, hypot, sin

from backend.game import Order
from backend.game.enums.vesseltype import VESSELTYPE

class Rotate(Order):
    NAME = "Rotate"
    TYPE = "MOVEMENT"

    SHOW_BASE = False
    SHOW_LINE = True
    SHOW_VALUE = True
    SHOW_TARGET = True


    def On_Do(self, target:tuple[int, int]=None) -> None:
        data = self.Get_Data(target)

        # check if target valid
        if data['value'] == None: return

        self.vessel.rotation = data['value']

        self.vessel.turn_turns_amount -= 1


    def Get_Default_Data(self):
        return {
            'position':self.vessel.position,
            'value':'',
            'show_value':'',
            }


    def Get_Data(self, target: tuple[int, int] | list[int] | None = None) -> dict[str, any]:
        if target == None: super().Get_Default_Data() 
        if self.Is_Disabled(): super().Get_Default_Data()

        delta_X = self.vessel.position[0] - target[0]
        delta_Y = self.vessel.position[1] - target[1]

        new_rotation = degrees(atan2(delta_Y, -delta_X)) % 360
        deltaRotation = (self.vessel.rotation - new_rotation) % 360

        if self.vessel.turns < deltaRotation and deltaRotation < -self.vessel.turns % 360: return super().Get_Data()

        # return
        data = super().Get_Default_Data()
        data['value'] = new_rotation
        data['show_value'] = str(round(deltaRotation, 3))
        return data


    def Is_Disabled(self) -> bool:
        # no turns left
        if self.vessel.turn_turns_amount <= 0: return True

        # move rule
        if self.vessel.TYPE == VESSELTYPE.BATTLESHIP:
            return self.vessel.SPEED - self.vessel.turn_speed < 15
        elif self.vessel.TYPE == VESSELTYPE.CRUISER:
            return self.vessel.SPEED - self.vessel.turn_speed < 10
        else: return True