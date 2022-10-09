import pygame

# engine
from engine import Scene
from backend.theatre import theatre



class MapMenu(Scene):
    def __init__(self, act) -> None:
        super().__init__(act)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct


        # TODO: DELETE
        self.vessel1_image = pygame.Surface((5,10), pygame.SRCALPHA)
        pygame.draw.polygon(self.vessel1_image, "#a00000", ((0,9),(2,0),(4,9)))

        self.vessel2_image = pygame.Surface((5,10), pygame.SRCALPHA)
        pygame.draw.polygon(self.vessel2_image, "#00a000", ((0,9),(2,0),(4,9)))


    # ----------ON_STUFF----------
    def On_Update(self):
        pass


    def On_Open(self) -> None:
        self.Update()

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        pass


    def On_Render(self) -> None:
        for vessel in self.act.game.forces:
            vessel_image = self.vessel1_image.copy() if vessel.owner==0 else self.vessel2_image.copy()
            vessel_image = pygame.transform.rotate(vessel_image, vessel.rotation)

            self.surface.blit(vessel_image, (
                vessel.position[0] * 2 - vessel_image.get_width() / 2, 
                vessel.position[1] * 2 - vessel_image.get_height() / 2))

            mouse_position = pygame.mouse.get_pos()
            mouse_position = (mouse_position[0]/2, mouse_position[1]/2)
            target_screen_position = vessel.movement_actions[0].Fix_Args(self.act.game, mouse_position)['position']
            target_screen_position = (target_screen_position[0] * 2, target_screen_position[1] * 2)
            # action
            pygame.draw.line(self.surface, "#ff0000", (vessel.position[0] * 2, vessel.position[1] * 2), target_screen_position)

            self.act.surface.blit(self.surface, self.rect)


