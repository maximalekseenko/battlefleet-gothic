import pygame


# engine
from engine import Element
from backend.theatre import theatre
from backend.game import Action



class OrderButton(Element):
    def __init__(self, scene, order) -> None:
        super().__init__(scene, (0, 0, 25, 25))

        self.order:Action = order

        self.is_highlighted = False

        self.Update()

    
    def On_Tick(self) -> None:
        pass


    def On_Update(self):
        self.surface.fill(theatre.settings["ui_color"])
        text = theatre.FONT24.render(self.order.DISPLAY_NAME, 1, theatre.settings["player_color"])
        self.surface.blit(text, text.get_rect(centerx=self.rect.width / 2, centery=self.rect.height / 2))


    def On_Handle(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.rect.collidepoint(event.pos)


    def On_Render(self, target: pygame.Surface) -> None:
        target.blit(self.surface, self.rect)

        if self.is_highlighted: 
            pygame.draw.rect(target, theatre.settings["player_color"], self.rect, 1)
