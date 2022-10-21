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

        self.hilighted_vessel:Vessel = None


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
        
        # vessel highlight
        if event.type == pygame.MOUSEMOTION:
            self.hilighted_vessel = self.act.game.Get_Vessel_In_Position(self.Convert_To_Map(event.pos))


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
        order_data = self.act.ordersmenu.selected_order.Get_Data(self.Convert_To_Map(pygame.mouse.get_pos()))
        order_data['position'] = self.Convert_To_Surface(order_data['position']) if order_data['position'] else self.Relative(pygame.mouse.get_pos())
        order_data['show_value'] = str(order_data['show_value']) if order_data['show_value'] else ''

        self._Render_Order(order_data)
        self._Render_Highlight()
        self._Render_Vessels()
        self._Render_Cursor(order_data)

        # finish
        self.act.surface.blit(self.surface, self.rect)


    def _Render_Order(self, order_data:dict[str,any]) -> None:
        if self.act.ordersmenu.selected_order and self.act.ordersmenu.selected_vessel:

            # line
            if self.act.ordersmenu.selected_order.SHOW_LINE:
                    pygame.draw.line(self.surface, "#a05000", 
                        self.Convert_To_Surface(self.act.ordersmenu.selected_vessel.position), 
                        order_data['position'])


    def _Render_Highlight(self) -> None:
        for vessel in self.act.game.forces:

            # get color add
            if self.act.ordersmenu.selected_vessel == vessel: color_add = 'l1'
            elif self.hilighted_vessel == vessel: color_add = 'd1'
            else: color_add = 'd2'

            # render
            pygame.draw.circle(self.surface, 
                theatre.COLOR[vessel.owner.color+color_add], 
                self.Convert_To_Surface(vessel.position),
                vessel.BASE_RADIUS*self.scaled_value, 1)


    def _Render_Vessels(self):
        for vessel in self.act.game.forces:

            vessel_surface = pygame.Surface((10, 5), pygame.SRCALPHA)
            pygame.draw.polygon(vessel_surface, theatre.COLOR[vessel.owner.color], ((0,0), (9,2), (0,4)))
            vessel_surface = pygame.transform.rotate(vessel_surface, vessel.rotation)
            
            self.surface.blit(vessel_surface, vessel_surface.get_rect(center=self.Convert_To_Surface(vessel.position)))


    def _Render_Cursor(self, order_data):

        RADIUS = 1.5

        # target
        if self.act.ordersmenu.selected_order.SHOW_TARGET:
            pygame.draw.line(self.surface, "#ffffff",
                (order_data['position'][0] + RADIUS,
                order_data['position'][1] + RADIUS),
                (order_data['position'][0] - RADIUS,
                order_data['position'][1] - RADIUS))
            pygame.draw.line(self.surface, "#ffffff",
                (order_data['position'][0] + RADIUS,
                order_data['position'][1] - RADIUS),
                (order_data['position'][0] - RADIUS,
                order_data['position'][1] + RADIUS))
            
        # base 
        if self.act.ordersmenu.selected_order.SHOW_BASE:
            pygame.draw.circle(self.surface, "#ffffff",
                order_data['position'],
                self.act.ordersmenu.selected_vessel.BASE_RADIUS*self.scaled_value, 1)

        # value
        if self.act.ordersmenu.selected_order.SHOW_VALUE:
            text_surf = theatre.FONT15.render(order_data['show_value'], 1, "#ffffff")
            self.surface.blit(text_surf, text_surf.get_rect(topleft=self.Relative(pygame.mouse.get_pos())))


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

