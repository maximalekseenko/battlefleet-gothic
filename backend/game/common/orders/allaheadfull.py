from backend.game import Order


class AllAheadFull(Order):
    NAME = "ALLAHEADFULL"
    TYPE = "SPECAL"
    DISPLAY_NAME = "ALL AHEAD FULL"
    TOOLTIP = "Move more."


    def Step(self, **kargs): 
        self.vessel.orders["MOVE"].use_maximum += 100
        self.vessel.orders["MOVE"].use_minimum = self.vessel.orders["MOVE"].use_maximum


    def On_Selected(self) -> None:
        self.Do()
