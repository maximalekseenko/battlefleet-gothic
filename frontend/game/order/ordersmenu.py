import pygame

# engine
from engine import Scene, Element
from frontend.theatre import theatre

# game
from backend.game import Vessel, Order

# logic
from .novessel import NoVessel
from .noorder import NoOrder

# visual
from .orderbutton import OrderButton



class OrdersMenu(Scene):
    def __init__(self, act) -> None:
        super().__init__(act)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct

        # elements
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


    def Do(self, position):
        self.selected_order.Do(position)
        self.selected_order = None


    # ----------ON_STUFF----------
    def On_Update(self):
        self._selected_vessel_none = NoVessel(self.act.game, self.act.game.player, (0,0), 0, -1)
        self._selected_order_none = NoOrder(self)

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
        for element in self.elements: element.Render(self.surface)

        # render on screen
        self.act.surface.blit(self.surface, self.rect)

