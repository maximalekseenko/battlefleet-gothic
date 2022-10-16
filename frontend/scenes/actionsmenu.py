import pygame

# engine
from engine import Scene, Element
from backend.theatre import theatre
from backend.game import Vessel, Order
from backend.game.common.orders.selectvessel import SelectVessel
from frontend.elements import OrderButton



class ActionsMenu(Scene):
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
        self._selected_action:Order = SelectVessel(self)


    @property
    def selected_vessel(self) -> Vessel:
        return self._selected_vessel


    @selected_vessel.setter
    def selected_vessel(self, value:Vessel|None) -> None:

        # if None
        if type(value) == None: self._selected_vessel == None

        # if same
        if value == self._selected_vessel: return

        # get orders
        self.elements.clear()
        for order in value.orders:
            self.elements.append(OrderButton(self, order))

        # if vessel
        else: self._selected_vessel = value


    @property
    def selected_action(self) -> Order:
        return self._selected_action


    @selected_action.setter
    def selected_action(self, value:Order|None) -> None:

        # if None
        if value == None: self._selected_action = SelectVessel(self)

        # if action
        else: self._selected_action = value


    def Position_Action(self, position):
        self.selected_action.Do(position)


    # ----------ON_STUFF----------
    def On_Update(self):
        if self.selected_vessel == None:
            # no selection
            text_a = theatre.FONT24.render("NO VESSEL", 1, theatre.settings['enemy_color'])
            text_b = theatre.FONT24.render("SELECTED", 1, theatre.settings['enemy_color'])
            self.noselection = pygame.Surface((self.rect.width, text_a.get_height() + text_b.get_height()), pygame.SRCALPHA)
            self.noselection.blit(text_a, text_a.get_rect(centerx=self.noselection.get_rect().centerx, y=0))
            self.noselection.blit(text_b, text_b.get_rect(centerx=self.noselection.get_rect().centerx, y=text_a.get_height()))
        else:
            content_top = self.rect.top + self.scrolled_value
            self.content_height = 0

            for orderbutton in self.elements:
                orderbutton.Update()
                orderbutton.rect.top = self.content_height + content_top
                self.content_height += orderbutton.rect.height + 1
            
        


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
            (self.rect.width, max(self.content_height, self.rect.height)))
            , 2)

        # render elements
        ## vessel not selected
        if self.selected_vessel == None: 
            self.act.surface.blit(self.noselection, self.noselection.get_rect(center=self.rect.center))
        ## vessel selected
        else: 
            for element in self.elements: element.Render(self.surface)

        # render on screen
        self.act.surface.blit(self.surface, (0,0))

    def _Render_Orders(self):
        if self.selected_vessel == None: return

        height = self.scrolled_value
        for order in self.selected_vessel.orders:

            # if not visible
            if order.Is_Invisible(): continue

            # surface
            order_surface = pygame.Surface((self.rect.width - 20, 25))
            order_surface.fill(self.selected_vessel.owner.color)

            # name
            order_name = theatre.FONT12.render(order.NAME, 2, "#000000")
            order_surface.blit(order_name, order_name.get_rect(midleft=(0,12.5)))

            # final
            self.surface.blit(order_surface, order_surface.get_rect(centerx=self.rect.centerx, top=height))
            height += 26

