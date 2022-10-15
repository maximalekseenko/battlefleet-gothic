from math import sin, cos, radians
import pygame
# from backend.game.armament import ARC, Armament


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
        self.surface = pygame.Surface((10, 5), pygame.SRCALPHA)
        pygame.draw.polygon(self.surface, self.vessel.owner.color, ((0,0), (9,2), (0,4)))
        self.surface = pygame.transform.rotate(self.surface, self.vessel.rotation)
        
        self.rect.center = self.scene.Convert_To_Surface(self.vessel.position)

        # self._Update_Tooltip()


    # def _Update_Tooltip(self):
    #     self.tooltip_surface = pygame.Surface((120, 100), pygame.SRCALPHA)
    #     self.tooltip_surface.fill("#000000a0")

    #     # top
    #     text_type = theatre.FONT12.render(self.vessel.TYPE, 0, self.vessel.owner.color)
    #     text_class = theatre.FONT12.render(self.vessel.CLASSNAME, 2, self.vessel.owner.color)
    #     self.tooltip_surface.blit(text_type, text_type.get_rect(topleft=(0,0)))
    #     self.tooltip_surface.blit(text_class, text_type.get_rect(topright=self.tooltip_surface.get_rect().topright))

    #     # weaponry 

    #     # characteristics
    #     ## hits
    #     char_pos = (20,20)
    #     char_name = theatre.FONT12.render("HITS", 1, self.vessel.owner.color)
    #     char_value = theatre.FONT12.render(f"{self.vessel.hits_current}/{self.vessel.HITS}", 1, self.vessel.owner.color)
    #     self.tooltip_surface.blit(char_name, char_name.get_rect(midbottom=char_pos))
    #     self.tooltip_surface.blit(char_value, char_value.get_rect(midtop=char_pos))
    #     ## turns
    #     char_pos = (60,20)
    #     char_name = theatre.FONT12.render("TURNS", 1, self.vessel.owner.color)
    #     char_value = theatre.FONT12.render(f"{self.vessel.TURNS}˚", 1, self.vessel.owner.color)
    #     self.tooltip_surface.blit(char_name, char_name.get_rect(midbottom=char_pos))
    #     self.tooltip_surface.blit(char_value, char_value.get_rect(midtop=char_pos))
    #     ## shields
    #     char_pos = (100,20)
    #     char_name = theatre.FONT12.render("Shields", 1, self.vessel.owner.color)
    #     char_value = theatre.FONT12.render(f"{self.vessel.TURNS}*", 1, self.vessel.owner.color)
    #     self.tooltip_surface.blit(char_name, char_name.get_rect(midbottom=char_pos))
    #     self.tooltip_surface.blit(char_value, char_value.get_rect(midtop=char_pos))
    #     ## armour
    #     char_pos = (20,40)
    #     char_name = theatre.FONT12.render("ARMOUR", 1, self.vessel.owner.color) 
    #     char_value = theatre.FONT12.render(f"{self.vessel.TURNS}*", 1, self.vessel.owner.color)
    #     self.tooltip_surface.blit(char_name, char_name.get_rect(midbottom=char_pos))
    #     self.tooltip_surface.blit(char_value, char_value.get_rect(midtop=char_pos))
    #     ## turrets
    #     char_pos = (60,40)
    #     char_name = theatre.FONT12.render("TURRETS", 1, self.vessel.owner.color)
    #     char_value = theatre.FONT12.render(f"{self.vessel.TURNS}*", 1, self.vessel.owner.color)
    #     self.tooltip_surface.blit(char_name, char_name.get_rect(midbottom=char_pos))
    #     self.tooltip_surface.blit(char_value, char_value.get_rect(midtop=char_pos))
    #     ## turns
    #     char_pos = (100,40)
    #     char_name = theatre.FONT12.render("TURNS", 1, self.vessel.owner.color)
    #     char_value = theatre.FONT12.render(f"{self.vessel.TURNS}*", 1, self.vessel.owner.color)
    #     self.tooltip_surface.blit(char_name, char_name.get_rect(midbottom=char_pos))
    #     self.tooltip_surface.blit(char_value, char_value.get_rect(midtop=char_pos))


    # def On_Tick(self) -> None:
    #     if self.vessel.Is_Collision(self.scene.Convert_To_Map(pygame.mouse.get_pos())):
    #         self.tooltip_time += 1
    #     else:
    #         self.tooltip_time = 0


    # def On_Handle(self, event:pygame.event.Event):

    #     # highlight
    #     if event.type == pygame.MOUSEMOTION:
    #         self.is_highlighted = self.vessel.Is_Collision(self.scene.Convert_To_Map(event.pos))

    
    def On_Render(self, target:pygame.Surface):

        # highlight and select
        # if self.vessel == self.scene.act.actionsmenu.selected_vessel: self.Render_Highlight(target, theatre.settings["player_color"])
        # elif self.is_highlighted: self.Render_Highlight(target, theatre.settings["neutral_color"])

        # tooltip
        
        # self.Render_Tooltip(target)

        # main
        target.blit(self.surface, self.rect)


    # def Render_Tooltip(self, target:pygame.Surface):
    #     if self.tooltip_time < 100: return
        
    #     target.blit(self.tooltip_surface, self.rect.center)


    # def Render_Highlight(self, target, color):

    #     for armament in self.vessel.ARMAMENTS:
    #         self.Render_Armament_Arcs(target, armament)

    #     pygame.draw.circle(target, color, self.rect.center, self.vessel.BASE_RADIUS, 1)
    #     pygame.draw.line(target, color,
    #         (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation + 45)), 
    #          self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation + 45))),
    #         (self.rect.centerx + 60 * cos(radians(self.vessel.rotation + 45)), 
    #          self.rect.centery + 60 * sin(radians(self.vessel.rotation + 45))))
    #     pygame.draw.line(target, color,
    #         (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation - 45)), 
    #          self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation - 45))),
    #         (self.rect.centerx + 60 * cos(radians(self.vessel.rotation - 45)), 
    #          self.rect.centery + 60 * sin(radians(self.vessel.rotation - 45))))
    #     pygame.draw.line(target, color,
    #         (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation + 135)), 
    #          self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation + 135))),
    #         (self.rect.centerx + 60 * cos(radians(self.vessel.rotation + 135)), 
    #          self.rect.centery + 60 * sin(radians(self.vessel.rotation + 135))))
    #     pygame.draw.line(target, color,
    #         (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation - 135)), 
    #          self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation - 135))),
    #         (self.rect.centerx + 60 * cos(radians(self.vessel.rotation - 135)), 
    #          self.rect.centery + 60 * sin(radians(self.vessel.rotation - 135))))


    # def Render_Armament_Arcs(self, target:pygame.Surface, armament:Armament):
    #     arcs_surface = pygame.Surface((armament.RANGE * 2, armament.RANGE * 2), pygame.SRCALPHA)

    #     arcs_surface_rect = arcs_surface.get_rect()
    #     pygame.draw.circle(arcs_surface, armament.COLOR + "50", arcs_surface_rect.center, armament.RANGE, 
    #         draw_top_right = armament.FIREARC == ARC.PROW, 
    #         draw_top_left = armament.FIREARC == ARC.PORT, 
    #         draw_bottom_left = armament.FIREARC == False,
    #         draw_bottom_right = armament.FIREARC == ARC.STARBOARD)


    #     arcs_surface = pygame.transform.rotate(arcs_surface, 45 + self.vessel.rotation)

    #     # blit arcs
    #     target.blit(arcs_surface, arcs_surface.get_rect(center=self.rect.center))


    # def _Blit_Highlight(self, target:pygame.Surface, color):
    #     self._Blit_Arcs(target, "#a0000020", 60, left=False, right=False)
    #     self._Blit_Arcs(target, "#0000a020", 60, front=False, back=False)
    #     # pygame.draw.circle(target, color, self.rect.center, self.vessel.BASE_RADIUS, 1)
    #     # pygame.draw.line(target, color,
    #     #     (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation + 45)), 
    #     #      self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation + 45))),
    #     #     (self.rect.centerx + 60 * cos(radians(self.vessel.rotation + 45)), 
    #     #      self.rect.centery + 60 * sin(radians(self.vessel.rotation + 45))))
    #     # pygame.draw.line(target, color,
    #     #     (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation - 45)), 
    #     #      self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation - 45))),
    #     #     (self.rect.centerx + 60 * cos(radians(self.vessel.rotation - 45)), 
    #     #      self.rect.centery + 60 * sin(radians(self.vessel.rotation - 45))))
    #     # pygame.draw.line(target, color,
    #     #     (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation + 135)), 
    #     #      self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation + 135))),
    #     #     (self.rect.centerx + 60 * cos(radians(self.vessel.rotation + 135)), 
    #     #      self.rect.centery + 60 * sin(radians(self.vessel.rotation + 135))))
    #     # pygame.draw.line(target, color,
    #     #     (self.rect.centerx + self.vessel.BASE_RADIUS * cos(radians(self.vessel.rotation - 135)), 
    #     #      self.rect.centery + self.vessel.BASE_RADIUS  * sin(radians(self.vessel.rotation - 135))),
    #     #     (self.rect.centerx + 60 * cos(radians(self.vessel.rotation - 135)), 
    #     #      self.rect.centery + 60 * sin(radians(self.vessel.rotation - 135))))

