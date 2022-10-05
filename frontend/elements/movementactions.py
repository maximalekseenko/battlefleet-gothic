from math import floor
import pygame


# engine
from engine import Element
from backend.theatre import theatre



class MovementActions(Element):
    def __init__(self, scene) -> None:

        # super
        super().__init__(scene)

        # for snippets
        from frontend.scenes import ActionsMenu
        self.scene:ActionsMenu

        # variables
        self.actions_collision_rects:list[pygame.Rect]
        self.height:int = 0


    def On_Update(self):

        self.rect = pygame.Rect(0, 0, self.scene.surface.get_width(), floor(len(self.scene.selected_vessel.movement_actions) / 3) * 25)
        self.actions_collision_rects.clear()

        # surf
        self.surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        

        # title
        self.title_surf = theatre.FONT24.render("MOVEMENT", 1, theatre.settings['player_color'], theatre.settings['background_color'])
        pygame.draw.line(self.surf, theatre.settings['player_color'], 
            (1, self.title_surf.get_height() / 2), 
            (self.surf.get_width() - 1, self.title_surf.get_height() / 2))
        self.surf.blit(self.title_surf, self.title_surf.get_rect(centerx=self.surf.get_width() / 2, y = 0))


        
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


