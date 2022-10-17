from enum import Enum



class VESSELTYPE(Enum):
    ESCORT = 0
    CRUISER = 1
    BATTLESHIP = 2

    DEFENCE = 3
    ORDNANCE = 4

    CAPITAL = 5


    def __eq__(vessel_type_a, vessel_type_b: object) -> bool:
        if vessel_type_a.value == VESSELTYPE.CAPITAL.value:
            return vessel_type_b.value == VESSELTYPE.CRUISER.value \
                or vessel_type_b.value == VESSELTYPE.BATTLESHIP.value

        return super().__eq__(vessel_type_b)

