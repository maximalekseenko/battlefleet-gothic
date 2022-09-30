import pygame

# engine
from engine import Act
from theatre import theatre



class MainAct(Act):
    def __init__(self) -> None:
        super().__init__()

        # surface
        self.surface = pygame.display.get_surface()

        # menus (scenes)
        from mainmenu.scenes import MainMenu, SettingsMenu
        self.mainmenu:MainMenu = MainMenu(self, self.surface)
        self.settingsmenu:SettingsMenu = SettingsMenu(self, self.surface)

    
    def On_Open(self) -> None:
        self.Update()
        self.mainmenu.Open()
        self.settingsmenu.Close()


    def On_Update(self):
        self.mainmenu.Update()
        self.settingsmenu.Update()

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        if self.mainmenu.is_opened: self.mainmenu.Handle(event)
        elif self.settingsmenu.is_opened: self.settingsmenu.Handle(event)

    
    def On_Render(self) -> None:
        self.surface.fill(theatre.settings["background_color"])

        if self.mainmenu.is_opened: self.mainmenu.Render()
        elif self.settingsmenu.is_opened: self.settingsmenu.Render()