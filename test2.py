from backend.game.common.orders.move import Move
from backend.game.common.orders.rotate import Rotate
from backend.game.common.orders.allaheadfull import AllAheadFull
from backend.game import Vessel, VESSELTYPE, Armament, FIREARC
from backend.game.common.orders.weaponsbattrey import WeaponsBattrey


class PortWeaponsBattery(WeaponsBattrey):
    NAME = "Port-WEAPONS-BATTERY"
    RANGE = 60
    FIREPOWER = 6
    ARMAMENT_ORDER = None
    FIREARC = FIREARC.PORT

class StarboardWeaponsBattery(Armament):
    NAME = "STARBOARD-WEAPONS-BATTERY"
    RANGE = 60
    FIREPOWER = 6
    ARMAMENT_ORDER = None
    FIREARC = FIREARC.STARBOARD


class PortLanceBattrey(Armament):
    NAME = "PORT-LANCE-BATTREY"
    RANGE = 45
    FIREPOWER = 2
    ARMAMENT_ORDER = None
    FIREARC = FIREARC.PORT

class PortLanceBattrey(Armament):
    NAME = "STARBOARD-LANCE-BATTREY"
    RANGE = 45
    FIREPOWER = 2
    ARMAMENT_ORDER = None
    FIREARC = FIREARC.PORT

class Torpedos(Armament):
    NAME = "Torpedos"
    RANGE = 100
    FIREPOWER = 3
    ARMAMENT_ORDER = None
    FIREARC = FIREARC.PROW



class LunarClassCruiser(Vessel):

    # datasheet
    CLASSNAME = "LUNAR"
    HITS = 8
    TYPE = VESSELTYPE.CRUISER
    SPEED = 20
    TURNS = 45
    BASE_RADIUS = 3.2
    


    # actions
    ORDERS = [Move, Rotate, AllAheadFull, PortWeaponsBattery]