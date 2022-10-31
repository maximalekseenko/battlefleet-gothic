from backend.game import Vessel, VESSELTYPE


class NoVessel(Vessel):
    # datasheet
    CLASSNAME = ""
    HITS = 0
    TYPE = VESSELTYPE.DEFENCE
    SPEED = 0
    TURNS = 0
    ARMAMENTS = []
    BASE_RADIUS = 0
    


    # actions
    ORDERS = []