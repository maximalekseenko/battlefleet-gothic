from backend.game.action import Action
from backend.game.common.actions.move import Move
from backend.game.common.actions.allaheadfull import AllAheadFull
from backend.game.vessel import Vessel
from backend.game.armament import Armament, ARC


class WeaponsBatteryPort(Armament):
    COLOR = "#a0a000"
    NAME = "Weapons Battery"
    RANGE = 60
    FIREPOWER = 6
    FIREARC:ARC.LEFT

class WeaponsBatteryStarboard(Armament):
    COLOR = "#a0a000"
    NAME = "Weapons Battery"
    RANGE = 60
    FIREPOWER = 6
    FIREARC:ARC.LEFT

class LancePort(Armament):
    COLOR = "#0000a0"
    NAME = "Weapons Battery"
    RANGE = 30
    FIREPOWER = 6
    FIREARC:ARC.LEFT

class LanceStarboard(Armament):
    COLOR = "#a0a000"
    NAME = "Weapons Battery"
    RANGE = 30
    FIREPOWER = 6
    FIREARC:ARC.LEFT


class LunarClassCruiser(Vessel):

    # datasheet
    CLASSNAME = "LUNAR"
    HITS = 8
    TYPE = "CRUISER"
    SPEED = 20
    TURNS = 45
    ARMAMENTS = [WeaponsBatteryPort(), WeaponsBatteryStarboard(), LancePort(), LanceStarboard()]
    BASE_RADIUS = 5


    # actions
    ORDERS = [Move, AllAheadFull]
    MOVEMENT_ACTIONS = [Move,Action]
    SPECAL_ACTIONS = [Action,Action,Action,Action,Action,Action]
    VESSEL_ACTIONS = [Action,Action,Action]