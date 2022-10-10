import pygame
from backend.game import Vessel, Action

# engine
from engine import Scene, Element
from backend.theatre import theatre



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
        
        # public variables
        self.selected_vessel:Vessel = None
        self.selected_action:Action = None


    def Select_Vessel(self, vessel:Vessel):
        self.selected_vessel = vessel
        self.Update()


    # ----------ON_STUFF----------
    def On_Update(self):

        height = self.rect.height

        if self.selected_vessel == None:
            # no selection
            text_a = theatre.FONT24.render("NO VESSEL", 1, theatre.settings['enemy_color'])
            text_b = theatre.FONT24.render("SELECTED", 1, theatre.settings['enemy_color'])
            self.noselection = pygame.Surface((self.rect.width, text_a.get_height() + text_b.get_height()), pygame.SRCALPHA)
            self.noselection.blit(text_a, text_a.get_rect(centerx=self.noselection.get_rect().centerx, y=0))
            self.noselection.blit(text_b, text_b.get_rect(centerx=self.noselection.get_rect().centerx, y=text_a.get_height()))
        else:
            from frontend.elements import Separatior, SpecalOrdersHolder
            self.elements.clear()
            if len(self.selected_vessel.specal_actions):
                self.elements += [Separatior(self, "SPECAL"), SpecalOrdersHolder(self)]
            if len(self.selected_vessel.movement_actions):
                self.elements += [Separatior(self, "MOVEMENT"), SpecalOrdersHolder(self)]
            if len(self.selected_vessel.armament_actions):
                self.elements += [Separatior(self, "ARMAMENTS"), SpecalOrdersHolder(self), SpecalOrdersHolder(self)]
            if len(self.selected_vessel.vessel_actions):
                self.elements += [Separatior(self, "OTHER"), SpecalOrdersHolder(self)]

            # element heights
            height = 0
            for element in self.elements: 
                element.rect.top = height + self.scrolled_value
                element.Update()
                height += element.rect.height


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

        # render background and outline
        self.surface.fill(theatre.settings['background_color'])
        pygame.draw.rect(self.surface, theatre.settings['neutral_color'], ((0,0), self.rect.size), 2)

        # render elements
        ## vessel not selected
        if self.selected_vessel == None: 
            self.act.surface.blit(self.noselection, self.noselection.get_rect(center=self.rect.center))
        ## vessel selected
        else: 
            for element in self.elements: element.Render(self.surface)

        # render on screen
        self.act.surface.blit(self.surface, (0,0))
