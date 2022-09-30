import pygame

# engine
from engine import Scene
from theatre import theatre

# act
from . import game_act


class Load_Scene(Scene):
    def __init__(self, act, surface) -> None:
        self.act:game_act.Game_Act
        super().__init__(act, surface)

    
    def On_Open(self) -> None:
        pass