from curses.ascii import isalpha
import pygame


# engine
from engine import Element
from backend.theatre import theatre



class ColorSetting(Element):
    def __init__(self, scene, setting_name:str, setting_key:str, from_center_top:tuple[int,int]) -> None:

        # super
        super().__init__(scene)

        # for positions
        self.from_center_top:tuple[int,int] = from_center_top
        self.surface = pygame.display.get_surface()

        # setting
        self.setting_name:str = setting_name
        self.setting_key:str = setting_key
        self.setting_value:list[int] = theatre.settings[self.setting_key].copy()

        # rects
        self.rect:pygame.Rect   = pygame.Rect(0, 0, 200, 25)
        self.rect_t:pygame.Rect = pygame.Rect(0, 2, 98, 21)
        self.rect_r:pygame.Rect = pygame.Rect(100, 0, 32, 25)
        self.rect_g:pygame.Rect = pygame.Rect(134, 0, 32, 25)
        self.rect_b:pygame.Rect = pygame.Rect(168, 0, 32, 25)

        # collision rects
        self.collision_rect_r:pygame.Rect = pygame.Rect(0, 0, 30, 25)
        self.collision_rect_g:pygame.Rect = pygame.Rect(0, 0, 30, 25)
        self.collision_rect_b:pygame.Rect = pygame.Rect(0, 0, 30, 25)

        # edit and highlight
        self.edit_id:int = -1
        self.highlight_id:int = -1

        # update
        self.Update()


    def On_Update(self):
        # get value
        self.setting_value:list[int] = theatre.settings[self.setting_key].copy()

        # update visuals
        self._Update_Rect()
        self._Update_Surf()

        # highlight
        mouse_pos = pygame.mouse.get_pos()
        if   self.collision_rect_r.collidepoint(mouse_pos): self.highlight_id = 0
        elif self.collision_rect_g.collidepoint(mouse_pos): self.highlight_id = 1
        elif self.collision_rect_b.collidepoint(mouse_pos): self.highlight_id = 2
        else: self.highlight_id = -1


    def _Update_Rect(self):

        # rect
        self.rect.x = self.from_center_top[0] + self.surface.get_size()[0] / 2
        self.rect.y = self.from_center_top[1]
        self.rect.x -= self.rect.width / 2
        self.rect.y -= self.rect.height / 2

        # colision rect red
        self.collision_rect_r.x = self.from_center_top[0] + self.surface.get_size()[0] / 2 + self.rect_r.x
        self.collision_rect_r.y = self.from_center_top[1]
        self.collision_rect_r.x -= self.rect.width / 2
        self.collision_rect_r.y -= self.rect.height / 2

        # colision rect green
        self.collision_rect_g.x = self.from_center_top[0] + self.surface.get_size()[0] / 2 + self.rect_g.x
        self.collision_rect_g.y = self.from_center_top[1]
        self.collision_rect_g.x -= self.rect.width / 2
        self.collision_rect_g.y -= self.rect.height / 2

        # colision rect blue
        self.collision_rect_b.x = self.from_center_top[0] + self.surface.get_size()[0] / 2 + self.rect_b.x
        self.collision_rect_b.y = self.from_center_top[1]
        self.collision_rect_b.x -= self.rect.width / 2
        self.collision_rect_b.y -= self.rect.height / 2

    
    def _Update_Surf(self):

        # surf
        self.surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        # text
        pygame.draw.rect(self.surf, theatre.settings['ui_color'], self.rect_t)
        text_surf = theatre.BUTTON_FONT.render(self.setting_name, 1, theatre.settings['player_color'])
        self.surf.blit(text_surf, text_surf.get_rect(center=self.rect_t.center))

        # red
        pygame.draw.rect(self.surf, theatre.settings['ui_color'], self.rect_r)
        red_surf = theatre.BUTTON_FONT.render(str(self.setting_value[0]), 1, theatre.settings['player_color'])
        self.surf.blit(red_surf, red_surf.get_rect(center=self.rect_r.center))

        # green
        pygame.draw.rect(self.surf, theatre.settings['ui_color'], self.rect_g)
        green_surf = theatre.BUTTON_FONT.render(str(self.setting_value[1]), 1, theatre.settings['player_color'])
        self.surf.blit(green_surf, green_surf.get_rect(center=self.rect_g.center))

        # red
        pygame.draw.rect(self.surf, theatre.settings['ui_color'], self.rect_b)
        blue_surf = theatre.BUTTON_FONT.render(str(self.setting_value[2]), 1, theatre.settings['player_color'])
        self.surf.blit(blue_surf, blue_surf.get_rect(center=self.rect_b.center))

    
    def Editing_Finish(self):
        if 0 > self.edit_id or 2 < self.edit_id: return

        # validate value
        if self.setting_value[self.edit_id] < 0: self.setting_value[self.edit_id] = 0
        if self.setting_value[self.edit_id] > 255: self.setting_value[self.edit_id] = 255

        # set value
        theatre.settings[self.setting_key][self.edit_id] = self.setting_value[self.edit_id]

        # edit
        self.edit_id = -1

        # update self
        self.scene.act.Update()


    def On_Handle(self, event:pygame.event.Event):
        
        # window resize
        if event.type == pygame.WINDOWRESIZED:
            self.Update()

        # highlight
        if event.type == pygame.MOUSEMOTION:
            if   self.collision_rect_r.collidepoint(event.pos): self.highlight_id = 0
            elif self.collision_rect_g.collidepoint(event.pos): self.highlight_id = 1
            elif self.collision_rect_b.collidepoint(event.pos): self.highlight_id = 2
            else: self.highlight_id = -1

        # start editing
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 0 <= self.edit_id <= 2: self.Editing_Finish()
                if   self.collision_rect_r.collidepoint(event.pos): self.edit_id = 0
                elif self.collision_rect_g.collidepoint(event.pos): self.edit_id = 1
                elif self.collision_rect_b.collidepoint(event.pos): self.edit_id = 2
                else: self.edit_id = -1

        # input
        if event.type == pygame.KEYDOWN:
            if 0 > self.edit_id or 2 < self.edit_id: return

            # next
            if event.key == pygame.K_TAB:
                self.edit_id = (self.edit_id + 1) % 3

            # erase
            if event.key == pygame.K_BACKSPACE:
                self.setting_value[self.edit_id] //= 10
            
            # end
            elif event.key == pygame.K_RETURN:
                return self.Editing_Finish()

            # char
            elif event.unicode.isdigit(): self.setting_value[self.edit_id] = self.setting_value[self.edit_id] * 10 + int(event.unicode)

            # update
            self._Update_Surf()

    
    def On_Render(self, target:pygame.Surface):

        # main
        target.blit(self.surf, self.rect)

        # highlight
        if self.highlight_id == 0: pygame.draw.rect(target, theatre.settings["player_color"], self.collision_rect_r, theatre.BUTTON_HIGHLIGHT_WIDTH)
        if self.highlight_id == 1: pygame.draw.rect(target, theatre.settings["player_color"], self.collision_rect_g, theatre.BUTTON_HIGHLIGHT_WIDTH)
        if self.highlight_id == 2: pygame.draw.rect(target, theatre.settings["player_color"], self.collision_rect_b, theatre.BUTTON_HIGHLIGHT_WIDTH)

        # edit
        if self.edit_id == 0: pygame.draw.rect(target, theatre.settings["enemy_color"], self.collision_rect_r, theatre.BUTTON_HIGHLIGHT_WIDTH)
        if self.edit_id == 1: pygame.draw.rect(target, theatre.settings["enemy_color"], self.collision_rect_g, theatre.BUTTON_HIGHLIGHT_WIDTH)
        if self.edit_id == 2: pygame.draw.rect(target, theatre.settings["enemy_color"], self.collision_rect_b, theatre.BUTTON_HIGHLIGHT_WIDTH)


