from backend.game.common.actions.move import Move
from backend.game.vessel import Vessel
from backend.game.armament import Armament, FIREARC


class WeaponsBattery(Armament):
    def __init__(self, firearc) -> None:
        super().__init__(firearc)


class LunarClassCruiser(Vessel):

    # datasheet
    HITS = 8
    TYPE = Vessel.TYPECRUISER
    SPEED = 20
    TURNS = 45
    ARMAMENTS = [WeaponsBattery(FIREARC.LEFT), WeaponsBattery(FIREARC.RIGHT)]


    # actions
    MOVEMENT_ACTIONS = [Move]
    SPECAL_ACTIONS = []
    VESSEL_ACTIONS = []
    ARMAMENT_ACTIONS = []