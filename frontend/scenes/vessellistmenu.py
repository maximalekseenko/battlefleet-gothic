import pygame

# engine
from engine import Scene
from frontend.theatre import theatre



class VessellistMenu(Scene):
    def __init__(self, act, surface: pygame.Surface) -> None:
        super().__init__(act, surface)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct

        # variables
        self.selected_vessel = None

    # ----------ON_STUFF----------
    def On_Update(self):
        pass


    def On_Open(self) -> None:
        pass

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        pass


    def On_Render(self) -> None:
        if self.selected_vessel:
            pass
