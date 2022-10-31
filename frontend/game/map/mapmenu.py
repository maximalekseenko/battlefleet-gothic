import pygame
import backend.game as game

# engine
from engine import Scene
from frontend.theatre import theatre



class MapMenu(Scene):
    def __init__(self, act) -> None:
        super().__init__(act)

        # for snippets
        from frontend.acts import GameAct
        self.act:GameAct


        from .visualizer import Vizualizer
        self.vizualizer = Vizualizer(self)

        self.scrolled_point:list[int] = [0, 0]
        self.scaled_value:int = 2

        self.hilighted_vessel:game.Vessel = None


    # ----------ON_STUFF----------


    def On_Open(self) -> None:
        self.Update()

    
    def On_Handle(self, event: pygame.event.Event) -> None:

        if event.type == pygame.MOUSEBUTTONDOWN: 
            if not self.rect.collidepoint(event.pos): return
            self._Handle_MBD(event.button, event.pos)

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
            self._Handle_Zoom(event.y)
            
        # vessel highlight
        if event.type == pygame.MOUSEMOTION:
            self.hilighted_vessel = self.act.game.Get_Vessel_In_Position(self.Convert_Relative_To_Map(self.Relative(event.pos)))

    # def _Handle_Move(self, key) -> None:

    def _Handle_MBD(self, button, position):

        # position order
        if button == 1: self.act.ordersmenu.selected_order.Do(self.Convert_Global_To_Map(position))

        # cancel order selection
        elif button == 3: self.act.ordersmenu.selected_order = None


    def _Handle_Zoom(self, value):

        SCALE_MIN = 1.5
        SCALE_MAX = 15
        SCALE_SPEED = 0.01

        # save old mouse position
        mouse_position = pygame.mouse.get_pos()

        # get map point mouse was focus on
        map_mouse_position = self.Convert_Global_To_Map(mouse_position)

        # scale
        self.scaled_value -= value * SCALE_SPEED
        ## check limits
        if self.scaled_value < SCALE_MIN: self.scaled_value = SCALE_MIN
        if self.scaled_value > SCALE_MAX: self.scaled_value = SCALE_MAX

        # get focus map point position after scale
        new_mouse_position = self.Convert_Map_To_Global(map_mouse_position)

        # scroll for mouse to be on that map point
        self.scrolled_point[0] += mouse_position[0] - new_mouse_position[0]
        self.scrolled_point[1] += mouse_position[1] - new_mouse_position[1]


    def On_Render(self) -> None:

        # background and outline
        self.surface.fill(theatre.settings['background_color'])
        pygame.draw.rect(self.surface, theatre.settings['neutral_color'], ((0,0), self.rect.size), 1)

        # rendering
        ## game background
        self._Render_Game_Background()
        self._Render_Vessel_Highlights()
        # ## order base
        self._Render_Vessel_Visuals()
        # ## order arc


        # TODO:DELETE
        self.act.ordersmenu.selected_order.Preview(self.Convert_Global_To_Map(pygame.mouse.get_pos()))
        

        # finish
        self.act.surface.blit(self.surface, self.rect)


    def _Render_Game_Background(self) -> None:
        COLOR =  "#000000"
        pygame.draw.rect(self.surface, COLOR, (
            self.Convert_Map_To_Relative((0, 0)), 
            (self.act.game.size[0] * self.scaled_value, self.act.game.size[1] * self.scaled_value)
            ))


    def _Render_Order_Line(self, order_data:dict[str,any]) -> None:
        COLOR = "#a05000"

        pygame.draw.line(self.surface, COLOR, 
            self.Convert_Map_To_Relative(self.act.ordersmenu.selected_vessel.position), 
            order_data['position'])


    def _Render_Order_Base(self, order_data:dict[str,any]) -> None:
        COLOR = "#a05000"

        pygame.draw.circle(self.surface, COLOR,
            order_data['position'],
            self.act.ordersmenu.selected_vessel.BASE_RADIUS*self.scaled_value, 1)


    def _Render_Order_Target(self, order_data:dict[str,any]) -> None:
        RADIUS = 1.5
        COLOR = "#ffffff"

        pygame.draw.line(self.surface, COLOR,
            (order_data['position'][0] + RADIUS,
            order_data['position'][1] + RADIUS),
            (order_data['position'][0] - RADIUS,
            order_data['position'][1] - RADIUS))
        pygame.draw.line(self.surface, COLOR,
            (order_data['position'][0] + RADIUS,
            order_data['position'][1] - RADIUS),
            (order_data['position'][0] - RADIUS,
            order_data['position'][1] + RADIUS))


    def _Render_Order_Value(self, order_data:dict[str,any]) -> None:
        COLOR = "#ffffff"

        text_surf = theatre.FONT15.render(order_data['value'], 1, COLOR)
        self.surface.blit(text_surf, text_surf.get_rect(topleft=self.Relative(pygame.mouse.get_pos())))


    def _Render_Vessel_Highlights(self) -> None:
        for vessel in self.act.game.forces:

            # get color add
            if self.act.ordersmenu.selected_vessel == vessel: color_add = 'l1'
            elif self.hilighted_vessel == vessel: color_add = 'd1'
            else: color_add = 'd2'

            # render
            pygame.draw.circle(self.surface, 
                theatre.COLOR[vessel.owner.color+color_add], 
                self.Convert_Map_To_Relative(vessel.position),
                vessel.BASE_RADIUS*self.scaled_value, 1)


    def _Render_Vessel_Visuals(self) -> None:
        for vessel in self.act.game.forces:

            # craete visual 
            # TODO:hash?
            vessel_surface = pygame.Surface((10, 5), pygame.SRCALPHA)
            pygame.draw.polygon(vessel_surface, theatre.COLOR[vessel.owner.color], ((0,0), (9,2), (0,4)))

            # rotate visual
            vessel_surface = pygame.transform.rotate(vessel_surface, vessel.rotation)
            
            # blit visual
            self.surface.blit(vessel_surface, vessel_surface.get_rect(center=self.Convert_Map_To_Relative(vessel.position)))


    def Convert_Relative_To_Map(self, point:list[int]):
        return game.position(
            (point[0] - self.scrolled_point[0]) / self.scaled_value,
            (point[1] - self.scrolled_point[1]) / self.scaled_value
        )

    def Convert_Global_To_Map(self, point:list[int]):
        return self.Convert_Relative_To_Map(self.Relative(point))


    def Convert_Map_To_Relative(self, point:game.position):
        return [
            point[0] * self.scaled_value + self.scrolled_point[0],
            point[1] * self.scaled_value + self.scrolled_point[1]
        ]


    def Convert_Map_To_Global(self, point:game.position):
        return self.Global(self.Convert_Map_To_Relative(point))

