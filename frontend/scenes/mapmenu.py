import pygame
from backend.game import action

# engine
from engine import Scene
from backend.theatre import theatre
from frontend.elements.vesselvisual import VesselVisual



class MapMenu(Scene):
    def __init__(self, act) -> None:
        super().__init__(act)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct

        self.vessel_visuals:list[VesselVisual] = list()

        self.scrolled_point:list[int] = [0, 0]
        self.scaled_value:int = 1


    # ----------ON_STUFF----------
    def On_Update(self):
        self.vessel_visuals.clear()

        for vessel in self.act.game.forces:
            self.vessel_visuals.append(VesselVisual(self, vessel))


    def On_Open(self) -> None:
        self.Update()

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        # validate
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if not self.rect.collidepoint(event.pos): return
            else: self.act.actionsmenu.selected_action.Do(position=self.Convert_To_Map(event.pos))

        # move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: self.scrolled_point[0] += 1
            elif event.key == pygame.K_d: self.scrolled_point[0] -= 1
            elif event.key == pygame.K_w: self.scrolled_point[1] += 1
            elif event.key == pygame.K_s: self.scrolled_point[1] -= 1
            else: return

            for vessel_visual in self.vessel_visuals: vessel_visual.Update()

        for vessel_visual in self.vessel_visuals:
            vessel_visual.Handle(event)
        



    def On_Render(self) -> None:

        # background
        self.surface.fill(theatre.settings['background_color'])
        pygame.draw.rect(self.surface, theatre.settings['neutral_color'], ((0,0), self.rect.size), 2)

        # vessels
        for vessel_visual in self.vessel_visuals:
            vessel_visual.Render(self.surface)

        # selected oreder
        # if self.act.actionsmenu.selected_action != None:
        #     mouse_position = pygame.mouse.get_pos()
        #     mouse_position = (mouse_position[0]/2, mouse_position[1]/2)
        #     target_screen_position = self.act.actionsmenu.selected_vessel.movement_actions[0].Fix_Args(self.act.game, mouse_position)['position']
        #     target_screen_position = (target_screen_position[0] * 2, target_screen_position[1] * 2)
        #     # action
        #     pygame.draw.line(self.surface, "#ff0000", (self.act.actionsmenu.selected_vessel.position[0] * 2, self.act.actionsmenu.selected_vessel.position[1] * 2), target_screen_position)

        # finish
        self.act.surface.blit(self.surface, self.rect)


    def Convert_To_Map(self, point:list[int]):
        return [
            point[0] / self.scaled_value - self.scrolled_point[0] - self.rect.left,
            point[1] / self.scaled_value - self.scrolled_point[1] - self.rect.top
        ]

    def Convert_To_Screen(self, point:list[int]):
        return [
            (point[0] + self.scrolled_point[0]) * self.scaled_value,
            (point[1] + self.scrolled_point[1]) * self.scaled_value
        ]
