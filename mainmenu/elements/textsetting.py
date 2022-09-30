from curses.ascii import isalpha
import pygame


# engine
from engine import Element
from theatre import theatre



class TextSetting(Element):
    def __init__(self, scene, setting_name:str, setting_key:str, from_center_top:tuple[int,int]) -> None:

        # super
        super().__init__(scene)

        # for positions
        self.from_center_top:tuple[int,int] = from_center_top
        self.surface = pygame.display.get_surface()

        # setting
        self.setting_name:str = setting_name
        self.setting_key:str = setting_key
        self.setting_value:str = theatre.settings[self.setting_key]

        # rects
        self.rect:pygame.Rect   = pygame.Rect(0, 0, 200, 25)
        self.rect_t:pygame.Rect = pygame.Rect(0, 2, 98, 21)
        self.rect_v:pygame.Rect = pygame.Rect(100, 0, 100, 25)

        # colision rect
        self.collision_rect:pygame.Rect = pygame.Rect(0, 0, 100, 25)

        # edit and highlight
        self.is_editing:bool = False
        self.is_highlighted:bool = False

        # update
        self.Update()


    def On_Update(self):

        # get value
        self.setting_value:str = theatre.settings[self.setting_key]

        # update visuals
        self._Update_Rect()
        self._Update_Surf()

        # highlight
        self.is_highlighted = self.collision_rect.collidepoint(pygame.mouse.get_pos())


    def _Update_Rect(self):

        # rect
        self.rect.x = self.from_center_top[0] + self.surface.get_size()[0] / 2
        self.rect.y = self.from_center_top[1]
        self.rect.x -= self.rect.width / 2
        self.rect.y -= self.rect.height / 2

        # colision rect red
        self.collision_rect.x = self.from_center_top[0] + self.surface.get_size()[0] / 2 + self.rect_v.x
        self.collision_rect.y = self.from_center_top[1]
        self.collision_rect.x -= self.rect.width / 2
        self.collision_rect.y -= self.rect.height / 2

    
    def _Update_Surf(self):

        # surf
        self.surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)

        # text
        pygame.draw.rect(self.surf, theatre.settings['ui_color'], self.rect_t)
        text_surf = theatre.BUTTON_FONT.render(self.setting_name, 1, theatre.settings['player_color'])
        self.surf.blit(text_surf, text_surf.get_rect(center=self.rect_t.center))

        # value
        pygame.draw.rect(self.surf, theatre.settings['ui_color'], self.rect_v)
        red_surf = theatre.BUTTON_FONT.render(str(self.setting_value), 1, theatre.settings['player_color'])
        self.surf.blit(red_surf, red_surf.get_rect(center=self.rect_v.center))

    
    def Editing_Finish(self):
        if not self.is_editing: return

        # validate value
        if len(self.setting_value) > 100: self.setting_value = self.setting_value[:100]

        # set value
        theatre.settings[self.setting_key] = self.setting_value

        # edit
        self.is_editing = False

        # update self
        self.scene.act.Update()


    def On_Handle(self, event:pygame.event.Event):
        
        # window resize
        if event.type == pygame.WINDOWRESIZED:
            self.Update()

        # highlight
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.collision_rect.collidepoint(event.pos)

        # start editing
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if   self.collision_rect.collidepoint(event.pos): self.is_editing = True
                elif self.is_editing: self.Editing_Finish()
                else: self.is_editing = False

        # input
        if event.type == pygame.KEYDOWN:
            if not self.is_editing: return

            # erase
            if event.key == pygame.K_BACKSPACE:
                self.setting_value = self.setting_value[:-1]
            
            # end
            elif event.key == pygame.K_RETURN:
                return self.Editing_Finish()

            # char
            else: self.setting_value += event.unicode

            # update
            self._Update_Surf()

    
    def On_Render(self, target:pygame.Surface):

        # main
        target.blit(self.surf, self.rect)

        # highlight
        if self.is_highlighted: pygame.draw.rect(target, theatre.settings["player_color"], self.collision_rect, theatre.BUTTON_HIGHLIGHT_WIDTH)

        # edit
        if self.is_editing: pygame.draw.rect(target, theatre.settings["enemy_color"], self.collision_rect, theatre.BUTTON_HIGHLIGHT_WIDTH)


