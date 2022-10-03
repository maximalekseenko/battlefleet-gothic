from .armament import Armament, FIREARC

class Vessel:

    TYPEESCORT = 0
    TYPECRUISER = 1
    TYPEBATTLESHIP = 2

    def __init__(self, owner, position:tuple[int,int], rotation:int, id:int) -> None:

        # game variables
        self.owner = owner
        self.id:int = id

        # datasheet
        self.hits:int = 8
        self.type:int = Vessel.TYPECRUISER
        self.speed:int = 20
        self.turns:int = 45
        self.armaments:list[Armament] = [Armament(FIREARC.LEFT), Armament(FIREARC.RIGHT)]

        # space
        self.position:tuple[int,int] = position
        self.rotation:int = rotation


        self.hits_current:int = 8
        # turn stuff
        self.turn_movement:int
        self.turn_rotation:int

        self.Turn_Reset()


    def Turn_Reset(self):
        self.turn_movement = self.speed
        self.turn_rotation = self.turns

        for armament in self.armaments: armament.Turn_Reset()


    def Turn(self, angle):

        # is already turned
        if self.turn_rotation == 0: return False

        # fix angle
        if angle > self.turn_rotation: 
            angle = self.turn_rotation
        elif angle < -self.turn_rotation: 
            angle = -self.turn_rotation

        # turn counter
        self.turn_rotation += abs(angle)

        self.rotation += angle