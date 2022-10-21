from math import atan2, cos, degrees, hypot, sin
from turtle import position

from backend.game import Order, vessel



class Move(Order):
    NAME = "Move"
    TYPE = "MOVEMENT"

    SHOW_BASE = True
    SHOW_LINE = True
    SHOW_VALUE = True
    SHOW_TARGET = True


    def On_Do(self, target:tuple[int, int]=None) -> None:
        data = self.Get_Data(target)
        target_position = data['position']
        target_distande = data['value']

        # check if target valid
        if target_position == None: return

        # check if turn speed left
        if self.vessel.turn_speed <= 0: return

        # check if same
        if target_position == self.vessel.position: return

        # remove turn distance
        self.vessel.turn_speed -= target_distande

        self.vessel.position = target_position


    def Get_Default_Data(self):
        return {
            'position':self.vessel.position,
            'value':None,
            'show_value':'',
        }


    def Get_Data(self, target: tuple[int, int] | list[int] | None = None) -> dict[str, any]:
        if target == None: return self.Get_Default_Data()

        delta_X = self.vessel.position[0] - target[0]
        delta_Y = self.vessel.position[1] - target[1]

        # get target distance
        sinner =   + sin(self.vessel.rad_rotation)
        cosinner = - cos(self.vessel.rad_rotation)
        target_distance = cosinner * delta_X + sinner * delta_Y

        # position for loop
        ## current position
        curr_position = self.vessel.position
        curr_distance = 0
        ## second valid position
        last_valid_position = self.vessel.position
        last_valid_distance = 0
        ## first valid positon
        curr_valid_position = self.vessel.position
        curr_valid_distance = 0
        ## movement pool
        movement_left = self.vessel.turn_speed

        STEP_ACC = 0.01

        # move in direction
        while movement_left - STEP_ACC >= 0:

            # get new current positon
            curr_position = (
                curr_position[0] + cos(self.vessel.rad_rotation) * STEP_ACC,
                curr_position[1] - sin(self.vessel.rad_rotation) * STEP_ACC)
            curr_distance += STEP_ACC

            # reduce movement pool
            movement_left -= STEP_ACC
            movement_left += self._Get_Position_Movement_Decrease(curr_position)

            # hash if current positon is valid
            if self._Is_Valid_Positon(curr_position):
                ## second valid = first
                last_valid_position = curr_valid_position
                last_valid_distance = curr_valid_distance
                ## first valid = current
                curr_valid_position = curr_position
                curr_valid_distance = curr_distance

            # if target reached
            if curr_distance >= target_distance:
                ## continue until we find valid
                if curr_valid_position == curr_position: break

        # find valid position, closest to target position
        ## first valid is closer
        if abs(last_valid_distance - target_distance) > abs(curr_valid_distance - target_distance):
            return_distance = curr_valid_distance
            return_position = curr_valid_position
        ## second valid is closer
        else:
            return_distance = last_valid_distance
            return_position = last_valid_position

        # empty pool if pool is sell then accurancy
        if return_distance + STEP_ACC >= self.vessel.turn_speed:
            return_distance = self.vessel.turn_speed

        # return
        data = self.Get_Default_Data()
        data['position'] = return_position
        data['value'] = return_distance
        data['show_value'] = round(return_distance, 5)
        return data


    def _Is_Valid_Positon(self, position:tuple[int, int]|list[int]) -> bool:

        # vessels
        for vessel in self.game.forces:
            if vessel == self.vessel: continue
            if hypot(position[0] - vessel.position[0], position[1] - vessel.position[1]) < vessel.BASE_RADIUS + self.vessel.BASE_RADIUS:
                return False

        # no obstacles
        return True


    def _Get_Position_Movement_Decrease(self, position:tuple[int, int]|list[int]) -> int:
        return 0


    def Is_Disabled(self) -> bool:
        return self.vessel.turn_speed <= 0
