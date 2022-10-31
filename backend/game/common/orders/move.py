import math
import backend.game as game



class Move(game.Order):
    KEYWORD = 'move'
    NAME = 'Move Vessel'
    PHASE = 'Movement'


    def Do(self, target:game.position) -> None:
        position, distande = self._Get_Position_And_Distance(target)

        # check if same
        if position == self.vessel.position: return

        # remove turn distance
        self.vessel.turn_speed -= distande

        # move vessel
        self.vessel.position = position


    def Preview(self, target: game.position | None) -> None:
        final_position, distace = self._Get_Position_And_Distance(target)
        
        self.game.visualizer.Line("#a000b0", self.vessel.position, final_position)
        self.game.visualizer.Highlight("#a000b0", self.vessel, final_position)
        self.game.visualizer.Arcs("#a000b0", final_position, 60)


    def _Get_Position_And_Distance(self, target: game.position) -> tuple[game.position, int]:
        delta = self.vessel.position - target

        # get target distance
        sinner =   + math.sin(self.vessel.rad_rotation)
        cosinner = - math.cos(self.vessel.rad_rotation)
        target_distance = cosinner * delta[0] + sinner * delta[1]

        # variables for loop
        curr_position = self.vessel.position.copy()
        curr_distance = 0
        ## first valid positon
        first_valid_position = self.vessel.position.copy()
        first_valid_distance = 0
        ## second valid position
        second_valid_position = self.vessel.position.copy()
        second_valid_distance = 0
        ## movement pool
        movement_left = self.vessel.turn_speed

        STEP_ACC = 0.01

        # move in direction
        while movement_left - STEP_ACC >= 0:

            # get new current positon
            curr_position.x += math.cos(self.vessel.rad_rotation) * STEP_ACC
            curr_position.y -= math.sin(self.vessel.rad_rotation) * STEP_ACC
            curr_distance += STEP_ACC

            # reduce movement pool
            movement_left -= STEP_ACC
            movement_left += self._Get_Position_Movement_Decrease(curr_position)

            # hash if current positon is valid
            if self._Is_Valid_Positon(curr_position):
                ## second valid = first
                second_valid_position = first_valid_position
                second_valid_distance = first_valid_distance
                ## first valid = current
                first_valid_position = curr_position.copy()
                first_valid_distance = curr_distance

            # if target reached
            if curr_distance >= target_distance:
                ## continue until we find valid
                if first_valid_position == curr_position: break

        # find valid position, closest to target position
        ## first valid is closer
        if abs(second_valid_distance - target_distance) > abs(first_valid_distance - target_distance):
            return_distance = first_valid_distance
            return_position = first_valid_position
        ## second valid is closer
        else:
            return_distance = second_valid_distance
            return_position = second_valid_position

        # empty pool if pool is less then accurancy
        if return_distance + STEP_ACC >= self.vessel.turn_speed:
            return_distance = self.vessel.turn_speed

        # return
        return return_position, return_distance


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


    @property
    def is_disabled(self):
        return self.vessel.turn_speed <= 0


