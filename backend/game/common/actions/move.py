import backend.game as game


class Move(game.Action):
    NAME = "MOVE"


    def Check(self, vessel, position) -> bool:
        if vessel.speed_current: return False
        return True


    def Do(self, vessel, position) -> None:
        return super().Do()


    def Get_Done(self, vessel, position) -> dict:
        if not self.Check(vessel, position): return {}

        return {
            'name': self.NAME,
            'vessel': vessel,
            'position': position,
        }