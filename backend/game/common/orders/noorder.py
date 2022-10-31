import backend.game as game


class NoOrder(game.Order):


    def __init__(self, scene) -> None:
        from frontend.scenes import OrdersMenu
        self.scene:OrdersMenu = scene

        self.game:game.Game = self.scene.act.game


    KEYWORD = 'noorder'
    NAME = 'Select Vessel'
    PHASE = 'All'


    def Get_Position_Data(self, mouse_pos: tuple[int, int]) -> dict:

        # get vessel on the mouse
        selected_vessel = self.game.Get_Vessel_In_Position(mouse_pos, False, False, False, True)

        # fill data
        data = super().Get_Position_Data(mouse_pos)
        data['value'] = str(selected_vessel.TYPE) if selected_vessel else False
        data['arc'] = False
        data['position'] = selected_vessel.position if selected_vessel else mouse_pos
        data['base'] = True
        data['target'] = True
        data['line'] = False

        # return data
        return data


    def Do_Position(self, position:game.position) -> None:
        self.scene.selected_vessel = self.game.Get_Vessel_In_Position(position, False, False, False, True)
        self.scene.Update()
