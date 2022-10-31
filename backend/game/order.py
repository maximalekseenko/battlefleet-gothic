from __future__ import annotations
import backend.game as game


class Order:
    """
    \n KEYWORD+NAME+PHASE+TARGET
    \n is_visible+is_disabled+is_warn
    \n Get_Front_Data
    """


    # constants
    KEYWORD:str = ''
    '''Keyword for finding event. Must be unique.'''
    NAME:str = ''
    '''Name that will be shown on OrdersMenu.'''
    PHASE:None = None
    '''TODO.'''


    # properties
    @property
    def is_invisible(self) -> bool:
        '''Should this order be shown in the menu.'''
        return False

    @property
    def is_disabled(self) -> bool:
        '''Should this order be shown as disabled in the menu.'''
        return False

    @property
    def is_warn(self) -> bool:
        '''Should this order be highlighed red in the menu and prevent round finish.'''
        return False

    def Preview(self, target:game.position|None) -> None: ...

    def Do(self, position:game.position|None) -> None: ...


    def __init__(self, vessel:game.Vessel, id:int) -> None:

        self.vessel:game.Vessel = vessel
        self.game:game.Game = vessel.game
        self.id:int = id
