import pygame
from backend.game import Vessel

# engine
from engine import Scene
from frontend.theatre import theatre



class MapMenu(Scene):
    def __init__(self, act) -> None:
        super().__init__(act)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct

        self.scrolled_point:list[int] = [0, 0]
        self.scaled_value:int = 2


    # ----------ON_STUFF----------


    def On_Open(self) -> None:
        self.Update()

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        if event.type == pygame.MOUSEBUTTONDOWN: 
            if not self.rect.collidepoint(event.pos): return
            else:

                # position order
                if event.button == 1: 
                    self.act.ordersmenu.Position_Action(self.Convert_To_Map(event.pos))

                # cancel order selection
                elif event.button == 3:
                    self.act.ordersmenu.selected_order = None

        # move
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: self.scrolled_point[0] += 1
            elif event.key == pygame.K_d: self.scrolled_point[0] -= 1
            elif event.key == pygame.K_w: self.scrolled_point[1] += 1
            elif event.key == pygame.K_s: self.scrolled_point[1] -= 1
            else: return

        # zoom
        elif event.type == pygame.MOUSEWHEEL:
            if not self.rect.collidepoint(pygame.mouse.get_pos()): return

            self.scaled_value -= event.y / 100
        



    def On_Render(self) -> None:

        # background
        self.surface.fill(theatre.settings['background_color'])
        pygame.draw.rect(self.surface, theatre.settings['neutral_color'], ((0,0), self.rect.size), 1)

        # game borders
        pygame.draw.rect(self.surface, "#000000", (
            self.Convert_To_Surface((0, 0)), 
            (self.act.game.size[0] * self.scaled_value, self.act.game.size[1] * self.scaled_value)
            ))

        # order
        if self.act.ordersmenu.selected_order != None and self.act.ordersmenu.selected_vessel != None:
            target = self.act.ordersmenu.selected_order.Fix_Target(self.Convert_To_Map(pygame.mouse.get_pos()))
            if target: pygame.draw.line(self.surface, "#a05000", 
                self.Convert_To_Surface(self.act.ordersmenu.selected_vessel.position), 
                self.Convert_To_Surface(target))

        # vessels
        for vessel in self.act.game.forces:
            self._Render_Vessel(vessel)

        # finish
        self.act.surface.blit(self.surface, self.rect)


    def Convert_To_Map(self, point:list[int]):
        return [
            (point[0] - self.scrolled_point[0] - self.rect.left) / self.scaled_value,
            (point[1] - self.scrolled_point[1] - self.rect.top) / self.scaled_value
        ]

    def Convert_To_Surface(self, point:list[int]):
        return [
            point[0] * self.scaled_value + self.scrolled_point[0],
            point[1] * self.scaled_value + self.scrolled_point[1]
        ]

    def _Render_Vessel(self, vessel:Vessel):
        vessel_surface = pygame.Surface((10, 5), pygame.SRCALPHA)
        pygame.draw.polygon(vessel_surface, theatre.COLOR[vessel.owner.color], ((0,0), (9,2), (0,4)))
        vessel_surface = pygame.transform.rotate(vessel_surface, vessel.rotation)
        
        self.surface.blit(vessel_surface, vessel_surface.get_rect(center=self.Convert_To_Surface(vessel.position)))