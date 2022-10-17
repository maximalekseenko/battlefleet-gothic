import pygame
import json


from engine import Theatre

from .color import COLOR



class Theatre(Theatre):
    def __init__(self) -> None:
        super().__init__()
        pygame.key.set_repeat(100, 10)

        self.COLOR = COLOR()

        # cursor
        from math import sin, cos
        cursor = pygame.Surface((15, 15), pygame.SRCALPHA)
        cursor_rect = cursor.get_rect()
        pygame.draw.circle(cursor, "#ffffff", cursor_rect.center, 2.5)
        pygame.draw.line(cursor, "#ffffff", 
            (cursor_rect.centerx, cursor_rect.centery + sin(cursor_rect.height / 5)), 
            cursor_rect.midtop)
        pygame.draw.line(cursor, "#ffffff", 
            (cursor_rect.centerx, cursor_rect.centery - sin(cursor_rect.height / 5)), 
            cursor_rect.midbottom)
        pygame.draw.line(cursor, "#ffffff", 
            (cursor_rect.centerx - cos(cursor_rect.height / 5), cursor_rect.centery), 
            cursor_rect.midleft)
        pygame.draw.line(cursor, "#ffffff", 
            (cursor_rect.centerx + cos(cursor_rect.height / 5), cursor_rect.centery), 
            cursor_rect.midright)

        pygame.mouse.set_cursor(pygame.cursors.Cursor(cursor_rect.center, cursor))

        # consts
        self.FONT60 = pygame.font.Font(None, 60)
        self.FONT24 = pygame.font.Font(None, 24)
        self.FONT12 = pygame.font.Font(None, 12)
        self.FONT15 = pygame.font.Font(None, 15)
        self.FONT20 = pygame.font.Font(None, 20)
        self.FONT6 = pygame.font.Font(None, 6)
        self.BUTTON_SIZE = (300, 25)
        self.BUTTON_FONT = pygame.font.Font(None, 24)
        self.PLAYER_NAME_LEN_MAX = 20
        self.BUTTON_HIGHLIGHT_WIDTH = 3

        self.DEFAULT_SETTINGS = {
            "background_color":[50, 50, 50],
            "ui_color":[50, 50, 200],
            "neutral_color":[200, 200, 200],
            "player_color":[50, 200, 50],
            "enemy_color":[200, 50, 50],

            "player_name":"isckdcks",
            "server_ip":"0.0.0.0",
            "server_port":"0000",
        }


        # settings
        self.settings:dict

        self.Read_Settings()


    def Read_Settings(self):

        # read from file
        with open("settings.json", 'r') as settings_file: settings_data:dict = json.load(settings_file)

        # reset settings
        self.settings = self.DEFAULT_SETTINGS.copy()

        # set variables
        for setting_item in settings_data.items():
            self.settings[setting_item[0]] = setting_item[1]


    def Write_Settings(self):

        # write to file
        with open("settings.json", 'w') as settings_file: json.dump(self.settings, settings_file)
        

theatre = Theatre()