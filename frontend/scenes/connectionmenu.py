import pygame

# engine
from engine import Scene
from backend.theatre import theatre



class ConnectionMenu(Scene):
    def __init__(self, act, surface: pygame.Surface) -> None:
        super().__init__(act, surface)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct

        # elements
        from frontend.elements import MenuButton
        
        self.text:pygame.Surface = theatre.FONT60.render("", 1, theatre.settings['player_color'])

        self.btn_connect:MenuButton = MenuButton(self, text="Connect", from_center_top=(0, 200), on_click=self.btn_connect_click)
        self.btn_cancel:MenuButton = MenuButton(self, text="AAA", from_center_top=(0, 400), on_click=self.btn_cancel_click)

        self.is_connectiong:bool = False


    # ----------BUTTONS----------
    def btn_connect_click(self):
        self.is_connectiong = True

        self.btn_cancel.text = "Cancel"
        self.text = theatre.FONT60.render("Connecting...", 1, theatre.settings['player_color'])
        self.Update()


    def btn_cancel_click(self):
        self.Close()
        theatre.current_act = theatre.mainact


    # ----------ON_STUFF----------
    def On_Update(self):

        # update buttons
        self.btn_cancel.Update()
        self.btn_connect.Update()

        # update text rect
        self.text_rect = self.text.get_rect(center=(pygame.display.get_window_size()[0] / 2, 200))


    def On_Open(self) -> None:

        # reset flags
        self.is_connectiong = False

        # reset ui
        self.btn_cancel.text = "Back"
        self.text = theatre.FONT60.render("", 1, theatre.settings['player_color'])

        # update
        self.Update()


    def On_Close(self) -> None:
        print("A")

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        self.btn_connect.Handle(event)
        self.btn_cancel.Handle(event)


    def On_Render(self) -> None:

        # render text
        self.surface.blit(self.text, self.text_rect)

        # render buttons
        if not self.is_connectiong: self.btn_connect.Render(self.surface)
        self.btn_cancel.Render(self.surface)
