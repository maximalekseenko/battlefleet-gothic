import pygame

# engine
from engine import Act
from frontend.theatre import theatre



class GameAct(Act):
    def __init__(self) -> None:
        super().__init__()

        # surface
        self.surface = pygame.display.get_surface()

        # game
        from backend.game import Game
        self.game:Game = Game()

        # scenes
        from frontend.scenes import ConnectionMenu, OrdersMenu, MapMenu, VesselInfoMenu
        self.connectionmenu:ConnectionMenu = ConnectionMenu(self, self.surface)
        self.ordersmenu:OrdersMenu = OrdersMenu(self)
        self.mapmenu:MapMenu = MapMenu(self)
        self.vesselinfomenu:VesselInfoMenu = VesselInfoMenu(self)


        # TODO: DELETE
        from test2 import LunarClassCruiser
        p1 = self.game.Join(1)
        vessel1p1 = self.game.Add_Vessel(LunarClassCruiser, p1, (10, 20 ), -10)
        vessel2p1 = self.game.Add_Vessel(LunarClassCruiser, p1, (10, 30 ), 0)
        vessel3p1 = self.game.Add_Vessel(LunarClassCruiser, p1, (10, 40 ), 30)

        p2 = self.game.Join(2)
        vessel1p2 = self.game.Add_Vessel(LunarClassCruiser, p2, (80, 20), 180+45)
        vessel2p2 = self.game.Add_Vessel(LunarClassCruiser, p2, (80, 30), 180+10)
        vessel3p2 = self.game.Add_Vessel(LunarClassCruiser, p2, (80, 40), 180)
        
        self.game.player = self.game.players[0]

        self.game.Start()

        self.ordersmenu.selected_vessel = vessel1p1
        self.ordersmenu.selected_order = vessel1p1.orders[0]


    def On_Tick(self) -> None:
        self.ordersmenu.Tick()
        self.mapmenu.Tick()
        self.vesselinfomenu.Tick()

    
    def On_Update(self):

        # update menu rects
        self._Update_Menu_Rects()

        # update menus
        self.connectionmenu.Update()
        self.ordersmenu.Update()
        self.vesselinfomenu.Update()


    def _Update_Menu_Rects(self):

        # vessel list menu
        self.vesselinfomenu.rect = pygame.Rect(
            0,
            0,
            150,
            150)

        # orders menu
        self.ordersmenu.rect = pygame.Rect(
            0,
            self.vesselinfomenu.rect.bottom,
            150,
            self.surface.get_height() - 150)

        # map menu
        self.mapmenu.rect = pygame.Rect(
            self.ordersmenu.rect.right,
            0,
            self.surface.get_width() * 2/4,
            self.surface.get_height())



    def On_Open(self) -> None:

        # update menu rects
        self._Update_Menu_Rects()

        # reset menus
        # self.connectionmenu.Open()
        self.ordersmenu.Open()
        self.mapmenu.Open()
        self.vesselinfomenu.Open()


    def On_Close(self) -> None:

        # close menus
        self.connectionmenu.Close()
        self.ordersmenu.Close()
        self.mapmenu.Close()
        self.vesselinfomenu.Close()

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        # window resize
        if event.type == pygame.WINDOWRESIZED: self.Update()

        else:
            # handle menus if needed
            self.connectionmenu.Handle(event)
            self.ordersmenu.Handle(event)
            self.mapmenu.Handle(event)
            self.vesselinfomenu.Handle(event)

    
    def On_Render(self) -> None:

        # fill background
        self.surface.fill(theatre.settings["background_color"])

        # render menus if needed
        self.connectionmenu.Render()
        self.ordersmenu.Render()
        self.mapmenu.Render()
        self.vesselinfomenu.Render()