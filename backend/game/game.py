import pygame
import backend.game as game
from backend.game.player import Player
from backend.game.vessel import Vessel


class Game:
    def __init__(self, **preferences) -> None:
        self.players = list()
        self.size = (90, 60)
        self.accuracy = 5

        self.vessel_id_last:int = -1
        self.forces:list[game.Vessel] = list()

        from random import shuffle
        self.player_colors:list[pygame.Color] = [
            "GRAY",
            "RED",
            "GREEN",
            "BLUE",
            "MAGENTA",
            "YELLOW",
            "CYAN",
            ]
        shuffle(self.player_colors)

        # flags
        self.is_started = False

        self.player:Player = None

        # vizualizer
        if 'visualizer' in preferences: self.visualizer = preferences['visualizer']


    def Add_Vessel(self, vessel_type, owner:Player|int, position:tuple[int, int], rotation:int) -> game.Vessel:

        if type(owner) == int: owner = self.players[owner]

        # create new vessel
        new_vessel = vessel_type(self, owner, position, rotation, self.vessel_id_last + 1)
        
        # modify game data
        self.vessel_id_last += 1
        self.forces.append(new_vessel)

        # return
        return new_vessel


    def Join(self, socket, slot:int=None) -> None:

        new_player = Player(self, socket)
        self.players.append(new_player)
        return new_player

    
    def Start(self):
        self.is_started = True


    def Handle_Order(self, socket, order_data:dict) -> None:
        if not order_data: return

        # get vessel
        vessel = self.Get_Vessel_By_Id(order_data['vesselid'])
        if vessel.owner.socket != socket: return

        # get order
        order = vessel.Get_Order_By_Id(order_data['orderid'])
        order.Do(order_data['target'])


    def player_thread(self, socket):
        pass


    def Round(self, value) -> any:
        return round(value, self.accuracy)


    def Get_Player_Color(self):
        return self.player_colors.pop()


    def Get_Vessel_In_Position(self, position, is_enemy=False, is_ally=False, is_neutral=False, is_own=False) -> Vessel:

        if is_enemy and is_ally and is_neutral and is_own == False: return None

        for vessel in self.forces:
            if vessel.Is_Collision(position):
                return vessel
        
        return None


    def Get_Vessel_By_Id(self, id) -> Vessel:
        for vessel in self.forces:
            if vessel.id == id: return vessel
