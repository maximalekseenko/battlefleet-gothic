import math
from backend.game import Armament, Order, position, Vessel



class WeaponsBattrey(Order):
    KEYWORD = 'weaponsbattrey'
    TAGS = ['armament']
    NAME = "Weapons Battrey"


    def Do(self, target:position):
        target_vessel = self.game.Get_Vessel_In_Position(target, is_enemy=True)
        if not target_vessel: return

        if not self._Is_Valid_Target(target_vessel): return

        target_vessel.hits -= 1


    def Preview(self, target:position|None):
        self.game.visualizer('Arcs', color='#a00000', vessel=self.vessel)

        # with target
        if target != None:

            # get target vessel
            target_vessel = self.game.Get_Vessel_In_Position(target, is_enemy=True)
            if not target_vessel: return

            # check target
            if not self._Is_Valid_Target(target_vessel): return

            # render
            self.game.visualizer('Line', color="#a000b0", position=self.vessel.position, position2=target_vessel.position)


    def _Is_Valid_Target(self, target_vessel:Vessel):
        if math.hypot(*(self.vessel.position - target_vessel.position)) > 50: return False
        return True
