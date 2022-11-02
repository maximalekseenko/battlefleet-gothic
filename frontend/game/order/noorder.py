import backend.game as game


class NoOrder(game.Order):
    KEYWORD = 'noorder'
    NAME = 'Select Vessel'
    PHASE = 'All'


    def __init__(self, scene) -> None:
        from .ordersmenu import OrdersMenu
        self.scene:OrdersMenu = scene

        self.game:game.Game = self.scene.act.game


    def Do(self, position:game.position) -> None:
        self.scene.selected_vessel = self.game.Get_Vessel_In_Position(position, False, False, False, True)
        self.scene.Update()
