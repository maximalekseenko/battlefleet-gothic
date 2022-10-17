import pygame


# engine
from engine import Element
from frontend.theatre import theatre



class OrderButton(Element):
    def __init__(self, scene, order) -> None:
        super().__init__(scene, surface_flags=pygame.SRCALPHA)

        # for snippets
        from frontend.scenes import OrdersMenu
        self.scene:OrdersMenu

        # variables
        from backend.game import Order
        self.order:Order = order

        self.is_highlighted:bool = False


    def On_Update(self):

        HEIGHT = 20
        WIDTH_DISTANCE = 20

        # rect
        width = max(0, self.scene.rect.width - WIDTH_DISTANCE)
        self.rect = pygame.Rect(0, 0, width, HEIGHT)
        self.rect.centerx = self.scene.rect.centerx

        # text
        text_surf = theatre.FONT20.render(self.order.NAME, 0, theatre.COLOR.UI.TEXT)
        self.surface.blit(text_surf, text_surf.get_rect(midleft=self.rect.midleft))
        
        # is_highlighted
        self.is_highlighted = self.rect.collidepoint(pygame.mouse.get_pos())

    
    def On_Handle(self, event:pygame.event.Event):

        # button highlight
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.rect.collidepoint(self.scene.Relative(event.pos))

        # button click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                # can be clicked
                if self.order.Is_Disabled(): return
                if self.order.Is_Invisible(): return
                if not self.rect.collidepoint(self.scene.Relative(event.pos)): return

                # resolve click
                self.scene.selected_order = self.order


    def On_Render(self, target:pygame.Surface):

        # can be rendered
        if self.order.Is_Invisible(): return

        # render background
        self._Render_Background(target)

        # render text
        self._Render_Content(target)

        # outline
        self._Render_Outline(target)




    def _Render_Background(self, target:pygame.Surface):

        # disabled
        if self.order.Is_Disabled():
            pygame.draw.rect(target, theatre.COLOR[self.order.vessel.owner.color+'d2'], self.rect)

        # selected
        elif self.order == self.scene.selected_order: 
            pygame.draw.rect(target, theatre.COLOR[self.order.vessel.owner.color+'l1'], self.rect)
        
        # idle
        else: 
            pygame.draw.rect(target, theatre.COLOR[self.order.vessel.owner.color], self.rect)


    def _Render_Content(self, target:pygame.Surface):
        target.blit(self.surface, self.rect)


    def _Render_Outline(self, target:pygame.Surface):
        if self.is_highlighted:

            LENGTH = 10
            WIDTH = 3
            
            # ┏ ┐
            # ┗ ┘
            pygame.draw.line(target, theatre.COLOR.UI.OUTLINE,
                self.rect.topleft,
                (self.rect.left + LENGTH, self.rect.top), WIDTH)
            pygame.draw.line(target, theatre.COLOR.UI.OUTLINE,
                self.rect.topleft,
                self.rect.bottomleft, WIDTH)
            pygame.draw.line(target, theatre.COLOR.UI.OUTLINE,
                self.rect.bottomleft,
                (self.rect.left + LENGTH, self.rect.bottom), WIDTH)

            # ┌ ┓
            # └ ┛
            pygame.draw.line(target, theatre.COLOR.UI.OUTLINE,
                self.rect.topright,
                (self.rect.right - LENGTH, self.rect.top), WIDTH)
            pygame.draw.line(target, theatre.COLOR.UI.OUTLINE,
                self.rect.topright,
                self.rect.bottomright, WIDTH)
            pygame.draw.line(target, theatre.COLOR.UI.OUTLINE,
                self.rect.bottomright,
                (self.rect.right - LENGTH, self.rect.bottom), WIDTH)
        

