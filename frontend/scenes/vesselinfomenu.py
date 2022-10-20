import pygame

# engine
from engine import Scene
from frontend.theatre import theatre



class VesselInfoMenu(Scene):
    def __init__(self, act, base: pygame.Surface | pygame.Rect | None = None) -> None:
        super().__init__(act, base)

        from frontend.acts import GameAct
        self.act:GameAct


    def On_Open(self) -> None:
        self.Update()


    def On_Update(self):
        self._Update_Rects()
        self._Update_Text()


    def _Update_Rects(self):
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


    def _Update_Text(self):
        self.hits_text = theatre.FONT15.render("hits", 1, theatre.COLOR.UI.TEXT)
        self.hits_text_rect = self.hits_text.get_rect(midtop=self.hits_rect.midtop)

        self.speed_text = theatre.FONT15.render("speed", 1, theatre.COLOR.UI.TEXT)
        self.speed_text_rect = self.speed_text.get_rect(midtop=self.speed_rect.midtop)

        self.turns_text = theatre.FONT15.render("turns", 1, theatre.COLOR.UI.TEXT)
        self.turns_text_rect = self.turns_text.get_rect(midtop=self.turns_rect.midtop)

        self.shields_text = theatre.FONT15.render("shields", 1, theatre.COLOR.UI.TEXT)
        self.shields_text_rect = self.shields_text.get_rect(midtop=self.shields_rect.midtop)

        self.armour_text = theatre.FONT15.render("armour", 1, theatre.COLOR.UI.TEXT)
        self.armour_text_rect = self.armour_text.get_rect(midtop=self.armour_rect.midtop)
        
        self.turrets_text = theatre.FONT15.render("turrets", 1, theatre.COLOR.UI.TEXT)
        self.turrets_text_rect = self.turrets_text.get_rect(midtop=self.turrets_rect.midtop)

    
    def On_Render(self) -> None:
        self.surface.fill(theatre.settings["background_color"])

        self._Render_UI()

        if self.act.ordersmenu._selected_vessel != None or self.act.mapmenu.hilighted_vessel != None:
            self._Render_Text()
            self._Render_Stats()

        # render on screen
        self.act.surface.blit(self.surface, self.rect)


    def _Render_UI(self):
        if self.act.mapmenu.hilighted_vessel != None: color = self.act.mapmenu.hilighted_vessel.owner.color
        elif self.act.ordersmenu._selected_vessel != None: color = self.act.ordersmenu.selected_vessel.owner.color
        else: color = self.act.game.player.color

        pygame.draw.rect(self.surface, theatre.COLOR[color+'d1'], self.top_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d1'], self.hits_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d1'], self.speed_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d1'], self.turns_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d1'], self.shields_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d1'], self.armour_rect)
        pygame.draw.rect(self.surface, theatre.COLOR[color+'d1'], self.turrets_rect)
        
        
    def _Render_Text(self):
        self.surface.blit(self.hits_text, self.hits_text_rect)
        self.surface.blit(self.speed_text, self.speed_text_rect)
        self.surface.blit(self.turns_text, self.turns_text_rect)
        self.surface.blit(self.shields_text, self.shields_text_rect)
        self.surface.blit(self.armour_text, self.armour_text_rect)
        self.surface.blit(self.turrets_text, self.turrets_text_rect)


    def _Render_Stats(self):
        if self.act.mapmenu.hilighted_vessel != None: vessel = self.act.mapmenu.hilighted_vessel
        elif self.act.ordersmenu._selected_vessel != None: vessel = self.act.ordersmenu.selected_vessel

        # type
        stat_text = f"{vessel.TYPE.name}"
        stat_surf = theatre.FONT15.render(stat_text, 1, theatre.COLOR.UI.TEXT)
        self.surface.blit(stat_surf, stat_surf.get_rect(midleft=self.top_rect.midleft))

        # hits
        stat_text = f"{vessel.hits}/{vessel.HITS}"
        stat_surf = theatre.FONT15.render(stat_text, 1, theatre.COLOR.UI.TEXT)
        self.surface.blit(stat_surf, stat_surf.get_rect(center=self.hits_rect.center))

        # speed
        stat_text = f"{round(vessel.turn_speed,2)}/{vessel.speed}"
        stat_surf = theatre.FONT15.render(stat_text, 1, theatre.COLOR.UI.TEXT)
        self.surface.blit(stat_surf, stat_surf.get_rect(center=self.speed_rect.center))

        # turns
        stat_text = f"{vessel.turn_turns_amount} {vessel.turns}"
        stat_surf = theatre.FONT15.render(stat_text, 1, theatre.COLOR.UI.TEXT)
        self.surface.blit(stat_surf, stat_surf.get_rect(center=self.turns_rect.center))

        # shields
        stat_text = f"{vessel.HITS}"
        stat_surf = theatre.FONT15.render(stat_text, 1, theatre.COLOR.UI.TEXT)
        self.surface.blit(stat_surf, stat_surf.get_rect(center=self.shields_rect.center))

        # armour
        stat_text = f"{vessel.HITS}"
        stat_surf = theatre.FONT15.render(stat_text, 1, theatre.COLOR.UI.TEXT)
        self.surface.blit(stat_surf, stat_surf.get_rect(center=self.armour_rect.center))

        # turrets
        stat_text = f"{vessel.HITS}"
        stat_surf = theatre.FONT15.render(stat_text, 1, theatre.COLOR.UI.TEXT)
        self.surface.blit(stat_surf, stat_surf.get_rect(center=self.turrets_rect.center))

