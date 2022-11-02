from backend.game import Order
import backend.game as game


class AllAheadFull(Order):
    KEYWORD = "allaheadfull"
    NAME = "All Ahead Full"


    def Preview(self, target: game.position | None) -> None:
        pass


    def Do(self, position: game.position | None) -> None:
        self.vessel.turn_speed += 100