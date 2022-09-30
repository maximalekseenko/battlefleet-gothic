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
        from frontend.scenes import ConnectingMenu
        self.connectingmenu:ConnectingMenu = ConnectingMenu(self, self.surface)


    def On_Open(self) -> None:
        self.connectingmenu.Open()

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        self.connectingmenu.Handle(event)

    
    def On_Render(self) -> None:
        self.surface.fill(theatre.settings["background_color"])

        self.connectingmenu.Render()