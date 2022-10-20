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

        # remove turn distance
        self.vessel.turn_speed -= self.distance

        self.vessel.position = target

        
    def Fix_Target(self, target:tuple[int, int]=None) -> any:
        if target == None: return

        delta_X = self.vessel.position[0] - target[0]
        delta_Y = self.vessel.position[1] - target[1]

        # direction check
        if 90 < (self.vessel.rotation - degrees(atan2(delta_Y, -delta_X)) % 360) % 360 < 270: 
            return self.vessel.position

        # get target distance
        sinner =   - sin(self.vessel.rad_rotation)
        cosinner = + cos(self.vessel.rad_rotation)
        target_distance = abs(cosinner * delta_X + sinner * delta_Y)

        # hash
        curr_position = self.vessel.position
        curr_distance = 0

        last_valid_position = self.vessel.position
        last_valid_distance = 0

        curr_valid_position = self.vessel.position
        curr_valid_distance = 0

        movement_left = self.vessel.turn_speed

        STEP_ACC = 1/self.game.accuracy

        print()
        while movement_left - STEP_ACC >= 0:

            # get new positon
            curr_position = (
                curr_position[0] + cos(self.vessel.rad_rotation) * STEP_ACC,
                curr_position[1] - sin(self.vessel.rad_rotation) * STEP_ACC)
            curr_distance += STEP_ACC

            # count movements
            movement_left -= STEP_ACC
            movement_left += self._Get_Position_Movement_Decrease(curr_position)

            # hash position if valid
            if self._Is_Valid_Positon(curr_position):
                last_valid_position = curr_valid_position
                last_valid_distance = curr_valid_distance
                curr_valid_position = curr_position
                curr_valid_distance = curr_distance

            # if target reached
            if curr_distance >= target_distance:
                if curr_valid_position == curr_position: break

        # return
        if abs(last_valid_distance - target_distance) > abs(curr_valid_distance - target_distance):
            return_distance = curr_valid_distance
            return_position = curr_valid_position
        else:
            return_distance = last_valid_distance
            return_position = last_valid_position

        # fix distance
        if return_distance + STEP_ACC >= self.vessel.turn_speed:
            return_distance = self.vessel.turn_speed

        # return 
        self.distance = return_distance
        return return_position


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
