import pygame

# engine
from engine import Act
from theatre import theatre

# scenes
from .load_scene import Load_Scene
from .battle_scene import Battle_Scene


class Game_Act(Act):
    def __init__(self) -> None:
        super().__init__()

        # surface
        self.surface = pygame.display.get_surface()

        # scenes
        self.load_scene:Load_Scene = Load_Scene(self, self.surface)
        self.battle_scene:Battle_Scene = Battle_Scene(self, self.surface)

        self.load_scene.Open()

    
    def On_Handle(self, event: pygame.event.Event) -> None:
        if self.load_scene.is_opened: self.load_scene.Handle(event)
        elif self.battle_scene.is_opened: self.battle_scene.Handle(event)

    
    def On_Render(self) -> None:
        self.surface.fill(theatre.background_color)

        if self.load_scene.is_opened: self.load_scene.Render(self.surface)
        elif self.battle_scene.is_opened: self.battle_scene.Render(self.surface)