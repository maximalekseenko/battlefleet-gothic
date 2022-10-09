import pygame
import backend.game as game
from backend.game.player import Player


class Game:
    def __init__(self, **preferences) -> None:
        self.players = list()
        self.size = (90, 60)

        self.vessel_id_last:int = -1
        self.forces:list[game.Vessel] = list()

        from random import shuffle
        self.player_colors:list[pygame.Color] = [
            "#505050", #grey
            "#500000", #red
            "#005000", #green
            "#000050", #blue
            "#500050", #magenta
            "#505000", #yellow
            "#005050", #cyan
            ]
        shuffle(self.player_colors)

        # flags
        self.is_started = False


    def Add_Vessel(self, vessel_type, owner:Player|int, position:tuple[int, int], rotation:int) -> game.Vessel:

        if type(owner) == int: owner = self.players[owner]

        # create new vessel
        new_vessel = vessel_type(owner, position, rotation, self.vessel_id_last + 1)
        
        # modify game data
        self.vessel_id_last += 1
        self.forces.append(new_vessel)

        # return
        return new_vessel


    def Join(self, socket, slot:int=None) -> None:

        new_player = Player(self, socket)
        self.players.append(new_player)
        return new_player

        # # slot specified
        # if slot != None:
        #     # validate slot
        #     ## out of range
        #     if slot < 0 or slot > len(self.players): return
        #     ## already occupied
        #     if self.players[slot] == None: return

        # # slot not specified -> get empty
        # if slot == None:

        #     # find empty slot
        #     for slot in range(len(self.players)):
        #         if self.players[slot] == None: 
        #             break

        #     # no slots avaliable
        #     if slot == None: return

        # fill slot
        # self.players[slot] = socket

    
    def Start(self):
        self.is_started = True


    def Handle_Action(self, socket, action_data:dict):
        if not action_data: return

        actor = action_data['actor']

        action = actor.Get_Action(name=action_data['name'], type=action_data['type'])
        action.Do(self, **action_data)


    def player_thread(self, socket):
        pass


    def Get_Player_Color(self):
        return self.player_colors.pop()