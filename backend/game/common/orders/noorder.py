import backend.game as game


class NoOrder(game.Order):
    NAME = "SELECTVESSEL"
    TYPE = ""

    SHOW_BASE = False
    SHOW_LINE = False
    SHOW_VALUE = True
    SHOW_TARGET = True

    def __init__(self, scene) -> None:
        from frontend.scenes import OrdersMenu
        self.scene:OrdersMenu = scene

        self.game:game.Game = self.scene.act.game


    def Do(self, position=None) -> None:
        self.scene.selected_vessel = self.Get_Data(position)['value']
        self.scene.Update()


    def Get_Data(self, target: tuple[int, int] | list[int] | None = None) -> dict[str, any]:
        vessel = self.game.Get_Vessel_In_Position(target, False, False, False, True)

        data = super().Get_Data()
        data['value'] = vessel
        if vessel != None: 
            data['position'] = vessel.position
            data['show_value'] = str(vessel.TYPE)
        return data


    def Get_Done(self, game:game.Game, position) -> dict:
        if not self.Check(game, position): return None

        return {
            'type': self.TYPE,
            'name': self.NAME,
            'actor': self.vessel,
            'position': position,
        }

