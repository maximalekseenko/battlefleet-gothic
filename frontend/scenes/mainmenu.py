import pygame

# engine
from engine import Scene
from backend.theatre import theatre



class MainMenu(Scene):
    def __init__(self, act, surface: pygame.Surface) -> None:
        super().__init__(act, surface)

        # for snippets
        from frontend.acts import MainAct
        self.act:MainAct

        # elements
        from frontend.elements import MenuButton
        from engine import Element
        self.elements:list[Element] = [
            MenuButton(self, text="Play", from_center_top=(0, 100), on_click=self.btn_play_click),
            MenuButton(self, text="Settings", from_center_top=(0, 200), on_click=self.btn_settings_click),
            MenuButton(self, text="Exit", from_center_top=(0, 300), on_click=self.btn_exit_click),
        ]

    # ----------BUTTONS----------
    def btn_play_click(self):
        theatre.current_act = theatre.gameact


    def btn_settings_click(self):
        self.Close()
        self.act.settingsmenu.Open()


    def btn_exit_click(self):
        theatre.Finish()


    # ----------ON_STUFF----------
    def On_Update(self):
        for element in self.elements: element.Update()


    def On_Open(self) -> None:
        for element in self.elements: element.Update()

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        for element in self.elements: element.Handle(event)


    def On_Render(self) -> None:
        for element in self.elements: element.Render(self.surface)
