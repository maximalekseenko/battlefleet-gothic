import pygame

# engine
from engine import Scene, Element
from frontend.theatre import theatre
from backend.game import Vessel, Order
from backend.game.common.orders.novessel import NoVessel
from backend.game.common.orders.noorder import NoOrder
from frontend.elements import OrderButton



class OrdersMenu(Scene):
    def __init__(self, act) -> None:
        super().__init__(act)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct

        # elements
        self.noselection:pygame.Surface
        self.elements:list[Element] = list()

        # variables
        self.scrolled_value = 0
        self.content_height = 0
        
        # private variables
        self._selected_vessel:Vessel = None
        self._selected_order:Order = None


    @property
    def selected_vessel(self) -> Vessel:
        if self._selected_vessel == None:
            return self._selected_vessel_none
        else:
            return self._selected_vessel


    @selected_vessel.setter
    def selected_vessel(self, value:Vessel|None) -> None:

        # if same
        if value == self._selected_vessel: return
        
        self.elements.clear()

        # if None
        if value == None: 
            self._selected_vessel = None
            return

        # if vessel
        else: 
            self._selected_vessel = value
            
            # get orders
            for order in value.orders:
                self.elements.append(OrderButton(self, order))


    @property
    def selected_order(self) -> Order:
        if self._selected_order == None:
            return self._selected_order_none
        else:
            return self._selected_order


    @selected_order.setter
    def selected_order(self, value:Order|None) -> None:

        # if None
        if value == None: self._selected_order = None

        # if order
        else: self._selected_order = value


    def Position_Action(self, position):
        self.selected_order.Do(position)
        self.selected_order = None


    # ----------ON_STUFF----------
    def On_Update(self):
        self._selected_vessel_none = NoVessel(self.act.game, self.act.game.player, (0,0), 0, -1)
        self._selected_order_none = NoOrder(self)

        if self.selected_vessel == None:
            # no selection
            text_a = theatre.FONT24.render("NO VESSEL", 1, theatre.settings['enemy_color'])
            text_b = theatre.FONT24.render("SELECTED", 1, theatre.settings['enemy_color'])
            self.noselection = pygame.Surface((self.rect.width, text_a.get_height() + text_b.get_height()), pygame.SRCALPHA)
            self.noselection.blit(text_a, text_a.get_rect(centerx=self.noselection.get_rect().centerx, y=0))
            self.noselection.blit(text_b, text_b.get_rect(centerx=self.noselection.get_rect().centerx, y=text_a.get_height()))
        else:
            content_top = self.scrolled_value
            self.content_height = 0

            DISTANCE = 3

            for orderbutton in self.elements:
                orderbutton.Update()
                orderbutton.rect.top = self.content_height + content_top
                self.content_height += orderbutton.rect.height + DISTANCE
            
        


    def On_Open(self) -> None:
        self.Update()

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        # scroll
        if event.type == pygame.MOUSEWHEEL:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if event.y != 0:
                    self.scrolled_value += event.y

                    # # validate
                    # if self.scrolled_value > 0: self.scrolled_value = 0
                    # if self.scrolled_value < -self.rect.height: self.scrolled_value = -self.rect.height

                    self.Update()

        # handle to elements
        for element in self.elements: element.Handle(event)


    def On_Render(self) -> None:

        # render background
        self.surface.fill(theatre.settings['background_color'])

        # render outline
        pygame.draw.rect(self.surface, theatre.settings['neutral_color'], (
            (0, self.scrolled_value), 
            (self.rect.width, max(self.content_height, self.rect.height))), 2)

        # render elements
        ## vessel not selected
        if self.selected_vessel == None: 
            self.act.surface.blit(self.noselection, self.noselection.get_rect(center=self.rect.center))
        ## vessel selected
        else: 
            for element in self.elements: element.Render(self.surface)

        # render on screen
        self.act.surface.blit(self.surface, self.rect)

