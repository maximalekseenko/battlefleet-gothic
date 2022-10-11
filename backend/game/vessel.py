import math


from .action import Action
from .armament import Armament
from .player import Player



class Vessel:

    TYPEESCORT = 0
    TYPECRUISER = 1
    TYPEBATTLESHIP = 2

    # actions
    MOVEMENT_ACTIONS:list[Action]
    SPECAL_ACTIONS:list[Action]
    VESSEL_ACTIONS:list[Action]
    ARMAMENT_ACTIONS:list[Action]
    ORDERS:list[type[Action]]


    # datasheet
    CLASSNAME:int
    HITS:int
    TYPE:int
    SPEED:int
    TURNS:int
    ARMAMENTS:list[Armament]
    LEADERSHIP:int
    BASE_RADIUS:int


    def __init__(self, game, owner:Player, position:tuple[int,int], rotation:int, id:int) -> None:

        from .game import Game
        self.game:Game = game

        # game variables
        self.owner:Player = owner
        self.id:int = id
        self.position:tuple[int,int] = position
        self.rotation:int = rotation


        self.orders:dict[str,Action]

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
        self.armament_actions = [action for action in self.ARMAMENTS]


    def Turn_Reset(self):
        self.orders = {order.NAME: order(self) for order in sorted(self.ORDERS, key=Action.Get_Order_Size)}

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


    def Get_Action(self, name:str, type:str) -> Action:
        if type == "MOVEMENT":
            for action in self.movement_actions:
                if action.NAME == name: return action
        if type == "ARMAMENT":
            for action in self.armament_actions:
                if action.NAME == name: return action
        if type == "SPECAL":
            for action in self.specal_actions:
                if action.NAME == name: return action
        if type == "VESSEL":
            for action in self.vessel_actions:
                if action.NAME == name: return action
        

    def Is_Collision(self, point):
        return math.dist(self.position, point) <= self.BASE_RADIUS



