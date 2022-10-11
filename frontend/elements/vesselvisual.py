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

        self.tooltip_time = 0

        self.Update()


    def On_Update(self):
        self.surface = pygame.Surface((5,10), pygame.SRCALPHA)
        pygame.draw.polygon(self.surface, self.vessel.owner.color, ((0,9), (2,0), (4,9)))
        self.surface = pygame.transform.rotate(self.surface, self.vessel.rotation)
        
        self.rect.center = self.scene.Convert_To_Surface(self.vessel.position)


    def On_Tick(self) -> None:
        if self.vessel.Is_Collision(self.scene.Convert_To_Map(pygame.mouse.get_pos())):
            self.tooltip_time += 1
        else:
            self.tooltip_time = 0


    def On_Handle(self, event:pygame.event.Event):

        # highlight
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.vessel.Is_Collision(self.scene.Convert_To_Map(event.pos))

    
    def On_Render(self, target:pygame.Surface):

        # highlight and select
        if self.vessel == self.scene.act.actionsmenu.selected_vessel: self._Blit_Highlight(target, theatre.settings["player_color"])
        elif self.is_highlighted: self._Blit_Highlight(target, theatre.settings["neutral_color"])

        # tooltip
        if self.tooltip_time >= 100:
            self._Blit_Tooltip(target)

        # main
        target.blit(self.surface, self.rect)


    def _Blit_Tooltip(self, target):
        pygame.draw.line(target, theatre.settings["neutral_color"],
        (self.rect.center), (0, self.rect.centery))


    def _Blit_Arcs(self, target:pygame.Surface, color, radius:int, left=True, front=True, right=True, back=True):
        arcs_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        arcs_surface_rect = arcs_surface.get_rect()
        pygame.draw.circle(arcs_surface, color, arcs_surface_rect.center, radius, 
            draw_top_right = front, draw_top_left = left, draw_bottom_left = back, draw_bottom_right = right)
        
        # # lines
        # ## up
        # if left or front: pygame.draw.line(arcs_surface, theatre.settings["neutral_color"],
        #     (arcs_surface_rect.centerx, self.vessel.BASE_RADIUS),
        #     (arcs_surface_rect.centerx, arcs_surface_rect.centery + radius))
        # ## left
        # if front or right: pygame.draw.line(arcs_surface, theatre.settings["neutral_color"],
        #     (self.vessel.BASE_RADIUS, arcs_surface_rect.centery),
        #     (arcs_surface_rect.centerx + radius, arcs_surface_rect.centery))
        # ## down
        # if right or back: pygame.draw.line(arcs_surface, theatre.settings["neutral_color"],
        #     (arcs_surface_rect.centerx, -self.vessel.BASE_RADIUS),
        #     (arcs_surface_rect.centerx, -arcs_surface_rect.centery - radius))
        # ## right
        # if front or right: pygame.draw.line(arcs_surface, theatre.settings["neutral_color"],
        #     (-self.vessel.BASE_RADIUS, arcs_surface_rect.centery),
        #     (-arcs_surface_rect.centerx - radius, arcs_surface_rect.centery))

        arcs_surface = pygame.transform.rotate(arcs_surface, 45 + self.vessel.rotation)

        # blit arcs
        target.blit(arcs_surface, arcs_surface.get_rect(center=self.rect.center))


    def _Blit_Highlight(self, target:pygame.Surface, color):
        self._Blit_Arcs(target, "#a0000020", 60, left=False, right=False)
        self._Blit_Arcs(target, "#0000a020", 60, front=False, back=False)
        # pygame.draw.circle(target, color, self.rect.center, self.vessel.BASE_RADIUS, 1)
        # pygame.draw.line(target, color,
        #     (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation + 45)), 
        #      self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation + 45))),
        #     (self.rect.centerx + 60 * cos(radians(self.vessel.rotation + 45)), 
        #      self.rect.centery + 60 * sin(radians(self.vessel.rotation + 45))))
        # pygame.draw.line(target, color,
        #     (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation - 45)), 
        #      self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation - 45))),
        #     (self.rect.centerx + 60 * cos(radians(self.vessel.rotation - 45)), 
        #      self.rect.centery + 60 * sin(radians(self.vessel.rotation - 45))))
        # pygame.draw.line(target, color,
        #     (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation + 135)), 
        #      self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation + 135))),
        #     (self.rect.centerx + 60 * cos(radians(self.vessel.rotation + 135)), 
        #      self.rect.centery + 60 * sin(radians(self.vessel.rotation + 135))))
        # pygame.draw.line(target, color,
        #     (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation - 135)), 
        #      self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation - 135))),
        #     (self.rect.centerx + 60 * cos(radians(self.vessel.rotation - 135)), 
        #      self.rect.centery + 60 * sin(radians(self.vessel.rotation - 135))))

