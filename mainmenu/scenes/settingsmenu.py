import pygame

# engine
from engine import Scene, Element
from theatre import theatre



class SettingsMenu(Scene):
    def __init__(self, act, surface) -> None:
        super().__init__(act, surface)

        # for snippets
        from mainmenu import MainAct
        self.act:MainAct

        # elements
        from mainmenu.elements import MenuButton, ColorSetting, TextSetting

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
 

    # ----------TEXTBOXES----------   
    def tbx_color(scene, tbx, setting_name, num):

        # get value
        value = int(tbx.text) if tbx.text.isnumeric() else 0

        # validate value
        if value < 0: value = 0
        if value > 255: value = 255

        # set value
        getattr(theatre, setting_name)[num] = value

        # update self
        tbx.text = str(value)
        scene.Update()


    def tbx_name(scene, tbx):
        if len(tbx.text) > theatre.PLAYER_NAME_LEN_MAX: tbx.text = tbx.text[:theatre.PLAYER_NAME_LEN_MAX]
        theatre.player_name = tbx.text
        tbx.Update()


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