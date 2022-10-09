import pygame


# engine
from engine import Element
from backend.theatre import theatre



class MenuButton(Element):
    def __init__(self, scene, text:str, topcenter:tuple[int,int], on_click) -> None:

        # super
        super().__init__(scene, (topcenter, (200, 30)))

        # variables
        self.topcenter = topcenter
        self.text:str = text
        self.on_click = on_click

        # update
        self.Update()


    def On_Update(self):

        # rect
        self.rect.centerx = self.scene.rect.centerx + self.topcenter[0]
        self.rect.centery = self.topcenter[1]
        
        # surf
        self.surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.surf.fill(theatre.settings["ui_color"])

        # text
        self.text_surf = theatre.BUTTON_FONT.render(self.text, 1, theatre.settings['player_color'])
        self.surf.blit(self.text_surf, self.text_surf.get_rect(center=self.surf.get_rect().center))
        
        # is_highlighted
        self.is_highlighted = self.rect.collidepoint(pygame.mouse.get_pos())


    
    def On_Handle(self, event:pygame.event.Event):
        
        # window resize
        if event.type == pygame.WINDOWRESIZED:
            self.Update()

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


