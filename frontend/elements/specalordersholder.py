import pygame


# engine
from engine import Element
from backend.theatre import theatre



# other
from frontend.elements import Clickable



class SpecalOrdersHolder(Element):
    def __init__(self, scene) -> None:

        # super
        super().__init__(scene)

        # for snippets
        from frontend.scenes import ActionsMenu
        self.scene:ActionsMenu

        # variables
        self.highlight_id = -1
        self.orders_clickables:list[Clickable] = list()
        self.height:int = 0


    def On_Update(self):
        rows = len(self.scene.selected_vessel.specal_actions) * 51 // self.scene.rect.width + 1
        cols = self.scene.rect.width // 51
        row_move = self.scene.rect.width % 51 // 2

        # main rect
        self.rect = pygame.Rect(
            self.rect.x, 
            self.rect.y + self.height, 
            self.scene.rect.width, 
            rows * 51)

        # action rects
        self.orders_clickables.clear()
        for i in range(len(self.scene.selected_vessel.specal_actions)):
            self.orders_clickables.append(Clickable(self.scene, pygame.Rect(
                self.rect.x + i % cols * 51 + row_move,
                self.rect.y + i // cols * 51,
                50,
                50), None))
        
        # is_highlighted
        self.is_highlighted = self.rect.collidepoint(pygame.mouse.get_pos())


    def On_Handle(self, event:pygame.event.Event):

        # clickables
        for clickable in self.orders_clickables: 
            clickable.Handle(event)


    
    def On_Render(self, target:pygame.Surface):

        # actions
        for clickable in self.orders_clickables: clickable.Render(target)

        # highlight
        if self.is_highlighted: pygame.draw.rect(target, theatre.settings["player_color"], self.rect.move(0,self.height), theatre.BUTTON_HIGHLIGHT_WIDTH)


