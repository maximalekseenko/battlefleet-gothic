from .action import Action
from .armament import Armament



class Vessel:

    TYPEESCORT = 0
    TYPECRUISER = 1
    TYPEBATTLESHIP = 2

    # actions
    MOVEMENT_ACTIONS:list[Action]
    SPECAL_ACTIONS:list[Action]
    VESSEL_ACTIONS:list[Action]
    ARMAMENT_ACTIONS:list[Action]


    # datasheet
    HITS:int
    TYPE:int
    SPEED:int
    TURNS:int
    ARMAMENTS:list[Armament]
    LEADERSHIP:int


    def __init__(self, owner, position:tuple[int,int], rotation:int, id:int) -> None:

        # game variables
        self.owner = owner
        self.id:int = id
        self.position:tuple[int,int] = position
        self.rotation:int = rotation

        # turn stuff
        self.movement_actions:list[Action]
        self.specal_actions:list[Action]
        self.vessel_actions:list[Action]
        self.armament_actions:list[Action]
        self.hits_current:int
        self.speed_current:int
        self.turns_current:int

        self.Game_Reset()
        self.Turn_Reset()


    def Game_Reset(self):

        # hits
        self.hits_current = self.HITS

        # actions
        self.movement_actions = [action(self) for action in self.MOVEMENT_ACTIONS]
        self.specal_actions = [action(self) for action in self.SPECAL_ACTIONS]
        self.vessel_actions = [action(self) for action in self.VESSEL_ACTIONS]
        # self.armament_actions = [action for action in self.ARMAMENTS]


    def Turn_Reset(self):
        self.speed_current = self.SPEED
        self.turns_current = self.TURNS

        for armament in self.ARMAMENTS: armament.Turn_Reset()


    def Turn(self, angle):

        # is already turned
        if self.turns_current == 0: return False

        # fix angle
        if angle > self.turns_current: 
            angle = self.turns_current
        elif angle < -self.turns_current: 
            angle = -self.turns_current

        # turn counter
        self.turns_current += abs(angle)

        self.rotation += angle