from __future__ import annotations
import pygame
import backend.game as game


class Vizualizer:
    
    def __init__(self, game:game.Game, scene) -> None:
        self.game:game.Game = game
        self.scene = scene


    def Highlight(self, color:pygame.Color, vessel:game.Vessel, pos:game.position=None):
        if pos == None: pos = vessel.position
        pos = self.scene.Convert_Map_To_Relative(pos)

        pygame.draw.circle(self.scene.surface, color, pos, vessel.BASE_RADIUS * self.scene.scaled_value, 1)


    def Line(self, color:pygame.Color, start_pos:game.position, end_pos:game.position):
        start_pos = self.scene.Convert_Map_To_Relative(start_pos)
        end_pos = self.scene.Convert_Map_To_Relative(end_pos)

        pygame.draw.line(self.scene.surface, color, start_pos, end_pos)


    def Arc(self, color:pygame.Color, start_rot:int, end_rot:int):
        ...


    # def Arcs(self, color:pygame.Color, start_rot:int, end_rot:int)
    