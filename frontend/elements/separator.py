import pygame


# engine
from engine import Element
from backend.theatre import theatre



class Separatior(Element):
    def __init__(self, scene, text:str) -> None:
        super().__init__(scene)

        # for snippets
        from frontend.scenes import ActionsMenu
        self.scene:ActionsMenu

        # variables
        self.text:str = text
        self.height:int = 0


    def On_Update(self):
        
        # render text
        text_surf = theatre.FONT24.render(self.text, 1, theatre.settings['player_color'], theatre.settings['background_color'])
        
        # rect
        self.rect = pygame.Rect(0, 0, self.scene.rect.width, text_surf.get_height())

        # create surf
        self.surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        # draw line on surf
        pygame.draw.line(self.surf, theatre.settings['player_color'], (1, self.rect.centery), (self.rect.width - 1, self.rect.centery))
        
        # blit text on surf
        self.surf.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    
    def On_Render(self, target:pygame.Surface):

        # main
        target.blit(self.surf, (0, self.height))

