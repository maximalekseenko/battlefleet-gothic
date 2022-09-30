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

    
    def On_Update(self):

        # update menus
        self.connectionmenu.Update()


    def On_Open(self) -> None:

        # reset menus
        self.connectionmenu.Open()


    def On_Close(self) -> None:

        # close menus
        self.connectionmenu.Close()

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        # handle menus if needed
        self.connectionmenu.Handle(event)

    
    def On_Render(self) -> None:

        # fill background
        self.surface.fill(theatre.settings["background_color"])

        # render menus if needed
        self.connectionmenu.Render()