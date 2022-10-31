from __future__ import annotations
import math

import backend.game as game


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
    # game
    MOVEMENT_CHECKS:list = list()

    # datasheet
    TYPE:game.VESSELTYPE
    HITS:int
    '''starting hits'''
    SPEED:int
    '''starting speed'''
    TURNS:int
    '''starting turns'''

    # lists
    ORDERS:list[type[game.Order]]
    ARMAMENTS:list[type[game.Armament]]

    BASE_RADIUS:int


    def __init__(self, __game, owner:game.Player, position:game.position, rotation:int, id:int) -> None:
        self.game:game.Game = __game

        # position
        if type(position) != game.position: position = game.position(*position)
        self.position:game.position = position

        # properties
        self._rotation:int = 0

        # game variables
        self.owner:game.Player = owner
        self.id:int = id
        self.rotation = rotation

        # datasheet
        self.hits = self.HITS
        self.speed = self.SPEED
        self.turns = self.TURNS

        # lists
        self.orders:list[game.Order] = list()

        order_id = 0
        for order in self.ORDERS:
            self.orders.append(order(self, order_id))
            order_id += 1

        self.Turn_Reset()

    
    def Turn_Reset(self):
        self.turn_speed = self.speed
        self.turn_turns_amount = 1


    @property
    def rotation(self) -> int:
        return self._rotation
    
    @rotation.setter
    def rotation(self, value):
        self._rotation = value % 360

    @property
    def rad_rotation(self) -> int:
        return math.radians(self.rotation)


    def Is_Collision(self, point:game.position) -> bool:
        return math.hypot(self.position[0] - point[0], self.position[1] - point[1]) <= self.BASE_RADIUS


    def Get_Order_By_Id(self, id) -> game.Order:
        for order in self.orders:
            if order.id == id: return order

