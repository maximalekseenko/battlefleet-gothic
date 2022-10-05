import pygame

# engine
from engine import Act
from backend.theatre import theatre



class GameAct(Act):
    def __init__(self) -> None:
        super().__init__()

        # surface
        self.surface = pygame.display.get_surface()
        self.mapsurface = pygame.Surface((
            self.surface.get_width() * 2/4, 
            self.surface.get_height()))
        self.vessellistsurface = pygame.Surface((
            self.surface.get_width() * 1/4,
            self.surface.get_height()))
        self.minimapsurface = pygame.Surface((
            self.surface.get_width() * 1/4, 
            self.surface.get_height()))

        # scenes
        from frontend.scenes import ConnectionMenu, ActionsMenu, MapMenu, VessellistMenu
        self.connectionmenu:ConnectionMenu = ConnectionMenu(self, self.surface)
        self.actionsmenu:ActionsMenu = ActionsMenu(self)
        self.mapmenu:MapMenu = MapMenu(self, self.mapsurface)
        self.vessellistmenu:VessellistMenu = VessellistMenu(self, self.vessellistsurface)

        # game
        from backend.game import Game
        self.game:Game = Game()

        # TODO: DELETE
        # player1 = PseudoPlayer(["test"])
        from test2 import LunarClassCruiser
        self.game.Join(1)
        vessel1p1 = self.game.Add_Vessel(LunarClassCruiser, 0, (0, 20 ), -90)
        vessel2p1 = self.game.Add_Vessel(LunarClassCruiser, 0, (0, 30 ), -90)
        vessel3p1 = self.game.Add_Vessel(LunarClassCruiser, 0, (0, 40 ), -90)

        # player 2
        # player2 = PseudoPlayer(["test"])
        self.game.Join(2)
        vessel1p2 = self.game.Add_Vessel(LunarClassCruiser, 1, (90, 20), 90)
        vessel2p2 = self.game.Add_Vessel(LunarClassCruiser, 1, (90, 30), 90)
        vessel3p2 = self.game.Add_Vessel(LunarClassCruiser, 1, (90, 40), 45)

        self.game.Start()

        self.actionsmenu.selected_vessel = vessel1p1

    
    def On_Update(self):

        # update menu rects
        self._Update_Menu_Rects()

        # update menus
        self.connectionmenu.Update()
        self.actionsmenu.Update()


    def _Update_Menu_Rects(self):

        # actions menu
        self.actionsmenu.rect = pygame.Rect(
            0, 0,
            self.surface.get_width() * 1/4,
            self.surface.get_height())

    def On_Open(self) -> None:

        # update menu rects
        self._Update_Menu_Rects()

        # reset menus
        # self.connectionmenu.Open()
        self.actionsmenu.Open()
        self.mapmenu.Open()
        self.vessellistmenu.Open()

        # update
        # self.Update()


    def On_Close(self) -> None:

        # close menus
        self.connectionmenu.Close()
        self.actionsmenu.Close()
        self.mapmenu.Close()
        self.vessellistmenu.Close()

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        # window resize
        if event.type == pygame.WINDOWRESIZED: self.Update()

        else:
            # handle menus if needed
            self.connectionmenu.Handle(event)
            self.actionsmenu.Handle(event)
            self.mapmenu.Handle(event)
            self.vessellistmenu.Handle(event)

    
    def On_Render(self) -> None:

        # fill background
        self.surface.fill(theatre.settings["background_color"])
        self.mapsurface.fill(theatre.settings["background_color"])

        # render menus if needed
        self.connectionmenu.Render()
        self.actionsmenu.Render()
        self.mapmenu.Render()
        self.vessellistmenu.Render()

        # collect surfaces
        # self.surface.blit(self.actionssurface, (0, 0))
        # self.surface.blit(self.mapsurface, (self.actionssurface.get_width(), 0))
        # self.surface.blit(self.vessellistsurface, (self.surface.get_width() - self.vessellistsurface.get_width(), 0))
        # self.surface.blit(self.minimapsurface, (self.surface.get_width() - self.minimapsurface.get_width(), 0))
        
        
        
        