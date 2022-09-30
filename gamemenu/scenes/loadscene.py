import pygame

# engine
from engine import Scene
from theatre import theatre

# act
from .. import gameact


class Load_Scene(Scene):
    def __init__(self, act, surface) -> None:
        self.act:gameact.Game_Act
        super().__init__(act, surface)

    
    def On_Open(self) -> None:
        pass