class Order:
    '''
    \n constants:
    *   `KEYWORD`:`str` - Keyword for finding event. Must be unique.
    *   `NAME`:`str` - Name that will be shown on OrdersMenu.
    *   `PHASE`:`???` - 
    *   `TARGET`:`None`|`Vessel`|`position` - Target this event needs to start.
    
    \n properties:
    *   `is_visible`->`bool` - Should this order be shown in the menu.
    *   `is_disabled`->`bool` - Should this order be shown as disabled in the menu.
    *   `is_warn`->`bool` - Should this order be highlighed red in the menu and prevent round finish.

    \n functions:
    *   Get_Front_Data ->
    *   Give

    \n KEYWORD+NAME+PHASE+TARGET
    \n is_visible+is_disabled+is_warn
    '''


    # constants
    KEYWORD:str = ''
    NAME:str = ''
    PHASE:None = ''
    TARGET:str = None


    # properties
    @property
    def is_visible(self) -> bool: return True
    @property
    def is_disabled(self) -> bool: return False
    @property
    def is_warn(self) -> bool: return False


    # functions
    def Get_Front_Data(self, mouse_pos:tuple[int,int]|None) -> dict:
        """
        \n Returns data for frontal preview of this order. 
        \n Note, that `mouse_pos` is in map units.
        \n keys:
        *   `'value'`:`str` - what text should be rendered near the cursor. If `False` wont be rendered at all.
        *   `'arc'`:`???` - ???. If `False` wont be rendered at all.
        *   `'position'`:`position` - position of the target. 
        *   `'base'`:`bool` - should base of the selected vessel be rendered around the `'position'`.
        *   `'target'`:`bool` - should target dot be rendered at `'position'`. If `False` wont be rendered at all.
        *   `'line'`:`bool` - should be line from selected vessel to target be rendered.
        \n value+arc+position+base+target+line
        """

        return {
            'value'     : False,
            'arc'       : False,
            'position'  : mouse_pos,
            'base'      : False,
            'target'    : False,
            'line'      : False,
        }




    def __init__(self, vessel, id:int) -> None:

        from .vessel import Vessel
        self.vessel:Vessel = vessel

        from .game import Game
        self.game:Game = vessel.game

        self.id:int = id

