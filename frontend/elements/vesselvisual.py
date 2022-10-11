from math import sin, cos, radians
import pygame


# engine
from engine import Element
from backend.theatre import theatre



class VesselVisual(Element):
    def __init__(self, scene, vessel) -> None:
        super().__init__(scene)

        # for snippents
        from frontend.scenes import MapMenu
        self.scene:MapMenu

        from backend.game import Vessel
        self.vessel:Vessel = vessel
        self.is_highlighted:bool = False

        self.Update()


    def On_Update(self):
        self.surface = pygame.Surface((5,10), pygame.SRCALPHA)
        pygame.draw.polygon(self.surface, self.vessel.owner.color, ((0,9), (2,0), (4,9)))
        self.surface = pygame.transform.rotate(self.surface, self.vessel.rotation)
        
        self.rect.center = self.scene.Convert_To_Surface(self.vessel.position)


    def On_Handle(self, event:pygame.event.Event):

        # highlight
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.vessel.Is_Collision(self.scene.Convert_To_Map(event.pos))

    
    def On_Render(self, target:pygame.Surface):

        # highlight and select
        if self.vessel == self.scene.act.actionsmenu.selected_vessel: self._Blit_Highlight(target, theatre.settings["player_color"])
        elif self.is_highlighted: self._Blit_Highlight(target, theatre.settings["neutral_color"])

        # main
        target.blit(self.surface, self.rect)


    def _Blit_Highlight(self, target, color):
        pygame.draw.circle(target, color, self.rect.center, self.vessel.BASE_RADIUS, 1)
        pygame.draw.line(target, color,
            (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation + 45)), 
             self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation + 45))),
            (self.rect.centerx + 60 * cos(radians(self.vessel.rotation + 45)), 
             self.rect.centery + 60 * sin(radians(self.vessel.rotation + 45))))
        pygame.draw.line(target, color,
            (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation - 45)), 
             self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation - 45))),
            (self.rect.centerx + 60 * cos(radians(self.vessel.rotation - 45)), 
             self.rect.centery + 60 * sin(radians(self.vessel.rotation - 45))))
        pygame.draw.line(target, color,
            (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation + 135)), 
             self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation + 135))),
            (self.rect.centerx + 60 * cos(radians(self.vessel.rotation + 135)), 
             self.rect.centery + 60 * sin(radians(self.vessel.rotation + 135))))
        pygame.draw.line(target, color,
            (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation - 135)), 
             self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation - 135))),
            (self.rect.centerx + 60 * cos(radians(self.vessel.rotation - 135)), 
             self.rect.centery + 60 * sin(radians(self.vessel.rotation - 135))))

