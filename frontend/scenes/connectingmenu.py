import pygame

# engine
from engine import Scene
from backend.theatre import theatre



class ConnectingMenu(Scene):
    def __init__(self, act, surface: pygame.Surface) -> None:
        super().__init__(act, surface)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct

        # elements
        from frontend.elements import MenuButton
        from engine import Element
        self.text = Element(self)
        self.btn_cancel = MenuButton(self, text="Connect", from_center_top=(0, 400), on_click=self.btn_cancel_click)

    # ----------BUTTONS----------
    def btn_cancel_click(self):
        self.Close()
        theatre.current_act = theatre.mainact


    # ----------ON_STUFF----------
    def On_Open(self) -> None:
        self.btn_cancel.Update()


    def On_Close(self) -> None:
        print("A")

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        self.btn_cancel.Handle(event)


    def On_Render(self) -> None:
        self.btn_cancel.Render(self.surface)
