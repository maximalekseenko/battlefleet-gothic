import pygame


# engine
from engine import Element
from backend.theatre import theatre



class OrderButton(Element):
    def __init__(self, scene, order) -> None:
        super().__init__(scene, surface_flags=pygame.SRCALPHA)

        # for snippets
        from frontend.scenes import ActionsMenu
        self.scene:ActionsMenu

        # variables
        from backend.game import Order
        self.order:Order = order

        self.is_highlighted:bool = False


    def On_Update(self):

        # rect
        width = max(0, self.scene.rect.width - 20)
        self.rect = pygame.Rect(0, 0, width, 20)
        self.rect.centerx = self.scene.rect.centerx
        
        # surf
        self.surface.fill(self.order.vessel.owner.color)

        # text
        name_surf = theatre.FONT20.render(self.order.NAME, 0, "#000000")
        self.surface.blit(name_surf, name_surf.get_rect(midleft=self.rect.midleft))
        
        # is_highlighted
        self.is_highlighted = self.rect.collidepoint(pygame.mouse.get_pos())

    
    def On_Handle(self, event:pygame.event.Event):

        # button highlight
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.rect.collidepoint(event.pos)

        # button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos): 
                    self.scene.selected_action = self.order


    def On_Render(self, target:pygame.Surface):

        # main
        target.blit(self.surface, self.rect)

        # highlight
        # if self.is_highlighted: pygame.draw.rect(target, theatre.settings["player_color"], self.rect, theatre.BUTTON_HIGHLIGHT_WIDTH)


