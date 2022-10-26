import math
from backend.game import Armament, Order



class WeaponsBattrey(Armament):
    NAME = "WEAPONSBATTREY"
    TYPE = "WEAPON"
    SHOW_BASE = False
    SHOW_LINE = True
    SHOW_VALUE = True
    SHOW_TARGET = True
    SHOW_ARC = True

    # def On_Give
    # Is_Visible
    # Is_Enabled
    # Is_Warn
    def Get_Default_Data(self): return {
        'position':self.vessel.position,
        'value':None,
        'show_value':''}


    def Get_Data(self, target: tuple[int, int] | list[int] | None = None) -> dict[str, any]:
        if target==None: return self.Get_Default_Data()

        target_vessel = self.game.Get_Vessel_In_Position(target, False, False, False, True)
        if target_vessel == None: return self.Get_Default_Data()

        if math.hypot(self.vessel.position[0] - target[0], self.vessel.position[1] - target[1]) > self.RANGE: return {
            'position':self.vessel.position,
            'value':"OUT OF RANGE",
            'show_value':''}

        return {
            'position':target_vessel.position,
            'value':target_vessel,
            'show_value':target_vessel.TYPE}
    # On_Do
    # Get_Display_Text