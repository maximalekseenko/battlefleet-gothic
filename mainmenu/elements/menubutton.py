import pygame


# engine
from engine import Element
from theatre import theatre



class MenuButton(Element):
    def __init__(self, scene, text:str, from_center_top:tuple[int,int], on_click) -> None:

        # super
        super().__init__(scene)

        # variables
        self.text:str = text
        self.from_center_top:tuple[int,int] = from_center_top
        self.surface = pygame.display.get_surface()
        self.on_click = on_click

        # rect
        self.rect = pygame.Rect(0, 0, 200, 30)

        # update
        self.Update()


    def On_Update(self):

        # rect
        self.rect.x = self.from_center_top[0] + self.surface.get_size()[0] / 2
        self.rect.y = self.from_center_top[1]
        self.rect.x -= self.rect.width / 2
        self.rect.y -= self.rect.height / 2
        
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


