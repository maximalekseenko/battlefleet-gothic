from .vessel import Vessel


class Game:
    def __init__(self, **preferences) -> None:
        self.players = [None, None]
        self.size = (90, 60)

        self.vessel_id_last:int = -1
        self.forces:list[Vessel] = list()

        # flags
        self.is_started = False


    def Add_Vessel(self, vessel_type, owner_index:int, position:tuple[int, int], rotation:int):
        self.forces.append(vessel_type(self.players[owner_index], position, rotation, self.vessel_id_last + 1))
        self.vessel_id_last += 1


    def Join(self, socket, slot:int=None) -> None:

        # slot specified
        if slot != None:
            # validate slot
            ## out of range
            if slot < 0 or slot > len(self.players): return
            ## already occupied
            if self.players[slot] == None: return

        # slot not specified -> get empty
        if slot == None:

            # find empty slot
            for slot in range(len(self.players)):
                if self.players[slot] == None: 
                    break

            # no slots avaliable
            if slot == None: return

        # fill slot
        self.players[slot] = socket

    
    def Start(self):
        self.is_started = True


    def Handle_Actions(self, socket, actions:list):
        for action in actions:
            pass


    def player_thread(self, socket):
        pass


    