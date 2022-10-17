import pygame

# engine
from engine import Act
from frontend.theatre import theatre



class MainAct(Act):
    def __init__(self) -> None:
        super().__init__()

        # surface
        self.surface = pygame.display.get_surface()

        # menus (scenes)
        from frontend.scenes import MainMenu, SettingsMenu
        self.mainmenu:MainMenu = MainMenu(self, self.surface)
        self.settingsmenu:SettingsMenu = SettingsMenu(self, self.surface)

    
    def On_Open(self) -> None:

        # reset menus
        self.mainmenu.Open()
        self.settingsmenu.Close()

        
    def On_Close(self) -> None:

        # close menus
        self.mainmenu.Close()
        self.settingsmenu.Close()


    def On_Update(self):

        # update all menus
        self.mainmenu.Update()
        self.settingsmenu.Update()

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        # switch-case pass to menus
        if self.mainmenu.is_opened: self.mainmenu.Handle(event)
        elif self.settingsmenu.is_opened: self.settingsmenu.Handle(event)

    
    def On_Render(self) -> None:

        # fill background
        self.surface.fill(theatre.settings["background_color"])

        # switch-case render menus
        if self.mainmenu.is_opened: self.mainmenu.Render()
        elif self.settingsmenu.is_opened: self.settingsmenu.Render()