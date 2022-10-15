import math

from .order import Order
from .armament import Armament
from .player import Player
from .enums import VESSELTYPE


class Vessel:
    '''
    \n constants:
    
    *   `TYPE`
    *   `HITS`
    *   `SPEED`
    *   `TURNS`

    *   `ORDERS`
    *   `ARMAMENTS`

    *   `BASE_RADIUS`
    '''

    # datasheet
    TYPE:VESSELTYPE
    HITS:int
    '''starting hits'''
    SPEED:int
    '''starting speed'''
    TURNS:int
    '''starting turns'''

    # lists
    ORDERS:list[type[Order]]
    ARMAMENTS:list[type[Armament]]

    BASE_RADIUS:int


    def __init__(self, game, owner:Player, position:tuple[int,int], rotation:int, id:int) -> None:
        
        from .game import Game
        self.game:Game = game

        # properties
        self._rotation:int = 0

        # game variables
        self.owner:Player = owner
        self.id:int = id
        self.position:tuple[int,int] = position
        self.rotation = rotation

        # datasheet
        self.hits = self.HITS
        self.speed = self.SPEED
        self.turns = self.TURNS

        # lists
        self.orders:list[Order] = list()

        order_id = 0
        for order in self.ORDERS:
            self.orders.append(order(self, order_id))
            order_id += 1


    @property
    def rotation(self) -> int:
        return self._rotation
    
    @rotation.setter
    def rotation(self, value):
        self._rotation = value % 360

    @property
    def rad_rotation(self) -> int:
        return math.radians(self.rotation)


    def Get_Order_By_Id(self, id) -> Order:
        for order in self.orders:
            if order.id == id: return order

