import pygame


# engine
from engine import Element
from backend.theatre import theatre



class Clickable(Element):
    def __init__(self, scene, rect:pygame.Rect, on_click) -> None:
        super().__init__(scene)

        # variables
        self.on_click = on_click

        # rect
        self.rect = rect

        # update
        self.Update()


    def On_Update(self):
        
        # surf
        self.surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.surf.fill(theatre.settings["ui_color"])

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
                    self.on_click()

    
    def On_Render(self, target:pygame.Surface):

        # main
        target.blit(self.surf, self.rect)

        # highlight
        if self.is_highlighted: pygame.draw.rect(target, theatre.settings["player_color"], self.rect, theatre.BUTTON_HIGHLIGHT_WIDTH)


