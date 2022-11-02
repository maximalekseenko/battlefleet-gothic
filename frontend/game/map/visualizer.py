import pygame
import math
import backend.game as game
from .mapmenu import MapMenu


class Visualizer:
    
    def __init__(self, scene:MapMenu) -> None:
        self.scene:MapMenu = scene

        self.layers:list[list] = [list(), list(), list()]

        self.requests:dict[str, tuple[function, list]] = {
            'Highlight': [self.Highlight, self.layers[1]],
            'Line': [self.Line, self.layers[1]],
            'Arcs': [self.Arcs, self.layers[1]],
        }

    
    def __call__(self, function:str, 
            **kargs) -> None:
        kargs['function'] = function

        self.requests[function][1].append(kargs)


    def visualize(self, layer:int):
        while self.layers[layer]:
            item = self.layers[layer].pop()
            self.requests[item['function']][0](**item)


    def Highlight(self, color:pygame.Color, vessel:game.Vessel, position:game.position=None, **kargs):
        if position == None: position = vessel.position
        position = self.scene.Convert_Map_To_Relative(position)

        pygame.draw.circle(self.scene.surface, color, position, vessel.BASE_RADIUS * self.scene.scaled_value, 1)


    def Line(self, color:pygame.Color, position:game.position, position2:game.position, **kargs):
        position = self.scene.Convert_Map_To_Relative(position)
        position2 = self.scene.Convert_Map_To_Relative(position2)

        pygame.draw.line(self.scene.surface, color, position, position2)


    def Arcs(self, color:pygame.Color, vessel:game.Vessel, position:game.position=None, **kargs):
        if position == None: position = vessel.position
        position = self.scene.Convert_Map_To_Relative(position)
        
        # hands
        pygame.draw.line(self.scene.surface, color, 
            [   position[0] + vessel.BASE_RADIUS * self.scene.scaled_value * math.cos(vessel.rad_rotation + math.pi*0.25),
                position[1] - vessel.BASE_RADIUS * self.scene.scaled_value * math.sin(vessel.rad_rotation + math.pi*0.25)],
            [   position[0] + 60 * self.scene.scaled_value * math.cos(vessel.rad_rotation + math.pi*0.25), 
                position[1] - 60 * self.scene.scaled_value * math.sin(vessel.rad_rotation + math.pi*0.25)])
        pygame.draw.line(self.scene.surface, color, 
            [   position[0] + vessel.BASE_RADIUS * self.scene.scaled_value * math.cos(vessel.rad_rotation - math.pi*0.25),
                position[1] - vessel.BASE_RADIUS * self.scene.scaled_value * math.sin(vessel.rad_rotation - math.pi*0.25)],
            [   position[0] + 60 * self.scene.scaled_value * math.cos(vessel.rad_rotation - math.pi*0.25), 
                position[1] - 60 * self.scene.scaled_value * math.sin(vessel.rad_rotation - math.pi*0.25)])
        pygame.draw.line(self.scene.surface, color, 
            [   position[0] + vessel.BASE_RADIUS * self.scene.scaled_value * math.cos(vessel.rad_rotation + math.pi*1.25),
                position[1] - vessel.BASE_RADIUS * self.scene.scaled_value * math.sin(vessel.rad_rotation + math.pi*1.25)],
            [   position[0] + 60 * self.scene.scaled_value * math.cos(vessel.rad_rotation + math.pi*1.25), 
                position[1] - 60 * self.scene.scaled_value * math.sin(vessel.rad_rotation + math.pi*1.25)])
        pygame.draw.line(self.scene.surface, color, 
            [   position[0] + vessel.BASE_RADIUS * self.scene.scaled_value * math.cos(vessel.rad_rotation - math.pi*1.25),
                position[1] - vessel.BASE_RADIUS * self.scene.scaled_value * math.sin(vessel.rad_rotation - math.pi*1.25)],
            [   position[0] + 60 * self.scene.scaled_value * math.cos(vessel.rad_rotation - math.pi*1.25), 
                position[1] - 60 * self.scene.scaled_value * math.sin(vessel.rad_rotation - math.pi*1.25)])
    