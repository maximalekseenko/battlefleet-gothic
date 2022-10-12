from enum import Enum



class FIREARC(Enum):
    PORT = 0
    '''(left)'''
    PROW = 1
    '''(front)'''
    STARBOARD = 2
    '''(right)'''

    DORSAL = 3
    '''(left/front/right)'''


    def __eq__(arc_a, arc_b: object) -> bool:
        if arc_a == FIREARC.DORSAL:
            return arc_b == FIREARC.PORT or arc_b == FIREARC.PROW or arc_b == FIREARC.STARBOARD

        return super().__eq__(arc_b)