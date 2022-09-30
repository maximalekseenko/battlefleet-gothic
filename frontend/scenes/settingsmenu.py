import pygame

# engine
from engine import Scene, Element
from backend.theatre import theatre



class SettingsMenu(Scene):
    def __init__(self, act, surface) -> None:
        super().__init__(act, surface)

        # for snippets
        from frontend.acts import MainAct
        self.act:MainAct

        # elements
        from frontend.elements import MenuButton, ColorSetting, TextSetting

        self.elements:list[Element] = [
            ColorSetting(self, from_center_top=(-125, 100), setting_name="Background", setting_key="background_color"),
            ColorSetting(self, from_center_top=(-125, 140), setting_name="Ui", setting_key="ui_color"),
            ColorSetting(self, from_center_top=(-125, 180), setting_name="Neutral", setting_key="neutral_color"),
            ColorSetting(self, from_center_top=(-125, 220), setting_name="Player", setting_key="player_color"),
            
            ColorSetting(self, from_center_top=(125, 100), setting_name="Enemy", setting_key="enemy_color"),
            TextSetting(self, from_center_top=(125, 140), setting_name="Name", setting_key="player_name"),
            TextSetting(self, from_center_top=(125, 180), setting_name="IP", setting_key="server_ip"),
            TextSetting(self, from_center_top=(125, 220), setting_name="Port", setting_key="server_port"),
            MenuButton(self, text="Save and back", from_center_top=(0, 400), on_click=self.btn_back_click)
        ]


    # ----------BUTTONS----------
    def btn_back_click(scene):
        scene.Close()
        scene.act.mainmenu.Open()


    # ----------ON_STUFF----------
    def On_Update(self) -> None:
        for element in self.elements: element.Update()


    def On_Open(self) -> None:
        for element in self.elements: element.Update()

    
    def On_Close(self) -> None:
        theatre.Write_Settings()


    def On_Handle(self, event: pygame.event.Event) -> None:
        for element in self.elements: element.Handle(event)


    def On_Render(self) -> None:
        for element in self.elements: element.Render(self.surface)