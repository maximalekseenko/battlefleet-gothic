import pygame

# engine
from engine import Scene
from frontend.theatre import theatre



class VesselInfoMenu(Scene):
    def __init__(self, act, base: pygame.Surface | pygame.Rect | None = None) -> None:
        super().__init__(act, base)

        from frontend.acts import GameAct
        self.act:GameAct

        self._hashed_selected_vessel = None


    def On_Open(self) -> None:
        self.Update()


    def On_Update(self):

        SIZE = (40, 40)
        SIDE_DISTANCE = 10
        SEP_DISTANCE = 3

        # rects
        #   [         top           ]
        #   [ hits   speed    turns ]
        #   [shields armour  turrets]


        self.top_rect = pygame.Rect(
            SIDE_DISTANCE, SIDE_DISTANCE,
            self.rect.width - 2 * SIDE_DISTANCE,
            SIZE[0] / 2)

        self.hits_rect = pygame.Rect((0, 0), SIZE)
        self.hits_rect.topleft = (self.top_rect.left, self.top_rect.bottom + SEP_DISTANCE)

        self.speed_rect = pygame.Rect((0, 0), SIZE)
        self.speed_rect.midtop = (self.top_rect.centerx, self.top_rect.bottom + SEP_DISTANCE)

        self.turns_rect = pygame.Rect((0, 0), SIZE)
        self.turns_rect.topright = (self.top_rect.right, self.top_rect.bottom + SEP_DISTANCE)

        self.shields_rect = pygame.Rect((0, 0), SIZE)
        self.shields_rect.topleft = (self.top_rect.left, self.speed_rect.bottom + SEP_DISTANCE)

        self.armour_rect = pygame.Rect((0, 0), SIZE)
        self.armour_rect.midtop = (self.top_rect.centerx, self.speed_rect.bottom + SEP_DISTANCE)

        self.turrets_rect = pygame.Rect((0, 0), SIZE)
        self.turrets_rect.topright = (self.top_rect.right, self.speed_rect.bottom + SEP_DISTANCE)


    
    def On_Render(self) -> None:
        self.surface.fill(theatre.settings["background_color"])

        self._Render_UI()

        if self.act.ordersmenu.selected_vessel == None: return

        # TODO AAAA

        # render on screen
        self.act.surface.blit(self.surface, self.rect)


    def _Render_UI(self):
        if self.act.mapmenu.hilighted_vessel != None: color = self.act.mapmenu.hilighted_vessel.owner.color
        elif self.act.ordersmenu.selected_vessel != None: color = self.act.ordersmenu.selected_vessel.owner.color
        else: color = theatre.COLOR.BLACK
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d2'], self.top_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d2'], self.hits_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d2'], self.speed_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d2'], self.turns_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d2'], self.shields_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d2'], self.armour_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d2'], self.turrets_rect)
        