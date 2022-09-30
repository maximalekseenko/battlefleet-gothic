import pygame

# engine
from engine import Act
from backend.theatre import theatre



class GameAct(Act):
    def __init__(self) -> None:
        super().__init__()

        # surface
        self.surface = pygame.display.get_surface()

        # scenes
        from frontend.scenes import ConnectionMenu
        self.connectionmenu:ConnectionMenu = ConnectionMenu(self, self.surface)


    def On_Open(self) -> None:
        self.connectionmenu.Open()

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        self.connectionmenu.Handle(event)

    
    def On_Render(self) -> None:
        self.surface.fill(theatre.settings["background_color"])

        self.connectionmenu.Render()