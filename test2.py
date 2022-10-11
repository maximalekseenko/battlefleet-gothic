from backend.game.action import Action
from backend.game.common.actions.move import Move
from backend.game.common.actions.allaheadfull import AllAheadFull
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
    BASE_RADIUS = 5


    # actions
    ORDERS = [Move, AllAheadFull]
    MOVEMENT_ACTIONS = [Move,Action]
    SPECAL_ACTIONS = [Action,Action,Action,Action,Action,Action]
    VESSEL_ACTIONS = [Action,Action,Action]