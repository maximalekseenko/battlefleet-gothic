import pygame


# engine
from engine import Element
from backend.theatre import theatre



class Separatior(Element):
    def __init__(self, scene, text:str) -> None:
        super().__init__(scene, surface_flags=pygame.SRCALPHA)

        # for snippets
        from frontend.scenes import ActionsMenu
        self.scene:ActionsMenu

        # variables
        self.text:str = text


    def On_Update(self):
        
        # render text
        text_surf = theatre.FONT24.render(self.text, 1, theatre.settings['player_color'], theatre.settings['background_color'])
        
        # rect
        self.rect = pygame.Rect(0, self.rect.top, self.scene.rect.width, text_surf.get_height())
        text_rect = text_surf.get_rect(center=self.surface.get_rect().center)

        # draw line on surface
        pygame.draw.line(self.surface, theatre.settings['player_color'], 
            self.surface.get_rect().midleft, text_rect.midleft)
            
        pygame.draw.line(self.surface, theatre.settings['player_color'], 
            text_rect.midright, self.surface.get_rect().midright)
        
        # blit text on surf
        self.surface.blit(text_surf, text_rect)


    
    def On_Render(self, target:pygame.Surface):
        target.blit(self.surface, self.rect)

